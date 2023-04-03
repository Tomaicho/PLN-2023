import re
import json

file = open ("dicionario_medico.xml", encoding = "utf8")
text = file.read()

text = re.sub(r'</?page.*>', '', text)
text = re.sub(r'\n\n+', '\n', text)

text = re.sub(r'<text.*><b>(.+)</b></text>', r'@\1', text)
text = re.sub(r'<text.*> </text>', r'\n', text)
text = re.sub(r'<text.*>(.+)</text>', r'#\1', text)

entries = re.findall(r'@(.*)((?:\n#.+)+)', text)

new_entries = [(designation.strip('@'), description.strip('\n#').replace('#',
                '').replace('\n', ' ')) for designation, description in entries]

file.close()

html = open('dicionario_from_xml.html', 'w', encoding = 'utf8')

header = '''<html>
<head>
<meta charset='utf-8'/>
</head>
<h1>Dicionário Médico</h1>
<body>
    <table border = "1" cellpadding = "5" cellspacing = "5">
        <tr>
            <th style="width:20%">Designação</th>
            <th>Descrição</th>
        </tr>

'''
body = ''
for designation, description in new_entries:
    body += '<tr><td>' + designation  + '</td>'
    body += '<td>' + description  + '</td></tr>'

footer = '''
    </table>
</body>
</html>'''

html.write(header + body + footer)

html.close()

pydic = {}

for entry in new_entries:
    pydic[entry[0]]= entry[1]
'''
for key in pydic:
    print(key + '-> ' + pydic[key])'''

dic_json = open('dic_json.json', 'w', encoding = 'utf8')

#To write on json file (pydic can be list or dic; tuple would create list)
json.dump(pydic, dic_json, ensure_ascii=False, indent=4)

dic_json.close()
