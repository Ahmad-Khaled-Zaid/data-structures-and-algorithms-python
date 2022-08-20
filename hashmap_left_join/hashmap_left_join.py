def left_join(hashmap_1, hashmap_2):
    result = []

    for key in hashmap_1:
        value_from_hash_1 = hashmap_1.get(key)
        value_from_hash_2 = hashmap_2.get(key)
        row = [
            key,
            value_from_hash_1,
            value_from_hash_2
        ]
        result.append(row)

    return result
