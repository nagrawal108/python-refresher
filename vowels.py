# Function to count vowels in each input string and return a list of counts

def count_vowels(strings):
    vowels = "aeiouAEIOU"
    counts = []
    for string in strings:
        count = 0
        for char in string:
            if char in vowels:
                count += 1
        counts.append(count)
    return counts

# Example usage
input_strings = ["Hello World", "Python Programming", "OpenAI"]
vowel_counts = count_vowels(input_strings)
print(vowel_counts)  # Output: [3, 4, 4]


#create a list of even number from 1 to 20
even_numbers = [num for num in range(1, 21) if num % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20] 