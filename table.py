import pickle

class Table():
    def __init__(self):
        # self.cols = columns
        self.table = []

class Insert():
    def __init__(self, raw_input, table):
        self.valid = self.is_valid()
        self.raw_input = raw_input
        self.table_name = raw_input.split(" ")[2]
        self.row = self.get_row_vals()
        self.table = table

    def get_row_vals(self):
        val_index = self.raw_input.upper().find('VALUES')
        vals = self.raw_input.strip()[val_index + 7:-1].split(",")
        return vals

    def execute(self):
        serialized_row = pickle.dumps(self.row)
        self.table.table.append(serialized_row)
        
    def is_valid(self):
        return True

class Select():
    def __init__(self, table):
        self.table = table.table

    def execute(self):
        for row in self.table:
            print(pickle.loads(row))
        return True

    def is_valid(self):
        pass
