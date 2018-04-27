from tigereye.configs.default import DefaultConfig
class ProductConfig(DefaultConfig):

    DEBUG = False
    TESTING =False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost/tigereye1703'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO =False
    JSON_SORT_KEYS=False
