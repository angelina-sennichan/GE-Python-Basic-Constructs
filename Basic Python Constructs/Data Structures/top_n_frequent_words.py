from collections import Counter

def top_n_words(text, n):
    words = text.split()
    word_count = Counter(words)
    return word_count.most_common(n)

text = "great service great product"
top_n_value = 2
result = top_n_words(text, top_n_value)
print(result)
