import logging
import os
from neo4j import GraphDatabase
from dotenv import load_dotenv

load_dotenv()

URI = os.getenv("NEO4J_URI")
AUTH = (os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))

driver = GraphDatabase.driver(URI, auth=AUTH)


def create_query(llm_query):
    try:
        session = driver.session()
        query = llm_query
        records = session.run(query)
        record_dict = []
        for record in records:
            record_dict.append(record.data())
        return record_dict

    except Exception as e:
        logging.exception(f"Error: {e}")
        raise

    finally:
        if session:
            session.close()
        driver.close()
