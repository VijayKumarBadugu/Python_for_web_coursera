import re
import sys
file_des = open(sys.argv[1],"r")
total =0
for line in file_des:
	num_list = re.findall('[0-9]+',line)
	num_list = map(int, num_list)
	total = total +	sum((num_list))
print total
