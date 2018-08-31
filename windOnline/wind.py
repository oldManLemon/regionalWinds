import pyodbc
import math
import tableWorker

server = 'localhost\\SQLEXPRESS'
database = 'flaskblog'
username = 'nbar'
password = 'nb'

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = conn.cursor()

""" Data Expected """

#Region
#Importance
#TerrainCat
#Md=
#Kc=
#HightEves
#HeightRidge

Region = 'A'
Importance = '2' #1 needs two option s
TerrainCat = 'TerrainCat3'
Md = 0.95
Kc = 1
HeightRidge=10.5
EavesHeight=15.5
HeightRidge = int(math.ceil(HeightRidge))
EavesHeight = int(math.ceil(EavesHeight))
#print(HeightRidge)

#Table Work
Vs = tableWorker.regionalWind(Region,'25')
VuNumber = tableWorker.importanceLevels('[Non Cyclonic]',Importance)
Vu = tableWorker.regionalWind(Region, str(VuNumber))
mCatRidge = tableWorker.terrainCats(TerrainCat,str(HeightRidge))
mCatEaves =tableWorker.terrainCats(TerrainCat,str(EavesHeight))
serviceR = float(Vs)*mCatRidge
serviceE = float(Vs)*mCatEaves
serviceR = int(round(serviceR))
serviceE = int(round(serviceE))
ultimateR = float(Vu)*mCatRidge*1*1*Md
ultimateE = float(Vu)*mCatEaves*1*1*Md
ultimateE = int(round(ultimateE))
ultimateR = int(round(ultimateR))
pressureServiceR = (0.6 * serviceR**2/1000)



print('Vs=', Vs)
print('Vu=', Vu)
print('mzCat Rdige', mCatRidge)
print('mzCat Eaves', mCatEaves)
print('Serivce Ridge', serviceR)
print('Serivce Eaves', serviceE)
print('Ultimate Ridge', ultimateR)
print('Utlimate Eaves', ultimateE)
print(pressureServiceR)







""" print(test)
test = float(test)
print("mzcat = "+ (test * 0.84)) """
#print(37*0.84)

