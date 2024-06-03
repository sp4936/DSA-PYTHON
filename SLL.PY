'''Singly Linked List'''

class Node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next
        
class SLL:
    def __init__(self, start = None):
        self.start = start
        
    def is_empty(self):
        return self.start == None
    
    def insert_at_start(self, data):
        n = Node(data,self.start)
        self.start = n
        
    def insert_at_last(self,data):
        n = Node(data, next = None)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            self.start = n
            
    def search(self, element):
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                if (temp.data == element):
                    return True
                else:
                    return False
            
        return False
                
            
        
        