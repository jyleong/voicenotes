from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

stopWords = set(stopwords.words("english"))

mockstr = ["Water shows its colour when it gathers As a handful of thought, clear as water It falls into an ocean, where in time Becomes the bluest of all","As I’m sitting in the middle of the bus, I am looking back towards the rear of the bus where you are staring out the window on this gorgeous late-summer day. Your pure skin is radiating with the gleams of reflection off the cars and windows outside on this long bus ride. And I’m noticing you noticing the many things outside the window. You are such a curious person. Whatever it is that you are listening to through your earbuds, I don’t know. But if I were to imagine, it would be as if you’re watching a movie; the flow of life on the streets passing by you. Too bad that this movie cannot show you how beautiful you are, staring out the window.","Receiving beauty is the expansion of the self outwards to time and being Each moment in beauty perception in the mind’s eye awakes you to embrace — The newly found increment of the universe; then, This universe in which you belong to begins to belong to you Each slice of the past now allows you to pull into you, a fragment of the future Touching the essence of each new encounter, absorbed into your being This encloses the relation between you and the whole And where you go becomes who you are You were, are, will — being — you, me, all."]

txt = ".".join([item for item in mockstr])
words = word_tokenize(txt)

print("txt", txt)
print("==============================================================")

freqTable = dict()
for word in words:
    word = word.lower()
    if word in stopWords:
            continue
    if word in freqTable:
            freqTable[word] += 1
    else:
        freqTable[word] = 1


sentences = sent_tokenize(txt)
sentenceValue = dict()

for sentence in sentences:
    # print(sentence)
    for wordValue in freqTable:
        # print(freqTable[wordValue])
        if wordValue in sentence.lower():
            if sentence[:12] in sentenceValue:
                sentenceValue[sentence[:12]] += freqTable[wordValue]
            else:
                sentenceValue[sentence[:12]] = freqTable[wordValue]

sumValues = 0
for sentence in sentenceValue:
    sumValues += sentenceValue[sentence]

# Average value of a sentence from original text
average = int(sumValues/ len(sentenceValue))

summary = ''
for sentence in sentences:
        if sentence[:12] in sentenceValue and sentenceValue[sentence[:12]] > (1.5 * average):
            summary +=  " " + sentence

print("summary", summary)