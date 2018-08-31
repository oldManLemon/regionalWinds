import pyodbc

from settings import server, database,username,password,conn
# server = server
# database = database
# username = username
# password = password
# conn = conn
# cursor = conn.cursor()

server = 'localhost\\SQLEXPRESS'
database = 'flaskblog'
username = 'nbar'
password = 'nb'

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = conn.cursor()
#    """  if table == '1':
#         table = "dbo.RegionalWind"
#         cmd = "select " + x + "from " + table + "where speed ="+y+";"
#         return """
#I'm learning to deal with clasess so this may be silly but is what it is
# class Lookup:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

    
#     def regionalWind(x,y):
#         cmd =  "select "+ x +" from dbo.RegionalWind where speed="+y+";"  
#         cursor.execute(cmd)
#         rows = cursor.fetchone()
#         for row in rows:
#             return row
    
#     def importanceLevels(x,y):
#         cmd =  "select "+ x +" from dbo.ImportanceLevels where speed="+y+";"  
#         cursor.execute(cmd)
#         rows = cursor.fetchone()
#         for row in rows:
#             return row


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






#region1 = regionalWind('C','25')
#print(region1)
