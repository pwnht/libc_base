import os
import datetime
while True:
    try:
        os.system('python get_libc.py')
    except:
	now=datetime.datetime.new()
        print 'Error in:'+datetime.datetime.strftime(now,'%Y-%m-%d %H:%M:%S')
        continue
