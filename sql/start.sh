#/opt/mssql-tools/bin/sqlcmd -U sa -P $1 -Q 'CREATE DATABASE didarul'
#/opt/mssql-tools/bin/sqlcmd -U sa -P $1 -d 'didarul' -i /usr/src/app/sql.sql
/opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P SuperP4ssw0rd! -d master -i /usr/src/app/sql.sql