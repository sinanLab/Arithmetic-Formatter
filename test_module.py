# Example 1: Formatting arithmetic problems without answers
problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
arranged_problems = arithmetic_arranger(problems, show_answers=True)

# Example 2: Formatting arithmetic problems with answers
problems = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
arranged_problems = arithmetic_arranger(problems, show_answers=True)
print(arranged_problems)
