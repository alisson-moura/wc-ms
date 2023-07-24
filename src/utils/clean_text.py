import re
import spacy
import nltk

spc_pt = spacy.load('pt_core_news_sm')

def clean(text):
    # Remover caracteres que não são letras e tokenização
    words = re.findall(r'\b[A-zÀ-úü]+\b', text.lower())
    
    #Remover stopwords
    stopwords = nltk.corpus.stopwords.words('portuguese')
    #Adicionando stopwords que não estão na lista do nltk

    stopwords.append("'")
    stopwords.append("pra")
    stopwords.append("tá")
    stopwords.append("ai")
    stop = set(stopwords)

    meaningful_words = [w for w in words if w not in stopwords]
    meaningful_words_string = " ".join(meaningful_words)

    #Instanciando o objeto spacy
    spc_words =  spc_pt(meaningful_words_string)

    #Lemmização 
    tokens = [token.lemma_ if token.pos_ == 'VERB' else str(token) for token in spc_words]

    #problemas com verbo ir
    ir = ['vou', 'vais', 'vai', 'vamos', 'ides', 'vão']
    tokens = ['ir' if token in ir else str(token) for token in tokens]

    #problemas com o verbo atender
    atender = ['atendir']
    tokens = ['atender' if token in atender else str(token) for token in tokens]

    return tokens 