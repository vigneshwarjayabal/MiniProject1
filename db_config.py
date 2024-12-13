from sqlalchemy import create_engine

def get_db_connection():
    engine = create_engine(
        "postgresql+psycopg2://postgres:dhoni00728@miniprojectdb.cv8yqowiopcb.ap-south-1.rds.amazonaws.com:5432/postgres"
    )
    return engine.connect()
