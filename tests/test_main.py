import pytest

from pandas import DataFrame

from main import (
    loadPersonalInfo,
    loadFinancialInfo,
    filterRowsByCountry,
    selectIdAndEmail,
    dropCreditCardNumber,
    innerJoin,
    renameColumns,
)


@pytest.fixture
def personal_info():
    data = {
        'id': [i for i in range(5)],
        'email': [
            'aaa@foo.com',
            'bbb@bar.com',
            'ccc@spam.com',
            'ddd@eggs.com',
            'eee@bazz.com',
        ],
        'country': [
            'AAA',
            'BBB',
            'CCC',
            'DDD',
            'EEE',
        ]
    }
    return DataFrame(data=data)


@pytest.fixture
def financial_info():
    data = {
        'id': [i for i in range(5)],
        'btc_a': [
            '001xfoos',
            '002xbars',
            '0x01spam',
            '013xeggs',
            '010xbazz',
        ],
        'cc_t': [
            'visa',
            'mastercard',
            'visa',
            'mastercard',
            'supercard',
        ],
        'cc_n': [
            '00123456789',
            '00986421135',
            '12385162788',
            '23456123819',
            '12345679654',
        ]
    }
    return DataFrame(data=data)


def test_loadPersonalInfo_raises_ValueError_if_missing_required_columns():
    with pytest.raises(ValueError):
        loadPersonalInfo('data/financial_info.csv')


def test_loadPersonalInfo_raises_ValueError_if_missing_filepath():
    with pytest.raises(FileNotFoundError):
        loadPersonalInfo('data/non_existing_file.csv')


def test_loadFinancialInfo_raises_ValueError_if_missing_required_columns():
    with pytest.raises(ValueError):
        loadFinancialInfo('data/client_info.csv')


def test_loadFinancialInfo_raises_ValueError_if_missing_filepath():
    with pytest.raises(FileNotFoundError):
        loadFinancialInfo('data/non_existing_file.csv')


def test_filterByCountry_returns_empty_Dataframe_if_country_not_in_DataFrame(personal_info):
    """
    TODO: Ejemplo para demostrar que funciona.
    """
    result = filterRowsByCountry(personal_info, countries=['ZZZ'])
    assert len(result) == 0


def test_filterByCountry_returns_two_rows_for_countries_AAA_and_BBB(personal_info):
    """
    TODO: Ejemplo para demostrar que funciona.
    """
    result = filterRowsByCountry(personal_info, countries=['AAA', 'BBB'])
    assert len(result) == 2


def test_selectIdAndEmail_returns_columns_id_and_email(personal_info):
    """
    TODO: Ejemplo para demostrar que funciona.
    """
    result = selectIdAndEmail(personal_info)
    assert 'id' in result.columns and 'email' in result.columns


def test_selectIdAndEmail_raises_error_if_columns_id_and_email_dont_exist(personal_info):
    """
    TODO: Ejemplo para demostrar que funciona.
    """
    # Remove columns
    personal_info = personal_info.drop(['id', 'email'], axis=1)
    with pytest.raises(KeyError):
        selectIdAndEmail(personal_info)


def test_dropCreditCardNumber_raises_error_if_column_cc_n_doesnt_exist(financial_info):
    """
    TODO: Ejemplo para demostrar que funciona.
    """
    # Remove columns
    financial_info = financial_info.drop(['cc_n'], axis=1)
    with pytest.raises(KeyError):
        dropCreditCardNumber(financial_info)


@pytest.mark.parametrize('col', ['id', 'email', 'btc_a', 'cc_n'])
def test_innerJoin_returns_DataFrame_with_expected_columns(personal_info, financial_info, col):
    """
    TODO: Ejemplo para demostrar que funciona.
    """
    result = innerJoin(personal_info, financial_info, key=['id'])
    assert col in result.columns


@pytest.mark.parametrize('col', ['client_identifier', 'bitcoin_address', 'credit_card_type'])
def test_renameColumns_returns_DataFrame_with_expected_columns(personal_info, financial_info, col):
    """
    TODO: Ejemplo para demostrar que funciona.
    """
    result = innerJoin(personal_info, financial_info, key=['id'])
    result = renameColumns(result)
    assert col in result
