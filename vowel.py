'''to check if a given word contains vowel'''

word=input("Enter a word:")
vowel=['a','e','i','o','u']
found=[]
for char in word:
	if char in vowel:
		if char not in found:
			found.append(char)
for vowel in found:
	print(vowel)

