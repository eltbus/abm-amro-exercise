from pandas import DataFrame

from app.core import pipeline


def test_pipeline_returns_expected_result_for_sample_with_country_AAA(
    personal_info_file, financial_info_file
):
    sample_data = {
        "client_identifier": [0],
        "email": ["aaa@foo.com"],
        "bitcoin_address": ["foos"],
        "credit_card_type": ["visa"],
    }

    expected = DataFrame(data=sample_data)
    result = pipeline(personal_info_file, financial_info_file, countries_to_filter=["AAA"])
    assert expected.equals(result)


# TODO: assert filter is NOT called if countries to filter is empty
