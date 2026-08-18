sentence = input("Enter a sentence: ")

print(f"Length: {len(sentence)}")

lst_words = sentence.split()
print(f"First word: {lst_words[0]}")

print(f"Reversed: {sentence[::-1]}")
