# my first python program! Hi! Are we learning git yet? 
import sys
for line in sys.stdin:
	line=line.strip()
	idx=line.find('a')
	if idx !=-1:
		print line[idx:]



