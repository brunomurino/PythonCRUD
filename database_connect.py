import sqlalchemy as sql
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import inspect

def runQuery(query, connect_string = 'mysql+mysqlconnector://root:password@localhost/EINSTEIN'):

    engine = sql.create_engine(connect_string)
    
    with engine.connect() as con:

        rs = con.execute(query)
        if (rs.returns_rows):
            return rs.fetchall(), rs.keys()
        return "No rows to show."
               