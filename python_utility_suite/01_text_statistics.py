from collections import Counter
import re

# Get text from the user
text = input("Enter a paragraph: ").strip()

# Extract words
words = re.findall(r"\b[\w']+\b", text.lower())

# Calculate statistics
word_count = len(words)
character_count = len(text)
character_count_no_spaces = len("".join(text.split()))
unique_words = len(set(words))

# Find the longest word
longest_word = max(words, key=len) if words else "None"

# Count word frequencies
word_frequency = Counter(words)

# Display results
print("\n" + "=" * 45)
print("       📝 TEXT STATISTICS ANALYZER")
print("=" * 45)

print(f"Total words           : {word_count}")
print(f"Total characters      : {character_count}")
print(f"Characters without spaces: {character_count_no_spaces}")
print(f"Unique words          : {unique_words}")
print(f"Longest word          : {longest_word}")

print("\n🔝 TOP 5 FREQUENT WORDS")
print("-" * 45)

for word, count in word_frequency.most_common(5):
    print(f"{word:<20} {count}")

print("=" * 45)