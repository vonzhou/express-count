#encoding:utf-8
"""
Read from dataset.txt and dump data to specific express type 
such as shunfeng.txt

"""

import sys
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

for exp in exp_list:
	# print exp
	temp = open(exp, 'w')
	temp.seek(0)
	exp_files[exp] = temp


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
		# print exp_name
		if exp_name not in exp_set:
			exp_set.add(exp_name)
			temp = open(exp_name, 'w')
			temp.seek(0)
			exp_files[exp_name] = temp

		# print 'write line to ', exp_name 
		fi = exp_files[exp_name]

		areas = line[(k+1):-1]
		# if flag:
		# 	fi.write('\t\t'+ current_city + ':\n')
		# 	flag = False
		# print '|||'+areas
		# area_list = areas.split(',')
		fi.write('\t\t' + areas + '\n')


for afile in exp_files.values():
	afile.flush()

for afile in exp_files.values():
	afile.close()

out = open('sum.txt', 'w')
exp_files2 = dict()
for afilename in exp_set:
	afile = open(afilename, 'r')
	exp_files2[afilename] = afile
	out.write(afile.name + ':\n')
	for line in afile:
		# print 'line:', line
		out.write('\t'+line)
out.flush()
out.close()

for afile in exp_files2.values():
	afile.close()


