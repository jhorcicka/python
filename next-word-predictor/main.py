
from collections import defaultdict, Counter

corpus = [
  "I love cats",
  "I love dogs",
  "You love cats",
  "Cats are cute",
  "Dogs are loyal"
]

bigram_counts = defaultdict(Counter)

for sentence in corpus:
  words = sentence.split()
  for i in range(len(words) - 1):
    bigram_counts[words[i]][words[i+1]] += 1

print(bigram_counts)

def predict_next_word(prev_word):
  if prev_word in bigram_counts:
    return bigram_counts[prev_word].most_common(1)[0][0]
  else:
    return "<unknown>"

print("I => ", predict_next_word("I"))    # love
print("love => ", predict_next_word("love")) # cats
print("Dogs => ", predict_next_word("Dogs")) # are

