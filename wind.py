import pyodbc


server = 'localhost\SQLEXPRESS'
database = 'flaskblog'
username = 'nbar'
password = 'nb'

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = conn.cursor()
cmd= "select B from dbo.RegionalWind where speed = '2000';"
cursor.execute(cmd)
rows = cursor.fetchone()

Speed = 0
A = 1
W = 2
B = 3
C = 4
D = 5
for row in rows:
    print(row)

#Speed Factors
wFive = 0
wTen = 1
wTwenty = 2
def factors(x,y):
    for row in rows:
        print(row)

    
    # def headOffenders(jobChosen):
    #     findJob = "select * from dbo.Projects where ProjectNo='"+str(jobChosen)+"';"
    #     cursor.execute(findJob)
    #     row = cursor.fetchone()