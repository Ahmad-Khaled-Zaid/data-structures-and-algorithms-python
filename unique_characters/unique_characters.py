from hash_table.hash_table import HashTable


def unique_chars(string):
    hash_map = {}
    for c in string:
        if hash_map.get(c) is False:
            hash_map[c] = True
        else:
            return False
    return False


if __name__ == '__main__':
    print(unique_chars("I love cats"))
