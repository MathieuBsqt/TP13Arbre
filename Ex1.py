class Node:
    def __init__(self,val):
        self.__val=val
        self.__right=None
        self.__left=None


    def getright(self):
        return self.__right
    def getleft(self):
        return self.__left
    def setleft(self,left):
        self.__left=left
    def setright(self,right):
        self.__right=right
    def getval(self):
        return self.__val

    def __str__(self):
        return str(self.__val)




