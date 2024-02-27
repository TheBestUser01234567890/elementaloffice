import xml
from xml.dom import minidom
joycfg = minidom.parse('joy-shared.config')
isStandalone = joycfg.getElementsByTagName('isStandalone')
if(isStandalone.attributes['name'].value):
 input("Joy is currently disabled or integrated into Write.\nPress enter to continue.")