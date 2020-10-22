s = "abb"

for i in range(0, len(s)):
    for j in range(i, len(s)):
        print(s[i:j+1])