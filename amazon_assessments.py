'''Given a list of reviews, a list of keywords and an integer k. Find the most popular k keywords in order of most to
least frequently mentioned.
The comparison of strings is case-insensitive.
Multiple occurances of a keyword in a review should be considred as a single mention.
If keywords are mentioned an equal number of times in reviews, sort alphabetically.

Example 1:
Input:
k = 2
keywords = ["anacell", "cetracular", "betacellular"]
reviews = [
  "Anacell provides the best services in the city",
  "betacellular has awesome services",
  "Best services provided by anacell, everyone should use anacell",
]
Output:
["anacell", "betacellular"]
Explanation:
"anacell" is occuring in 2 different reviews and "betacellular" is only occuring in 1 review.
Example 2:

Input:
k = 2
keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
reviews = [
  "I love anacell Best services; Best services provided by anacell",
  "betacellular has great services",
  "deltacellular provides much better services than betacellular",
  "cetracular is worse than anacell",
  "Betacellular is better than deltacellular.",
]
Output:
["betacellular", "anacell"]
Explanation:
"betacellular" is occuring in 3 different reviews. "anacell" and "deltacellular" are occuring in 2 reviews,
but "anacell" is lexicographically smaller.
'''

k = 2
keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
reviews = [
    "I love anacell Best services; Best services provided by anacell",
    "betacellular has great services",
    "deltacellular provides much better services than betacellular",
    "cetracular is worse than anacell",
    "Betacellular is better than deltacellular.",
]


def top_k_frequent(top_k, words, list_of_texts):
    """
    Find the top k most frequent words
    :param top_k: integer
    :param words: list
    :param list_of_texts: list of strings
    :return: list
    """
    dict_top_freq = {}
    for word in words:
        dict_top_freq[word.lower()] = 0
        for string in list_of_texts:
            if word.lower() in string.lower():
                dict_top_freq[word.lower()] += 1

    list_top_sorted = sorted(dict_top_freq.items(), key=lambda item: item[1], reverse=True)

    list_k = []
    for i in list_top_sorted:
        list_k.append(i[0])

    return list_k[:top_k]


list_top_k = top_k_frequent(k, keywords, reviews)
print(list_top_k)
