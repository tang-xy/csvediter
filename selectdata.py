import csv
import pandas as pd
import os
import xlrd
import sqlite3

con_list = ['采掘业','传媒','电力','房地产','建筑','交通','农','批发零售','社会服务','信息技术','制造业','综合']
conn = sqlite3.connect(R"D:\Documents\政府经济\2019.3.22\text.db3")

for con in con_list:

    c = conn.cursor()
    sql ='''
    SELECT 利润表{0}.Stkcd,利润表{0}.Accper,B001101000,B002000000,C001000000,A001111000,A001212000,A001000000
FROM 利润表{0},现金流量表{0},资产负债表{0}
WHERE (利润表{0}.Stkcd = 现金流量表{0}.Stkcd
AND 利润表{0}.Stkcd = 资产负债表{0}.Stkcd
AND 利润表{0}.Accper = 现金流量表{0}.Accper
AND 利润表{0}.Accper = 资产负债表{0}.Accper)
AND 利润表{0}.Typrep = 'A' 
AND 现金流量表{0}.Typrep = 'A'
AND 资产负债表{0}.Typrep = 'A'
AND (利润表{0}.Accper = '2013-01-01' OR 利润表{0}.Accper = '2014-01-01' OR 利润表{0}.Accper = '2015-01-01' OR 利润表{0}.Accper = '2016-01-01' OR 利润表{0}.Accper = '2017-01-01')
    '''.format(con)
    res = c.execute(sql)
    with open(R"D:\Documents\政府经济\result_2\\" + con + '.csv', 'w', encoding='utf-8') as f:
        write = csv.writer(f)
        write.writerow(["利润表{0}.Stkcd".format(con), '利润表{0}.Accper'.format(con),'B001101000','B002000000','C001000000','A001111000','A001212000','A001000000'])
        for line in res:
            write.writerow(line)
