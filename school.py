'''
school.py v1.3 developed by Seok Ho Lee
(A.K.A. Mercen Lee)
Github : https://github.com/Mercen-Lee
Tistory : https://mercen.net/
'''
from urllib.request import urlopen; from urllib.parse import quote
from json import loads; from re import sub; from datetime import datetime as dt

class School:
    toDate = dt.now().strftime('%Y%m%d')
    def __init__(self,Token=None,Name=None,Grade=None,Class=None,Date=toDate,Meal=2):
        self.apiUrl = 'https://open.neis.go.kr/hub/'; self.apiKey = 'Info?KEY='+Token+'&Type=json&'
        for x in ['Name','Grade','Class','Date','Meal']: exec('self.'+x+'='+x)

    def Info(self):
        infoLink = self.apiUrl+'/school'+self.apiKey+'SCHUL_NM='+quote(self.Name)
        infoJson = loads(urlopen(infoLink).read())['schoolInfo'][1]['row'][0]
        infoBase = 'ATPT_OFCDC_SC_CODE='+infoJson['ATPT_OFCDC_SC_CODE']
        infoCode = '&SD_SCHUL_CODE='+infoJson['SD_SCHUL_CODE']; return infoBase,infoCode

    def Timetable(self):
        infoBase,infoCode = self.Info()
        if self.Name.endswith('초등학교'): schoolLevel = 'elsTimetable'
        elif self.Name.endswith('중학교'): schoolLevel = 'misTimetable'
        elif self.Name.endswith('고등학교'): schoolLevel = 'hisTimetable'
        timeName = '&GRADE='+str(self.Grade)+'&CLASS_NM='+str(self.Class)+'&ALL_TI_YMD='+str(self.Date)
        timeLink = self.apiUrl+schoolLevel+self.apiKey[4:]+infoBase+infoCode+timeName
        timeJson = loads(urlopen(timeLink).read())[schoolLevel][1]['row']; timeTable = []
        for x in timeJson: timeTable.append(sub('[-,:.*]','',x['ITRT_CNTNT']).strip()); return timeTable

    def Meals(self):
        infoBase,infoCode = self.Info()
        mealName = '&MLSV_YMD='+str(self.Date)+'&MMEAL_SC_CODE='+str(self.Meal)
        mealLink = self.apiUrl+'mealServiceDiet'+self.apiKey+infoBase+infoCode+mealName; meals = []
        mealJson = loads(urlopen(mealLink).read())['mealServiceDietInfo'][1]['row'][0]['DDISH_NM']
        for x in mealJson.split('<br/>'): meals.append(sub('[-,:.* ]','',x).split('(')[0]); return meals
