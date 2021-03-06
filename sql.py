#!/usr/bin/python3

import mysql.connector as cn
import random 

db=cn.connect(host="localhost",user="pytester",password="test")
cursor=db.cursor()
#create database
cursor.execute("""CREATE DATABASE IF NOT EXISTS customer""")
db.commit()
#use database
cursor.execute("""USE customer""")
db.commit()

#create tb_customer_account table
cursor.execute("""CREATE TABLE IF NOT EXISTS tb_customer_account(
    id_customer integer PRIMARY KEY,
    cpf_cnpj text,
	nm_customer text,
	is_active bit,
	vl_total float	)""")
db.commit()

cursor.execute(""" SELECT count(*) as tot FROM tb_customer_account """)
data = cursor.fetchone()

if data[0] !=0:
	pass
else:
	names = ["Pedro","Jose","Ana", "Dayana", "Luis", "Maria", "Janet", "Ramon", "Maciel", "Andre Kamicado", "Luisa Jimenez", " David", "Esther", "Yaima", "Raisa", "Jhon", "Victor", "Alejandro", "Danay", "Adriana"   ]
	for i in range(len(names)):
		a = random.randint(0,1) #generating 50-50 True-False Active client 
		my_id = random.randint(1000,4000) # generate id
		cpf_gen  = random.randint(10**8,9*10**8) # generate random cpf can be change to if-else to generate  too cnpj 14 digits
		value  = round(random.uniform(0,2000),2) # generate random value for client
		sql_form = """INSERT INTO tb_customer_account()  VALUES (%s, %s, \'%s\', %s, %s);"""
		sql =  sql_form %( my_id,cpf_gen,names[i], a, value) 
		#print(sql )
		cursor.execute(sql)



sql = "SELECT * FROM tb_customer_account  WHERE id_customer BETWEEN 1500 AND 2700 AND vl_total > 560 ORDER BY vl_total DESC;"
cursor.execute(sql)

results = cursor.fetchall()
for row in results:
      id_customer = row[0]
      cpf_cnpj = row[1]
      nm_customer = row[2]
      is_active = row[3]
      vl_total = row[4]
      # Now print fetched result
      print ("id_customer = %s,cpf_cnpj = %s,nm_customer = %s,is_active = %s,vl_total = %s" % \
             (id_customer, cpf_cnpj, nm_customer, is_active, vl_total ))

cursor.execute("TRUNCATE TABLE tb_customer_account; ")
db.commit()	



"""result = cursor.fetchall()

for i in range(len(result)):
	print(result[i])
"""

cursor.close()   
