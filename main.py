from typing import List, Dict

from pandas import DataFrame


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
