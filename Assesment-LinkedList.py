class Node:
   
   def __init__(self, data):
      self.data = data
      self.prev= None
      self.next= None
     

   def add(self,prev= None, next=None):
      self.prev= prev
      self.next= next
    
   
# manufacturer
mf1 = Node('Volks')
mf2 = Node('Ford')

# brands
br1= Node('Brand-A')
br2= Node('Brand-B')

br3= Node('Brand-C')
br4= Node('Brand-D')

# Chass
ch1= Node(123456)
ch2= Node(654321)
ch3= Node(363636)
ch4= Node(555555)


# Add brand address to Chass
ch1.add(br1)
ch2.add(br2)
ch3.add(br3)
ch4.add(br4)


# Add manufacturer and chass address to brand.
br1.add(mf1,ch1)
br2.add(mf1,ch2)
br3.add(mf2,ch3)
br4.add(mf2,ch4)

dict_= {
   123456:ch1,
   654321:ch2,
   363636:ch3,
   555555:ch4
}


def print_data(ch):
    brand = ch.prev.data
    manufacturer = ch.prev.prev.data

    print(manufacturer, brand, ch.data)




input_ch= 654321
ch=dict_[input_ch]
#The input corresponds to the object ch4.
#Let's print
print_data(ch)
