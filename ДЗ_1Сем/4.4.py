import collections
with open ("text.txt","r",encoding="utf-8") as text:
    text=text.read()
words = text.split()
print(words)
counter = collections.Counter(words)
chast = counter.most_common()[0]
dlinnoe = max(words, key=len)
print(f'Самое частое слово: {chast}\nСамое длинное слово: {dlinnoe}')