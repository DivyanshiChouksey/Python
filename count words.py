# COUNT WORDS
# st = "The wizard of oz The sherlock homes Harry Potter and philoshperes stone Harry Potter and the secret chamber "
# lst = list(st.split())
lst = ['The', 'wizard', 'of', 'oz', 'The', 'sherlock', 'homes', 'Harry', 'Potter', 'and', 'philoshperes', 'stone', 'Harry', 'Potter',
 'and', 'The', 'secret', 'chamber']
countWord = {}
for word in lst:
    if word in countWord:
        countWord[word]+=1
    else:
        countWord[word]=1
print(countWord)
