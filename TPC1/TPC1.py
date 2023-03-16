import time
# Ex.1
nome = input('Write your name: ')
nome = nome.upper()
print(nome)

# Ex.2
def print_pares(lista):
    newlista=(x for x in lista if x%2 == 0)
    print(list(newlista))
print_pares((1,2,3,4,5,6,7,8,9,10))

# Ex.3
def print_inverse(file):
    f = open(file, 'r')
    linhas = f.read().splitlines()
    for linha in linhas:
        linha=linha[::-1]
        print(linha)
print_inverse('Git_Commands.txt')

# Ex.4
def most_common_words(file):
    f = open(file, 'r')
    texto = f.read().lower()
    pre_palavras=texto.split()
    count={}
    for palavra in pre_palavras:
        #palavra = pre_palavra.split()
        if str(palavra) == '':
            continue
        elif str(palavra) not in count:
            count.update({str(palavra): 1})
        else:
            count[str(palavra)] += 1
    sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
    new_count = dict(sorted_count)
    print(list(new_count.items())[:10])

most_common_words('texto.txt')

# Ex.5
def clean_text(file):
    f = open(file, 'r', encoding='utf-8')
    texto = f.read().lower()
    palavras = texto.split()
    i = 0
    texto_limpo = []
    for palavra in palavras:
        ls = list(palavra)
        for i in range (len(ls)):
            letra = ls[i]
            pont = [',', '.', ';', '?', '!', ':']
            asp = ['"', '(', ')']
            a = ['á', 'à', 'ã', 'â']
            o = ['ó', 'õ', 'ô']
            e = ['é', 'ê']
            if letra in pont:
                    ls.insert(i, ' ')
            if letra in asp:
                if i == 0:
                    ls.insert(i+1, ' ')
                else:
                    try:
                        if ls[i+1] in pont:
                            ls.insert(i, ' ')
                            ls.insert(i+2, ' ')
                    except:
                        ls.insert(i, ' ')
            if letra in a:
                ls[i] = 'a'
            if letra in o:
                ls[i] = 'o'
            if letra == 'í':
                ls[i] = 'i'
            if letra == 'ú':
                ls[i] = 'u'
            if letra in e:
                ls[i] = 'e'
            if letra == 'ç':
                ls[i] = 'c'
        palavra = ''.join(ls)
        texto_limpo.append(palavra)
    texto = ' '.join(texto_limpo)
    print(texto)

clean_text('texto.txt')

# Ficha 2
# Ex.1
def reverse(s): 
    s=s[::-1]
    print(s)
reverse('oila')

#Ex.2
def count_a(s):
    count = 0
    for l in s:
        if l == 'a' or l == 'A':
            count+=1
    print(count)
count_a('avcfAAhfhfa')

# Ex.3
def count_vowels(s):
    v = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for l in s:
        if l in v:
            count+=1
    print(count)
    
count_vowels('jfnafjfegjjifnfnodjdjuu')

# Ex.4
def lower(s):
    s = s.lower()
    print(s)

# Ex.5
def upper(s):
    s = s.upper()
    print(s)
