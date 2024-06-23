class Dog():
    type = 'mammal'
    
    def __init__(self,name):
        self.name = name
        
tom = Dog('tom')
kisan = Dog('kisan')

print("tom is a {}".format(tom.type))
print("tom is a {}".format(tom.name))