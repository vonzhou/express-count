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
	exp_files[exp] = temp

multilist = [[0 for col in range(200)] for row in range(30)]	
areas_list = [0 for col in range(200)]

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
			#exp_files[exp_name] = open(exp_name, 'w')
		lie = exp_set.index(expname)
		# print 'write line to ', exp_name 
		#fi = exp_files[exp_name]

		areas = line[(k+1):]
		newstr = areas
		kk = newstr.find("(")
		while kk >= 0:
			area = newstr[:kk-1]
			if area not in area_list:
				area_list.add(area)
			hang = area_list.index(area)
			newstr = newstr[newstr.find("(")+1:]    #这样一致到newstr里面不包含a为止
			kkk = newstr.find(")")
			multilist[hang][lie] = newstr[:kkk-1]
			newstr = newstr[newstr.find(",")+1:]    
		#area_list = areas.split(',')
		#for a in area_list:
			# print a
		#	fi.write(current_city + '-' + areas + '\n')
print("	")
for a in exp_list:
	print(a, end="	")
i = 0	
for b in area_list:
	print(b, end="	")
	for j in rang(0,29):
		print(multilist[i][j], end="	")
	print("\n")
	i=i+1
#for f in exp_files.values():
#	f.close()


