from turtle import left


class Node:
    def __init__(self, value, left, right, direction, parent, color="red"):
        self.value=value
        self.left=left
        self.right=right
        self.color=color
        self.parent=parent
        self.direction=direction
    def set_right(self, value):
        self.right=Node(value, None, None, "right", self)
    def set_left(self,value):
        self.left=Node(value, None, None, "left", self)
    def print(self):
        print("value is equal to" , self.value, "right child is", self.right, "left child is", self.left, "color is", self.color)
    
   
class Tree:
    def __init__(self, value):
        self.root=Node(value, None, None, "root", None, "black")

    def add(self, item):
        grandparent=None
        current_node=self.root
        direction_of_sibling=""
        while(True):
            if (item<current_node.value):
                if (current_node.left != None):
                    grandparent=current_node
                    current_node=current_node.left
                    direction_of_sibling="right"
                else:
                    current_node.set_left(item)
                    sibling=None
                    #return x,y,z,sibling
                    if direction_of_sibling=="right" and grandparent !=None:
                        sibling=grandparent.right  
                    elif direction_of_sibling=="left" and grandparent !=None:
                        sibling=grandparent.left
                    return current_node.left, current_node, grandparent, sibling
            else:
                if (current_node.right != None):
                    grandparent=current_node
                    current_node=current_node.right
                    direction_of_sibling="left"
                else:
                    current_node.set_right(item)
                    sibling=None
                    #return x,y,z,sibling
                    if direction_of_sibling=="right" and grandparent !=None:
                        sibling=grandparent.right  
                    elif direction_of_sibling=="left" and grandparent !=None:
                        sibling=grandparent.left
                    return current_node.right, current_node, grandparent, sibling
                            
    def insert_and_balance(self, item):
        x,y,z,s=self.add(item)
        self.rebalance_insert(x)

        #will be shorter
        #will call add and rebalanceInsert method within insert method
        
    def rebalance_insert(self, x):
        if self.root==x:
            x.color="black"
        else:                    
            x.color="red"
            y=x.parent
            if y.color=="red":
                z=y.parent
                if y.direction=="right":
                    s=z.left
                else:
                    s=z.right
                #double red condition. Balance out depending
                #on color of sibling

                if s==None or s.color=="black":
                    a,b,c=self.restructure(x)
                    b.color="black"
                    a.color="red"
                    c.color="red"
                else:
                    y.color="black"
                    s.color="black"
                    z.color="red"
                    self.rebalance_insert(z)

    def restructure(self, x):
        y = x.parent
        z = y.parent
    
        ## Left Left condition
        if y.direction == "left" and x.direction == "left":
		## Store metadata about z
            original_z_direction = z.direction
            original_z_parent = z.parent
		
        ## Swapping y,z and t as needed
            t = y.right
            y.right = z
            z.left = t
		
		## Change the direction and parents of y, z and t as needed
            if t !=None:
                t.parent = z
                t.direction = "left"
		
            z.parent = y
            z.direction = "right"
		
            if original_z_direction == "root":
		    ## Set the root of tree as y
                y.direction = "root"
                y.parent = None
                self.root = y
            elif original_z_direction == "left":
                y.direction = "left"
                y.parent = original_z_parent
                original_z_parent.left = y
            else:
                y.direction = "right"
                y.parent = original_z_parent
                original_z_parent.right = y
            return x,y,z
        elif y.direction=="right" and x.direction=="right":

            original_z_direction=z.direction
            original_z_parent=z.parent
            #Perform swapping
            t=y.left
            y.left=z
            z.right=t


            #Update Properties
        
            if t!=None:
                t.parent=z
                t.direction="right"

            z.parent=y
            z.direction="left"

            if original_z_direction=="root":
                y.direction="root"
                y.parent=None
                self.root=y



            elif original_z_direction=="left":
                y.direction="left"
                y.parent=original_z_parent
                original_z_parent.left=y



            else:
                y.direction="right"
                y.parent=original_z_parent
                original_z_parent.right=y
        
            return x,y,z

        elif y.direction=="left" and x.direction=="right":

            z.left=x
            x.left=y
            y.right=None
            #Update directions for x

            x.direction="left"

            #Update parents for x and y
            x.parent=z
            y.parent=x
            
            

            return self.restructure(y)

        else:

            #Perform SWAP

            z.right=x
            x.right=y
            y.left=None

            #Update directions for all variables
            
            y.parent=x
            x.parent=z
            x.direction="right"
            



            #Update Parents

            return self.restructure(y)
            

		
    

    def print(self):
        #obtain current_node. Traverse to the left. Once the child of the current_node is a None node, print current_node.
        #Print parent of current_node. Print right child or parent node.

        #Start from left. Left most node in tree. Once we reach left most node. Print that node
        #Print parent node. Traverse towareds right.


        current_node=self.root

        self.in_order_traversal(current_node)

    def in_order_traversal(self, node):
        if node.left !=None:
            self.in_order_traversal(node.left)
       
        print(node.value, node.color)

        if node.right !=None:
            self.in_order_traversal(node.right)


            

        
        

        




            #
            

            



    # def obtain_values(self, item):
    #     #obtain node, parent, grandparent, grandparent's parent, and sibling
    #     #obtain x,y,z, grandparent's parent, and s
    #     great_grandparent=None
    #     grandparent=None
    #     current_node=self.root
    #     direction_of_sibling=""
    #     while(True):
    #         if (item<current_node.value):
    #             if (current_node.left != None):
    #                 great_grandparent=grandparent
    #                 grandparent=current_node
    #                 current_node=current_node.left
    #                 direction_of_sibling="right"

    #             else:
    #                 sibling=None
    #                 #return x,y,z,sibling
    #                 if direction_of_sibling=="right" and grandparent !=None:
    #                     sibling=grandparent.right  
    #                 elif direction_of_sibling=="left" and grandparent !=None:
    #                     sibling=grandparent.left
    #                 return current_node.left, current_node, grandparent, great_grandparent, sibling


    #         else:
    #             if (current_node.right != None):
    #                 great_grandparent=grandparent
    #                 grandparent=current_node
    #                 current_node=current_node.right
    #                 direction_of_sibling="left"
    #             else:
    #                 sibling=None
    #                 #return x,y,z,sibling
    #                 if direction_of_sibling=="right" and grandparent !=None:
    #                     sibling=grandparent.right  
    #                 elif direction_of_sibling=="left" and grandparent !=None:
    #                     sibling=grandparent.left
    #                 return current_node.right, current_node, grandparent, great_grandparent, sibling




        

        #pseudocode is provided
        #think about way to get parent, grandparent, and sibling
        #multiple inside rebalance insert
        #utility functions(to get parent of node)




        #if we are at root node, return root node. otherwise, traverse everything else.

    



t=Tree(5)
t.insert_and_balance(9)
t.insert_and_balance(6)
# t.insert_and_balance(1)
# t.insert_and_balance(9)
# t.insert_and_balance(0)
# t.insert_and_balance(0.5)
# t.insert_and_balance(3)
# t.insert_and_balance(8)
# t.insert_and_balance(6)


t.print()
print(t.root.value)










#Add a node

#might need rotation algorithm

#try implement other things in template