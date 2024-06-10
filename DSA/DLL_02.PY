class Node:
    def __init__(self,prev = None, item = None, next = None):
        self.prev = prev
        self.item = item
        self.next = next
        
class DLL:
    def __init__(self, start = None):
        self.start = start
        
    def isEmpty(self):
        return self.start == None
    
    def insert_at_start(self,item):
        n = Node(None,item,self.start)
        if not self.isEmpty():
            self.start.prev = n
        self.start = n
        
    def insert_at_last(self,data):
        temp = self.start
        while(temp is not None):
            temp = temp.next
        n = Node(temp,data,None)
        temp.next = n
        
    def search(self,data):
        temp = self.start
        if self.start == None:
            return False
        while temp is not None:
            if temp.item == data:
                return True
            temp = temp.next
        return False
    
    def insert_after(self,data,new_data):
        temp = self.start
        if self.start is None:
            n = (None,data,None)
            self.start = n
        while(temp.item is not data):
            temp = temp.next
            if temp.next is None:
                return False
            n = (temp,new_data,temp.next)
            temp.next.prev = n
            temp.next = n

                
    def traverse(self):
        temp = self.start
        while temp is not None:
            print(temp.item)
            temp = temp.next
            
    def delete_first(self):
        self.start = self.start.next
        self.start.prev = None
        
    def delete_last(self):
        temp = self.start
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None
        
    def delete_item(self,data):
        temp = self.start
        while temp.item is not data:
            temp = temp.next
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
            
        
        
            
            
        