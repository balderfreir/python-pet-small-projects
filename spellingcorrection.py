import textblob

phrases = input("What are we checking?"
                " Phrase separated by comma : ").split(',')
corrected_phrases = []
for ph in phrases:
    corrected_phrases.append(textblob.TextBlob(ph))
print("Words for correction :", phrases)
print("Corrected Words are :")
for i in corrected_phrases:
    print(i.correct(), end="; ")
