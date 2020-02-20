#Linear search algorithm

seq=[13,12,51,74,32]

search=int(input("Enter the search value : "))

for i in seq:
    if i==search:
        print("element is found at ",seq.index(i)," index")
        break
else:
    print("searching element is not found")
