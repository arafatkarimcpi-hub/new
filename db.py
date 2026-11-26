from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL="postgresql+psycopg2://db_yum6_user:BaguEVAgJZQ1rWRVzAGhIoBsqNXqp2D2@dpg-dc3s7pmc6qcc73bov03g-a.oregon-postgres.render.com/db_yum6"
engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
base = declarative_base()


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
