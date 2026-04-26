import os
import pandas as pd
from databricks import sql

def run_query(query):
    conn = sql.connect(
        server_hostname="dbc-6dbe4321-f3d1.cloud.databricks.com",
        http_path="/sql/1.0/warehouses/d0a173fa756955f0",
        access_token="dapia70dc060cf578c7cb84785a71d624c39"
)

    cursor = conn.cursor()
    cursor.execute(query)

    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]

    df = pd.DataFrame(rows, columns=columns)

    cursor.close()
    conn.close()

    return df