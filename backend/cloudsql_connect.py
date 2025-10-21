import os
from google.cloud.sql.connector import Connector
import sqlalchemy


def get_engine():
    connector = Connector()

    def getconn():
        conn = connector.connect(
            os.environ["INSTANCE_CONNECTION_NAME"],
            "pg8000",
            user=os.environ["POSTGRES_USER"],
            password=os.environ.get("CLOUD_DB_PASSWORD"),
            db=os.environ["POSTGRES_DB"],
        )
        return conn

    engine = sqlalchemy.create_engine(
        "postgresql+pg8000://",
        creator=getconn,
        pool_size=5,
        max_overflow=2,
        pool_pre_ping=True,
    )
    return engine
