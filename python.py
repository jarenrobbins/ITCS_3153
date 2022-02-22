from math import dist

#creating variables for methods
lst = [43, 6, 23, 9, 93, 549, 5, 7, 2, 5]
lst1 = [2,4]
lst2 = [5,3]
lst3 = ["this is me", "writing a file", "yay"]

#putting the list in reverse
def practice1(lst):
    lst.reverse()
    return lst

#finding the index of the largest number
def practice2(lst):
    maxpos = lst.index(max(lst))
    return maxpos

#making a new list with only the odd numbers
def practice3(lst):
    only_odd = [num for num in lst if num % 2 == 1]
    return only_odd

#euclidean distance
def practice4(lst1, lst2):
    return dist(lst1, lst2)

#reading a file
def practice5(file):
    f = open(file).read()
    return f.splitlines()

#writing to a file
def practice6(file, lst3):
    f = open(file, "w")
    f.writelines(["%s\n" %item for item in lst3])
    f.close()

#testing methods
print("lst: %s" %lst)
print("lst reversed: %s" %practice1(lst))
print("index of max element: %s" %practice2(lst))
print("odd elements only: %s" %practice3(lst))
print("lst1: %s" %lst1)
print("lst2: %s" %lst2)
print("euclidean distnce: %s" %practice4(lst1, lst2))
print("read file: %s" %practice5("readFile.txt"))
practice6("writeFile.txt", lst3)
print()


#creating a class titles BankAccount
class BankAccount:
    
    #constructor
    def __init__(self, id, balance):
        self.id = id
        self.balance = balance
            
    #deposit method
    def deposit(self, dep):
        self.balance += dep
        return self.balance
    
    #withdrawal method
    def withraw(self, wth):
        self.balance -= wth
        return self.balance
    
#creating two instances of BankAccount
account = BankAccount(0, 200)
account1 = BankAccount(1, 500)

#testing methods
print("account balance: %s" %account.balance)
print("account1 balance: %s" %account1.balance)
print("account1 gives $150 to account because communism")
account1.withraw(150)
account.deposit(150)
print("account balance: %s" %account.balance)
print("account1 balance: %s" %account1.balance)


