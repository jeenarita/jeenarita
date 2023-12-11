# group the keys of same values
# ******************************
dict = {'a':1, 'b':2, 'd':3, 'c':2 }
print(dict.get(2))
result = {}
for key, value in dict.items():
    result[value] = result.get(value, []) + [key]
    print(value)
    print("result.get(value, [])----",result.get(value, []))
    print("reslt[value]---",result[value])
    print(result)

print(result)

# *****************************************************************************************************

def group_by_owners(files):
    result = {}
    for key, value in files.items():
        result[value] = result.get(value, []) + [key]
    
    return result

if __name__ == "__main__":    
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }   
    print(group_by_owners(files))
