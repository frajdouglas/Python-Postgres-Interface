import pyodbc
import random
import pandas as pd


class PostGresConnector:
    user = ""
    password = ""
    postgres_driver = ""
    server = ""
    database = ""
    port = 0
    conn_string = ""
    conn = "" # pyodbc connection
    cursor = "" # pyodbc connection cursor

    def __init__(self,
                 user,
                 password,
                 server,
                 database,
                 port
                 ):
        """
        Create PostGresConnector class detailing Postgres connection details
        and create cursor object to enable queries to be sent to database.

        Parameters
        ------
        user:
            Username of database user.
        password:
            Password of database user.
        server:
            Server address.
        database:
            Postgres database name.
        port:
            Port.

        Returns
        ------
        print("Connection Successful"):
            Print will show if successfully connected, error will show if
            connection failed.
        """
        self.user = user
        self.password = password
        self.postgres_driver = '{PostgreSQL Unicode}'
        self.server = server
        self.database = database
        self.port = port
        self.conn_string = ('driver=' + self.postgres_driver +
                ';server=' + self.server +
                ';database=' + self.database +
                ';uid=' + self.user +
                ';pwd=' + self.password +
                ';port=' + self.port +
                ';sslmode=require'
                )
        self.conn = pyodbc.connect(self.conn_string)
        self.cursor = self.conn.cursor()
        print("Connection Successful")


    def query(self,
              query_file):
        """
        Send query stores in text file to Postgres Database and return result
        in pandas.Dataframe format

        Parameters
        ------
        self:
            Connection details specified in constructor.
        
        query_file:
            File with query stored in it. Example: 

        Returns
        ------
        query_result:
            Requested data in pandas.DataFrame format.
        """
        query_text = open(
            r'' + query_file,'r')
        read_text = query_text.read()
        query_result = pd.read_sql_query(read_text,self.conn)
        return(query_result)
    

    
