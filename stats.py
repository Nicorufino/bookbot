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