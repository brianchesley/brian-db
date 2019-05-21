def main():
    input_buffer = input("db > ")
    while True:
        if input_buffer[0] == '.':
            meta_command(input_buffer)
    
        statement = Statement(input_buffer)
        if statement.valid:
            pass
        else:
            print("Unrecognized keyword at start of '%s'.\n")

    execute_statement(statement)
    print("Executed.\n")

def meta_command(input):
    if input == ".exit":
        exit()
    else:
        print('command not recognized')

class Statement():
    def __init__(self, input_buffer):
        self.type = self.get_statement(input_buffer)
        self.valid = False

    def get_statement(self, input):
        if input.upper == 'INSERT':
            self.type = 'INSERT'
            self.valid = True
        elif input.upper() == 'SELECT':
            self.type = 'SELECT'
            self.valid = True
        else:
            self.valid = False

def execute_statement(statement):
    if statement.type == 'INSERT':
        print('insert here')
    elif statement.type == 'SELECT':
        print('selecting')
    else:
        print('unknown type')

main()