# # Exercises A (Strings, Lists, Comprehensions)
# # Exercise 1: String Slicing (slicing.py)
# # Given text = "Artificial Intelligence":

# text = "Artificial Intelligence"
# Print the first 10 characters.
# print(text[:11])
# # Print the last 11 characters.
# print(text.strip()[len(text)-11 :])
# # Print every other character.
# print(text[0: len(text) + 1 : 2])
# # Print the string reversed.
# print(text[:: -1])
# # Print the middle character (use len()).
# print(text[len(text)//2])
# # Extract the word "Intelligence" using slicing only.
# print(text[11: len(text) +1])
# # Exercise 2: String Methods (methods.py)
# # Given email = " Bharath.Kumar@Example.COM ":
email = " Bharath.Kumar@Example.COM "
# # Strip whitespace.
# print(email.strip())
# # Convert to lowercase.
# print(email.lower())
# # Check if it ends with .com (after stripping and lowering).
# print(email.strip().lower().endswith(".com"))
# # Replace @ with at.
# print(email.replace("@", "at."))
# # Split on . and print the resulting list.
# print(email.split("."))
# # Count occurrences of the letter a (case-insensitive).
# print(email.count("a"))
# # Exercise 3: List Operations (list_ops.py)
# # Start with numbers = [5, 2, 8, 1, 9, 3, 7, 4, 6]:

numbers = [5, 2, 8, 1, 9, 3, 7, 4, 6]

# # Sort ascending and print.
# print(sorted(numbers))
# # Reverse and print.
# numbers.reverse()
# print(numbers)
# # Remove the number 9 and print.
# numbers.remove(9)
# print(numbers)
# # Insert 10 at the beginning and print.
# numbers.insert(0, 10)
# print(numbers)
# # Print sum, min, max.
# print(sum(numbers), min(numbers),max(numbers))
# # Create a new list of only even numbers using a list comprehension.
# even_numbers = [i for i in numbers if i %2 == 0]
# print(even_numbers)
# # Create a new list of each number squared using a list comprehension.
# square_list = [i ** 2 for i in numbers]
# print(square_list)

# # Exercise 4: Palindrome Checker (palindrome.py)
# # Ask user for a word or phrase.
# # Check if it is a palindrome (ignore case and spaces).
# # Print result.
# # Expected:

# # text

# # Enter: Race Car
# # "Race Car" is a palindrome!

# user_input = input("Enter a word or phrase: ")
# x = "".join(user_input.lower().split())
# print(x == x[::-1])

# # Exercise 5: Comprehension Challenges (comprehensions.py)
# # Solve each with a single list comprehension:

# # Numbers 1 to 50 divisible by both 3 and 5.
# numbers = [x for x in range(1, 51) if x % 3 == 0 and x % 5 == 0]
# print(numbers)

# # Given words = ["apple", "banana", "cherry", "date"], create [("apple", 5), ("banana", 6), ...] with each word and its length.
# words = ["apple", "banana", "cherry", "date"]
# result = [(x, len(x)) for x in words ]
# print(result)
# # Given matrix = [[1,2,3],[4,5,6],[7,8,9]], extract diagonal [1, 5, 9].
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# result = [matrix[i][i] for i in range(len(matrix))]
# print(result)
# # Given text = "Hello World 123", create a list of only alphabetic characters.
# text = "Hello World 123"
# result = [i for i in text if i.isalpha()]
# print(result)
# # Exercise 6: Debug This (debug_lists.py)
# # Four bugs. Fix each and comment the fix.

# # Python

# # # Goal: Remove failing scores (<40), sort remaining, compute average
# scores = [85, 32, 91, 28, 76, 45, 19, 67, 53, 38]

# passing = scores.remove(32, 28, 19, 38) ## remove only takes one argument only removes one item, fix with pass only one item
#  fix
# scores.remove(32) ## assignging with a variable will return NoneType
# passing.sort(reverse=false) ## passing will return None Type instead fix will be add scores to sort, false should be False
## fix
# scores.sort(reverse=False)
# print(scores)
# average = sum(passing) / len(scores)   ## instead of passing variable use scores variable

# fix
# average = sum(scores) / len(scores)

# print(f"Passing: {passing}")  ## instead of passing use scores variable

## fix
# print(f"Passing: {scores}")
# print(f"Average: {average:.2f}")
# # Expected output:
# Passing: [85, 91, 28, 76, 45, 19, 67, 53, 38]
# Average: 55.78
# # text

# # Passing: [91, 85, 76, 67, 53, 45]
# # Average: 69.50


# # Mini-Project A: Text Analyzer
# # Problem
# # Build a CLI tool that analyzes a paragraph and displays statistics.

# # Requirements
# # Ask user for a paragraph.
# # Compute and display:
# # Total characters (with spaces)
# # Total characters (no spaces)
# # Total words
# # Total sentences (ending with ., !, or ?)
# # Longest word
# # Most frequent word (case-insensitive)
# # Title case version
# # Text with all punctuation removed
# # Handle empty input.
# # Loop until user types quit.
# # Constraints
# # No imports. Only built-ins.
# # Use string methods, slicing, lists, comprehensions.
# # For word frequency, you can use .count() on the word list (after you learn dictionaries in Part B, you will see a better way).
# # Example
# # text

# # Enter text (or 'quit'):
# # The cat sat on the mat. The cat is happy!

# # --- Analysis ---
# # Characters (with spaces):    40
# # Characters (no spaces):      32
# # Words:                       10
# # Sentences:                   2
# # Longest word:                happy
# # Most frequent word:          the (3 times)
# # Title case:                  The Cat Sat On The Mat. The Cat Is Happy!
# # No punctuation:              The cat sat on the mat The cat is happy
# # Stretch Goal
# # Display the top 3 most frequent words.


## Mini-Project A: Text Analyzer
text = input("Enter text to anlayse the data: ")
ch_with_spaces = len(text)
ch_without_spaces = len(text.replace(" ", ""))
words_count = len(text.split(" "))


