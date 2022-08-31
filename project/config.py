class BaseConfig:
    TESTING = False

class DevelopmentConfig: 
    """Develoment Configuration"""
    pass

class TestingConfig: 
    """Testing Configuration"""
    pass 

class ProductionConfig(BaseConfig):
    """Production configuration"""
    pass