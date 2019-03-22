import csv
import pandas as pd
import os
import xlrd
import sqlite3
CREATE = False

def xlsx_to_csv(filename,outname):
    workbook = xlrd.open_workbook(filename)
    table = workbook.sheet_by_index(0)
    with open(outname, 'w', encoding='utf-8') as f:
        write = csv.writer(f)
        for row_num in range(table.nrows):
            row_value = table.row_values(row_num)
            write.writerow(row_value)

def xlsx_to_csv_pd(filename,outname):
    data_xls = pd.read_excel(filename, index_col=0)
    data_xls.to_csv(outname, encoding='utf-8')

def adddb(csvname,conn):
    c = conn.cursor()
    with open(csvname, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        (filepath,tempfilename) = os.path.split(csvname)
        (shotname,extension) = os.path.splitext(tempfilename)
        if CREATE == False:
            sql = '''CREATE TABLE ''' + shotname +'''
            (id int primary key 
            '''
            for line in reader:
                for l in line:
                    sql = sql + "," + l + " text\n" 
                break
            sql += ")"
            c.execute(sql)
            conn.commit()
        i = 1
        for line in reader:
            break
        for line in reader:
            break
        for line in reader:
            sql = '''INSERT
                INTO ''' + shotname + '''
             VALUES(
            ''' + str(i)
            for l in line:
                sql = sql + ",'" + l + "'"
            sql += ')'
            c.execute(sql)
            i+=1
            print(i)
        
        conn.commit()
    print("success!")

def gci(filepath):
#遍历filepath下所有文件，包括子目录
    conn = sqlite3.connect(R"D:\Documents\政府经济\2019.3.22\text.db3")
    files = os.listdir(filepath)
    for fi in files:
        fi_d = os.path.join(filepath,fi)            
        if os.path.isdir(fi_d):
            filexlsxs = os.listdir(fi_d)
            for x in filexlsxs:
                low_files=os.path.splitext(os.path.join(fi_d,x))
                filename,types=low_files
                if(types == ".xlsx"):
                    filename = os.path.join(fi_d,x)
                    break
            outname = os.path.join(R"D:\Documents\政府经济\db",fi + ".csv")     
            xlsx_to_csv_pd(filename,outname)
            adddb(outname,conn)
        else:
            print(os.path.join(filepath,fi_d))

gci(R"D:\Documents\政府经济\2019.3.22")