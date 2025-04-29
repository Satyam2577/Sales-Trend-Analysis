import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

# Connect to SQLite (file-based)
conn = sqlite3.connect('employee_sales.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    order_date TEXT NOT NULL,
    amount REAL NOT NULL
)
''')
conn.commit()

# Add employee data
def add_employee():
    name = name_entry.get().strip()
    date = date_entry.get().strip()
    amount = amount_entry.get().strip()

    if not name or not date or not amount:
        messagebox.showerror("Error", "Please fill all fields.")
        return

    try:
        datetime.strptime(date, '%Y-%m-%d')  # validate date format
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Error", "Enter a valid date (YYYY-MM-DD) and amount.")
        return

    cursor.execute('INSERT INTO sales (name, order_date, amount) VALUES (?, ?, ?)', (name, date, amount))
    conn.commit()
    messagebox.showinfo("Success", f"Record added for {name}")
    name_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

# Show top 5 employees by annual revenue
def show_top_5():
    query = '''
    SELECT 
        name,
        SUM(amount) AS annual_revenue
    FROM 
        sales
    GROUP BY 
        name
    ORDER BY 
        annual_revenue DESC
    LIMIT 5
    '''
    df = pd.read_sql_query(query, conn)
    
    if df.empty:
        messagebox.showinfo("No Data", "No sales data available.")
        return
    
    # Plotting
    plt.figure(figsize=(8, 6))
    plt.bar(df['name'], df['annual_revenue'], color='orange')
    plt.title('Top 5 Employees by Annual Sales')
    plt.xlabel('Employee Name')
    plt.ylabel('Per Annum Amount (₹)')
    plt.tight_layout()
    plt.show()

# GUI setup
root = tk.Tk()
root.title("Employee Sales Entry")

tk.Label(root, text="Employee Name").grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Order Date (YYYY-MM-DD)").grid(row=1, column=0, padx=10, pady=5)
tk.Label(root, text="Amount (₹)").grid(row=2, column=0, padx=10, pady=5)

name_entry = tk.Entry(root)
date_entry = tk.Entry(root)
amount_entry = tk.Entry(root)

name_entry.grid(row=0, column=1, padx=10, pady=5)
date_entry.grid(row=1, column=1, padx=10, pady=5)
amount_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Button(root, text="Add Entry", command=add_employee).grid(row=3, column=0, columnspan=2, pady=10)
tk.Button(root, text="Show Top 5 Employees", command=show_top_5).grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
