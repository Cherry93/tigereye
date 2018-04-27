import sys
import os
class DefaultConfig(object):

    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost/tigereye1703'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO =True
    BASEDIR = os.path.abspath(os.path.join(os.path.dirname(__file__),'../..'))
    LOG_DIR = os.path.join(BASEDIR,'logs')

