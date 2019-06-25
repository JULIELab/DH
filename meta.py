import xml.etree.ElementTree as ET
import sys
import os

os.chdir('letters/xml/')
#with open("../stat.tsv","w") as f:
letters = []
for t in os.listdir(os.getcwd()):
    id = t.split('.')[0]
    print('ID:',id)
    tree = ET.parse(t)
    root = tree.getroot()
    for elem in root.findall("./{http://www.tei-c.org/ns/1.0}teiHeader/{http://www.tei-c.org/ns/1.0}profileDesc/{http://www.tei-c.org/ns/1.0}correspDesc/{http://www.tei-c.org/ns/1.0}correspAction/[@type='sent']/{http://www.tei-c.org/ns/1.0}persName"):
        sender = elem.text
    for elem in root.findall("./{http://www.tei-c.org/ns/1.0}teiHeader/{http://www.tei-c.org/ns/1.0}profileDesc/{http://www.tei-c.org/ns/1.0}correspDesc/{http://www.tei-c.org/ns/1.0}correspAction/[@type='sent']/{http://www.tei-c.org/ns/1.0}placeName"):
        if not elem:
            dispatch = 'unbekannt'
        else:
            dispatch = elem.text
    for elem in root.findall("./{http://www.tei-c.org/ns/1.0}teiHeader/{http://www.tei-c.org/ns/1.0}profileDesc/{http://www.tei-c.org/ns/1.0}correspDesc/{http://www.tei-c.org/ns/1.0}correspAction/[@type='sent']/{http://www.tei-c.org/ns/1.0}date"):
        if not elem:
            date = 'unbekannt'
        else:
            date = elem.text
    for elem in root.findall("./{http://www.tei-c.org/ns/1.0}teiHeader/{http://www.tei-c.org/ns/1.0}profileDesc/{http://www.tei-c.org/ns/1.0}correspDesc/{http://www.tei-c.org/ns/1.0}correspAction/[@type='received']/{http://www.tei-c.org/ns/1.0}persName"):
        recipient = elem.text  
    for elem in root.findall("./{http://www.tei-c.org/ns/1.0}teiHeader/{http://www.tei-c.org/ns/1.0}profileDesc/{http://www.tei-c.org/ns/1.0}correspDesc/{http://www.tei-c.org/ns/1.0}correspAction/[@type='received']/{http://www.tei-c.org/ns/1.0}placeName"):
        if not elem:
            destination = 'unbekannt'
        else:
            destination = elem.text
    for elem in root.findall("./{http://www.tei-c.org/ns/1.0}text/{http://www.tei-c.org/ns/1.0}body/{http://www.tei-c.org/ns/1.0}div/{http://www.tei-c.org/ns/1.0}p"):
        print('Inhalt:')
        content = ''
        for i in elem.itertext():
            content+=i
            content+=' '
    letter = {'sender':sender,'dispatch':dispatch,'date':date,'recipient':recipient,'destination':destination,'content':content}
    print(letter)
    print('\n')