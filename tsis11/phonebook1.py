import psycopg2
import csv
import sqlite3

# 连接到PostgreSQL数据库
conn = psycopg2.connect(database="dev", user="postgres", password="nanaw040310", host="localhost", port="5432")

# 添加联系人
def add_contact(name, phone_number):
    cur = conn.cursor()  
    cur.execute("INSERT INTO contacts (name, phone_number) VALUES (%s, %s)", (name, phone_number))
    conn.commit()
    cur.close()

# 更新联系人
def update_contact(id, name, phone_number):
    cur = conn.cursor()
    cur.execute("UPDATE contacts SET name=%s, phone_number=%s WHERE id=%s", (name, phone_number,id))
    conn.commit()
    cur.close()

# 删除联系人
def delete_contact(name):
    cur = conn.cursor()
    cur.execute("DELETE FROM contacts WHERE name = %s", (name,))
    conn.commit()
    cur.close()

# 获取所有联系人
def get_contacts():
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts")
    rows = cur.fetchall()
    cur.close()
    return rows

# 获取单个联系人
def get_contact(id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts WHERE id=%s", (id,))
    row = cur.fetchone()
    cur.close()
    return row

def get_contacts_by_name(name):
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts WHERE name = %s", (name,))
    rows = cur.fetchall()
    cur.close()
    return rows
'''def get_contact_by_name(name):
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts WHERE name = %s", (name,))
    row = cur.fetchone()
    cur.close()
    return row'''

def get_contact_by_character(char):
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts WHERE name LIKE %s", ('%'+char+'%',))
    rows = cur.fetchall()
    cur.close()
    return rows

def get_contacts_with_phone_number( digits):
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts WHERE phone_number LIKE %s", ('%' + digits + '%',))
    rows = cur.fetchall()
    cur.close()
    return rows
def call_insert_user(name, phone):
    cur = conn.cursor()
    cur.execute("CALL insert_or_update_contact(%s, %s)", (name, phone))
    conn.commit()
    cur.close()

def call_insert_users():
    cur = conn.cursor()
    # ask the user to enter a list of sub-lists
    input_str = input("Enter a list of sub-lists in the format [['name1', 'number1'], ['name2', 'number2'], ...]: ")
    # evaluate the input string as a Python expression to get the list of sub-lists
    contacts_list = eval(input_str)
    #contacts_list = [['John Doe', '1234567890'],['Jane Smith', '2345678901'],['Bob Johnson', '3456789012'],['Alice Lee', '4567890123']]
    # 将参数列表转换为 PostgresSQL 数组格式
    contacts_array = psycopg2.extensions.adapt(contacts_list).getquoted().decode()
    # 构建存储过程的 SQL 语句
    sql = f"CALL insert_multiple_contacts({contacts_array})"
    # 执行存储过程
    cur.execute(sql)
    conn.commit()
    cur.close()

def get_data_with_pagination(table_name, limit, offset):
    cur = conn.cursor()
    # execute SQL query
    query = "SELECT * FROM {} LIMIT %s OFFSET %s".format(table_name)
    cur.execute(query, (limit, offset))
    # fetch rows
    rows = cur.fetchall()
    conn.close()
    return rows

def delete():
    cur = conn.cursor()
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    cur.execute("CALL delete_data(%s, %s)", (name, phone_number))
    conn.commit()
    cur.close()

while True:
    command = input("which one?(add,csv,update,delete,get_all,get_one,get_name,get_phone_number,get_name_with_c,exit,pro,multiple_contacts,query,dele):")
    if command == "add":
        name = input("please enter the name:")
        phone_number = input("please enter the phone number:")
        add_contact(name, phone_number)
    elif command == "csv":
        with open('contacts.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)  # 跳过CSV文件的标题行
            for row in reader:
                try:
                    name = row[0]
                    phone_number = row[1]
                    add_contact(name, phone_number)
                except (IndexError, ValueError) as e:
                    print(f"Coundn't add... {row}: {e}")
    elif command == "update":
        id = input("please enter the ID:")
        name = input("please enter the name:")
        phone_number = input("please enter the phone number:")
        update_contact(id, name, phone_number)
    elif command == "delete":
        n = input("please enter the name:")
        delete_contact(n)
    elif command == "get_all":
        contacts = get_contacts()
        for contact in contacts:
            print(contact)
    elif command == "get_one":
        id = input("please enter contact's id:")
        contact = get_contact(id)
        print(contact)
    elif command == "get_name":
        name = input("please enter name:")
        names = get_contacts_by_name(name)
        print(names)
    elif command == "get_phone_number":
        pn = input("please enter digit:")
        pns = get_contacts_with_phone_number(pn)
        print(pns)
    elif command == "get_name_with_c":
        c = input("please enter character:")
        cs = get_contact_by_character(c)
        print(cs)
    elif command == "pro":
        namee = input("please enter your name:")
        phonen = input("please enter your phone number:")
        call_insert_user(namee,phonen)
    elif command == "multiple_contacts":
        call_insert_users()
    elif command == "query":
        data = get_data_with_pagination("contacts", 10, 0)
        print(data)
    elif command == "dele":
        delete()
    elif command == "exit":
        break
    else:
        print("error execution...")
    

# 关闭数据库连接
conn.close()