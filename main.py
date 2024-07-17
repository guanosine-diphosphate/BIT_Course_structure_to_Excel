import pandas as pd
from bs4 import BeautifulSoup


def process(file: str):
    f = open(file, 'r', encoding="utf-8").read()
    # print(f)
    soup = BeautifulSoup(f, 'html.parser')
    trs = soup.find_all('tr')
    # print(trs[1])
    colums_raw = trs[1].find_all('th')
    colums = []
    for colum in colums_raw:
        colums.append(colum.text)
    courseList = []
    for tr in trs:
        course = []
        tds = tr.find_all('td')
        for td in tds:
            course.append(td.text)
        courseList.append(course)
    courseList = courseList[2:]
    return (courseList, colums)


def writeExcel(input):
    courseList = input[0]
    colums = input[1]
    print(colums)
    pd_list = pd.DataFrame(courseList, columns=colums)
    pd_list.to_excel('培养方案.xlsx', index=False)


if __name__ == '__main__':
    data = process("html.txt")
    writeExcel(data)
