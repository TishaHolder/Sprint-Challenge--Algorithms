'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    if len(word) < 1:
        return 0
    
    elif word.find("th") >= 0:
        found_index = word.find("th")         
        new_index = found_index + 2
        new_word = word[new_index: len(word)]   

        return 1 + count_th(new_word)
    else:
        return 0
