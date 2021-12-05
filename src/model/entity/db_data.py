from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from flask_sqlalchemy import SQLAlchemy

# db_login = os.environ["POSTGRESQL_LOGIN"]
# db_pwd = os.environ["POSTGRESQL_PWD"]
# db_port = "5432"
# db_name = "flask_blog"
# db_host = "localhost"
#
# engine = create_engine(
#     f"postgresql://{db_login}:{db_pwd}@{db_host}:{db_port}/{db_name}"
# )
# Base = declarative_base(bind=engine)
# Session = sessionmaker(bind=engine)

db = SQLAlchemy()
__all__ = ("db",)