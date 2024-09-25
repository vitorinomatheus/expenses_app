from ..domain_imports import Expense, Repository, UserAvrSocial, UserAvrExpenseFeel, UserAvrExpenseType, UserAvrExpenseEmotional, UserAvrTimePeriod
from collections import defaultdict
import calendar
from datetime import datetime

class ExpenseAnalysisService:
    def __init__(self, repository: Repository):
        self.repository = repository

    def process_expense(self, expense: Expense):
        self.save_expense(expense)
        self.calc_average_per_category(expense)
        self.calc_relations(expense)

    def save_expense(self, expense: Expense):
        expense.day_of_week = expense.date.weekday()
        expense.month_week = self.get_month_week(expense.date)

        return self.repository.save_entity(expense)

    def calc_average_per_category(self, expense: Expense):
        user_id = expense.user_id
        user_expenses = self.repository.get_filtered_list(expense, 'user_id', user_id)         

        self.calc_average_emotional(user_expenses, user_id)
        self.calc_average_expense_feel(user_expenses, user_id)
        self.calc_average_expense_type(user_expenses, user_id)
        self.calc_average_social(user_expenses, user_id)
        self.calc_average_time_period(user_expenses, user_id)

    def calc_average_expense_feel(self, user_expenses: list[Expense], user_id: int):
        new_avrs: dict = self.calc_averages(user_expenses, 'cat_expense_feel')

        for cat, avr in new_avrs.items():
            new_avr = UserAvrExpenseFeel(
                expense_feel = cat,
                user_id = user_id,
                value = avr
            )

            self.repository.save_entity(new_avr)       

    def calc_average_expense_type(self, user_expenses: list[Expense], user_id: int):
        new_avrs: dict = self.calc_averages(user_expenses, 'cat_expense')

        for cat, avr in new_avrs.items():
            new_avr = UserAvrExpenseType(
                expense_feel = cat,
                user_id = user_id,
                value = avr
            )

            self.repository.save_entity(new_avr)  

    def calc_average_emotional(self, user_expenses: list[Expense], user_id: int):
        new_avrs: dict = self.calc_averages(user_expenses, 'cat_emotional')

        for cat, avr in new_avrs.items():
            new_avr = UserAvrExpenseEmotional(
                expense_feel = cat,
                user_id = user_id,
                value = avr
            )

            self.repository.save_entity(new_avr)   

    def calc_average_social(self, user_expenses: list[Expense], user_id: int):
        new_avrs: dict = self.calc_averages(user_expenses, 'cat_social')
        
        for cat, avr in new_avrs.items():
            new_avr = UserAvrSocial(
                expense_feel = cat,
                user_id = user_id,
                value = avr
            )

            self.repository.save_entity(new_avr)  

    def calc_averages(user_expenses: list[Expense], category: str) -> dict:
        if not user_expenses:
            return {}
        
        expenses_sums = defaultdict(lambda: {'sum': 0, 'count': 0})
        expenses_avrs = {}

        for expense in user_expenses:
            cat_value = getattr(expense, category)
            expenses_sums[cat_value]['sum'] += expense.value
            expenses_sums[cat_value]['count'] += 1

        for cat, data in expenses_sums.items():
            if data['count'] > 0:
                avr = data['sum'] / data['count']
                expenses_avrs[cat] = {'value': avr}

        return expenses_avrs

    def calc_average_time_period(self, user_expenses: list[Expense], user_id: int):
        if not user_expenses:
            return

        sums_by_week_day = defaultdict(lambda: {'sum': 0, 'count': 0})
        sums_by_month_week = defaultdict(lambda: {'sum': 0, 'count': 0})

        for expense in user_expenses:
            day_of_week_value = getattr(expense, 'day_of_week')
            week_month_value = getattr(expense, 'month_week')

            sums_by_week_day[day_of_week_value]['sum'] += expense.value
            sums_by_week_day[day_of_week_value]['count'] += 1

            sums_by_month_week[week_month_value]['sum'] += expense.value
            sums_by_month_week[week_month_value]['count'] += 1

        for cat, data in sums_by_week_day.items():
            if data['count'] > 0:
                avr = data['sum'] / data['count']
                time_avr = UserAvrTimePeriod (
                    user_id = user_id,
                    week_day = cat,
                    value = avr
                )

                self.repository.save_entity(time_avr)

        for cat, data in sums_by_month_week.items():
            if data['count'] > 0:
                avr = data['sum'] / data['count']
                time_avr = UserAvrTimePeriod (
                    user_id = user_id,
                    month_week = cat,
                    value = avr
                )

                self.repository.save_entity(time_avr)

        


    def calc_relations(self, expense: Expense):
        pass

    def calc_relation_emotional_social():
        pass

    def calc_relation_emotional_period():
        pass

    def calc_relation_social_period():
        pass

    def get_month_week(date: datetime) -> int:
        first_day_of_month = date.replace(day=1)
        day_of_month = date.day
        adjusted_day_of_month = day_of_month + first_day_of_month
        week_of_month = (adjusted_day_of_month - 1) // 7 + 1

        return week_of_month