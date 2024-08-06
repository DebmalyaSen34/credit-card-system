import mysql.connector
import pandas as pd
from mysql.connector import Error

db_config = {
    'user': 'root',
    'password': 'Batman@2003',
    'host': 'localhost',
    'database': 'creadit_card_management_system'
}

def create_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        
        if(conn.is_connected()):
            print("Successfully connected to the database!")
            return conn
    except Error as e:
        print(f'Error: {e}')
        return None
    
def create_user(user_id, user_name, user_mob, user_mail, user_address, user_branch_id):
    
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        sql = """INSERT INTO USER1 (user_id, user_name, user_mob, user_mail, user_address, user_branch_id)
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        data = (user_id, user_name, user_mob, user_mail, user_address, user_branch_id)
        try:
            cursor.execute(sql, data)
            conn.commit()
            print(f"User {user_id} created successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()
            
def find_user(search_criteria):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        # Construct SQL query based on the search criteria
        sql = "SELECT * FROM USER1 WHERE"
        conditions = []
        params = []
        
        if 'user_id' in search_criteria:
            conditions.append("user_id = %s")
            params.append(search_criteria['user_id'])
        if 'user_name' in search_criteria:
            conditions.append("user_name LIKE %s")
            params.append(f"%{search_criteria['user_name']}%")
        if 'user_mail' in search_criteria:
            conditions.append("user_mail LIKE %s")
            params.append(f"%{search_criteria['user_mail']}%")
        
        if conditions:
            sql += " AND ".join(conditions)
        
        try:
            cursor.execute(sql, params)
            result = cursor.fetchall()
            if result:
                for row in result:
                    print(row)
            else:
                print("No users found matching the criteria.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()
            
            
def read_users():
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        sql = "SELECT * FROM USER1"
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                print(row)
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()
            
def update_user(user_id, new_email):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        sql = "UPDATE USER1 SET user_mail = %s WHERE user_id = %s"
        data = (new_email, user_id)
        try:
            cursor.execute(sql, data)
            conn.commit()
            print(f"User {user_id} updated successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()
            
def delete_user(user_id):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        sql = "DELETE FROM USER1 WHERE user_id = %s"
        try:
            cursor.execute(sql, (user_id,))
            conn.commit()
            print(f"User {user_id} deleted successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()
            
def load_and_insert(csv_file, table_name):
    
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    df = pd.read_csv(csv_file)
    
    columns = ', '.join(df.columns)
    placeholders = ', '.join(['%s'] * len(df.columns))
    sql = f'INSERT INTO {table_name} ({columns}) VALUES ({placeholders})'
    
    for row in df.itertuples(index=False, name=None):
        cursor.execute(sql, tuple(row))
        
    conn.commit()
    
create_connection()

load_and_insert('data/branch_dummy_data.csv', 'branch')
load_and_insert('data/user_dummy_data.csv', 'user1')
load_and_insert('data/credit_card_dummy_data.csv', 'credit_card')
load_and_insert('data/limits_dummy_data.csv', 'limits')
load_and_insert('data/application_dummy_data.csv', 'applications')

create_user(12, 'Vamsi Krishna', 5557890125, 'cjvamsikrishna@gmail.com', 'Vijaywada', 5)

delete_user(5)

update_user(6, 'debmalyasen005@gmail.com')

read_users()