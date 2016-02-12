# my first python program! 
import sys
for line in sys.stdin:
	line=line.strip()
	idx=line.find('a')
	if idx !=-1:
		print line[idx:]



