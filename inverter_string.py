def invert_string(string):
    inverted_str = ''
    for idx in range(len(string)-1, -1, -1):
        inverted_str += string[idx]
    return inverted_str


input_string = input('Digite a string que deseja inverter:\n')
inverted_input = invert_string(input_string)
print(f"Sua string invertida: {inverted_input}")