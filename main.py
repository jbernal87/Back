#!/usr/bin/python

import random

class client:
  def __init__(self, ids, cpf, customer, active, balance ):
	  self.ids = ids
	  self.cpf = cpf
	  self.customer = customer
	  self.active = active
	  self.balance = balance
  
  def id_customer(self):
    return self.ids
  
  def cpf_cnpj(self):
    return self.cpf
  
  def nm_customer(self):
    return self.customer
  
  def is_active(self):
    return "Active" if self.active else "No active"
  
  def vl_total(self):
    return self.balance
    
  
class manage_client():
  def __init__(self):	
    self.client_list = []
  
  def add_client(self,clt):
    self.client_list.append(clt)
    
  def get_client_list(self):
    return self.client_list

  def get_media(self):
    counter = 0
    counter_e = 0
    for x in self.client_list:
      an_id = x.id_customer() 
      value = x.vl_total()
      if an_id > 1500 and an_id < 2700 and value>560 :
        print(x.nm_customer())
        counter+=value
        counter_e+=1
    
    return counter/counter_e if counter_e > 0 else 0
        

mc = manage_client()  
# c = client("jose","23733826876","jose luis bernal" , True, 1600)

names = ["Pedro","Jose","Ana", "Dayana", "Luis", "Maria", "Janet", "Ramon", "Maciel", "Andre Kamicado", "Luisa Jimenez", " David", "Esther", "Yaima", "Raisa", "Jhon", "Victor", "Alejandro", "Danay", "Adriana"   ]

for i in range(0,20):
  a = random.randint(1,2) #generating 50-50 True-False Active client
  if a == 1:
	  a == True
  else:
	  a == False
	  
  my_id = random.randint(1000,4000) # generate id
  cpf_gen  = random.randint(10**8,9*10**8) # generate random cpf can be change to if-else to generate  too cnpj 14 digits
	
  a_client = client(my_id,cpf_gen,names[i], a , random.randint(0,4000))
	
  mc.add_client(a_client)
  
  
print(mc.get_media())

	



"""
print(c.is_active())
l = mc.get_client_list()
test to see if mc add client
print(len(l))
mc.add_client(c)
print(len(l))
"""
		
