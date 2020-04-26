import spacy
nlp = spacy.load('en_core_web_sm')

#Reading the Tantra File
tantra_textFile = "./tantra10.txt"
tantras = open(tantra_textFile).read()

# Just to remove irregular white spaces if there is any
tantras = " ".join(tantras.split())

# for feeding to the spacy module
tantra_doc = nlp(tantras)

# Storing all the sentences as list
sentences = list(tantra_doc.sents)
# print(sentences)
# print(len(sentences))


count = 0
pastLen = 100
fileSpacy = open("tantrasSpacy.txt","a")
for sentence in sentences:

    # If previous sentence have word count less than 5 then we append the current sentence to the previous one.
    if pastLen < 5:
        fileSpacy.write(" ")
        fileSpacy.write(str(sentence))
        fileSpacy.write("\n")
        pastLen = 100
        count = 0

    else:
        #Implementation of counters to ensure that longer sentences dont get appended to each other
        count += 1
        if count == 2:
            count = 1
            fileSpacy.write("\n")
        fileSpacy.write(str(sentence))
        pastLen = len(sentence)
fileSpacy.close()
