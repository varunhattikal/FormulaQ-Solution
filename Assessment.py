def print_full_diamond(num_lines):
    input_string = "FORMULAQSOLUTIONS"
    str_len = len(input_string)
    for i in range(num_lines // 2 + 1):
        chars_to_print = min(i * 2 + 1, str_len)
        spaces = " " * (num_lines // 2 - i)
        line_str = ' '.join(input_string[:chars_to_print])
        print(spaces + line_str.center(num_lines * 2 - 1))
    for i in range(num_lines // 2 - 1, -1, -1):
        chars_to_print = min(i * 2 + 1, str_len)
        spaces = " " * (num_lines // 2 - i)
        line_str = ' '.join(input_string[:chars_to_print])
        print(spaces + line_str.center(num_lines * 2 - 1))
     num_lines = 17
    print_full_diamond(num_lines)
