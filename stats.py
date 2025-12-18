#takes in a string and returns the number of words as an int
def count_words(string_of_words):
    word_list = []
    num_words = 0
    word_list = string_of_words.split()
    num_words = len(word_list)
    return num_words

# takes in a string, and returns a dicionary containing
def get_char_count(string_of_words):
    frequency = {}
    for char in string_of_words:
        if char.lower() in frequency:
            frequency[char.lower()] += 1
        else:
            frequency[char.lower()] = 1
    return frequency
def value_get(list_of_dicts):
    return list_of_dicts["num"]
#sort dictionaries keys by their values desc
def get_sorted_dicts(dictionary):
    output_dictionary_list = []
    for key in dictionary:
        if key.isalpha():
            temp_dict = {"char": key, "num": dictionary[key]}
            output_dictionary_list.append(temp_dict)
    output_dictionary_list.sort(reverse=True, key=value_get)
    return output_dictionary_list

