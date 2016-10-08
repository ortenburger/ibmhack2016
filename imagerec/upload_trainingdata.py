#!/usr/bin/env python3
import zipfile
import os
from subprocess import call

trainingsname='mushrooms'

def zipit(src, dst):
	zf = zipfile.ZipFile("%s.zip" % (dst), "w", zipfile.ZIP_DEFLATED)
	abs_src = os.path.abspath(src)
	print(src)
	print(dst)
	for dirname, subdirs, files in os.walk(src):
		for filename in files:
			print('Zipping: ' + filename)
			absname = os.path.abspath(os.path.join(dirname, filename))
			arcname = absname[len(abs_src) + 1:]
			zf.write(absname, arcname)
	zf.close()

shroomslist = next(os.walk('buildtrainingdata'))[1]

fileslist= ''
for i in shroomslist:
	print(i)
	fileslist = fileslist +' -F "' + i + '_positive_examples=@' + i + '.zip"'
	zipit('buildtrainingdata/' + i, i)
print(
	'-X POST '+ fileslist +
	' -F "name=' + trainingsname +'" '+
	'"https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classifiers?api_key={b12a413b8f731dca6878744f8455b764f3c9e24b}&version=2016-05-20"'
)

"""
call(['curl -X POST '+ fileslist +
	' -F "name=' + trainingsname +'" '+
	'"https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classifiers?api_key={b12a413b8f731dca6878744f8455b764f3c9e24b}&version=2016-05-20"'])
"""
