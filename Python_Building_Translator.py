## We will built a translator that will convert words into another language
## Lets Define our Language for our Dwarf Translator
# Giraffe Language
# vowels -> g
#----------------------
# dog -> dgg
# cat -> cgt

## word that we want to translate 
def translate(word):
	translation = ""
	for letter in word:
		if letter in "AEIOUaeiou":
			translation = translation + "g"
		else:
			translation = translation + letter
	return translation

print(translate(input("Enter a Word to Tranlate :")))

## Optimized fixed Uppper Case Problem like ON >gN to ON > GN 
def translate(word):
	translation = ""
	for letter in word:
		#
		if letter.lower() in "aeiou":
			if letter.isupper():
				translation=translation + "G"
			else:
				translation = translation + "g"
		else:
			translation = translation + letter
	return translation

print(translate(input("Enter a Word to Tranlate :")))