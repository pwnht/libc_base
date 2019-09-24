import json
import os
config=json.load(file('./json/config.json'))
pre_name=config['data_name']
init=config['init']
index=0
da_name=pre_name[index]
top_name=config['top_name']
num=[]
add      =  lambda address    :data.update({hex(address):1})
save     =  lambda dicr,file       :json.dump(dicr,open(file,'w'),sort_keys=True, indent=4, separators=(',', ':'))
get_index= lambda address :(address%0x10000000000)/0x1000000000
def get_count(address):
	write_in_file(address)
	return data[hex(address)]
def load(file_name):
	try:
		return json.load(file(file_name))
	except:
		f=open(file_name,'w')
		f.write('{}')
		f.close()
	return json.load(file(file_name))
def update(address):
	write_in_file(address)
	try:
		data[hex(address)]+=1
	except:
		add(address)
def get_top():
    address = []
    for i in range(1,11):
        address.append(top[str(i)])
    count_number = []
    for i in address:
	write_in_file(int(i,16))
        count_number.append(data[i])
    return address,count_number
def up_top():
    j=1
    for i in num:
        top[str(j)]=hex(i)
        j+=1

def write_in_file(address):
	global index
	global data
	global da_name
	if index!=get_index(address):
		save(data,da_name)
		index=get_index(address)
		da_name=pre_name[index]
		data=load(da_name)
def init_top():
	j=1
	for i in num:
		top.update({str(j):hex(i)})
		j+=1
def sort():
	num_count=[]
	for i in num:
		num_count.append(get_count(i))
	num_count.sort()
	for i in num_count:
		for j in num:
			if i==get_count(j):
				k=num_count.index(i)
				n=num.index(j)
				temp=num[k]
				num[k]=num[n]
				num[n]=temp
				
data=load(da_name)
top=load(top_name)

