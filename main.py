#Zacząłem trochę bezsensu rozkminiać samemu dlatego implementacja
#różni się trochę od tych standardowych typu:
#class newNode:
#    def __init__(self, key):
#        self.key = key
#        self.left = None
#        self.right = None
#
# Function to find sum of all the element
#def addBT(root):
#    if (root == None):
#        return 0
#    return (root.key + addBT(root.left) +
#                       addBT(root.right))
#



#Jednak dokończyłem juz po swojemu. Wynik mojej pracy można obejrzeć niżej.
# implementacja klasy dla wierzchołków
class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

# implementacja klasy zawieracjącej metody
class Methods:
    def __init__(self, node):
        self.node = node

    def MAKE_LIST(self, node):
        list = []

        def make_list(nod, visited):
            visited.append(nod.val)
            for v in nod.children:
                make_list(v, visited)

        make_list(node, list)
        return list

    def sum(self):
        l = self.MAKE_LIST(self.node)
        suma = 0
        for element in l:
            suma = suma + element
        return suma

    def average(self):
        l = self.MAKE_LIST(self.node)
        suma = 0
        for element in l:
            suma = suma + element
        average = suma/len(l)
        return average

    def median(self):
        lst = self.MAKE_LIST(self.node)
        sortedLst = sorted(lst)
        lstLen = len(lst)
        index = (lstLen - 1) // 2
        if (lstLen % 2):
            return sortedLst[index]
        else:
            return (sortedLst[index] + sortedLst[index + 1]) / 2.0


# implementacja wierzchołków
a = Node(5)
b = Node(3)
c = Node(7)
d = Node(2)
e = Node(5)
f = Node(1)
g = Node(0)
h = Node(2)
i = Node(8)
j = Node(5)

# implemetacja położenia względem innych wierzchołków
a.children = [b, c]
b.children = [d, e]
c.children = [f, g]
g.children = [h, i]
i.children = [j]

# stworzenie obiektu wyliczającego metody dla całego drzewa
count1 = Methods(a)

# wywołanie metod dla obiektu count1
print(count1.sum())
print(count1.average())
print(count1.median())

# stworzenie obiektu wyliczającego metody dla poddrzewa zaczynającego się od wierzchołka c
count2 = Methods(c)

# wywołanie metod dla obiektu count2
print(count2.sum())
print(count2.average())
print(count2.median())

#Wyniki się zgadzają, niestety testów juz nie zdążyłem bo jest czwartek wieczór i termin mnie goni.