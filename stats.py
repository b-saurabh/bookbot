def __sort_on__(items):
    return items['count']


def sort_chars(chars):
    list_chars = []
    for char in chars:
        list_chars.append({'char': char, 'count': chars[char]})
    list_chars.sort(reverse=True, key=__sort_on__)
    return list_chars


def get_num_chars(text):
    """
    Returns a dictionary with the count of each character in the lowercased text,
    including symbols and spaces.
    """
    text = text.lower()
    char_count = {}
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count


def get_num_words(text):
    """
    Returns the counts of the words found in a text
    """
    words = text.split()  # defaults to whitespace as a separator
    return len(words)
