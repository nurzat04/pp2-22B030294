import psycopg2
import csv

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

def get_contacts_with_phone_number(digits):
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts WHERE phone_number LIKE %s", ('%' + digits + '%',))
    rows = cur.fetchall()
    cur.close()
    print(rows)


while True:
    command = input("请输入命令(add,csv,update,delete,get_all,get_one,get_name,get_phone_number,get_name_with_c,exit):")
    if command == "add":
        name = input("请输入联系人的姓名：")
        phone_number = input("请输入联系人的电话号码：")
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
                    print(f"无法添加联系人 {row}: {e}")
    elif command == "update":
        id = input("请输入联系人的ID:")
        name = input("请输入联系人的姓名：")
        phone_number = input("请输入联系人的电话号码：")
        update_contact(id, name, phone_number)
    elif command == "delete":
        n = input("请输入联系人的name:")
        delete_contact(n)
    elif command == "get_all":
        contacts = get_contacts()
        for contact in contacts:
            print(contact)
    elif command == "get_one":
        id = input("请输入联系人的ID:")
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
    elif command == "exit":
        break
    else:
        print("无效的命令，请重新输入。")


# 关闭数据库连接
conn.close()