# Hash Map
def hashMap(queryType, query):
    hashmap = {}
    result_sum = 0

    for i in range(len(queryType)):
        
        if queryType[i] == "insert":
            x, y = query[i]
            hashmap[x] = y
            
        elif queryType[i] == "get":
            x = query[i][0]
            if x in hashmap:
                result_sum += hashmap[x]
        elif queryType[i] == "addToKey":
            x = query[i][0]
            new_hashmap = {}
            for key in hashmap:
                new_key = key + x
                new_hashmap[new_key] = hashmap[key]
            hashmap = new_hashmap
        elif queryType[i] == "addToValue":
            y = query[i][0]
            new_hashmap = {}
            for key in hashmap:
                new_hashmap[key] = hashmap[key] + y
            hashmap = new_hashmap
    return result_sum

# Example usage
queryType1 = ["insert", "insert", "addToValue", "addToKey", "get"]
query1 = [[1, 2], [2, 3], [2], [1], [3]]
print(hashMap(queryType1, query1))  # Output: 5

queryType2 = ["insert", "addToValue", "get", "insert", "addToKey", "addToValue", "get"]
query2 = [[1, 2], [2], [1], [2, 3], [1], [-1], [3]]
print(hashMap(queryType2, query2))  # Output: 6