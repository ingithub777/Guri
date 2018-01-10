import urllib.request
from pandas import DataFrame
import os
import xml.etree.ElementTree as ET

result = []
response = urllib.request.urlopen('http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s'%(urllib.parse.quote('전체'),urllib.parse.quote('전체')))

xml = response.read().decode('UTF-8')
root = ET.fromstring(xml)

for element in root.findall('item'):
    store_name = element.findtext('aname1')
    store_sido = element.findtext('aname2')
    store_gungu = element.findtext('aname3')
    store_address = element.findtext('aname5')

    result.append([store_name]+[store_sido]+[store_gungu]+[store_address])

nene_table = DataFrame(result,columns=('sotre','sido','gungu','store_address'))

if os.path.isdir("E:\python.warkspace\Guri\XML\V2_BigData"):
    if os.path.isdir("E:\python.warkspace\Guri\XML\V2_BigData/Name_Data1"):
        if os.path.isfile('E:\python.warkspace\Guri\XML\V2_BigData/Name_Data1/nene1.csv'):

            if os.path.isfile("E:\python.warkspace\Guri\XML\V2_BigData\count.txt"):
                count_number = open("E:\python.warkspace\Guri\XML\V2_BigData\count.txt", 'r')
                count = str(count_number.readline())
                count_number.close()
                nene_table.to_csv('nene%s.csv' % count, encoding="cp949", mode='w', index=True)
                count = int(count) + 1
                count = str(count)
                count_number_new = open("E:\python.warkspace\Guri\XML\V2_BigData\count.txt", 'w')
                count_number_new.write(count)
                count_number_new.close()
                count = int(count)

            else:
                make_count = open("E:\python.warkspace\Guri\XML\V2_BigData\count.txt",'a')
                data = '2'
                make_count.write(data)
                make_count.close()
                count_number = open("E:\python.warkspace\Guri\XML\V2_BigData\count.txt", 'r')
                count = str(count_number.readline())
                count_number.close()
                nene_table.to_csv('nene%s.csv' % count, encoding="cp949", mode='w', index=True)
                count = int(count) + 1
                count = str(count)
                count_number_new = open("E:\python.warkspace\Guri\XML\V2_BigData\count.txt", 'w')
                count_number_new.write(count)
                count_number_new.close()
else:
    os.mkdir("E:\python.warkspace\Guri\XML\V2_BigData")
    os.mkdir("E:\python.warkspace\Guri\XML\V2_BigData/Name_Data1")
    nene_table.to_csv('E:\python.warkspace\Guri\XML\V2_BigData/Name_Data1/nene1.csv', encoding="cp949", mode='w', index=True)



    # if count == "11":
    #     if os.path.isfile("E:\python.warkspace\Guri\XML\V2_BigData/nene10.csv"):
    #         os.system("mkdir Name_Data")
    #         if os.path.isfile("E:\python.warkspace\Guri\XML\V2_BigData/Name_Data/nene10.csv"):
    #             count_number = open("E:\python.warkspace\Guri\XML\V2_BigData/Name_Data/nene10.csv", 'r')
    #             count = str(count_number.readline())
    #             count_number.close()
    #             nene_table.to_csv('nene%s.csv' % count, encoding="cp949", mode='w', index=True)
    #             count = int(count) + 1
    #             count = str(count)
    #         else:
    #             nene_table.to_csv('E:\python.warkspace\Guri\XML\V2_BigData/Name_Data/nene10.csv', encoding="cp949", mode='w',
    #                               index=True)

    # if count >= 3:
    #     if os.path.isfile("E:\python.warkspace\Guri\XML\V2_BigData/nene3.csv"):
    #         os.system("mkdir Name_Data")
    #         if os.path.isfile("E:\python.warkspace\Guri\XML\V2_BigData/Name_Data/nene10.csv"):
    #             count_number = open("E:\python.warkspace\Guri\XML\V2_BigData/Name_Data/nene10.csv", 'r')
    #             count = str(count_number.readline())
    #             count_number.close()
    #             nene_table.to_csv('nene%s.csv' % count, encoding="cp949", mode='w', index=True)
    #             count = int(count) + 1
    #             count = str(count)
    #         else:
    #             nene_table.to_csv('E:\python.warkspace\Guri\XML\V2_BigData/Name_Data/nene3.csv', encoding="cp949", mode='w', index=True)