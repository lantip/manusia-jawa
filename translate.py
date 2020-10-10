from googletrans import Translator
import os
import time
translator = Translator()
dotras = []
for filename in os.listdir('source/PITHECANTHROPUS- SCHICHTEN AUF JAVA/'):
    urut = filename.split('.')[0].split('_')[-1]
    if not 'final' in urut:
        flnm = int(urut)
        if flnm > 34:
            dotras.append({'id':flnm,
                           'file': filename})
    else:
        dotras.append({'id':1000,
                        'file': filename})

urutan = sorted(dotras, key = lambda i: i['id'])

for files in urutan:
    filename = files['file']
    with open('source/PITHECANTHROPUS- SCHICHTEN AUF JAVA/'+filename, 'r') as fle:
        trans = translator.translate(fle.read())
        with open('result/PITHECANTHROPUS- SCHICHTEN AUF JAVA - English Version.txt','a') as sle:
            sle.write(trans.text)
    time.sleep(1)
