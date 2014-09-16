#!/usr/bin/python

import sys

cutting = False
for line in sys.stdin:
	if line.find("</pre>") >= 0:
		pos = line.find("</pre>")
		line = line[:pos] + line[pos + 6:]
	if cutting:
		if line.find(">"):
			cutting = False
			line = line[line.find(">") + 1:]
			sys.stdout.write(line)
	else:
		if line.find("<pre") >= 0:
			pos = line.find("<pre")
			if line.find(">",pos) > 0:
				line = line[:pos] + line[line.find(">",pos) + 1:]
			else:
				cutting = True
				line = line[:pos]
		sys.stdout.write(line)
sys.stdout.flush()
