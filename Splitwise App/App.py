import tkinter as tk
from tkinter import messagebox
from typing import List, Dict
from Splitwise import Splitwise


# GUI code
class SplitwiseUI:
    def __init__(self, root):
        self.splitwise = Splitwise()

        self.root = root
        self.root.title("Splitwise")

        # User Frame
        self.user_frame = tk.Frame(root)
        self.user_frame.pack(pady=10)
        
        self.user_label = tk.Label(self.user_frame, text="Add User")
        self.user_label.pack()

        self.user_name_label = tk.Label(self.user_frame, text="Name:")
        self.user_name_label.pack(side=tk.LEFT)
        self.user_name_entry = tk.Entry(self.user_frame)
        self.user_name_entry.pack(side=tk.LEFT)

        self.add_user_button = tk.Button(self.user_frame, text="Add User", command=self.add_user)
        self.add_user_button.pack(side=tk.LEFT)

        # Group Frame
        self.group_frame = tk.Frame(root)
        self.group_frame.pack(pady=10)

        self.group_label = tk.Label(self.group_frame, text="Add Group")
        self.group_label.pack()

        self.group_name_label = tk.Label(self.group_frame, text="Name:")
        self.group_name_label.pack(side=tk.LEFT)
        self.group_name_entry = tk.Entry(self.group_frame)
        self.group_name_entry.pack(side=tk.LEFT)

        self.add_group_button = tk.Button(self.group_frame, text="Add Group", command=self.add_group)
        self.add_group_button.pack(side=tk.LEFT)

        # Add User to Group Frame
        self.add_user_to_group_frame = tk.Frame(root)
        self.add_user_to_group_frame.pack(pady=10)

        self.add_user_to_group_label = tk.Label(self.add_user_to_group_frame, text="Add User to Group")
        self.add_user_to_group_label.pack()

        self.user_id_label = tk.Label(self.add_user_to_group_frame, text="User ID:")
        self.user_id_label.pack(side=tk.LEFT)
        self.user_id_entry = tk.Entry(self.add_user_to_group_frame)
        self.user_id_entry.pack(side=tk.LEFT)

        self.group_id_label = tk.Label(self.add_user_to_group_frame, text="Group ID:")
        self.group_id_label.pack(side=tk.LEFT)
        self.group_id_entry = tk.Entry(self.add_user_to_group_frame)
        self.group_id_entry.pack(side=tk.LEFT)

        self.add_user_to_group_button = tk.Button(self.add_user_to_group_frame, text="Add User to Group", command=self.add_user_to_group)
        self.add_user_to_group_button.pack(side=tk.LEFT)

        # Expense Frame
        self.expense_frame = tk.Frame(root)
        self.expense_frame.pack(pady=10)

        self.expense_label = tk.Label(self.expense_frame, text="Add Expense")
        self.expense_label.pack()

        self.expense_amount_label = tk.Label(self.expense_frame, text="Amount:")
        self.expense_amount_label.pack(side=tk.LEFT)
        self.expense_amount_entry = tk.Entry(self.expense_frame)
        self.expense_amount_entry.pack(side=tk.LEFT)

        self.paid_by_label = tk.Label(self.expense_frame, text="Paid By User ID:")
        self.paid_by_label.pack(side=tk.LEFT)
        self.paid_by_entry = tk.Entry(self.expense_frame)
        self.paid_by_entry.pack(side=tk.LEFT)

        self.split_between_label = tk.Label(self.expense_frame, text="Split Between User IDs (comma-separated):")
        self.split_between_label.pack(side=tk.LEFT)
        self.split_between_entry = tk.Entry(self.expense_frame)
        self.split_between_entry.pack(side=tk.LEFT)

        self.group_id_expense_label = tk.Label(self.expense_frame, text="Group ID:")
        self.group_id_expense_label.pack(side=tk.LEFT)
        self.group_id_expense_entry = tk.Entry(self.expense_frame)
        self.group_id_expense_entry.pack(side=tk.LEFT)

        self.add_expense_button = tk.Button(self.expense_frame, text="Add Expense", command=self.add_expense)
        self.add_expense_button.pack(side=tk.LEFT)

        # Balance Frame
        self.balance_frame = tk.Frame(root)
        self.balance_frame.pack(pady=10)

        self.balance_label = tk.Label(self.balance_frame, text="Get Balances for Group")
        self.balance_label.pack()

        self.group_id_balance_label = tk.Label(self.balance_frame, text="Group ID:")
        self.group_id_balance_label.pack(side=tk.LEFT)
        self.group_id_balance_entry = tk.Entry(self.balance_frame)
        self.group_id_balance_entry.pack(side=tk.LEFT)

        self.get_balance_button = tk.Button(self.balance_frame, text="Get Balances", command=self.get_balances)
        self.get_balance_button.pack(side=tk.LEFT)

        self.balance_output_label = tk.Label(self.balance_frame, text="")
        self.balance_output_label.pack()

    def add_user(self):
        name = self.user_name_entry.get()
        user_id = len(self.splitwise.users) + 1
        self.splitwise.add_user(user_id, name)
        messagebox.showinfo("Success", f"User {name} added with ID {user_id}")

    def add_group(self):
        name = self.group_name_entry.get()
        group_id = len(self.splitwise.groups) + 1
        self.splitwise.add_group(group_id, name)
        messagebox.showinfo("Success", f"Group {name} added with ID {group_id}")

    def add_user_to_group(self):
        user_id = int(self.user_id_entry.get())
        group_id = int(self.group_id_entry.get())
        self.splitwise.add_user_to_group(user_id, group_id)
        messagebox.showinfo("Success", f"User ID {user_id} added to Group ID {group_id}")

    def add_expense(self):
        amount = float(self.expense_amount_entry.get())
        paid_by_id = int(self.paid_by_entry.get())
        split_between_ids = list(map(int, self.split_between_entry.get().split(',')))
        group_id = int(self.group_id_expense_entry.get())
        expense_id = len(self.splitwise.groups[group_id].expenses) + 1 if group_id in self.splitwise.groups else 1
        self.splitwise.add_expense(expense_id, amount, paid_by_id, split_between_ids, group_id)
        messagebox.showinfo("Success", f"Expense of {amount} added")

    def get_balances(self):
        group_id = int(self.group_id_balance_entry.get())
        balances = self.splitwise.get_balances(group_id)
        balance_text = "\n".join([f"User ID {user_id}: {balance:.2f}" for user_id, balance in balances.items()])
        self.balance_output_label.config(text=balance_text)
