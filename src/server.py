import pyodbc
from flask import Flask, request, make_response
app = Flask(__name__)

# Get Driver from cat /etc/odbcinst.ini

drivers = [item for item in pyodbc.drivers()]
driver = drivers[-1]
print("driver:{}".format(driver))
server = 'mssql'
database = 'Northwind'
uid = 'sa'
pwd = 'SuperP4ssw0rd!'
conn = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={uid};PWD={pwd}'

@app.route('/')
def index():
    cnxn = pyodbc.connect(conn)
    cursor = cnxn.cursor()
    print ('Using the following SQL Server version:')
    #tsql = "SELECT @@version;"
    tsql = "SELECT * FROM dbo.Customers"
    with cursor.execute(tsql):
        row = cursor.fetchone()
        response = make_response(str(row), 200)
        response.headers["Content-Type"] = "text/plain"
        return response
