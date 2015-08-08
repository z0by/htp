TEXT = """From fairest creatures we desire increase,
That thereby beauty's rose might never die,
But as the riper should by time decease,
His tender heir might bear his memory:
But thou contracted to thine own bright eyes,
Feed'st thy light's flame with self-substantial fuel,
Making a famine where abundance lies,
Thy self thy foe, to thy sweet self too cruel:
Thou that art now the world's fresh ornament,
And only herald to the gaudy spring,
Within thine own bud buriest thy content,
And tender churl mak'st waste in niggarding:
Pity the world, or else this glutton be,
To eat the world's due, by the grave and thee."""

def tokinize(text):
    REMOVE_WORDS = ['!',',','.','?','!',':']
    words = text.split()
    new_words = []
    for word in words:
        word = word.lower()
        for char in  REMOVE_WORDS:
            word = word.replace(char,'')
        if word is not '':
            new_words.append(word)
    return new_words

def stat(text):
    _dict = {}
    for word in text:
        if _dict.get(word):
            _dict[word]+=1
        else:
            _dict[word]=1
    return _dict

print stat(tokinize(TEXT))
