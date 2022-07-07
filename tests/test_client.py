from app import create_api
from fastapi.testclient import TestClient

api = create_api()
client = TestClient(api)


def test_marketing_push_targets_raises_error_if_no_files_not_uploaded():
    response = client.post("/marketing_push_targets")
    assert response.status_code == 400
    assert response.json() == {'message': 'No personal_info file sent'}


def test_marketing_push_targets_raises_error_and_identifies_personal_info_as_the_missing_file(financial_info_file):
    response = client.post(
        "/marketing_push_targets",
        files={
            'financial_info': financial_info_file,
        }
    )
    assert response.status_code == 400
    assert response.json() == {'message': 'No personal_info file sent'}


def test_marketing_push_targets_raises_error_and_identifies_financial_info_as_the_missing_file(personal_info_file):
    response = client.post(
        "/marketing_push_targets",
        files={
            'personal_info': personal_info_file,
        }
    )
    assert response.status_code == 400
    assert response.json() == {'message': 'No financial_info file sent'}
