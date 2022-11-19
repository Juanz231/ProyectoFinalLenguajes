import spacy
from spacy.lang.es.examples import sentences

def Menu():
    print("------- Bienvenido al analizador de sintaxis -------")
    print("Indicaciones:\n")
    print("- Los verbos permitidos son: ", "[" "corre, ", "salta,", "camina,", "habla,", "baila,", "canta,", "come,", "saluda,",
          "tira,", "juega,", "corren,", "saltan,"
                                     "caminan,", "hablan,", "bailan,", "cantan,", "comen,", "saludan,", "tiran,", "juegan"+"]")
    print("- Los sustantivos permitidos son: ", "[", "Juan,", "Ana,", "Sara,", "David,", "Diego,", "Valentina,", "Camila,",
          "Santiago,", "Esteban,", "Camilo,"+"]\n")
    print("- Si la oración a analizar está en tiempo pasado, poner las tildes necesarias.\n")
    while (True):
        opcion = input("Ingrese 0 para salir, 1 para analizar texto: ")
        if opcion == "0":
            exit()
        if opcion == "1":
            print("Ingrese el texto a analizar: ")
            texto = input()
            validar(texto)


def validar(texto):
    listaVerbos = ["corre", "salta", "camina", "habla", "baila", "canta", "come", "saluda", "tira", "juega", "corren",
                   "saltan"
                   "caminan", "hablan", "bailan", "cantan", "comen", "saludan", "tiran", "juegan"]
    listaNombres = ["Juan", "Ana", "Sara", "David", "Diego", "Valentina", "Camila", "Santiago", "Esteban", "Camilo"]

    frases = spacy.load("es_core_news_sm")
    arreglo = frases(texto)
    frase = str(arreglo)
    #for token in arreglo:
        #print(token.text,token.pos_)
    guarda = 0

    for i in range(len(arreglo)-1):
        if arreglo[i].pos_ == arreglo[i+1].pos_ :
            guarda = 1
        if str(arreglo[i].pos_) == "PROPN" and  str(arreglo[i+1]).lower() in listaVerbos:
            guarda = 0
        if (str(arreglo[i]).lower() in listaVerbos) and (str(arreglo[i+1]).lower() in listaVerbos):
            guarda = 1
            break
        if str(arreglo[len(arreglo) - 1].pos_) == "CCONJ":
            guarda = 1
    if guarda == 0:
        print("Frase valida")
    elif(guarda == 1):
        print("Frase invalida")
Menu()
