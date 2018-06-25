from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import config

base = declarative_base()

engine = create_engine(config.MYSQL_DATABASE_URL,
                       convert_unicode=True,
                       echo=config.SQLALCHEMY_ECHO,
                       pool_recycle=config.MYSQL_POOL_RECYCLE,
                       pool_timeout=config.MYSQL_POOL_TIMEOUT,)


Session = sessionmaker(autoflush=False, bind=engine)



