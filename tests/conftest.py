import pytest
from pandas import DataFrame


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
