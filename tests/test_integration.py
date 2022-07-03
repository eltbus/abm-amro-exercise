from pandas import DataFrame

from main import main


def test_main_returns_expected_result_for_sample_with_country_AAA(personal_info, financial_info, mocker):
    mocker.patch('main.loadPersonalInfo', return_value=personal_info)
    mocker.patch('main.loadFinancialInfo', return_value=financial_info)

    sample_data = {
        'client_identifier': [0],
        'email': ['aaa@foo.com'],
        'bitcoin_address': ['001xfoos'],
        'credit_card_type': ['visa'],
    }

    expected = DataFrame(data=sample_data)
    result = main('...', '...', countries_to_filter=['AAA'])
    assert expected.equals(result)


# TODO: assert filter is NOT called if countries to filter is empty
