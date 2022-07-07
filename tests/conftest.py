from tempfile import SpooledTemporaryFile

import pytest
from pandas import DataFrame


@pytest.fixture
def client_ids():
    return [i for i in range(5)]


@pytest.fixture
def emails():
    return [
        "aaa@foo.com",
        "bbb@bar.com",
        "ccc@spam.com",
        "ddd@eggs.com",
        "eee@bazz.com",
    ]


@pytest.fixture
def countries():
    return [
        "AAA",
        "BBB",
        "CCC",
        "DDD",
        "EEE",
    ]


@pytest.fixture
def btc_accounts():
    return [
        "foos",
        "bars",
        "spam",
        "eggs",
        "bazz",
    ]


@pytest.fixture
def creditcard_types():
    return [
        "visa",
        "mastercard",
        "visa",
        "mastercard",
        "supercard",
    ]


@pytest.fixture
def creditcard_numbers():
    return [
        "00123456789",
        "00986421135",
        "12385162788",
        "23456123819",
        "12345679654",
    ]


def lines(*args, sep=','):
    for i in zip(*args):
        yield sep.join(map(str, i))


@pytest.fixture
def personal_info_file(client_ids, emails, countries):
    with SpooledTemporaryFile(mode='w+') as w:
        header = ','.join(['id', 'email', 'country'])
        w.write(f'{header}\n')
        data = '\n'.join(list(lines(client_ids, emails, countries)))
        w.write(data)
        w.seek(0)
        yield w


@pytest.fixture
def financial_info_file(client_ids, btc_accounts, creditcard_types, creditcard_numbers):
    with SpooledTemporaryFile(mode='w+') as w:
        header = ','.join(['id', 'btc_a', 'cc_t', 'cc_n'])
        w.write(f'{header}\n')
        data = '\n'.join(list(lines(client_ids, btc_accounts, creditcard_types, creditcard_numbers)))
        w.write(data)
        w.seek(0)
        yield w


@pytest.fixture
def personal_info(client_ids, emails, countries):
    data = {
        "id": client_ids,
        "email": emails,
        "country": countries,
    }
    return DataFrame(data=data)


@pytest.fixture
def financial_info(client_ids, btc_accounts, creditcard_types, creditcard_numbers):
    data = {
        "id": client_ids,
        "btc_a": btc_accounts,
        "cc_t": creditcard_types,
        "cc_n": creditcard_numbers,
    }
    return DataFrame(data=data)
