import pandas as pd
import os
import codecs

flist=os.listdir('./findjob')

data=[]
for textfile in flist:
    if textfile=='.ipynb_checkpoints':
        continue
    with open('./findjob/%s' %(textfile),'r',encoding='utf-8',) as f:

        data_str=f.read().split('===========================================')[2]
        data_row=data_str.split('\n')[1:-1]   #轉成串列
        data.append(data_row)
#        print(data_row)
#        print(data_str)
#    print('********************')

columns=['公司名稱','職位名稱','工作待遇','工作地點','工作經歷','科系要求','語言條件','linux','MySQL','Java','Python','AWS','LAN','MS SQL','C#','PHP','Github','JavaScript']
df=pd.DataFrame(data=data,columns=columns)

def tmpfilter(s):
    result=s.split(':')[1]
    return result

for c in columns:
    df[c] = df[c].apply(lambda s: s.split(':')[1])


df.to_csv('./findjob.csv',index=False,encoding='utf-8-sig')  #要用utf-8-sig轉出，才不會打開CSV檔亂碼




