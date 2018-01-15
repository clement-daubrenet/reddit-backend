class Development(object):
    DEBUG = False

    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:postgres@localhost/postgres'


class Testing(object):
    DEBUG = False

    SQLALCHEMY_DATABASE_URI = 'postgres://user:pass@test/my_database'


class Production(object):
    DEBUG = False

    SQLALCHEMY_DATABASE_URI = 'postgres://user:pass@prod/my_database'
