# -*-coding:utf8-*-
from app import create_api

api = create_api()


if __name__ == '__main__':
    import yaml
    with open('openapi.yaml', 'w') as f:
        yaml.dump(api.openapi(), f, allow_unicode=True)
