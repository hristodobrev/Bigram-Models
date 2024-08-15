from collections import Counter
import random

reader = open('data/story.txt')

punctuation = '.;,-“’”:?—‘!()_''"'

bigram_counter = Counter()
window = []
bigrams = []

for line in reader:
    for word in line.split():
        clean_word = word.strip(punctuation).lower()
        window.append(clean_word)
        if len(window) >= 2:
            bigram = tuple(window)
            bigrams.append(bigram)
            bigram_counter[bigram] +=1
            window.pop(0)

successor_map = {}
for bigram in bigrams:
    if bigram[0] not in successor_map:
        successor_map[bigram[0]] = [bigram[1]]
    else:
        successor_map[bigram[0]].append(bigram[1])

# for line in dict(sorted(successor_map.items(), key=lambda x: len(x[1]))):
#     print(line, successor_map[line])

# for key, value in bigram_counter.most_common(10):
#     print(key, value)

word = "the"
for i in range(50):
    print(word, end=' ')
    word = random.choice(successor_map[word])