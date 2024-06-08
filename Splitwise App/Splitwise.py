from typing import List, Dict
import pandas as pd

class User:
    def __init__(self, user_id: int, name: str):
        self.user_id = user_id
        self.name = name

class Expense:
    def __init__(self, expense_id: int, amount: float, paid_by: User, split_between: List[User]):
        self.expense_id = expense_id
        self.amount = amount
        self.paid_by = paid_by
        self.split_between = split_between
        self.splits = self.calculate_splits()

    def calculate_splits(self):
        split_amount = self.amount / len(self.split_between)
        splits = {}
        for user in self.split_between:
            splits[user.user_id] = split_amount
        return splits

class Group:
    def __init__(self, group_id: int, name: str):
        self.group_id = group_id
        self.name = name
        self.users = []
        self.expenses = []

    def add_user(self, user: User):
        self.users.append(user)

    def add_expense(self, expense: Expense):
        self.expenses.append(expense)

    def calculate_balances(self):
        balances = {user.user_id: 0 for user in self.users}
        for expense in self.expenses:
            for user_id, amount in expense.splits.items():
                if user_id != expense.paid_by.user_id:
                    balances[user_id] -= amount
                    balances[expense.paid_by.user_id] += amount
        return balances

class Splitwise:
    def __init__(self):
        self.users = {}
        self.groups = {}

    def add_user(self, user_id: int, name: str):
        user = User(user_id, name)
        self.users[user_id] = user
        return user

    def add_group(self, group_id: int, name: str):
        group = Group(group_id, name)
        self.groups[group_id] = group
        return group

    def add_user_to_group(self, user_id: int, group_id: int):
        user = self.users.get(user_id)
        group = self.groups.get(group_id)
        if user and group:
            group.add_user(user)

    def add_expense(self, expense_id: int, amount: float, paid_by_id: int, split_between_ids: List[int], group_id: int):
        paid_by = self.users.get(paid_by_id)
        split_between = [self.users[user_id] for user_id in split_between_ids]
        expense = Expense(expense_id, amount, paid_by, split_between)
        group = self.groups.get(group_id)
        if group:
            group.add_expense(expense)

    def get_balances(self, group_id: int):
        group = self.groups.get(group_id)
        if group:
            return group.calculate_balances()