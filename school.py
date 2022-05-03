'''
school.py v1.2 developed by Seok Ho Lee
(A.K.A. Mercen Lee)
Github : https://github.com/Mercen-Lee
Tistory : https://mercen.net/
'''
from urllib.request import urlopen; from urllib.parse import quote
from json import loads; from re import sub

class School:
    def __init__(self,token):
        self.apiUrl = 'https://open.neis.go.kr/hub/'
        self.apiKey = 'Info?KEY='+token+'&Type=json&'

    def Info(self,schoolName):
        infoLink = self.apiUrl+'/school'+self.apiKey+'SCHUL_NM='+quote(schoolName)
        infoJson = loads(urlopen(infoLink).read())['schoolInfo'][1]['row'][0]
        infoBase = 'ATPT_OFCDC_SC_CODE='+infoJson['ATPT_OFCDC_SC_CODE']
        infoCode = '&SD_SCHUL_CODE='+infoJson['SD_SCHUL_CODE']
        return infoBase,infoCode

    def Class(self,schoolName,schoolGrade,schoolClass,classDate):
        infoBase,infoCode = self.Info(schoolName)
        if schoolName.endswith('초등학교'): schoolLevel = 'elsTimetable'
        elif schoolName.endswith('중학교'): schoolLevel = 'misTimetable'
        elif schoolName.endswith('고등학교'): schoolLevel = 'hisTimetable'
        className = '&GRADE='+str(schoolGrade)+'&CLASS_NM='+str(schoolClass)+'&ALL_TI_YMD='+str(classDate)
        classLink = self.apiUrl+schoolLevel+self.apiKey[4:]+infoBase+infoCode+className
        classJson = loads(urlopen(classLink).read())[schoolLevel][1]['row']; classList = []
        for x in classJson: classList.append(sub('[-,:.*]','',x['ITRT_CNTNT']).strip())
        return classList

    def Meal(self,schoolName,mealCode,mealDate):
        infoBase,infoCode = self.Info(schoolName)
        mealName = '&MLSV_YMD='+str(mealDate)+'&MMEAL_SC_CODE='+str(mealCode)
        mealLink = self.apiUrl+'mealServiceDiet'+self.apiKey+infoBase+infoCode+mealName; mealList = []
        mealJson = loads(urlopen(mealLink).read())['mealServiceDietInfo'][1]['row'][0]['DDISH_NM']
        for x in mealJson.split('<br/>'): mealList.append(sub('[-,:.* ]','',x).split('(')[0])
        return mealList
