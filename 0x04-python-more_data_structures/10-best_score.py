#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    best_score = 0
    best_k = 0

    for k, v in sorted(a_dictionary.items()):
        if v > best_score:
            best_score = v
            best_k = k

    if best_k != 0:
        return best_k
    else:
        return None


a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))