import pyodbc


server = 'localhost\\SQLEXPRESS'
database = 'flaskblog'
username = 'nbar'
password = 'nb'

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = conn.cursor()

def regionalWind(x,y):
    cmd =  "select "+ x +" from dbo.RegionalWind where speed="+y+";"  
    cursor.execute(cmd)
    rows = cursor.fetchone()
    for row in rows:
        return row

def importanceLevels(x,y):
    cmd =  "select "+ x +" from dbo.ImportanceLevels where Importance="+y+";"  
    cursor.execute(cmd)
    rows = cursor.fetchone()
    for row in rows:
        return row

def terrainCats(x,y):
    cmd =  "select "+ x +" from dbo.terrainCat where heightZ="+y+";"  
    cursor.execute(cmd)
    rows = cursor.fetchone()
    for row in rows:
        return row

