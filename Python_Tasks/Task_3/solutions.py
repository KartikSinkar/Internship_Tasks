# Task 3: Python Coding & Problem-Solving

# Q1. Find the Frequency of Each Word in a Sentence
def word_frequency(sentence):
    frequency = {}
    for word in sentence.split():
        frequency[word] = frequency.get(word, 0) + 1
    return frequency


# Q2. Find the Frequency of Each Character in a Word
def character_frequency(word):
    frequency = {}
    for character in word:
        frequency[character] = frequency.get(character, 0) + 1
    return frequency


# Q3. Find the First Non-Repeating Character in a Word
def first_non_repeating_character(word):
    frequency = character_frequency(word)
    for character in word:
        if frequency[character] == 1:
            return character
    return None


# Q4. Check Whether Two Strings Are Anagrams
def are_anagrams(s1, s2):
    return character_frequency(s1) == character_frequency(s2)


# Q5. Find the First Repeating Character in a String
def first_repeating_character(string):
    seen = set()
    for character in string:
        if character in seen:
            return character
        seen.add(character)
    return None


# Q6. Move All Zeros to the End of a List
def move_zeros_to_end(nums):
    non_zeros = [number for number in nums if number != 0]
    zeros = [number for number in nums if number == 0]
    return non_zeros + zeros


# Q7. Find the Second Highest Distinct Number in a List
def second_highest_distinct(nums):
    unique_numbers = sorted(set(nums), reverse=True)
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]


# Q8. Remove Duplicates Without Changing the Original Order
def remove_duplicates(nums):
    result = []
    seen = set()
    for number in nums:
        if number not in seen:
            result.append(number)
            seen.add(number)
    return result


# Q9. Find the Missing Number from 1 to N
def find_missing_number(nums, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


# Q10. Find Two Numbers Whose Sum Equals a Target
def two_sum_first_pair(nums, target):
    seen = []
    for number in nums:
        complement = target - number
        if complement in seen:
            return [complement, number]
        seen.append(number)
    return []


# Q11. Find the Number Closest to Zero
def closest_to_zero(nums):
    if not nums:
        return None
    return min(nums, key=lambda number: (abs(number), -number))


# Q12. Find Common Elements Between Two Lists
def common_elements(list1, list2):
    second_list_values = set(list2)
    result = []
    seen = set()
    for number in list1:
        if number in second_list_values and number not in seen:
            result.append(number)
            seen.add(number)
    return result


# Q13. Rotate a List to the Right by K Positions
def rotate_right(nums, k):
    if not nums:
        return []
    k = k % len(nums)
    if k == 0:
        return nums[:]
    return nums[-k:] + nums[:-k]


# Q14. Find the Maximum Sum of Two Consecutive Elements
def maximum_consecutive_sum(nums):
    return max(nums[index] + nums[index + 1] for index in range(len(nums) - 1))


# Q15. Find All Pairs of Numbers Whose Sum Equals a Target
def all_unique_pairs(nums, target):
    pairs = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pairs.add(tuple(sorted((nums[i], nums[j]))))
    return [list(pair) for pair in sorted(pairs)]
