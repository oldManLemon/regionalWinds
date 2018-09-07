import pyodbc
import math
import sys
sys.path.append("F:/windForms")
#import windOnline
import windOnline.tableWorker
#import windOnline
#import tableWorker


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
def windCalcs(HeightRidge,EavesHeight,Region,Importance,TerrainCat,Md,Kc):
    HeightRidge = int(math.ceil(HeightRidge))
    EavesHeight = int(math.ceil(EavesHeight))
    #print(HeightRidge)

    #Table Work
    Vs = windOnline.tableWorker.regionalWind(Region,'25')
    if Importance == '1C':
         VuNumber = windOnline.tableWorker.importanceLevels('[Cyclonic]','1')
    elif Importance == '1N':
         VuNumber = windOnline.tableWorker.importanceLevels('[Non Cyclonic]','1')
    else:

        VuNumber = windOnline.tableWorker.importanceLevels('[Non Cyclonic]',Importance)
    #print("Vus",VuNumber)    
    Vu = windOnline.tableWorker.regionalWind(Region, str(VuNumber))
    #print('Md', Md)
    mCatRidge = windOnline.tableWorker.terrainCats(TerrainCat,str(HeightRidge))
    mCatEaves =windOnline.tableWorker.terrainCats(TerrainCat,str(EavesHeight))

    #Calc Work
    serviceR = float(Vs)*mCatRidge
    serviceE = float(Vs)*mCatEaves
    serviceR = int(round(serviceR))
    serviceE = int(round(serviceE))
    ultimateR = float(Vu)*mCatRidge*1*1*float(Md)
    ultimateE = float(Vu)*mCatEaves*1*1*float(Md)
    ultimateE = int(round(ultimateE))
    ultimateR = int(round(ultimateR))
    pressureServiceR = (0.6 * serviceR**2/1000)


    return(Vs, Vu, mCatRidge,mCatEaves,serviceR,serviceE,ultimateR,ultimateR, pressureServiceR)
    #print('Vs=', Vs)
    #print('Vu=', Vu)
    #print('mzCat Rdige', mCatRidge)
    #print('mzCat Eaves', mCatEaves)
    #print('Serivce Ridge', serviceR)
    #print('Serivce Eaves', serviceE)
    #print('Ultimate Ridge', ultimateR)
    #print('Utlimate Eaves', ultimateE)
    #print('Pressure Serive Rdige Height',pressureServiceR)

# calcTest = windCalcs(HeightRidge,EavesHeight,Region,Importance,TerrainCat,Md,Kc)
# print('The Test',calcTest)
# print(calcTest[0])




""" print(test)
test = float(test)
print("mzcat = "+ (test * 0.84)) """
#print(37*0.84)

