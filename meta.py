import xml.etree.ElementTree as ET
import sys
import os

os.chdir('letters/xml/')
#with open("../stat.tsv","w") as f:
for t in os.listdir(os.getcwd()):
    print('ID:',t.split('.')[0])
    tree = ET.parse(t)
    root = tree.getroot()
    for elem in root.findall("./{http://www.tei-c.org/ns/1.0}teiHeader/{http://www.tei-c.org/ns/1.0}profileDesc/{http://www.tei-c.org/ns/1.0}correspDesc/{http://www.tei-c.org/ns/1.0}correspAction/[@type='sent']/{http://www.tei-c.org/ns/1.0}persName"):
            #f.write(elem.text)
            #f.write('\t')
        print('Absender:',elem.text)
    for elem in root.findall("./{http://www.tei-c.org/ns/1.0}teiHeader/{http://www.tei-c.org/ns/1.0}profileDesc/{http://www.tei-c.org/ns/1.0}correspDesc/{http://www.tei-c.org/ns/1.0}correspAction/[@type='sent']/{http://www.tei-c.org/ns/1.0}placeName"):
        print('Absendeort:',elem.text)
    if not elem:
        print('Absendeort: unbekannt')
    for elem in root.findall("./{http://www.tei-c.org/ns/1.0}teiHeader/{http://www.tei-c.org/ns/1.0}profileDesc/{http://www.tei-c.org/ns/1.0}correspDesc/{http://www.tei-c.org/ns/1.0}correspAction/[@type='sent']/{http://www.tei-c.org/ns/1.0}date"):
        print('Datum:',elem.text)
    if not elem:
        print('Datum: unbekannt')
    for elem in root.findall("./{http://www.tei-c.org/ns/1.0}teiHeader/{http://www.tei-c.org/ns/1.0}profileDesc/{http://www.tei-c.org/ns/1.0}correspDesc/{http://www.tei-c.org/ns/1.0}correspAction/[@type='received']/{http://www.tei-c.org/ns/1.0}persName"):
        print('Empfänger:',elem.text)  
    for elem in root.findall("./{http://www.tei-c.org/ns/1.0}teiHeader/{http://www.tei-c.org/ns/1.0}profileDesc/{http://www.tei-c.org/ns/1.0}correspDesc/{http://www.tei-c.org/ns/1.0}correspAction/[@type='received']/{http://www.tei-c.org/ns/1.0}placeName"):
        print('Empfangsort:',elem.text)
    if not elem:
        print('Empfangsort: unbekannt')
    for elem in root.findall("./{http://www.tei-c.org/ns/1.0}text/{http://www.tei-c.org/ns/1.0}body/{http://www.tei-c.org/ns/1.0}div/{http://www.tei-c.org/ns/1.0}p"):
        print('Inhalt:')
        content = ''
        for i in elem.itertext():
            content+=i
            content+=' '
        print(content)
    print('\n')