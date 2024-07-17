# import pandas as pd
from bs4 import BeautifulSoup
from pandas import DataFrame


def process(file: str):
    f = open(file, 'r', encoding="utf-8").read()
    # print(f)
    soup = BeautifulSoup(f, 'html.parser')
    trs = soup.find_all('tr')
    # print(trs[1])
    try:
        columns_raw = trs[1].find_all('th')
        columns = []
        for colum in columns_raw:
            columns.append(colum.text)
        course_list = []
        for tr in trs:
            course = []
            tds = tr.find_all('td')
            for td in tds:
                course.append(td.text)
            course_list.append(course)
        course_list = course_list[2:]
    except IndexError:
        print("Make sure the html.txt isn't empty")
        input("Press Enter to continue...")
        return None

    return course_list, columns


def write_excel(input):
    course_list, columns = input
    pd_list = DataFrame(course_list, columns=columns)
    pd_list.to_excel('培养方案.xlsx', index=False)


if __name__ == '__main__':
    data = process("html.txt")
    if data is not None:
        write_excel(data)
    else:
        print("Failed to Process the txt file")
