def vowel_count(text):
    count=0
    for ch in text.lower():
        if ch in "aeiou":
            count +=1
    return count 
print(vowel_count("Ashish"))
print(vowel_count("aeiou"))   # 5
print(vowel_count("python"))  # 1
print(vowel_count("sky"))     # 0
print(vowel_count("Ashish"))  # 2
