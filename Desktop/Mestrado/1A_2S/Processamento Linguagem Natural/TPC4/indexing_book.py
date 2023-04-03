import json
import re

json_dic = open("dic_json.json", encoding  = 'utf8')

terms = json.load(json_dic)

json_dic.close()

book = open("LIVRO-Doenças-do-Aparelho-Digestivos.html")
text = book.read()
book.close()

# Isto mata o PC:
# count=0
# for term in terms:
#     to_find = term
#     to_display = terms[term]
#     text = re.sub(rf'{to_find}', rf'<a title={to_display}>{to_find}</a>', text)
#     count += 1
#     print(count)

words = text.split()
for i in range(len(words)):
    tmp = words[i].strip(',').strip("").strip('(').strip(')').strip('.')
    if tmp in terms.keys():
        words[i] = '<a href title="' + terms[tmp] + '">' + words[i] + '</a>'

new_text = " ".join(words)

new_book = open("LIVRO_v2.html", 'w', encoding='utf8')
new_book.write(new_text)
new_book.close()
