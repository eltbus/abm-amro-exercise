import pytest

from app.core import (
    load_personal_info,
    load_financial_info,
    filter_rows_by_country,
    select_id_and_email,
    drop_credit_cardnumber,
    inner_join,
    rename_columns,
)


def test_load_personal_info_raises_ValueError_if_missing_required_columns():
    with pytest.raises(ValueError):
        load_personal_info('data/financial_info.csv')


def test_load_personal_info_raises_ValueError_if_missing_filepath():
    with pytest.raises(FileNotFoundError):
        load_personal_info('data/non_existing_file.csv')


def test_load_financial_info_raises_ValueError_if_missing_required_columns():
    with pytest.raises(ValueError):
        load_financial_info('data/personal_info.csv')


def test_load_financial_info_raises_ValueError_if_missing_filepath():
    with pytest.raises(FileNotFoundError):
        load_financial_info('data/non_existing_file.csv')


def test_filter_rows_by_country_returns_empty_Dataframe_if_country_not_in_DataFrame(personal_info):
    """
    TODO: Ejemplo para demostrar que funciona.
    """
    result = filter_rows_by_country(personal_info, countries=['ZZZ'])
    assert len(result) == 0


def test_filter_rows_by_country_returns_two_rows_for_countries_AAA_and_BBB(personal_info):
    """
    TODO: Ejemplo para demostrar que funciona.
    """
    result = filter_rows_by_country(personal_info, countries=['AAA', 'BBB'])
    assert len(result) == 2


def test_select_id_and_email_returns_columns_id_and_email(personal_info):
    """
    TODO: Ejemplo para demostrar que funciona.
    """
    result = select_id_and_email(personal_info)
    assert 'id' in result.columns and 'email' in result.columns


def test_select_id_and_email_raises_error_if_columns_id_and_email_dont_exist(personal_info):
    """
    TODO: Ejemplo para demostrar que funciona.
    """
    # Remove columns
    personal_info = personal_info.drop(['id', 'email'], axis=1)
    with pytest.raises(KeyError):
        select_id_and_email(personal_info)


def test_drop_credit_cardnumber_raises_error_if_column_cc_n_doesnt_exist(financial_info):
    """
    TODO: Ejemplo para demostrar que funciona.
    """
    # Remove columns
    financial_info = financial_info.drop(['cc_n'], axis=1)
    with pytest.raises(KeyError):
        drop_credit_cardnumber(financial_info)


@pytest.mark.parametrize('col', ['id', 'email', 'btc_a', 'cc_n'])
def test_inner_join_returns_DataFrame_with_expected_columns(personal_info, financial_info, col):
    """
    TODO: Ejemplo para demostrar que funciona.
    """
    result = inner_join(personal_info, financial_info, key=['id'])
    assert col in result.columns


@pytest.mark.parametrize('col', ['client_identifier', 'bitcoin_address', 'credit_card_type'])
def test_rename_columns_returns_DataFrame_with_expected_columns(personal_info, financial_info, col):
    """
    TODO: Ejemplo para demostrar que funciona.
    """
    result = inner_join(personal_info, financial_info, key=['id'])
    result = rename_columns(result)
    assert col in result
