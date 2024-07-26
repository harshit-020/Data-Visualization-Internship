#  Read the content from a text file "ABC.txt" line by line and display it on the screen
Path = 'ABC.txt'
with open(Path, 'r') as file:
    print("Content of ABC.txt:")
    for line in file:
        print(line.strip())  # strip() removes any leading/trailing whitespace
print()

# Count and display the total number of words in a text file "ABC.txt"
with open(Path, 'r') as file:
    text = file.read()
    words = text.split()
    word_count = len(words)
    print(f"Total number of words in ABC.txt: {word_count}")
print()

# Count uppercase characters in a text file "ABC.txt"
with open(Path, 'r') as file:
    text = file.read()
    uppercase_count = sum(1 for char in text if char.isupper())
    print(f"Total number of uppercase characters in ABC.txt: {uppercase_count}")
print()

# Read lines from a text file "story.txt" and display words which are less than 4 characters
filename_story = 'story.txt'
with open(filename_story, 'r') as file:
    print("Words with less than 4 characters in story.txt:")
    for line in file:
        words = line.split()
        short_words = [word for word in words if len(word) < 4]
        for word in short_words:
            print(word)











