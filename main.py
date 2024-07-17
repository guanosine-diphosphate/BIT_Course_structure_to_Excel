from bs4 import BeautifulSoup
import pandas as pd
def process(file:str):
    f=open(file,'r',encoding="utf-8").read()
    # print(f)
    soup = BeautifulSoup(f,'html.parser')
    trs=soup.find_all('tr')
    courseList=[]
    for tr in trs:
        course=[]
        tds=tr.find_all('td')
        for td in tds:
            course.append(td.text)
        courseList.append(course)
    courseList=courseList[2:]
    return courseList
def writeExcel(courseList):
    colums="序号,开课学期,课程编号,课程名称,开课单位,学分,总学时,考核方式,课程属性,课程性质,是否考试".split(',')
    print(colums)
    pd_list=pd.DataFrame(courseList,columns=colums)
    pd_list.to_excel('培养方案.xlsx',index=False)
if __name__ == '__main__':
    data=process("html.txt")
    writeExcel(data)
