"""
Connects to a SQL database using pyodbc
DB Client is implemented using ObjectPool
"""
import pyodbc


# This will be our re-usable DB Client resource that the object pool will manage
# Tt will be a connection to cloud Microsoft Azure SQL Server database
class ReusableDBClient:
    # create the connection
    def __init__(self):
        self.__server = "tcp:qd-sqldb.database.windows.net,1433"
        self.__database = "QD-SQLDB"
        self.__user_name = "qd-admin"
        self.__password = "dce2ZbaMZ"

        try:
            self.__connection_string = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={self.__server};DATABASE={self.__database};UID={self.__user_name};PWD={self.__password};Encrypt=yes;TrustServerCertificate=no;'
            self.connection = pyodbc.connect(self.__connection_string)
            self.cursor = self.connection.cursor()
        except pyodbc.Error as err:
            print("Database Connection Error " + str(err))

    # close the connection when the object is deleted
    def __del__(self):
        self.cursor.close()
        self.connection.close()


# Manages the pool of objects, offers acquire and release operations to
# give the objects to client code and accept them back
class DBObjectPool:
    # initialize the pool... in our case, just one re-usable object
    def __init__(self):
        self.__reusables = [ReusableDBClient()]

    # give the resource to a client
    def acquire(self):
        return self.__reusables.pop()

    # accept the resource back from a client
    def release(self, reusable):
        self.__reusables.append(reusable)

    def close(self):
        for reusable in self.__reusables:
            del reusable
