import os

app_dir = os.path.abspath(os.path.dirname(__file__))
baseDB = os.path.join(app_dir, 'app.db')


class Config(object):
    CSRF_ENABLED = True

    SECRET_KEY = os.environ['SECRET_KEY']

    JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + baseDB

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.yandex.ru'

    MAIL_PORT = 465

    MAIL_USE_TLS = False

    MAIL_USE_SSL = True

    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'YOU_MAIL@yandex.ru'

    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'password'

    MAIL_DEFAULT_SENDER = MAIL_USERNAME

    PAGINATE_PAGE_SIZE = 5

    PAGINATE_PAGE_PARAM = 'page'

    PAGINATE_SIZE_PARAM = 'size'

    PAGINATE_RESOURCE_LINKS_ENABLED = True

    PAGINATE_PAGINATION_OBJECT_KEY = None

    PAGINATE_DATA_OBJECT_KEY = 'results'
