"""
Tree
-------

This is the tree file, it holds the main data structure that will be used for
testing. The tree contains a root node which then has children until the
leaves.
This is the main file for the interaction of tests.

Your task is to implement the methods for put and flatten.
"""

class Tree:


    """
    Tree Class
    Holds nodes, where each node in the tree has children, unless it is a leaf,
    where it has 0 children.

    Each node in the tree is type <class Node> defined in `node.py`.

    - Init: Sets up the tree with the specified root node.
    - put(node, child): Adds the child node to the specified node in the tree.
    - flatten(node): flatten the node.
    - swap(subtree_a, subtree_b): Swap the position of the subtrees.
    """

    #EACH NODE IN TREE IS TYPE CLASS NODE




    def __init__(self, root):
        """
        Initialises the tree with a root node.
        :param root: the root node.
        """
        self.root = root
        self.total = 0








    def subtree_up(self,node):
        subtree = 0
        # print("This is node: " + str(node.key))


        while(node.parent != None):
            subtree = node.subtree_value
            # print("THIS IS USBTRE: " + str(subtree))

            if(subtree > node.parent.subtree_value):

                node.parent.subtree_value = subtree

                node = node.parent
            else:
                node = node.parent

        if(node.parent == self.root):
            if(self.root.subtree_value < node.subtree_value):
                self.root.subtree_value = node.subtree_value

            else:
                self.root.subtree_value = self.root.key
            return



    def reset_subtree(self,node):
        if(node == self.root):
            node.subtree_value = node.key


        while(node.parent != None):


            node.subtree_value = node.key

            node = node.parent









    def put(self, node, child):
        """
        Inserts a node into the tree. Adds `child` to `node`.
        :param node: The node currently in the tree.
        :param child: The child to add to the tree.
        """
        node.add_child(child)
        self.subtree_up(child)




    def flatten_method(self, node,parent):


        oringalparent = parent
        # print("This is the parent: " + str(parent.key))

        if(node.parent != None):


            currentParent = node.parent
            # print("This is the node's parent changing: " + str(node.parent.key))

        else:
            return self.total

        if(len(node.children) >0):
            # print("This is the first children; "+ str(node.children[0].key))

            return self.flatten_method(node.children[0],oringalparent)

        else:
            if(node.parent == oringalparent):

                return self.total
            else:

                self.total  +=  node.key
                del node.parent.children[0]
                return self.flatten_method(currentParent,oringalparent)


    def flatten(self,node):
        if(node.parent != None):
            x = node.parent
            y = self.flatten_method(node,x)
            node.key += y
            self.total = 0
            node.subtree_value = node.key
            self.reset_subtree(node)
            self.subtree_up(node)
        else:
            total = 0
            while (len(node.children) >0):
                total += node.children[0].key
                del node.children[0]

            node.key = node.key + total
            node.subtree_value = node.key












        """
        Flatten the node given by removing the subtree rooted at this node.
        You must (a) flatten the subtree, (b) compute the sum of all nodes
        below and perform any updates
        to other nodes.

        :param node: The root of the subtree to flatten.

        Example

           A(5)
           / \
         B(3) C(6)
         /    |  \
        D(2) E(3) F(6)

        flatten(C)

           A(5)
           / \
         B(3) C(15)
         /
        D(2)

        """
# 1. get the children of node C  --> get the sum
#2. if each children has children --> gett the sum
#RECUSION OF GET SUM



        # TODO implement me.




    def swap(self, subtree_a, subtree_b):
#removing parent containing current node
        parentA = subtree_a.parent # ROOT
        parentB = subtree_b.parent # NODE_E



        for i in parentA.children:
            if (i == subtree_a):
                parentA.children.remove(i)




        for i in parentB.children:
            if (i == subtree_b):
                parentB.children.remove(i)




        if subtree_a not in parentB.children:

            self.put(parentB,subtree_a)



        if subtree_b not in parentA.children:

            self.put(parentA,subtree_b)

        subtree_a.parent = parentB
        subtree_b.parent = parentA


        self.reset_subtree(subtree_a.parent)
        self.reset_subtree(subtree_b.parent)



        subtree_a.parent.find_subtree()
        subtree_b.parent.find_subtree()

        self.subtree_up(subtree_a)
        self.subtree_up(subtree_b)







        """
        Swap subtree A with subtree B
        :param subtree_a: The root node of subtree_a.
        :param subtree_b: The root node of subtree_b.

        Example:

            A
           / \
           B  C
         /   / \
        D   J   K

        SWAP(B, C)
            A
           / \
          C  B
         / |  \
        J  K   D
        """
        # TODO implement me.
