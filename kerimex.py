text = input()

count = 0
seen = ""

for ch in text:
    if ch not in seen:
        seen += ch
        count += 1

print(count)