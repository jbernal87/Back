#!/usr/bin/python


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
    
  
  

c = client("jose","343455647864578","jose luis bernal" , True, 1600)

print(c.is_active())
		
