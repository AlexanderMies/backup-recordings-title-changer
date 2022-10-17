
from xml.dom import minidom
import xml.etree.ElementTree as ET
import os
import shutil

#for every dir in YEAR
	#this dir's name = this dir's xml.title


# this was the path on one of the CVN machines, 
# but the path this should execute in might be 
# smb://SERVER_IP/cvnsyn_45b/Course Backups/2021 or something
path = '/Users/cvn-cc-9/Desktop/testEnv/2023/'
for folder, subfolders, files in os.walk(path):
	if folder != path:
		for f in files:
			if f.endswith(".xml"):
				xmlPath = os.path.join(folder,f)
				#pull DOM from xml
				dom = minidom.parse(xmlPath)
				#pull title from DOM
				title = dom.getElementsByTagName('Title')
				#get text in title and clean
				intendedName = title[0].firstChild.nodeValue
				intendedName = intendedName.replace('/','.')

				#make string that will be final name (usually course num, section, name, date) but some are different
				fullPath = path+intendedName
				#replace old filename with new file name
				shutil.move(folder,fullPath)







