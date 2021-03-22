print("Enter the input string:\n")
word=raw_input()
word1=word.split()
if(len(word1)>1):
    w2=len(word1[-1])
    ans1=word1[0][0:2]
    ans2=word1[-1][w2-2:w2]
    print ans2+ans1
else:
    print "! Minimum 2 Words needs to be entered. !"