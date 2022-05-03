'''
school.py v1.1 developed by Seok Ho Lee
(A.K.A. Mercen Lee)
Github : https://github.com/Mercen-Lee
Tistory : https://mercen.net/
'''
from requests import get; from re import sub

class School:
    def __init__(self,token):
        self.apiUrl = 'https://open.neis.go.kr/hub/'
        self.apiKey = 'Info?KEY='+token+'&Type=json&'

    def Info(self,schoolName):
        schoolJson = get(self.apiUrl+'/school'+self.apiKey+'SCHUL_NM='+schoolName).json()
        schoolInfo = schoolJson['schoolInfo'][1]['row'][0]
        schoolBase = 'ATPT_OFCDC_SC_CODE='+schoolInfo['ATPT_OFCDC_SC_CODE']
        schoolCode = '&SD_SCHUL_CODE='+schoolInfo['SD_SCHUL_CODE']
        return schoolBase,schoolCode

    def Class(self,schoolName,schoolGrade,schoolClass,classDate):
        schoolBase,schoolCode = self.Info(schoolName)
        if schoolName.endswith('초등학교'): schoolLevel = 'elsTimetable'
        elif schoolName.endswith('중학교'): schoolLevel = 'misTimetable'
        elif schoolName.endswith('고등학교'): schoolLevel = 'hisTimetable'
        className = '&GRADE='+str(schoolGrade)+'&CLASS_NM='+str(schoolClass)+'&ALL_TI_YMD='+str(classDate)
        classJson = get(self.apiUrl+schoolLevel+self.apiKey[4:]+schoolBase+schoolCode+className).json()
        classBase = classJson[schoolLevel][1]['row']; classList = []
        for x in classBase: classList.append(sub('[-,:.*]','',x['ITRT_CNTNT']).strip())
        return classList

    def Meal(self,schoolName,mealCode,mealDate):
        schoolBase,schoolCode = self.Info(schoolName)
        mealName = '&MLSV_YMD='+str(mealDate)+'&MMEAL_SC_CODE='+str(mealCode)
        mealJson = get(self.apiUrl+'mealServiceDiet'+self.apiKey+schoolBase+schoolCode+mealName).json()
        mealBase = mealJson['mealServiceDietInfo'][1]['row'][0]['DDISH_NM'].split('<br/>'); mealList = []
        for x in mealBase: mealList.append(sub('[-,:.* ]','',x).split('(')[0])
        return mealList
