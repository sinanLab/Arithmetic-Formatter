def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dash_line = []
    answer_line = []

    for problem in problems:
        # Split the problem into operands and operator
        operand1, operator, operand2 = problem.split()

        # Check if the operands are valid integers
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        # Check if the operator is valid
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Check if the operands are within four digits
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calculate the answer
        if operator == '+':
            answer = str(int(operand1) + int(operand2))
        else:
            answer = str(int(operand1) - int(operand2))

        # Determine the maximum length of operands for alignment
        max_length = max(len(operand1), len(operand2))

        # Add the formatted strings to each line
        first_line.append(operand1.rjust(max_length + 2))
        second_line.append(operator + operand2.rjust(max_length + 1))
        dash_line.append('-' * (max_length + 2))
        answer_line.append(answer.rjust(max_length + 2))

    # Join the lines with spaces between each problem
    arranged_problems = '    '.join(first_line) + '\n'
    arranged_problems += '    '.join(second_line) + '\n'
    arranged_problems += '    '.join(dash_line)

    if show_answers:
        arranged_problems += '\n' + '    '.join(answer_line)

    return arranged_problems
