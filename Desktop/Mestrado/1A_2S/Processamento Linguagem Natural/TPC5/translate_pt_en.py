from deep_translator import GoogleTranslator
import json


file_dic = open("dic.json", encoding='utf8')
dic = json.load(file_dic)
file_dic.close()

en_file = open("termos_traduzidos.txt", encoding='utf8')
en_txt = en_file.read().splitlines()
en_file.close()

dic_pt_en = {}
for entry in en_txt:
    list = entry.split(" @ ")
    dic_pt_en[list[0]] = en = list[1]

new_dic = {}
for term, designation in dic.items():
    if term in dic_pt_en.keys():
        new_dic[term] = {
            "des": designation,
            "en": dic_pt_en[term]
        }
    else:
        new_dic[term] = {
            "des": designation,
            "en": GoogleTranslator(source='pt', target='en').translate(term)
        }

new_file_dic = open("dic_pt_en.json", "w", encoding="utf-8")
json.dump(new_dic, new_file_dic, ensure_ascii=False, indent=4)
new_file_dic.close()