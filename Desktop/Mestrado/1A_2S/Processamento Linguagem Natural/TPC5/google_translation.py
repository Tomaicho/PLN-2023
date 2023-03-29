from deep_translator import GoogleTranslator
import json

file_dic = open("dic.json", encoding='utf8')
dic = json.load(file_dic)
file_dic.close()

new_dic = {}
i=0
for term, designation in dic.items():
    new_dic[term] = {
        "des": designation,
        "en": GoogleTranslator(source='pt', target='en').translate(term),
        "de": GoogleTranslator(source='pt', target='de').translate(term)
        
    }
    i += 1
    print(i)
    if i == 200:
        break

new_file_dic = open("dic_pt_en_de.json", 'w', encoding='utf8')
json.dump(new_dic, new_file_dic, ensure_ascii=False, indent=4)
new_file_dic.close()