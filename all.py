#!/usr/bin/python3

import mysql.connector as cn 
import random 


class Database:
	host = 'localhost'
	user = 'pytester'
	password = 'test'
	data_base = 'customer'

	def __init__(self):
		self.db = cn.connect(host=self.host, user=self.user,password=self.password)
		self.cursor=self.db.cursor()
		self.cursor.execute("""CREATE DATABASE IF NOT EXISTS %s""" % self.data_base)
		self.cursor.execute("""USE customer""")
		self.db.commit()
	
	

	def do_query(self, query):
		try:
			self.cursor.execute(query)
			self.db.commit()
		except:
			self.db.rollback()

	def get_query(self, query):
		cursor = self.db.cursor()
		cursor.execute(query)
		return cursor.fetchall()

	def __del__(self):
		self.db.close()
		


db = Database()

names = ["Pedro","Jose","Ana", "Dayana", "Luis", "Maria", "Janet", "Ramon", "Maciel", "Andre Kamicado", "Luisa Jimenez", " David", "Esther", "Yaima", "Raisa", "Jhon", "Victor", "Alejandro", "Danay", "Adriana"   ]

for i in range(len(names)):
	a = random.randint(0,1) #generating 50-50 True-False Active client 
	my_id = random.randint(1000,4000) # generate id
	cpf_gen  = random.randint(10**8,9*10**8) # generate random cpf can be change to if-else to generate  too cnpj 14 digits
	value  = round(random.uniform(0,2000),2) # generate random value for client
	
	sql_form = """INSERT INTO tb_customer_account()  VALUES (%s, %s, \'%s\', %s, %s);"""
	sql =  sql_form %( my_id,cpf_gen,names[i], a, value) 

	db.do_query(sql)


select_sql = "SELECT * FROM tb_customer_account  WHERE id_customer BETWEEN 1500 AND 2700 AND vl_total > 560 ORDER BY vl_total DESC;"

people = db.get_query(select_sql)

counter = 0;
for row in people:
	id_customer = row[0]
	cpf_cnpj = row[1]
	nm_customer = row[2]
	is_active = row[3]
	vl_total = row[4]
	counter += vl_total
      # Now print fetched result
	print ("id_customer = %s, cpf_cnpj = %s, nm_customer = %s, is_active = %s, vl_total = %s" % \
             (id_customer, cpf_cnpj, nm_customer, is_active, vl_total ))


print("média do campo vl_total: {}".format(round(counter/len(people),2)) )

db.do_query("TRUNCATE TABLE tb_customer_account; ") # clear table to keep the program simple


