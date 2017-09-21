import json

stopwords = {'en': ['the', 'a', 'we'], 'es': ['los', 'las', 'él']}
stem = {'Porter': lambda x: x[:2], 'Snowball': lambda x: x[:3]}

##########################################################################

#                   ESCRIBE TUS DECORADORES AQUI

##########################################################################
















##########################################################################

#                       CODIGO A DECORAR

##########################################################################

def tokenize(text, sep, ngrams=1):
    text_splitted = text.split(sep)
    if ngrams == 1:
        return text_splitted

    text_splitted_ngrams = []
    number_of_tokens = int(len(text_splitted)/ngrams) + 1
    for token in range(number_of_tokens):
        text_splitted_ngrams.append(
        sep.join(text_splitted[token*ngrams:token*ngrams + ngrams]))
    return text_splitted_ngrams

def remove_stopwords(text, language='es'):
    return list(filter(lambda token: token not in stopwords[language], text))


def apply_stem(text, type_='Porter'):
    return list(map(stem[type_], text))


def save(text, filename, **kwargs):
    with open(filename + '.nlp', 'w+') as file:
        content = {'text': text}
        content.update(kwargs)
        json.dump(content, file)

def read(filename):
    with open(filename + '.nlp', 'r') as file:
        content = json.load(file)
    text = content['text']
    del content['text']
    return text, content

    
if __name__ == "__main__":
    try:
        archivo = read("archivo")
    except FileNotFoundError as err:
        print("Esto no es un archivo")

    eng = read("ingles")
    esp = read("español")

    print("Esto son los datos sin procesar como lista")
    list_ = tokenize(esp[0], " ", 1)
    print(list_)
    print(tokenize(eng[0], " ", 2))

    print("--------------------------------------\n")
    
    print("Probado stem")

    print(apply_stem(list_, type_='Porter'))
    print(apply_stem(list_, type_='Snowball'))

    print("--------------------------------------\n")

    print(" Ahora le quitaremos las palabras extra")

    lists = tokenize(esp[0], ' ', 1)
    lists = remove_stopwords(lists, language='es')


    liste = tokenize(eng[0], ' ', 1)
    liste = remove_stopwords(liste, language='en')

    string = " ".join(liste)+" : "+" ".join(lists)
    save(string, "resultados", iluminador = "Hernan")
