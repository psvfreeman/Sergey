print("OK")
import re
snl=[]
with open("C:\\Repository\python.ry") as f:
	while True:
			s = f.readline()
			if s== "":
				break
			sn = re.sub('^\s{2,5}',' '*4,s)
			snl += [sn]
print (snl)
with open ("C:\\Repository\python.ry","w") as f:
    f.writelines(snl)
    print(snl)

