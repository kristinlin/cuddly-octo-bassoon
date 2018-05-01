import string

#get book file
file = "132.txt"
book = open(file, 'r')

#remove all punctuation and newlines, intro outro, 
text = book.read().split('***')[2].encode('utf8').lower()
text = ''.join([l for l in text if l not in string.punctuation and l!='\r'])
text = text.replace('\n', ' ')

#get all words in book
words = [w for w in text.split(' ') if w!='']



def single_word(word, book):
    return len([ x for x in book if x == word])

def phrase(p, book):
    return reduce((lambda a, b: a+b),
                  [single_word(a, book) for a in p.split(' ')])

def most(book):
    checked = []
    def count_word(a):
        checked.append(a)
        return a
    return reduce((lambda a,b: a if single_word(a,book) > single_word(b,book) else b), [count_word(a) for a in book if a not in checked])



print "SEARCHING THE ART OF WAR BY SUN TZU"
print "frequency of 'the'"
print single_word('the', words)
print "frequency of 'a'"
print single_word('a', words)
print "frequency of 'war'"
print single_word('war', words)
print "frequency of 'victory'"
print single_word('victory', words)
print "frequency of 'triumph'"
print single_word('triumph', words)
print "frequence of 'the war'"
print phrase('the war', words)
print "frequence of 'a victory'"
print phrase('a victory', words)
print "calculating most frequent word... (warning: takes some time)"
print most(words)
