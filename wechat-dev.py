word = ["选择文件", "确认[y/n]", "无此选项", "加载中", "工作表中无数据"]
subject=["语文","数学","英语","科学","社会"]
havedata = []
print(word[3])
import glob
import os

import wxpy
import xlrd


def searchf():
    files = []
    types = ("*.xls", "*.xlsx")
    for typesc in types:
        for filess in glob.glob(typesc):
            files.insert(0, filess)
    return files
# 文件检索


def checkf(files):
    s = 0
    word = ["请选择文件:", "超出可选范围", "请输入数值"]
    for fileshow in files:
        s = s+1
        print("[", s, "]", fileshow)
    while True:
        try:
            discion = input(word[0])
            discion = int(discion)-1
            return files[discion]
        except IndexError:
            print(word[1])
        except ValueError:
            print(word[2])
# 文件选择(user)


def section(data, thing, itable=0):
    success = []
    data = xlrd.open_workbook(data)
    if isinstance(itable, list):
        for i in itable:
            table = data.sheet_by_index(int(i))
            nrows = table.nrows
            ncols = table.ncols
            for r in range(nrows):
                for c in range(ncols):
                    cell = table.cell(r, c).value
                    if cell == thing:
                        success.insert(0, r)
                        success.insert(1, c)
                        success.insert(2, i)
                        return success
    else:
        table = data.sheet_by_index(int(itable))
        nrows = table.nrows
        ncols = table.ncols
        for r in range(nrows):
            for c in range(ncols):
                cell = table.cell(r, c).value
                if cell == thing:
                    success.insert(0, r)
                    success.insert(1, c)
                    success.insert(2, itable)
                    return success


files = searchf()
if len(files) == 1:
    print(word[0], files[0])
    dis = input(word[1])
    if dis == "y":
        dis = files[0]
    elif dis == "n":
        pass
    else:
        print(word[2])
elif len(files) > 1:
    dis = checkf(files)
else:
    raise FileNotFoundError("Can not find files")
# 单文件处理
data = xlrd.open_workbook(dis)
for searchda in range(data.nsheets):
    try:
        table = data.sheet_by_index(searchda)
        nrows = table.nrows
        if nrows == 0:
            searchda = searchda+1
            print(searchda, word[4])
        else:
            havedata.insert(0, searchda)
    except IndexError:
        continue
# 寻找有数据工作表
if len(havedata) < 1:
    raise IndexError("No data")
# 无效文件退出
success = section(dis, "姓名", havedata)
# 寻找姓名
table = data.sheet_by_index(success[2])
namelist = table.col_values(success[1])
namelist.pop(0)
#姓名列表输出
tabell=success[2]
Chinese=section(dis,subject[0],tabell)
Math=section(dis,subject[1],tabell)
English=section(dis,subject[2],tabell)
Science=section(dis,subject[3],tabell)
History=section(dis,subject[4],tabell)
Csorelist=table.sheet_by_index(Chinese[1])
Msorelist=table.sheet_by_index(Math[1])
Esorelist=table.sheet_by_index(English[1])
Ssorelist=table.sheet_by_index(Science[1])
Hsorelist=table.sheet_by_index(History[1])
#取出成绩
sore=[namelist,Csorelist,Msorelist,Esorelist,Ssorelist,Hsorelist]