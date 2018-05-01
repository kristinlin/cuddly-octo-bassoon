import string

#get book file
file = "1400.txt"
book = open(file, 'r')

#remove all punctuation and newlines
text = ''.join([l for l in book.read() if l not in string.punctuation and l!='\n' and l!='\r'])

#get all words in book
words = [w for w in text.split(' ') if w!='']

def single_word(word, book):
    return len([ x for x in book if x == word])

def phrase(p, book):
    return reduce((lambda a, b: a+b), [single_word(a, book) for a in p.split(' ')])

def most(book):
    pass

print phrase("hello world", ["hello", "world", "hello", "Hello"])
