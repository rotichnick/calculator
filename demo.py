import psycopg2
conn=psycopg2.connect(dbname="postgres", user="postgres",password="1234",host="localhost",port="5432")
def create_table():
    cur=conn.cursor()
    cur.execute('''CREATE TABLE student(ID SERIAL, name text, age text, address text)''')
    conn.commit()
    conn.close()
    print("conn success")
def insert_data():
    conn=psycopg2.connect(dbname="postgres", user="postgres",password="1234",host="localhost",port="5432")
    cur=conn.cursor()
    name=input('name')
    age=input("age")
    address=input("address")
    query=('''INSERT INTO student(name, age, address) VALUES (%s,%s,%s);''')
    cur.execute(query,(name, age,address))
    conn.commit()
    conn.close()
    print("data inserted")

insert_data()