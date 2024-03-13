def check_fibonacci(num):
    sequence = [0, 1]
    while sequence[-1] <= num:
        sequence.append(sequence[-2] + sequence[-1])
    return num == sequence[-2]

while True:
    try: 
        input_num = int(input('Digite o número que deseja verificar:\n'))
        break
    except ValueError:
        print('\nPor favor, digite um número inteiro.\n')

is_on_fibonacci = check_fibonacci(input_num)

print((f"O número {input_num} "
       f"{'não pertence' if not is_on_fibonacci else 'pertence'} "
       "a sequência fibonacci."))
