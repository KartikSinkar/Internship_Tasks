# Task 3:
from solutions import (
    word_frequency,
    character_frequency,
    first_non_repeating_character,
    are_anagrams,
    first_repeating_character,
    move_zeros_to_end,
    second_highest_distinct,
    remove_duplicates,
    find_missing_number,
    two_sum_first_pair,
    closest_to_zero,
    common_elements,
    rotate_right,
    maximum_consecutive_sum,
    all_unique_pairs,
)

# Q1
print("Q1 Example:", word_frequency("python is easy and python is powerful"))
print("Q1 Additional:", word_frequency("red blue red"))

# Q2
print("Q2 Example:", character_frequency("banana"))
print("Q2 Additional:", character_frequency("hello"))

# Q3
print("Q3 Example:", first_non_repeating_character("swiss"))
print("Q3 Additional:", first_non_repeating_character("aabb"))

# Q4
print("Q4 Example:", are_anagrams("listen", "silent"))
print("Q4 Additional:", are_anagrams("hello", "world"))

# Q5
print("Q5 Example:", first_repeating_character("programming"))
print("Q5 Additional:", first_repeating_character("abc"))

# Q6
print("Q6 Example:", move_zeros_to_end([0, 3, 0, 1, 2, 0, 4]))
print("Q6 Additional:", move_zeros_to_end([1, 0, 2]))

# Q7
print("Q7 Example:", second_highest_distinct([10, 20, 40, 30, 40, 20]))
print("Q7 Additional:", second_highest_distinct([5, 5, 5]))

# Q8
print("Q8 Example:", remove_duplicates([4, 2, 4, 5, 2, 7, 5]))
print("Q8 Additional:", remove_duplicates([1, 1, 2, 3, 2]))

# Q9
print("Q9 Example:", find_missing_number([1, 2, 4, 5, 6], 6))
print("Q9 Additional:", find_missing_number([1, 3, 4], 4))

# Q10
print("Q10 Example:", two_sum_first_pair([2, 7, 11, 15], 9))
print("Q10 Additional:", two_sum_first_pair([1, 2, 4], 20))

# Q11
print("Q11 Example:", closest_to_zero([-8, -3, 2, 5, -2]))
print("Q11 Additional:", closest_to_zero([-1, 1, 4]))

# Q12
print("Q12 Example:", common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
print("Q12 Additional:", common_elements([2, 2, 3, 1], [1, 2]))

# Q13
print("Q13 Example:", rotate_right([1, 2, 3, 4, 5], 2))
print("Q13 Additional:", rotate_right([1, 2, 3], 0))

# Q14
print("Q14 Example:", maximum_consecutive_sum([4, 7, 2, 9, 5]))
print("Q14 Additional:", maximum_consecutive_sum([-5, -2, -8]))

# Q15
print("Q15 Example:", all_unique_pairs([2, 4, 3, 5, 7, 8, 1], 9))
print("Q15 Additional:", all_unique_pairs([1, 1, 2, 2, 3], 4))
