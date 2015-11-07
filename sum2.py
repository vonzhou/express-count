# -*- coding: UTF-8 -*-
"""
Read from dataset.txt and dump data to specific express type 
such as shunfeng.txt

"""

import sys
import simplejson
# from xpinyin import Pinyin
reload(sys)
sys.setdefaultencoding('utf-8')


exp_set = set()
current_city = 'not a city'
pre_city = ''
flag = True
exp_list = ['优速快递', '安能物流','快捷快递','新邦物流', '天地华宇', '速尔快递', '宅急送', '国通快递', 
		'飞豹快递', '广通速递', '增益速递', '邮政国内','全峰快递', '龙邦速运', '佳吉快递', '中通快递', 
		'韵达快递', '顺丰快递', '德邦', '天天快递', '汇通快递', '申通快递', '圆通快递', 'EMS']

exp_files = dict()
exp_set = set(exp_list)
area_set = set()

f = open('dataset.txt', 'r')
for line in f:
	line = line.strip()
	if line.startswith('+++'):
		pass
	else:
		# print line
		#write this line to XXX file
		k = line.find(':')
		exp_name = line[:k]
		# print exp_name
		if exp_name not in exp_set:
			exp_set.add(exp_name)

exp_set_dict = {}
count = 0
for e in exp_set:
	# print e, count
	exp_set_dict[unicode(e, 'utf-8')] = count
	count = count + 1	
	f = open(str(count)+'.txt', 'w')	
	exp_files[e] = f


f = open('dataset.txt', 'r')
for line in f:
	line = line.strip()
	if line.startswith('+++'):
		i = line.find('[')
		j = line.find(']')
		current_city = line[(i+1):j]
		flag = True
	else:
		# print line
		#write this line to XXX file
		k = line.find(':')
		exp_name = line[:k]
		
		fi = exp_files[exp_name]

		areas = line[(k+1):-1]
		area_list = areas.split(',')
		for a in area_list:
			i=a.find('(')
			j = a.find(')')
			if a != '' and i != -1 :
				this_area = a[:i]
				if this_area not in area_set:
					area_set.add(this_area)
		fi.write('\t\t' + areas + '\n')



N = exp_set_dict.__len__()
area_set_dict = {}
count = 0
for a in area_set:
	# print a, count
	area_set_dict[unicode(a,'utf-8')] = count
	count = count + 1
M = area_set_dict.__len__()

print 'Matrix:',M,N
Matrix = [[0 for x in range(M)] for x in range(N)] 

id_area_dict = {}
for k in area_set_dict.keys():
	print k, area_set_dict[k]
	id_area_dict[area_set_dict[k]] = k


# print type(Matrix)
# print (Matrix[0]).__len__()
# print 'tttttttttttttt',exp_set_dict[unicode('宅急送', 'utf-8')]

exp_files2 = dict()
row1 = []
for afilename in exp_set:
	
	afile = open(afilename, 'r')
	exp_files2[afilename] = afile
	# print afilename, afile.mode

	for line in afile:
		# print afilename, line.strip()
		area_list = line.strip().split(',')
		for a in area_list:
			i=a.find('(')
			j = a.find(')')
			if a != '' and i != -1 :
				this_area = a[:i]
				this_area_count = a[i+1:j]
				# print ':::',afile.name, this_area, this_area_count
				col = exp_set_dict[unicode(afile.name, 'utf-8')] 
				row = area_set_dict[unicode(this_area, 'utf-8')]
				# print row, col, this_area_count
				Matrix[col][row] = this_area_count
				

out = open('sum.txt', 'w')
for e in exp_set:
	out.write('\t'+e)
out.write('\n')

for a in area_set:
	out.write(a)

	for ee in exp_set:
		col = exp_set_dict[unicode(ee, 'utf-8')]
		row = area_set_dict[unicode(a, 'utf-8')]
		count = Matrix[col][row]
		out.write('\t'+str(count))
	out.write('\n')


out.flush()
out.close()

for afile in exp_files2.values():
	afile.close()


