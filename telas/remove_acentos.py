import unicodedata
def transformacao(texto):
    normalized = unicodedata.normalize('NFD', texto)
    return normalized.encode('ascii', 'ignore').decode('utf8').casefold()