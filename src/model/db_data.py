from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("")
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)