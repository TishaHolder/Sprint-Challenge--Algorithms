'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    #base case
    if len(word) < 1:
        return 0
    
    #if "th" is found
    elif word.find("th") >= 0:

        #store the starting index where it was found in found_index
        found_index = word.find("th") 

        #find returns the starting index, so add 2 to define the starting point of the next search        
        new_index = found_index + 2

        #start the next search from the new starting point to the end of the string
        new_word = word[new_index: len(word)]   

        #if "th" is found call count_th with the "new word"
        return 1 + count_th(new_word)
    else:
        #if it is not found return 0
        return 0
