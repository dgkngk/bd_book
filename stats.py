def word_counter(text):
    words = text.split()
    return len(words)

def char_counter(text):
    char_counts = {}

    lower_str = text.lower()
    for char in lower_str:
        if char.isalpha():
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1

    return char_counts

def char_lister(char_dict):
    char_list = []
    for key, value in char_dict.items():
        char_list.append({"char": key, "count": value})
    
    def sorter(dict):
        return dict['count']
    
    char_list.sort(key=sorter, reverse=True)
    return char_list

