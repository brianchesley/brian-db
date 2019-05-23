from table import Insert, Select

class Statement():
    def __init__(self, input_buffer, table):
        self.statement = input_buffer.split(" ")
        self.raw_input = input_buffer
        self.table = table        
        self.statement_factory()
        self.valid = True
        
    def statement_factory(self):
        if self.statement[0].upper() == 'INSERT':
            self.statement_class = Insert(self.raw_input, self.table)
        elif self.statement[0].upper() == 'SELECT':
            self.statement_class = Select(self.table)

    def execute(self):
        self.statement_class.execute()
        