from Ex1 import*

class BinaryTree:
    def __init__(self,root):
        self.__root=root

    def getRoot(self):
        return self.__root

node1=Node(12)
node2=Node(5)
node3=Node(17)
node4=Node(4)
node5=Node(5)
node6=Node(3)
node7=Node(19)
node8=Node(18)
node9=Node(21)


Arbre=BinaryTree(Node(12))
Arbre.getRoot().setleft(Node(5))
Arbre.getRoot().getleft().setleft(Node(4))
Arbre.getRoot().getleft().getleft().setleft(Node(3))

Arbre.getRoot().getleft().setright(Node(6))

Arbre.getRoot().setright(Node(17))
Arbre.getRoot().getright().setright(Node(19))
Arbre.getRoot().getright().getright().setright(Node(21))
Arbre.getRoot().getright().getright().setleft(Node(18))
