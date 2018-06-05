from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
Base.__table_args__ = {"mysql_engine": "InnoDB"}
