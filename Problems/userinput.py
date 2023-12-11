class TextInput:
    str_val = ''
    def add(self, character):
        global str_val
        self.str_val += character
        return self.str_val
    
    def get_value(self):
        return self.add('')
  
class NumericInput(TextInput):
    def __init__(self) -> None:
        super().__init__()
        
    str_vals = ''
    def add(self, chara):
        if chara.isnumeric() :
            self.str_vals += chara
        return self.str_vals

if __name__ == '__main__':
    input = NumericInput()
    input.add("1")
    input.add("a")
    input.add("0")
    print("value: ",input.get_value())