import sqlite3
from pydaisi import Daisi
import pandas as pd

daisi = Daisi("Sales Forecaster", base_url="https://dev3.daisi.io")

salesdb = sqlite3.connect("../sales-data/Sales.db")
df = pd.read_sql_query(
    """
    SELECT Date as ds, sum(Sale_dollars) as y
    FROM Sales
    GROUP BY ds
    ORDER BY ds asc
    """,
    salesdb,
)

f = daisi.forecast(10)
