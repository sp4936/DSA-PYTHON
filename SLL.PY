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
            while temp is not None:
                if (temp.data == element):
                    return True
                else:
                    return False
                temp = temp.next
            
        return None
    
    def inser_after(self, data, new_data):
        temp = self.start
        
        while temp.data != data:
            temp = temp.next
        n = Node(new_data, temp.next)
        temp.next = n
        
    def print_all_elements(self):
        temp = self.start
        while temp is not None:
            print(temp.data)
            temp = temp.next
        
                
                
                
my_obj = SLL()
my_obj.insert_at_start(20)
my_obj.print_all_elements()
            
        
        