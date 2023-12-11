import collections

Node = collections.namedtuple('Node', ['left', 'right', 'value'])

def contains(root, value):
    value_exists = False
    if root.value == value:
        return True
    elif root.value < value:
        if root.right == None:
            return False
        else:
            
            return contains(root.right, value)
            
    else:
        if root.left == None:
            return False
        else:
            
            return contains(root.left, value)
           
        
        
        
        if value_exists :
            return True
        else:
            return False
        
    
n1 = Node(value=1, left=None, right=None)
n3 = Node(value=3, left=None, right=None)
n2 = Node(value=2, left=n1, right=n3)
        
print(contains(n2,3))


 # if root.left != None and root.right != None:
        #     left_subtree = contains(root.left,value)
        #     right_subtree = contains(root.right, value)
        # elif root.left != None or root.right != None:  
        #     if root.left != None:
        #         left_subtree = contains(root.left,value)
        #     else:
        #         right_subtree = contains(root.right, value)
        # else:
        #     return False    
        
        # if left_subtree or right_subtree :
        #     return True