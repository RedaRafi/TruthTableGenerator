import re 
import csv
class myStack:
    def __init__(self):
        self.stack = []
    def push(self, x):
        self.stack.append(x)
    def size(self):
        return len(self.stack)
    def empty(self):
        return self.size() == 0
    def top(self):
        return self.stack[-1]
    def pop(self):
        res = self.top()
        self.stack.pop()
        return res

def Priority(c : str): 
# retourner l'ordre de priorité de l'opérateur 
# detection de symbole
    if (c == '('):
        return 0
    elif (c == '>' or c == '~'):
        return 1
    elif (c == 'v' or c == '^'):
        return 2
    else:
        assert(c == '!')
        return 3
def Oper(x : int, y : int , oper : str): 
    """Calculate expression (x oper y), which 'oper' is in [v,^,<->, ->]"""
# Calculer l'expression (x oper y), laquelle 'oper' est dans [v, ^, <->, ->]
    if (oper == 'v'):
        return (x | y) #x v y
    elif (oper == '^'):
        return (x & y) #x ^ y
    elif (oper == '>'):
        return ((1 ^ y) | x) #x -> y
    else:
        assert(oper == '~')
        return (1 if (x == y) else 0) #x <-> y

def preprocess(expression : str):  
    expression = re.sub(' ','', expression) # supprimer tout l'espace
#pour une programmation plus facile, j'ai converti tous les opérateurs multi-caractères en un seul caractère
    expression = re.sub('<->', '~', expression) 
    expression = re.sub('->', '>', expression) 
#- et ! les deux représentent l'opérateur NOT
    expression = re.sub('-', '!', expression)  
# + et v sont tous deux représentatifs de l'opérateur OR
    expression = re.sub('\+', 'v', expression)
#. et ^ les deux représentent l'opérateur AND
    expression = re.sub('\.', '^', expression)  
# supprimer tout !! opérateur
    while (re.search('!!',expression) != None):
        expression = re.sub('!!', '', expression)
    return expression

def GetVariable(expression : str): 
    """Récupère toutes les variables apparues dans 'expression'"""
    SetVar = set()
    ListVar = []
    for c in expression:
        if ('a' <= c) and (c <= 'z') and (c != 'v'): #v is an operator
            if (c in SetVar):
                continue
            SetVar.add(c)
            ListVar.append(c)
    return ListVar

def GetRPN(expression : str): 
# Utilisez l'algorithme de shunting-yard pour obtenir la notation polonaise inverse de l'expression à partir de la notation Infix
    stack = myStack()
    RPN = myStack()
    for c in expression:
        if c == '(':
            stack.push(c)
        elif c == ')':
            while True:
                x = stack.pop()
                if (x != '('):
                    RPN.push(x)
                else:
                    break
        elif c in ['v','^','>','~','!']:
            while (not stack.empty()) and Priority(c) <= Priority(stack.top()):
                RPN.push(stack.pop())
            stack.push(c)
        elif (c == '0' or c == '1' or (('a' <= c) and (c <= 'z') and (c != 'v'))):
            RPN.push(c)
    while (not stack.empty()): 
        RPN.push(stack.pop())
    return RPN

def Calculate(RPN : myStack, VariableValue: dict):  
    """Calculer la valeur d'expression à partir de RPN, avec la valeur de la variable est stockée dans 'VariableValue'"""
    res = myStack()
    for c in RPN.stack:
        if (c == '0' or c == '1' or (('a' <= c) and (c <= 'z') and (c != 'v'))): 
            #'v' est un opperateur 
            res.push(VariableValue[c])
        elif (c == '!'):
            # not X, !X, -X
            res.push(1 ^ res.pop()) 
        else:
            assert(c == '^' or c == 'v' or c == '>' or c == '~')
            x = res.pop()
            y = res.pop()
            res.push(Oper(x, y, c))
    assert(res.size() == 1)
    return res.pop()

def WriteToConsole(result : list):
    for row in result:
        tmp = row.pop()
        for x in row:
            print("  ", x, end = "  |", sep = '') 
        print("  ", tmp, sep = '')
        row.append(tmp)

def WriteToFile(result : list):
    csvFile = open('result.csv','w')
    writer = csv.writer(csvFile)
    writer.writerows(result)
    csvFile.close()

def Solve(expression : str):
    result = []

    ListVariable = GetVariable(expression)
    ListVariable.append(expression)
    result.append(ListVariable.copy())
    ListVariable.pop()

    expression = preprocess(expression)
    RPN = GetRPN(expression)
    n = len(ListVariable)

  # force brute toutes les valeurs de toutes les variables
    for mask in range(2 ** n):
        VariableValue = {'0' : 0, '1' : 1}
        cur = []
        for i in range(n):
            VariableValue[ListVariable[i]] = (mask >> (n - i - 1) & 1)
            cur.append(mask >> (n - i - 1) & 1)
        cur.append(Calculate(RPN, VariableValue))
        result.append(cur)
    WriteToConsole(result)
    WriteToFile(result)

def main():
    file = open("file.txt","r") 
    data=file.readlines()
    print("votre expression => ",data[4])
    # print(data[4])
    Solve(data[4])
    print("tableau stocker dans result.csv  ")

if __name__ == '__main__':
    main()
