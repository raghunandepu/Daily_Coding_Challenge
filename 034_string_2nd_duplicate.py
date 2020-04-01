# Program to print duplicate only for 2nd occurence
string = "necesscities"

def dupCheck(string):
    counts = {}
    for ele in string:
        if ele in counts:
            counts[ele] += 1
            if counts[ele] == 2:
                print (ele, "duplicate")
            else:
                print(ele, "not a duplicate")
        else:
            counts[ele] = 1 
            print(ele, "not a duplicate")
        

dupCheck(string)


# Output:
"""n not a duplicate
e not a duplicate
c not a duplicate
e duplicate
s not a duplicate
s duplicate
c duplicate
i not a duplicate
t not a duplicate
i duplicate
e not a duplicate
s not a duplicate"""