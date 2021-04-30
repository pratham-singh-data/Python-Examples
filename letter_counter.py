def seperator():
    for i in range(100):
        print("*", end = '')
    print()

def count_instances(string, letter):
    step = len(letter)
    
    choice = input("Enter \'y\' if cases are to be considered: ")
    
    if choice == 'y':
        pass
    else:
        string = string.lower()
        letter = letter.lower()
        
    curr = 0
    
    count = 0
    while curr + step <= len(string):
        op_string = string[curr: curr + step]
        curr += step
        
        if op_string == letter:
            count += 1
    
    return count

def letter_counter():
    string = input("Please enter the string that is to be operated on=>\n")
    letter = input("Please enter letter whose total instances are to be found: ")
    
    if letter in string:
        count = count_instances(string, letter)
        print(f"There are {count} instances of \'{letter}\' in given string")
    else:
        print(f"Sorry \'{letter}\' is not in the given string")    
    
    seperator()
    
def greet():
    name = input('What is your name:')
    print(f'Hello {name.title()}')
    
    seperator()
    
    print("This is a letter counter; here we will tell you how many instances of a certain charachter there is in a string")
    print()
    
if __name__ == '__main__':
    greet()
    letter_counter()