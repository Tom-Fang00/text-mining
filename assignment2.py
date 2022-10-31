import urllib.request

# url = 'https://archive.org/download/joannek.rowlingharrypotterbook1harrypotterandthephilosophersstoneenglishonlineclub.com/Joanne%20K.%20Rowling%20%28Harry%20Potter%2C%20Book%201%29%20-%20Harry%20Potter%20and%20the%20Philosophers%20Stone%20%5BEnglishOnlineClub.com%5D_djvu.txt'
# url = 'https://raw.githubusercontent.com/formcept/whiteboard/master/nbviewer/notebooks/data/harrypotter/Book%202%20-%20The%20Chamber%20of%20Secrets.txt'
url='https://raw.githubusercontent.com/pprzetacznik/nlp-n-grams/master/train_corpus/Harry%20Potter%203%20Prisoner%20of%20Azkaban.txt'
with urllib.request.urlopen(url) as f:
    response = urllib.request.urlopen(url)
    data = response.read()  # a `bytes` object
    text = data.decode('utf-8')
    #print(text) # for testing

collection = list(text.split())
harry_count=0
ron_count=0
hermione_count=0
word_count=0
for word_count in range (len(collection)):
    if collection[word_count] == "Harry" or collection[word_count] == "Potter":
        harry_count +=1
        word_count+=1
    elif collection[word_count] == "Hermione" or collection[word_count] == "Granger":
        hermione_count +=1
        word_count+=1
    elif collection[word_count] == "Ron" or collection[word_count] == "Weasley":
        ron_count +=1
        word_count+=1
    else:
        word_count+=1

print (f"Harry and Potter appeared in the text for a total of {harry_count} times")
print (f"Ron and Weasley appeared in the text for a total of {ron_count} times")
print (f"Hermione and Granger appeared in the text for a total of {hermione_count} times")

harry_full=0
ron_full=0
hermione_full=0
word_count2=1
for word_count2 in range (len(collection)):
    if collection[word_count2-1] == "Harry" and collection[word_count2] == "Potter":
        harry_full +=1
        word_count2+=1
    elif collection[word_count2-1] == "Hermione" and collection[word_count2] == "Granger":
        hermione_full +=1
        word_count2+=1
    elif collection[word_count2-1] == "Ron" and collection[word_count2] == "Weasley":
        ron_full +=1
        word_count2+=1
    else:
        word_count2+=1

print (f"Harry Potter's full name appeared in the text for a total of {harry_full} times")
print (f"Ron Weasley's full name appeared in the text for a total of {ron_full} times")
print (f"Hermione Granger's full name appeared in the text for a total of {hermione_full} times")
