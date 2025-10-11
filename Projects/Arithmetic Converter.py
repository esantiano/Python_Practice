import re

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
        
    
    var1 = []
    var2 = []
    ops = []
    spaces = []
    # remove the elements of the problem place them into appropriate lists
    for problem in problems:
        bSpace = problem.find(' ')
        eSpace = problem.find(' ',bSpace+1)
        
        first = captureFirst(problem)
        second = captureSecond(problem,bSpace)
        operation = captureOp(problem, bSpace,eSpace)
        if validateVar(first):
            if checkVarLen(first):
                var1.append(first)
            else:
                return 'Error: Numbers cannot be more than four digits.'
        else:
            return 'Error: Numbers must only contain digits.'
        
        if validateVar(second):
            if checkVarLen(second):
                var2.append(second)
            else:
                return 'Error: Numbers cannot be more than four digits.'
        else:
            return 'Error: Numbers must only contain digits.'
        
        if checkOp(operation):
            ops.append(operation)
        else:
            return 'Error: Operator must be \'+\' or \'-\'.'

        spaces.append(max(len(first), len(second)))
    
    finalStr = ''
    # create string
    for i in range(len(var1)):
        finalStr += var1[i].rjust(spaces[i]+2, ' ')
        if i != len(var1)-1:
            finalStr += ' '*4
    finalStr += '\n'

    for i in range(len(var2)):
        finalStr += ops[i]
        finalStr += var2[i].rjust(spaces[i]+1)
        if i != len(var2)-1:
            finalStr += ' '*4
    finalStr += '\n'
    
    for i in range(len(spaces)):
        finalStr += '-'*(spaces[i]+2)
        if i != len(spaces)-1:
            finalStr += ' '*4
    
    if show_answers:
        finalStr += '\n'
        for i in range(len(problems)):
            result = 0
            if ops[i] == '+':
                result = int(var1[i]) + int(var2[i])
            else:
                result = int(var1[i]) - int(var2[i])
            finalStr += str(result).rjust(spaces[i]+2, ' ')
            if i != len(problems)-1:
                finalStr += ' '*4
    return finalStr

def captureFirst(problem):
    bSpace = problem.find(' ')
    return problem[:bSpace]

def captureSecond(problem, bSpace):
    eSpace = problem.find(' ', bSpace+1)
    return problem[eSpace+1:]

def captureOp(problem, bSpace, eSpace):
    return problem[bSpace+1:eSpace]

def checkVarLen(var):
    return len(var) <= 4
        
def validateVar(var):
    regex = r'[0-9]+'
    return re.fullmatch(regex,var)

def checkOp(var):
    regex = r'[+-]'
    return re.fullmatch(regex,var)

print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
print('  3801      123\n-    2    +  49\n------    -----')
print('\n')

print(arithmetic_arranger(["1 + 2", "1 - 9380"]))
print('  1         1\n+ 2    - 9380\n---    ------')

print('\n')
print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
print('    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----')

print('\n')
print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))
print('  11      3801      1      123         1\n+  4    - 2999    + 2    +  49    - 9380\n----    ------    ---    -----    ------')

print('\n')
print(arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]))
print(arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]))

print(arithmetic_arranger(["3 + 855", "988 + 40"], True))
print('\n')
print('    3      988\n+ 855    +  40\n-----    -----\n  858     1028')
print('\n')
print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))
print('\n')
print('   32         1      45      123      988\n- 698    - 3801    + 43    +  49    +  40\n-----    ------    ----    -----    -----\n -666     -3800      88      172     1028')