import hashlib
import itertools
import time
import random
random.seed(1)


def find_answer_5():
    test_string = '1234567890abcdefghijklmnopqrstuvwxyz'
    answer = []
    dictonary = {}
    # read hash5.txt
    # since we have aditional '/n' character at the end of each line, we need to
    # delete it.
    with open("hash5.txt") as f:
        # lines = f.readlines()
        hashed_lines = [line.rstrip('\n') for line in f]
    # find all the comb of 5 characters
    combo = itertools.product(test_string, repeat=5)
    for each_combo in combo:
        #we need to change the tuple to string
        each_combo = ''.join(each_combo)
        new_hashed = hashlib.new('md5')
        # Unicode-objects must be encoded before hashing
        encoded_combo = each_combo.encode('utf-8')
        # need to update after encoding
        new_hashed.update(encoded_combo)
        hasehd_value = new_hashed.hexdigest()
        # dictonary[hasehd_value] = each_combo
        if hasehd_value in hashed_lines:
            answer.append(each_combo)
    return answer
    # tring to lookup for the hashed value
    # for indi_hash in hashed_lines:
    #     answer.append(dictonary[indi_hash])
    # return answer


def add_one_salt(list_to_hash):
    hashed_list = []
    list_with_oneslat = []
    letters = ascii_lowercase()
    for lines in list_to_hash:
        lines += random.choice(letters)
        list_with_oneslat.append(lines)
        # hash the values
        new_hashed = hashlib.new('md5')
        # Unicode-objects must be encoded before hashing
        encoded_combo = each_combo.encode('utf-8')
        # need to update after encoding
        new_hashed.update(encoded_combo)
        hasehd_value = new_hashed.hexdigest()
        hashed_list.append(hasehd_value)
    with open('salted6.txt', 'w') as f:
        for indiv_hashed in hashed_list:
            f.write(indiv_hashed)
            f.write('\n')
    return (hashed_list, list_with_oneslat)


start_time = time.time()
result = find_answer_5()
print('Total time used')
print(time.time() - start_time)
print(result)
