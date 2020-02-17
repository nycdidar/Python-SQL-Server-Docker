import pyodbc
import pandasql as ps
from flask import Flask, render_template, jsonify,request,make_response
import pandas as pd

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

# Copy to Clipboard for paste in Excel sheet
def copia (argumento):
    df=pd.DataFrame(argumento)
    df.to_clipboard(index=False,header=True)


@app.route('/')
def index():
    cnxn = pyodbc.connect(conn)
    cursor = cnxn.cursor()
    print ('Using the following SQL Server version:')
    #tsql = "SELECT @@version;"
    tsql = "SELECT * FROM dbo.Customers"
    df = pd.read_sql(tsql, cnxn)
    
    with cursor.execute(tsql):
        row = cursor.fetchone()
        response = make_response(str(row), 200)
        response.headers["Content-Type"] = "application/json"
        return jsonify({"Name": str(df.head) + ' ' + str(row[1])})

