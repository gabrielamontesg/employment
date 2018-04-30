'''
data_oes_unif: This program select and put together data of 
total employment per occupation per metropolitan area
from 2007 to 2017,
Gabriela Montes
04/28/2018 
'''


import pandas as pd
import numpy as np
import matplotlib as mplt

inpath='/Users/gmontes/Dropbox/JOBS/DATAINC/challenge2018/data_employment/'
#file1417='/Users/gmontes/Dropbox/JOBS/DATAINC/challenge2018/employment_evolution/oesdat_2014-2017.output.xlsx'
#completedata=pd.read_excel(file1417)


for i in range(14,18):
    print(f"=reading 20{i}===================================")
    dir=f'oesm{i}ma/'
    file=f'MSA_M20{i}_dl.xlsx'
    oesdat=pd.read_excel(inpath+dir+file)
    oesdat=oesdat[['PRIM_STATE','AREA_NAME', 'OCC_CODE', 'OCC_TITLE','TOT_EMP']]
    oesdat=oesdat[oesdat['OCC_CODE'].str.contains('-0000')].reset_index(drop=True)
    oesdat=oesdat.assign(YEAR=np.full(oesdat.shape[0], f'20{i}'))

    if i==14:
        completedata=oesdat
    else:
        print('append df')
        completedata=completedata.append(oesdat,ignore_index=True)

#outfile='oesdat_2014-2017.output.xlsx'
#print('Saving '+outfile+'...............')
#writer = pd.ExcelWriter(outfile)
#completedata.to_excel(writer)
#writer.save()    




for i in range(7,14):
    if i<10:
        yr=f'0{i}'
    else:
        yr=f'{i}'
    print(f"=reading 20{yr} ===================================")
    dir=inpath+f'oesm{yr}ma/'
    for j in range(1,4):
        file=dir+f'MSA_M20{yr}_dl_{j}.xls'
        print("reading file: "+file+".........")
        oesdat=pd.read_excel(file)
        oesdat=oesdat[['PRIM_STATE','AREA_NAME', 'OCC_CODE', 'OCC_TITLE','TOT_EMP']]
        #oesdat=oesdat.rename(index=str, columns={"GROUP": "OCC_GROUP"})
        oesdat=oesdat[oesdat['OCC_CODE'].str.contains('-0000')].reset_index(drop=True)
        oesdat=oesdat.assign(YEAR=np.full(oesdat.shape[0], f'20{yr}'))
        completedata=completedata.append(oesdat,ignore_index=True)

outfile='oesdat_2007-2017.output.xlsx'
print('Saving '+outfile+'...............')
writer = pd.ExcelWriter(outfile)
completedata.to_excel(writer)
writer.save()    

