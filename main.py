def main():
    input_buffer = input('db > ')
    while True:
        if input_buffer == '.exit':
            exit()
        else:
            print("input not recognized  ", input_buffer)
            break

main()