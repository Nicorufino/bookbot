def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    words = text.lower().split()
    characters_dictionary = {}
    for word in words:
        for char in word:
            if (char in characters_dictionary):
                characters_dictionary[char] = characters_dictionary[char] + 1
            else:
                characters_dictionary[char] = 1

    return characters_dictionary

def sort_on(dict):
    return dict["num"]

def sort_char_dictionary(dictionary):
    keys = list(dictionary.keys())
    complete_dictionary = []
    for i in range(len(dictionary)):
        complete_dictionary.append({"char": keys[i], "num": dictionary[keys[i]]})
    complete_dictionary.sort(reverse=True, key=sort_on)
    return complete_dictionary