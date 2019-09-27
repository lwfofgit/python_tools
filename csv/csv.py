# coding:utf-8
import csv
import logging
import hashlib

# 去掉csv文件中，重复的行
def quchong(file):
    ciku = open(r'full.csv', 'r')  # 打开需要去重文件，可自行修改
    xieci = open(r'full_1.csv', 'w')  # 打开处理后存放的文件
    cikus = ciku.readlines()
    list2 = {}.fromkeys(cikus).keys()  # 列表去重方法，将列表数据当作字典的键写入字典，依据字典键不可重复的特性去重
    i = 1
    for line in list2:
        if line[0] != ',':
            # print line[0:-1].decode('utf-8').encode('gbk')  # 数据量太多，会出现编码报错。蛋疼
            # print u"写入第：" + i + u" 个"
            print()
            i += 1
            xieci.writelines(line)
    xieci.close()


# 把列表或是dic转换成csv文件存储到当前脚本目录，列表里存的是json对象
def transform_to_csv(data, path):
    csvfile = open(path + '.csv', 'wb')
    writer = csv.writer(csvfile)
    if not data:
        logging.error("transform_to_csv->data:None")
        return
    if isinstance(data, list):
        writer.writerow(data[0].keys())
        for item in data:
            writer.writerow(item.values())
    elif isinstance(data, dict):
        writer.writerow(data.keys())
        writer.writerow(data.values())
    csvfile.close()


def get_application_id_list(path):
    csvFile = open(path, "r")
    reader = csv.reader(csvFile)

    # 建立空字典
    result = []
    i = 0
    for item in reader:
        # 忽略第一行
        if reader.line_num == 1:
            continue
        i = i + 1
        if len(result) == 100:
            break
        if item[1] == 'jpg' or item[3] == 'jpeg':
            result.append(item[2])
    csvFile.close()
    print(len(result))
    print(result)

# 读取csv文件中时间 item[1] 第二列
def get_application_id_list(path):
    csvFile = open(path, "r")
    reader = csv.reader(csvFile)

    # 建立空字典
    result = []
    i = 0
    for item in reader:
        # 忽略第一行
        if reader.line_num == 1:
            continue
        i = i + 1
        if item[1] == 'jpg' or item[3] == 'jpeg':
            result.append(item[2])
    csvFile.close()
    print(len(result))
    print(result)

if __name__ == '__main__':
    # path = '/Users/liwenfeng/work/csv/collect_resume_new.csv'
    # get_application_id_list(path)
    path = '/Users/liwenfeng/work/hunter_domian.csv'
    # get_hunter_domain_from_csv(path)
    import request