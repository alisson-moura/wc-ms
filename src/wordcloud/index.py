from src.utils.nps_classifier import nps
from src.utils.clean_text import clean

def generate_wordcloud_json(data):
    words = []

    # Verificando se a chave "items" existe no JSON
    if "items" in data and isinstance(data["items"], list) and len(data["items"]) > 0:
        for item in data['items'] :
            cleanedText = clean(item['feedback'])
            for text in cleanedText:
                found = False
                for word in words:
                    if word['text'] == text:
                        word['total'] += 1
                        word[nps(item['score'])] += 1
                        found = True
                        break
                if not found:
                    words.append({"text": text, "total": 1, "promotores": 0, "neutros": 0, "detratores": 0})
                    words[-1][nps(item['score'])] += 1
    else:
        return(words)
    
    return(words[:50])