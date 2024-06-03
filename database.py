import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
import re


# 插入数据的函数
def insert_person(name, age, zodiac, birth_planet, residence_planet):
    if not name:
        messagebox.showerror("Error", "姓名不能为空!")
    if re.search(r'\d', name):
        messagebox.showerror("Error", "姓名中不能有阿拉伯数字!")
        return
    else:
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Llh032002",
                database="MigrationDB"
            )
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO Person (name, age, zodiac, birth_planet, residence_planet)
                VALUES (%s, %s, %s, %s, %s)
            """, (name, age, zodiac, birth_planet, residence_planet))

            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Person data inserted successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")


# 查询所有数据的函数
def view_all_persons():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Llh032002",
            database="MigrationDB"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Person")
        records = cursor.fetchall()
        conn.close()
        return records
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
        return []


# 更新数据的函数
def update_person(person_id, name, age, zodiac, birth_planet, residence_planet):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Llh032002",
            database="MigrationDB"
        )
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE Person
            SET name=%s, age=%s, zodiac=%s, birth_planet=%s, residence_planet=%s
            WHERE id=%s
        """, (name, age, zodiac, birth_planet, residence_planet, person_id))

        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Person data updated successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")


# 删除数据的函数
def delete_person(person_id):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Llh032002",
            database="MigrationDB"
        )
        cursor = conn.cursor()

        cursor.execute("DELETE FROM Person WHERE id=%s", (person_id,))

        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Person data deleted successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")


# 插入星球数据的函数
def insert_planet(name):
    if not name:
        messagebox.showerror("Error", "名称不能为空!")
    if re.search(r'\d', name):
        messagebox.showerror("Error", "名称中不能有阿拉伯数字!")
        return
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Llh032002",
            database="MigrationDB"
        )
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO Planet (name)
            VALUES (%s)
        """, (name,))

        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Planet data inserted successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")


# 查询所有星球数据的函数
def view_all_planets():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Llh032002",
            database="MigrationDB"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Planet ORDER BY id ASC")
        records = cursor.fetchall()
        conn.close()
        return records
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
        return []


# 更新星球数据的函数
def update_planet(planet_id, name):
    if not name:
        messagebox.showerror("Error", "名称不能为空!")
    if re.search(r'\d', name):
        messagebox.showerror("Error", "名称中不能有阿拉伯数字!")
        return
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Llh032002",
            database="MigrationDB"
        )
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE Planet
            SET name=%s
            WHERE id=%s
        """, (name, planet_id))

        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Planet data updated successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")


# 删除星球数据的函数
def delete_planet(planet_id):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Llh032002",
            database="MigrationDB"
        )
        cursor = conn.cursor()

        cursor.execute("DELETE FROM Planet WHERE id=%s", (planet_id,))

        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Planet data deleted successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")


class MigrationManagementSystem(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Migration Management System")
        self.geometry("600x400")

        self.current_frame = None

        # 初始化界面
        self.show_main_menu()

    def show_main_menu(self):
        # 清空当前内容
        if self.current_frame:
            self.current_frame.destroy()

        # 创建主菜单框架
        self.current_frame = tk.Frame(self)
        self.current_frame.pack(expand=True, fill="both")

        # 创建按钮
        planet_button = tk.Button(self.current_frame, text="星球管理系统", command=self.show_planet_management)
        planet_button.pack(pady=50)

        person_button = tk.Button(self.current_frame, text="居民管理系统", command=self.show_person_management)
        person_button.pack(pady=30)

        exit_button = tk.Button(self.current_frame, text="退出", command=self.quit)
        exit_button.pack(pady=40)

    def show_planet_management(self):
        # 清空当前内容
        if self.current_frame:
            self.current_frame.destroy()

        # 创建星球管理框架
        self.current_frame = tk.Frame(self)
        self.current_frame.pack(expand=True, fill="both")

        # 创建回退按钮
        back_button = tk.Button(self.current_frame, text="Back", command=self.show_main_menu)
        back_button.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        # 添加星球管理内容
        insert_button = tk.Button(self.current_frame, text="插入", command=self.insert_planet)
        insert_button.grid(row=1, column=0, padx=150, pady=50)

        view_button = tk.Button(self.current_frame, text="查看", command=self.view_all_planets)
        view_button.grid(row=1, column=1, padx=20, pady=50)

        update_button = tk.Button(self.current_frame, text="更新", command=self.update_planet)
        update_button.grid(row=2, column=0, padx=150, pady=50)

        delete_button = tk.Button(self.current_frame, text="删除", command=self.delete_planet)
        delete_button.grid(row=2, column=1, padx=20, pady=50)

        # 更新窗口标题
        self.title("Migration Management System - Planet Management")

    def show_person_management(self):
        # 清空当前内容
        if self.current_frame:
            self.current_frame.destroy()

        # 创建人员管理框架
        self.current_frame = tk.Frame(self)
        self.current_frame.pack(expand=True, fill="both")

        # 创建回退按钮
        back_button = tk.Button(self.current_frame, text="Back", command=self.show_main_menu)
        back_button.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        # 添加人员管理内容
        insert_button = tk.Button(self.current_frame, text="添加居民", command=self.insert_person)
        insert_button.grid(row=1, column=0, padx=150, pady=50)

        view_button = tk.Button(self.current_frame, text="查看居民", command=self.view_all_persons)
        view_button.grid(row=1, column=1, padx=20, pady=50)

        update_button = tk.Button(self.current_frame, text="居民更新", command=self.update_person)
        update_button.grid(row=2, column=0, padx=150, pady=50)

        delete_button = tk.Button(self.current_frame, text="居民迁移", command=self.delete_person)
        delete_button.grid(row=2, column=1, padx=20, pady=50)

        # 更新窗口标题
        self.title("Migration Management System - Person Management")

    def insert_planet(self):
        # 清空当前内容
        if self.current_frame:
            self.current_frame.destroy()

        # 创建人员管理框架
        self.current_frame = tk.Frame(self)
        self.current_frame.pack(expand=True, fill="both")

        # 创建回退按钮
        back_button = tk.Button(self.current_frame, text="Back", command=self.show_planet_management)
        back_button.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        tk.Label(self.current_frame, text="名称:").grid(row=1, column=0, padx=40, pady=40)
        name_entry = tk.Entry(self.current_frame)
        name_entry.grid(row=1, column=1, padx=5, pady=10)

        def on_submit():
            name = name_entry.get()
            insert_planet(name)

        submit_button = tk.Button(self.current_frame, text="提交", command=on_submit)
        submit_button.grid(row=2, columnspan=2, pady=10)

    def view_all_planets(self):
        # 清空当前内容
        if self.current_frame:
            self.current_frame.destroy()

        # 创建星球管理框架
        self.current_frame = tk.Frame(self)
        self.current_frame.pack(expand=True, fill="both")

        # 创建回退按钮
        back_button = tk.Button(self.current_frame, text="Back", command=self.show_planet_management)
        back_button.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        # 查询所有星球数据
        records = view_all_planets()

        if records:
            for i, record in enumerate(records):
                tk.Label(self.current_frame, text=f"ID: {record[0]}, 名称: {record[1]}").grid(row=i + 1,
                                                                                              columnspan=2,
                                                                                              padx=40, pady=5)
        else:
            messagebox.showinfo("Info", "No planets found.")

    def update_planet(self):
        # 清空当前内容
        if self.current_frame:
            self.current_frame.destroy()

        # 创建星球管理框架
        self.current_frame = tk.Frame(self)
        self.current_frame.pack(expand=True, fill="both")

        # 创建回退按钮
        back_button = tk.Button(self.current_frame, text="Back", command=self.show_planet_management)
        back_button.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        tk.Label(self.current_frame, text="ID:").grid(row=1, column=0, padx=40, pady=5)
        planet_id_entry = tk.Entry(self.current_frame)
        planet_id_entry.grid(row=1, column=1, padx=40, pady=5)

        tk.Label(self.current_frame, text="新名称:").grid(row=2, column=0, padx=40, pady=5)
        new_planet_name_entry = tk.Entry(self.current_frame)
        new_planet_name_entry.grid(row=2, column=1, padx=40, pady=5)

        def on_update_planet():
            planet_id = planet_id_entry.get()
            name = new_planet_name_entry.get()
            update_planet(planet_id, name)

        update_button = tk.Button(self.current_frame, text="更新", command=on_update_planet)
        update_button.grid(row=3, columnspan=2, pady=10)

    def delete_planet(self):
        # 清空当前内容
        if self.current_frame:
            self.current_frame.destroy()

        # 创建星球管理框架
        self.current_frame = tk.Frame(self)
        self.current_frame.pack(expand=True, fill="both")

        # 创建回退按钮
        back_button = tk.Button(self.current_frame, text="Back", command=self.show_planet_management)
        back_button.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        tk.Label(self.current_frame, text="ID:").grid(row=1, column=0, padx=40, pady=5)
        planet_id_delete_entry = tk.Entry(self.current_frame)
        planet_id_delete_entry.grid(row=1, column=1, padx=40, pady=5)

        def on_delete_planet():
            planet_id = planet_id_delete_entry.get()
            delete_planet(planet_id)

        delete_button = tk.Button(self.current_frame, text="删除", command=on_delete_planet)
        delete_button.grid(row=2, columnspan=2, pady=10)

    def insert_person(self):
        # 清空当前内容
        if self.current_frame:
            self.current_frame.destroy()

        # 创建人员管理框架
        self.current_frame = tk.Frame(self)
        self.current_frame.pack(expand=True, fill="both")

        # 创建回退按钮
        back_button = tk.Button(self.current_frame, text="Back", command=self.show_person_management)
        back_button.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        tk.Label(self.current_frame, text="姓名:").grid(row=1, column=0, padx=10, pady=5)
        name_entry = tk.Entry(self.current_frame)
        name_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.current_frame, text="年龄:").grid(row=2, column=0, padx=10, pady=5)
        age_entry = tk.Entry(self.current_frame)
        age_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.current_frame, text="星座:").grid(row=3, column=0, padx=10, pady=5)
        zodiac_entry = tk.Entry(self.current_frame)
        zodiac_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(self.current_frame, text="出生星球:").grid(row=4, column=0, padx=10, pady=5)
        birth_planet_entry = tk.Entry(self.current_frame)
        birth_planet_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(self.current_frame, text="居住星球:").grid(row=5, column=0, padx=10, pady=5)
        residence_planet_entry = tk.Entry(self.current_frame)
        residence_planet_entry.grid(row=5, column=1, padx=10, pady=5)

        def on_submit():
            name = name_entry.get()
            age = int(age_entry.get())
            zodiac = zodiac_entry.get()
            birth_planet = birth_planet_entry.get()
            residence_planet = residence_planet_entry.get()
            insert_person(name, age, zodiac, birth_planet, residence_planet)

        submit_button = tk.Button(self.current_frame, text="提交", command=on_submit)
        submit_button.grid(row=6, columnspan=2, pady=10)

    def view_all_persons(self):
        # 清空当前内容
        if self.current_frame:
            self.current_frame.destroy()

        # 创建人员管理框架
        self.current_frame = tk.Frame(self)
        self.current_frame.pack(expand=True, fill="both")

        # 创建回退按钮
        back_button = tk.Button(self.current_frame, text="Back", command=self.show_person_management)
        back_button.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        # 查询所有人员数据
        records = view_all_persons()

        if records:
            for i, record in enumerate(records):
                tk.Label(self.current_frame,
                         text=f"ID: {record[0]}, 姓名: {record[1]}, 年龄: {record[2]}, 星座: {record[3]}, 出生星球: {record[4]}, 居住星球: {record[5]}").grid(
                    row=i + 1, columnspan=2, padx=10, pady=5)
        else:
            messagebox.showinfo("Info", "No persons found.")

    def update_person(self):
        # 清空当前内容
        if self.current_frame:
            self.current_frame.destroy()

        # 创建人员管理框架
        self.current_frame = tk.Frame(self)
        self.current_frame.pack(expand=True, fill="both")

        # 创建回退按钮
        back_button = tk.Button(self.current_frame, text="Back", command=self.show_person_management)
        back_button.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        tk.Label(self.current_frame, text="ID:").grid(row=1, column=0, padx=10, pady=5)
        person_id_entry = tk.Entry(self.current_frame)
        person_id_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.current_frame, text="新姓名:").grid(row=2, column=0, padx=10, pady=5)
        new_name_entry = tk.Entry(self.current_frame)
        new_name_entry.grid(row=2, column=1, padx=10, pady=5)

        def on_update_person():
            person_id = person_id_entry.get()
            name = new_name_entry.get()
            update_person(person_id, name)

        update_button = tk.Button(self.current_frame, text="更新", command=on_update_person)
        update_button.grid(row=3, columnspan=2, pady=10)

    def delete_person(self):
        # 清空当前内容
        if self.current_frame:
            self.current_frame.destroy()

        # 创建人员管理框架
        self.current_frame = tk.Frame(self)
        self.current_frame.pack(expand=True, fill="both")

        # 创建回退按钮
        back_button = tk.Button(self.current_frame, text="Back", command=self.show_person_management)
        back_button.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        tk.Label(self.current_frame, text="ID:").grid(row=1, column=0, padx=10, pady=5)
        person_id_delete_entry = tk.Entry(self.current_frame)
        person_id_delete_entry.grid(row=1, column=1, padx=10, pady=5)

        def on_delete_person():
            person_id = person_id_delete_entry.get()
            delete_person(person_id)

        delete_button = tk.Button(self.current_frame, text="删除", command=on_delete_person)
        delete_button.grid(row=2, columnspan=2, pady=10)


if __name__ == '__main__':
    app = MigrationManagementSystem()
    app.mainloop()
