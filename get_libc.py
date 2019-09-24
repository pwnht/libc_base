#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from pwn import *
from get_json import *
import signal
import time
context.log_level='critical'
elf = './pwn100'
io = None
start = True
stop = False
status=start
def in_num(address):
	try:
		return num.index(address)
	except:
		return -1
def get_libc_base():
	io = process(elf)
	address = io.libc.address
	io.close()
	return address
def signal_handler(signum, frame):
	print '---------------'
	print 'it is time to save'
	print '---------------'
	save(data,da_name)
def main():
	global init
	signal.signal(signal.SIGALRM, signal_handler)
	signal.alarm(3000)
	if init==0:
		while (len(num) <10):
			address = get_libc_base()
			try:
				num.index(address)
			except:
				num.append(address)
			update(address)
		init=1
		config['init']=1
		save(config,'./json/config.json')
		sort()
		print '--------------------'
		print 'save data'
		print '--------------------'
		init_top()
		save(top,top_name)
	while (status):
		address = get_libc_base()
		update(address)
		number = get_count(address)
		index = in_num(address)
		if index == -1:
			if number > get_count(num[9]):
				num[9] = address
				sort()
				up_top()
				save(top,top_name)
				print '--------------------'
				print 'top change'
				print '--------------------'
				continue
		sort()
if __name__=='__main__':

	main()

