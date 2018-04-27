from tigereye.configs.default import DefaultConfig


class TestConfig(DefaultConfig):
    TESTING = True
    # 从内存中读取 测试用
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SQLALCHEMY_ECHO = False