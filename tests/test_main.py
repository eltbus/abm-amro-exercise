import pytest

from pandas import DataFrame

from main import loadPersonalInfo, loadFinancialInfo, filterRowsByCountry


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


def test_filterByCountry_correctly_returns_two_rows_for_countries_AAA_and_BBB(personal_info):
    """
    TODO: Ejemplo para demostrar que funciona.
    """
    result = filterRowsByCountry(personal_info, countries=['AAA', 'BBB'])
    assert len(result) == 2
