

def check_brackets(string line):
    #checks if there is the same number of brackets in the string, basic version
    #need to make better to prevent cases like ))a+b(( which would evaluate
    #correctly with current implementation
    open_brac = line.count('(')
    close_brac = line.count(')')
    return open_brac == close_brac

def check_operators(string line):
    operators = ['+','-','/','^','*']
    for op in operators:
        #gets the indeces of operators in the string
        ind.append(index_of_operators.append([i for i, thing in enumerate(line) if thing == op]))

    for ind in indeces:
        #checks if there is a case of two operators together with no number
        if not any([((line[x-1] in operators) and (line[x+1] in operators)) for x in ind]):
            return False
    return True
