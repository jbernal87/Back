#!/usr/bin/python

import random, uuid



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






mc = manage_client()  
# c = client("jose","23733826876","jose luis bernal" , True, 1600)

names = ["Pedro","Jose","Ana", "Dayana", "Luis", "Maria", "Janet", "Ramon", "Maciel", "Andre Kamicado", "Luisa Jimenez", " David", "Esther", "Yaima", "Raisa", "Jhon", "Victor", "Alejandro", "Danay", "Adriana"   ]

def a_random_uuid(string_length=10):
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4()) # Convert UUID format to a Python string.
    random = random.upper() # Make all characters uppercase.
    random = random.replace("-","") # Remove the UUID '-'.
    return random[0:string_length] # Return the random string.

print(a_random_uuid(6))



"""
print(c.is_active())
l = mc.get_client_list()
test to see if mc add client
print(len(l))
mc.add_client(c)
print(len(l))
"""
		
