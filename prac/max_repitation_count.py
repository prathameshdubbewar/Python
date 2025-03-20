def max_repeated_char(word):
    char_count = {}

    for char in word:
        # Using get() to handle the case where the character is not in the dictionary
        char_count[char] = char_count.get(char, 0) + 1

    max_char = max(char_count, key=char_count.get)
    max_count = char_count[max_char]

    return max_char, max_count

# Example usage
word = "programming"
max_char, max_count = max_repeated_char(word)

print(f"In the word '{word}', the most repeated character is '{max_char}' with a count of {max_count}.")
