from aip import AipOcr

MYSQL_DATABASE_URL = 'mysql+pymysql://root:root@localhost:3306/anyi?charset=utf8'
SQLALCHEMY_ECHO = False
MYSQL_POOL_RECYCLE = 30
MYSQL_POOL_TIMEOUT = 30
SECRET_KEY = 'you-will-never-guess'

APP_ID = '11466403'
API_KEY = 'lEGZXRphGMwGr4UFsyudODEm'
SECRET_KEY = 'GTaPvMbI3u1KPPg436Xv48fGE7MyuDYO'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
