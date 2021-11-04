def getpairs(colors):
    # initializing the dictionary to store the frequency
    # every distinct sock
    dictionary = {}
    # getting the frequencies
    for color in range(len(colors)):
        if colors[color] not in dictionary:
            dictionary[colors[color]] = 1
        else:
            dictionary[colors[color]] += 1
            
    # initializing the totalpairs variable that'd
    # be incremented each time we divid the frequency of the distinct colors by 2
    totalpairs = 0
    for num in dictionary:
        totalpairs += dictionary[num] // 2
    
    # returning the answer
    return totalpairs

# Test cases used to verify the correctness of the code
test_colors1 = [5,8,8,6,3,3,2,2,6,7,7,2,2,5,2,3,4,5,6,7,9,9,1,9,9,11,1,1,8,12]
test_colors2 = [5,8,10,6,3,3,2,2,6,7,7,2,2,5,2,3,4,5,6,7,9,9,1,9,9,11,1,1,8,12,5,8,8,6,3,3,2,2,6,7,7,2,2,5,2,3,4,5,6,7,9,9,1,9,9,11,1,1,8,12,5,8,8,6,3,3,2,2,6,7,7,2,2,5,2,3,4,5,6,16]
# printing out the answer of the test case, along side the length of the test case
print(getpairs(test_colors1),len(test_colors1))
print(getpairs(test_colors2),len(test_colors2))
