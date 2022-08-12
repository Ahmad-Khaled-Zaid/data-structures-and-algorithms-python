from hash_table.hash_table import HashTable


def hashmap_repeated_word(string):
    string = string.lower().split(' ')
    hashmap = HashTable()
    for i in range(0, len(string)):
        if hashmap.contains(string[i].strip(',')):
            return string[i]
        else:
            hashmap.set(string[i].strip(','), i)
    return 'No duplicate'


if __name__ == "__main__":
    print(hashmap_repeated_word("Once upon a time, there was a brave princess who..."))
