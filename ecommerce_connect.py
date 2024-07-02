import sqlite3

connect = sqlite3.connect('ecommerce.db')

# Cursor - Responsável por realizar as operações dentro do DB
cursor = connect.cursor()

cursor.execute("""create table vendas (id Integer Primary Key,
               valor_venda NUM not null,
               cliente_id Integer Not Null,
               foreign key (cliente_id) references clientes (id))""")


cursor.execute("insert into vendas values(1,15.60, 1)")

# Salvar os valores
connect.commit()

cursor.execute("select * from vendas v join cliente c on v.cliente_id = c.id")

# Armazenar todos os valores na variávels
vendas = cursor.fetchall()
print(vendas)

connect.close()