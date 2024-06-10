class Node:
    def __init__(self, prev= None, data= None, next= None):
        self.prev = prev
        self.data = data
        self.next = next
        
class DLL:
    def __init__(self,start = None):
        self.start = start
        
    def isempty(self):
        return self.start == None
        
    def insert_first(self,data= None):
        if self.start is None:
            n = Node(data)
            self.start = n
        else:
            n = Node(data)
            n.next = self.start
            self.start = n
            
    def insert_last (self, data = None):
        if self.start is None:
            self.insert_first(data)
            
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            n = Node(data)
            n.prev = temp
            n.next = None
            
    def insert_element(self,element,new_data):
        temp = self.start
        while temp.data != element:
            temp = temp.next
        n = Node(temp,new_data,temp.next)
        temp.next = n
        
            
    
    def traverse(self):
        temp = self.start
        while temp is not None:
            print(temp.data)
            temp = temp.next        
            
        
        
my_obj = DLL()
my_obj.insert_first(10)
my_obj.insert_last(30)
#my_obj.insert_element(10,20)
my_obj.traverse()