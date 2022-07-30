#!/usr/bin/env python
# coding: utf-8

# In[38]:


#question 1 :
class point3d :
    def __init__(self,x ,y ,z) :
        self.x = x
        self.y = y
        self.z = z
    def courd (self) :
        print("my point's courdinations are ( {},{},{} )".format(self.x,self.y,self.z))
        
my_point = point3d(1,2,3)
my_point.courd()


# In[41]:


#question 2 :
class rectangle :
    def __init__(self,length,width) :
        self.length = length
        self.width = width 
    def perimeter (self) :
        perimeter = (self.length + self.width) * 2
        print("the rectangle's perimeter is :" ,perimeter)
    def area (self) :
        area = (self.length * self.width)
        print("the rectangle's area is :" ,area)
    
        
        
        
myrectangle = rectangle (4,3)
myrectangle.perimeter()
myrectangle.area()


# In[42]:


#question 3
class circle :
    def __init__(self, ox,oy ,r) :
        self.centerx = ox
        self.centery = oy
        self.radius = r
    def perimeter (self, r) :
        perimeter = 2*3.14*r
        print("the circle's perimeter is",perimeter)
    def area (self , r) :
        area = 3.14*r*r
        print("the circle's area is",area)
    def inside (self ,x ,y) :
        if (x-self.centerx)*(x-self.centerx) + (y - self.centery)*(y-self.centery) <= self.radius*self.radius :
            print('the point is inside the circle')
        else :
            print('the point is not inside the circle')


# In[47]:


#question 4 :
class bank :
    def __init__(self,balance) :
        self.balance = balance
    def deposit (self, depos) :
        newamount = self.balance + depos
        print("the new amount is" ,newamount)
        self.balance = newamount
    def withdraw (self , withd) :
        newamount = self.balance - withd
        print("the new amount is" ,newamount)
        self.balance = newamount


# In[51]:


balance1 = bank(2300) #an example to test , the balance amount is 2300 , then we deposit 200 and withdraw 300


# In[52]:


balance1.deposit(200)


# In[53]:


balance1.withdraw(300)


# In[ ]:




