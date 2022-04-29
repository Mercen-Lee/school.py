'''
school.py v1.0 developed by Seok Ho Lee
(A.K.A. Mercen Lee)

Github : https://github.com/Mercen-Lee
Tistory : https://mercen.net/
'''
preKey = 'INSERT YOUR API KEY HERE'

from requests import get
apiUrl = 'https://open.neis.go.kr/hub/'
apiKey = 'Info?KEY='+preKey+'&Type=json&'

def School(schoolName):
    schoolJson = get(apiUrl+'/school'+apiKey+'SCHUL_NM='+schoolName).json()
    schoolInfo = schoolJson['schoolInfo'][1]['row'][0]
    schoolBase = 'ATPT_OFCDC_SC_CODE='+schoolInfo['ATPT_OFCDC_SC_CODE']
    schoolCode = '&SD_SCHUL_CODE='+schoolInfo['SD_SCHUL_CODE']
    return schoolBase,schoolCode

def Meal(schoolName,mealCode,mealDate):
    schoolBase,schoolCode = School(schoolName)
    mealName = '&MLSV_YMD='+str(mealDate)+'&MMEAL_SC_CODE='+str(mealCode)
    mealJson = get(apiUrl+'mealServiceDiet'+apiKey+schoolBase+schoolCode+mealName).json()
    return mealJson['mealServiceDietInfo'][1]['row'][0]['DDISH_NM'].replace('<br/>','\n')

def classCrawl(schoolName,schoolGrade,schoolClass,classDate):
    schoolBase,schoolCode = School(schoolName)
    if schoolName.endswith('초등학교'): schoolLevel = 'elsTimetable'
    elif schoolName.endswith('중학교'): schoolLevel = 'misTimetable'
    elif schoolName.endswith('고등학교'): schoolLevel = 'hisTimetable'
    className = '&GRADE='+str(schoolGrade)+'&CLASS_NM='+str(schoolClass)+'&ALL_TI_YMD='+str(classDate)
    classJson = get(apiUrl+schoolLevel+apiKey[4:]+schoolBase+schoolCode+className).json()
    return classJson[schoolLevel][1]['row']

def Class(schoolName,schoolGrade,schoolClass,classTime,classDate):
    classJson = classCrawl(schoolName,schoolGrade,schoolClass,classDate)
    return classJson[classTime-1]['ITRT_CNTNT'].replace('-','')

def ClassAll(schoolName,schoolGrade,schoolClass,classDate):
    classJson = classCrawl(schoolName,schoolGrade,schoolClass,classDate); classList = ''
    for i in range(20):
        try: classList += str(i+1)+'교시 - '+classJson[i]['ITRT_CNTNT'].replace('-','')+'\n'
        except: break
    return classList[:-1]
