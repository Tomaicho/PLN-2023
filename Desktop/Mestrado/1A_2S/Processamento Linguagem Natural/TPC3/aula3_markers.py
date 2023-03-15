import re

file = open('dicionario_medico.txt', encoding='utf-8')
text = file.read()

text = re.sub(r'\n\n\f(.+\n\n)', r'\n\1', text)

text = re.sub(r'\n\n\f((?:.+)\n[A-ZÁÀÉÚÍÓÂÃÕ])', r'\n\n\1', text)

text = re.sub(r'\n\n\f', r'\n', text)

text = re.sub(r'\f', '', text)

text = re.sub(r'\n\n(.+)', r'\n\n@\1', text)

text = re.sub(r'\n([^@#\n].+)', r'\n#\1', text)

entries = re.findall(r'(@.+)((?:\n#.+)+)', text)

# Remove \n e # in descriptions e @ in designations
new_entries = [(designation.strip('@'), description.strip('\n#').replace('#',
                '').replace('\n', ' ')) for designation, description in entries]
file.close()

html = open('dicionario_medico_v2.html', 'w', encoding = 'utf8')

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