s = input()

count_pairs_v = [0]*len(s)

for i in range(len(s)):
    if s[i:i+2] == 'vv':
        count_pairs_v[i] = 1

left = 0
right = sum(count_pairs_v)
count = 0

for i in range(len(s)):
    if s[i] == 'o':
        count += left * right
    elif s[i] == 'v':
        left += count_pairs_v[i]
        right -= count_pairs_v[i]

print(count)