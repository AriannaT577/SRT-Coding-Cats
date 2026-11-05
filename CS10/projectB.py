start = 1
end = 2
nextnum = end
totalsum = 0
howmany = 30
nthterm = 0

for number in range (howmany):
    if start>1000000:
        break
    print(start)
    if start%2==0:
        totalsum+=start
    nextnum= start+end
    start = end
    end = nextnum

print("The sum of the even numbers in the Fibonacci sequence that are less then 1 000 000 is "+str(totalsum)+".")

#print("\nDo you wish to take a Fibinacci sequence quiz? Please type Y (yes) or N (no). ")
#ready = input()
#if ready == "Y":
#    print("Great! Type the number of the term you wish the quiz for. For example, 5 is the 4th term, 8 is the 5th term, and 13 is the 6th term:")
#    nthterm = input()
#    for number in range(nthterm):
#    if start>1000000:
#        break
#    if 
#    nextnum= start+end
#    start = end
#    end = nextnum    
#else:
#    print("Come back when you are ready!")
