statement = "Learning every day improves confidence"

vowels = "aeiouAEIOU"

for char in statement:
    if char.isalpha():
        if char in vowels:
            print(char, "is vowel")
        else:
            print(char, "is consonant")

            
statement = "Learning every day improves confidence"

vowels = "aeiouAEIOU"
vowel_list = []
consonant_list = []

for char in statement:
    if char.isalpha():
        if char in vowels:
            vowel_list.append(char)
        else:
            consonant_list.append(char)

print("Vowels:", vowel_list)
print("Consonants:", consonant_list)
