class Uzel:
    def __init__(self, left, right):
        self.left = left
        self.right = right

def is_symmetric(uzel: Uzel)->bool:
    if uzel == None:
        return True
    if ((uzel.left == None) == (uzel.right == None)):
        return True
    
    list_a1 = []
    list_a1.append(uzel.left)
    list_b1 = []
    list_b1.append(uzel.right)
    
    # prochazeni do sirky
    while True:
        if (len(list_a1) == 0):
            return True
        list_a2 = []
        list_b2 = []
        for i in range(len(list_a1)):
            # checks if the left a is similar to right b
            if ((list_a1[i].left == None) == (list_b1[i].right == None)):
                if (list_a1[i].left != None):
                    list_a2.append(list_a1[i].left)
                    list_b2.append(list_b1[i].right)
            else:
                return False
            # check if the right a is similar to left b        
            if ((list_a1[i].right == None) == (list_b1[i].left == None)):
                if (list_a1[i].right != None):
                    list_a2.append(list_a1[i].right)
                    list_b2.append(list_b1[i].left)
            else:
                return False
        list_a1 = list_a2.copy()
        list_b1 = list_b2.copy()
        