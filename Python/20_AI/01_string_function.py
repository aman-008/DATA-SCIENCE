def convert_to_dash(text):
    result = ''
    
    # Step 1: Replace non-alphanumeric characters with dashes
    for char in text:
        if char.isalnum():  # If the character is a letter or number
            result += char   # Keep it as is
        else:
            result += '-'    # Otherwise, replace it with a dash

    # Step 2: Collapse multiple consecutive dashes into a single dash
    final = ''
    prev_char = ''
    for char in result:
        if char == '-' and prev_char == '-':
            continue  # Skip if the previous character was also a dash
        final += char
        prev_char = char  # Update previous character for next iteration

    # Step 3: Remove leading/trailing dashes and convert to lowercase
    return final.strip('-').lower()

# Test examples to try the function
examples = [
    "hey this is good",              # Simple sentence
    "Hello, World!",                 # Includes punctuation
    "Python_is_awesome!",           # Includes underscores and exclamation
    "Clean   up   this --- string...", # Multiple spaces and dashes
    "123 easy as ABC!"              # Numbers mixed with letters
]

# Run the function on each example and print the result
for i, example in enumerate(examples, 1):
    result = convert_to_dash(example)
    print(f"Example {i}: {result}")
