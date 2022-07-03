from argparse import ArgumentParser
from typing import List, Dict
import sys

from pandas import DataFrame, read_csv


def loadPersonalInfo(filepath: str) -> DataFrame:
    """
    Loads CSV as pandas.DataFrame.

    Bad filepath ->
    Bad file schema (missing columns) ->
    """
    return read_csv(
        filepath,
        sep=',',  # type:ignore
        usecols=['id', 'email', 'country'],
        dtype={
            'id': int,
            'email': str,
            'country': str,
        }
    )


def loadFinancialInfo(filepath: str) -> DataFrame:
    """
    Loads CSV as pandas.DataFrame.

    Bad filepath ->
    Bad file schema (missing columns) ->
    """
    return read_csv(
        filepath,
        sep=',',  # type:ignore
        usecols=['id', 'btc_a', 'cc_t', 'cc_n'],
        dtype={
            'id': int,
            'btc_a': str,
            'cc_t': str,
            'cc_n': str,
        }
    )


def filterRowsByCountry(df: DataFrame, countries: List[str]) -> DataFrame:
    """
    Filter DataFrame rows by country.
    """
    return df[df['country'].isin(countries)]


def selectIdAndEmail(df: DataFrame) -> DataFrame:
    """
    Remove personal identifiable information from the first dataset, excluding emails and id.
    """
    return df[['id', 'email']]


def dropCreditCardNumber(df: DataFrame) -> DataFrame:
    """
    Remove column with credit card number.
    """
    return df.drop('cc_n', axis=1)  # type:ignore


def innerJoin(df1: DataFrame, df2: DataFrame, key: List[str]):
    """Inner join datasets on key(s)"""
    return df1.merge(df2, how='inner', on=key)


def renameColumns(df: DataFrame):
    mapper: Dict[str, str] = {
        'id': 'client_identifier',
        'btc_a': 'bitcoin_address',
        'cc_t': 'credit_card_type',
    }
    return df.rename(columns=mapper)  # type:ignore


def main(
    path_to_personal_info_file: str,
    path_to_financial_info_file: str,
    countries_to_filter: List[str],
):
    """
    Load datasets, filter them, select their columns, merge them, and rename the final columns.
    """
    client_info = loadPersonalInfo(filepath=path_to_personal_info_file)
    if countries_to_filter:
        client_info = filterRowsByCountry(client_info, countries_to_filter)  # type:ignore
    client_info = selectIdAndEmail(client_info)  # type:ignore

    financial_info = loadFinancialInfo(filepath=path_to_financial_info_file)
    financial_info = dropCreditCardNumber(financial_info)  # type:ignore

    result = innerJoin(client_info, financial_info, ['id'])
    return renameColumns(result)


if __name__ == '__main__':
    parser = ArgumentParser(description="Join personal and financial datasets with an optional country filter.")
    parser.add_argument(
        '--path-to-personal-info-file',
        dest='path_to_personal_info_file',
        required=True,
        help="CSV file with the following fields: 'id', 'email', 'country'.",
    )
    parser.add_argument(
        '--path-to-financial-info-file',
        dest='path_to_financial_info_file',
        required=True,
        help="CSV file with the following fields: 'id', 'btc_a', 'cc_t', 'cc_n'.",
    )
    parser.add_argument(
        '--countries-to-filter',
        dest='countries_to_filter',
        nargs='+',
        default=[],
        help="Optional list of countries to filter clients.",
    )
    args = parser.parse_args()
    result = main(
        path_to_personal_info_file=args.path_to_personal_info_file,
        path_to_financial_info_file=args.path_to_financial_info_file,
        countries_to_filter=args.countries_to_filter
    )

    result.to_csv(sys.stdout, index=False)  # type:ignore
