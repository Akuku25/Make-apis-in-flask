import os

class Config(object):
    """Parent configuration class"""
    DEBUG = True
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


class DevelopmentConfig(Config):
    """Configurations for development environment"""
    DEBUG = True

class StagingConfig(Config):
    """Staging environment configurations"""
    DEBUG = True

class ProductionConfig(Config):
    """Configurations for production environment"""
    DEBUG = False
    TESTING = False

app_config = {
    'development' : DevelopmentConfig,
    'staging' : StagingConfig,
    'production' : ProductionConfig,
}