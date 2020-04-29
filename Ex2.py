from Ex1 import*

class BinaryTree:
    def __init__(self,root):
        self.__root=root

    def getRoot(self):
        return self.__root

    def isRoot(self,node):
        if node == self.__root:
            return True
        else:
            return False

    def size(self,node):
        if node==None:
            return 0
        else:
            return 1+self.size(node.getleft())+self.size(node.getright())

    def printValues(self, node):
        if node is None:
            return ""
        else:
            return self.printValues(node.getleft()) + self.printValues(node.getright()) + " " + str(node.getval())

    def SumValues(self,node):
        if node==None:
            return 0
        else:
            return node.getval() + self.SumValues(node.getleft()) + self.SumValues(node.getright())

    def numberLeaves(self,node):
        if node ==None:
            return 0
        elif node.getright()==None and node.getleft()==None:
            return 1
        else:
            return self.numberLeaves(node.getright()) + self.numberLeaves(node.getleft())

    def numberInternalNodes(self, node):
        if node ==None:
            return 0
        elif node.getright()!=None or node.getleft()!=None:
            return 1+self.numberLeaves(node.getright()) + self.numberLeaves(node.getleft())



    def belongs(self, node, val):
        if node ==None:
            return False
        if node.getval()!=val:
            return self.belongs(node.getright(),val) or self.belongs(node.getleft(),val)
        else:
            return True

    def descendants(self,node,val):
        if node==None:
            return
        if node.getval() == val:
            return self.printValues(node.getleft()) + self.printValues(node.getright())
        else:
            return self.descendants(node.getright(),val), self.descendants(node.getleft(),val)

    def height(self, node):
        if node is None:
            return -1
        else:
            leftHeight = self.height(node.getleft())
            rightHeight = self.height(node.getright())
            print(leftHeight,rightHeight)
            return max(leftHeight, rightHeight) + 1
node1=Node(12)
node2=Node(5)
node3=Node(17)
node4=Node(4)
node5=Node(6)
node6=Node(3)
node7=Node(19)
node8=Node(18)
node9=Node(21)

node1.setleft(node2)
node1.setright(node3)

node2.setleft(node4)
node2.setright(node5)

node4.setleft(node6)
node3.setright(node7)
node7.setright(node9)
node7.setleft(node8)

Arbre=BinaryTree(node1)


print("Le noeud de l'arbre est le noeud :",Arbre.getRoot())
print("Le noeud est-il le noeud racine de l'arbre :",Arbre.isRoot(node1))
print("La taille de l'arbre est :",Arbre.size(node1))
print("Les valeurs des noeuds de l'arbre en commençant par les feuilles sont :",Arbre.printValues(node1))
print("Somme de toutes les valeurs des noeuds de l'arbre :",Arbre.SumValues(node1))
print("Nombre de feuilles dans l'arbre :",Arbre.numberLeaves(node1))
print("nombre de noeuds internes de l'arbre :",Arbre.numberInternalNodes(node1))
print("Le noeud est il présent dans l'arbre :", Arbre.belongs(node1,55))
print("Les descendants du noeud sont les noeuds :",Arbre.descendants(node1,17))
print("La hauteur de l'arbre est",Arbre.height(node1))
