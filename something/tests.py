import os
import sys
import uuid

import django
import pytest
from django.conf import settings
from New3.settings import BASE_DIR

if 'env setting':
    settings.configure()
    os.environ.setdefault('DJANGO_SETTING_MODULE', 'New3.settings')
    sys.path.append(BASE_DIR)
    django.setup()

from something.apps import SomethingConfig


@pytest.mark.parametrize('app', [SomethingConfig.name])
@pytest.mark.parametrize('expected', ['something'])
def test_app(app, expected):
    assert app == expected


@pytest.fixture()
def create_user(django_user_model, test_password):
    def make_user(**kwargs):
        kwargs['password'] = test_password
        if 'username' not in kwargs:
            kwargs['username'] = str(uuid.uuid4())
        return django_user_model.objects.create_user(**kwargs)

    return make_user


@pytest.fixture
def auto_login_user(client, create_user, test_password):
    def make_auto_login(user=None):
        if user is None:
            user = create_user()
        client.login(username=user.username, password=test_password)
        return client, user

    return make_auto_login

