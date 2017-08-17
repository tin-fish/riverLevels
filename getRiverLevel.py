#!/usr/bin/python
import urllib2
import re
from datetime import datetime
try:
	m=open('prevRiverLevel.dat','r')
	past = m.read().splitlines()
	m.close()
except:
	past=[]
url="https://flood-warning-information.service.gov.uk/station/7270"
HTML = urllib2.urlopen(url)
t = HTML.read().splitlines()
thisreadingmetric=""
for l in reversed(t):
	readingdate=re.match("\s+<td scope=\"row\"><time datetime=\"([\dT.\-:]+)Z\">([\dT.\-:]+)Z<\/time><\/td>",l)
	readingmetric=re.match("\s+<td class=\"numeric\">([\d.]+)<\/td>",l)
	if readingmetric:
		thisreadingmetric=readingmetric.group(1)
	if readingdate:
		thisreadingdate=readingdate.group(1)
		line = thisreadingdate+" "+str(thisreadingmetric)
		if not line in past:
			print line
			m=open('prevRiverLevel.dat','a')
			m.write(line+"\n")
			m.close
