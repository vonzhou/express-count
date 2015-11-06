"""
Count expresses in Hubei areas
http://www.kuaidi100.com/network/net_4201_all_all_1.htm  wuhan
http://www.kuaidi100.com/network/net_4202_all_all_1.htm huangshi
3 shiyan
XXX
5 yichang
xiangyang
e zhou
jingmen
xiaogan
jingzhou
huanggang
xianning
13 suizhou
http://www.kuaidi100.com/network/net_4228_all_all_1.htm enshi
http://www.kuaidi100.com/network/net_4254_all_all_1.htm  xiantao
http://www.kuaidi100.com/network/net_4255_all_all_1.htm  qianjiang
http://www.kuaidi100.com/network/net_4256_all_all_1.htm  tianmen
http://www.kuaidi100.com/network/net_4271_all_all_1.htm  shengnongjia



"""

from lxml import html
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

code_base = 4201
url_main= 'http://www.kuaidi100.com/network'
url_base = 'http://www.kuaidi100.com/network/net_'
url_tail = "_all_all_1.htm"
exp_area_dict = {}

city_code_dict = {"wuhan":4201, 'huangshi':4202, 'shiyan':4203, 'yichang':4205,
'xiangyang':4206, 'ezhou':4207, 'jingmen':4208,'xiaogan':4209, 'jingzhou':4210,
'huanggang':4211, 'xianning':4212, 'suizhou':4213,'enshi':4228, 'xiantao':4254,
'qianjiang':4255, 'tianmen':4256, 'shengnongjia':4271}

f = open('dataset.txt', 'w')

def getCityData(url_str):
    page = requests.get(url_str)
    tree = html.fromstring(page.content)

    selectbox = tree.xpath('//dl[@class="dl-select"]')

    # Type of expresses

    area = selectbox[0]
    datas = area.xpath('//dd/a')

    # The URL of express-type is net_4201_all_XX ...

    flag = True
    for r in datas:
        ref = r.attrib.get('href')
        exp_name = str(r.text)
        i = exp_name.find('(')
        exp_name = exp_name[:i]
        if ref != None:
            #ignore /network/
            myString = ref[9:]
            subs = myString.split('_')

            if subs[2] == 'all' and flag:
                type_url = url_main + ref
                f.write(exp_name + ':')
                type_page = requests.get(type_url)
                type_tree = html.fromstring(type_page.content)
                dlarea = type_tree.xpath('//dl[@class="dl-select"]')
                table = dlarea[0]
                datas = table.xpath('//dd/a')
                # Detect the nums in the areas
                for data in datas:
                    area_name = str(data.text)
                    ref = data.attrib.get('href')
                    # print '-----', text,ref
                    if area_name != None and ref != None:
                        i = area_name.find('(')
                        if i != -1:
                            myString = ref[9:]
                            subs = myString.split('_')
                            if subs[2] != 'all':
                                # exp_area_dict[exp_name]
                                f.write(area_name + ',')
                f.write('\n')
                # exp_area_dict[str(r.text)] = ref;
            else:
                flag = False


for city, code in city_code_dict.iteritems():
    tmp = url_base + str(city_code_dict[city]) + url_tail;
    f.write('+++++['+ city + ']+++++\n');
    getCityData(tmp)

f.close()




    # print exp_area_dict.keys()




#llls
