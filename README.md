📊 Employee Sales Entry & Analysis GUI


This project is a simple Python GUI application built using Tkinter, SQLite, and Matplotlib. It allows users to:
  Add employee sales records (name, order date, amount).
  Store the data persistently using an SQLite database.
  View a bar chart of the top 5 employees by annual sales (₹).

🛠 Technologies Used

Python 3
Tkinter (for GUI)
SQLite (for data storage)
Pandas (for data handling)
Matplotlib (for visualization)

📁 Features


Input form to add new employee sales data.
Validates date format (YYYY-MM-DD) and amount.
Stores data in employee_sales.db (SQLite file).
Visualizes top 5 employees by total yearly sales.

🚀 How to Run


Clone this repository or download the .py file.

Make sure you have the required libraries:

  pip install pandas matplotlib


Run the script:

  python employee_sales_gui.py


🧾 Sample Usage


  Input:
  
    Name: Satyam
    Date: 2023-01-15
    Amount: 1000

Output:
Adds record to DB
Click "Show Top 5 Employees" to see graph


📸 Screenshots


![Screenshot 2025-04-29 203457](https://github.com/user-attachments/assets/051f1f96-f65d-4405-aff4-5305a3cfff50)
![Screenshot 2025-04-29 203511](https://github.com/user-attachments/assets/7ab36585-453e-44bd-a86b-d37b6e80be0e)



📌 Notes


All data is saved to employee_sales.db in the project directory.
Ensure proper date formatting when entering order dates.
