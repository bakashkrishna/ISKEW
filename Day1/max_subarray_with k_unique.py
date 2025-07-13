s= input("Enter a string: ")
# s="aabacbebebe"
k= int(input("Enter the number of unique characters: "))
# k=3

n=len(s)

from collections import Counter

l=0
max_len=0
freq=Counter()

for r in range(n):
    freq[s[r]] += 1

    if freq[s[r]] == 1:
        k -= 1
    
    while k < 0:
        freq[s[l]] -= 1
        if freq[s[l]] == 0:
            k += 1
        l += 1
    
    max_len = max(max_len, r - l + 1)

# print(Counter(s))
# print(freq)
print(max_len)