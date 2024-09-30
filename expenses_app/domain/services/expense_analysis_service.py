from ..domain_imports import (
    Expense,
    Repository,
    UserAvrSocial,
    UserAvrExpenseFeel,
    UserAvrExpenseType,
    UserAvrEmotional,
    UserAvrTimePeriod,
    UserRelationSocialPeriod,
    UserRelationEmotionalPeriod,
    UserRelationEmotionalSocial
)
from collections import defaultdict
from datetime import datetime, timezone
from itertools import groupby
from operator import attrgetter

class ExpenseAnalysisService:
    def __init__(self, repository: Repository):
        self.repository = repository

    def process_expense(self, expense: Expense) -> Expense:
        saved_expense = self.save_expense(expense)

        user_id = expense.user_id  
        user_expenses = self.repository.get_expense_by_user_id(expense, user_id)

        self.calc_average_per_category(user_expenses, user_id)
        #self.calc_relations_per_category(user_expenses, user_id)
        return saved_expense

    def save_expense(self, expense: Expense):
        expense.date = datetime.now(timezone.utc)
        expense.day_of_week = expense.date.weekday()
        expense.month_week = self.get_month_week(expense.date)

        return self.repository.save_entity(expense)

    def calc_average_per_category(self, user_expenses: list[Expense], user_id: int):               
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
                value = avr['value']
            )

            self.repository.save_entity(new_avr)       

    def calc_average_expense_type(self, user_expenses: list[Expense], user_id: int):
        new_avrs: dict = self.calc_averages(user_expenses, 'cat_expense')

        for cat, avr in new_avrs.items():
            new_avr = UserAvrExpenseType(
                expense_type = cat,
                user_id = user_id,
                value = avr['value']
            )

            self.repository.save_entity(new_avr)  

    def calc_average_emotional(self, user_expenses: list[Expense], user_id: int):
        new_avrs: dict = self.calc_averages(user_expenses, 'cat_emotional')

        for cat, avr in new_avrs.items():
            new_avr = UserAvrEmotional(
                emotion_type = cat,
                user_id = user_id,
                value = avr['value']
            )

            self.repository.save_entity(new_avr)   

    def calc_average_social(self, user_expenses: list[Expense], user_id: int):
        new_avrs: dict = self.calc_averages(user_expenses, 'cat_social')
        
        for cat, avr in new_avrs.items():
            new_avr = UserAvrSocial(
                social_type = cat,
                user_id = user_id,
                value = avr['value']
            )

            self.repository.save_entity(new_avr)  

    def calc_averages(self, user_expenses: list[Expense], category: str) -> dict:
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

    def calc_relations(self, user_expenses: list[Expense], main_cat: str, related_cat: str) -> dict:
        result = {}
        
        if not user_expenses:
            return result
        
        relations = defaultdict(lambda: {'main_cat': 0, 'relate_to': 0})
        sorted_list = sorted(user_expenses, key=attrgetter(main_cat))

        for main_cat_value, cat_group in groupby(sorted_list, key=attrgetter(main_cat)):
            for expense in cat_group:
                related_cat_value = getattr(expense, related_cat)
                amount = expense.value
                
                relations[main_cat_value][related_cat_value]['total'] += amount
                relations[main_cat_value][related_cat_value]['count'] += 1
        
        for main_cat_value, related_cat_value in relations.items():
            result[main_cat_value] = {}
            for related_cat, relation_value in related_cat_value.items():
                if relation_value['count'] > 0:
                    result[main_cat_value][related_cat] = relation_value['total'] / relation_value['count']
        
        return result
    
    def calc_relations_per_category(self, user_expenses: list[Expense], user_id: int):
        self.calc_relation_emotional_period(user_expenses, user_id)
        self.calc_relation_emotional_social(user_expenses, user_id)
        self.calc_relation_social_period(user_expenses, user_id)

    def calc_relation_emotional_social(self, user_expenses: list[Expense], user_id: int):
        new_avrs: dict = self.calc_relations(user_expenses, 'cat_social', 'cat_emotional')
        
        for main_cat_value, related_cats in new_avrs.items():
            for related_cat, avr in related_cats.items():
                new_avr = UserRelationEmotionalSocial(
                    social_type=main_cat_value,
                    emotional_type=related_cat,
                    user_id=user_id,
                    value=avr
                )

            self.repository.save_entity(new_avr) 

    def calc_relation_emotional_period(self, user_expenses: list[Expense], user_id: int):
        new_avrs: dict = self.calc_relations(user_expenses, 'cat_emotional', 'month_week')
        
        for main_cat_value, related_cats in new_avrs.items():
            for related_cat, avr in related_cats.items():
                new_avr = UserRelationEmotionalPeriod(
                    emotional_type=main_cat_value,
                    month_week=related_cat,
                    user_id=user_id,
                    value=avr
                )

            self.repository.save_entity(new_avr) 

    def calc_relation_social_period(self, user_expenses: list[Expense], user_id: int):
        new_avrs: dict = self.calc_relations(user_expenses, 'cat_social', 'month_week')
        
        for main_cat_value, related_cats in new_avrs.items():
            for related_cat, avr in related_cats.items():
                new_avr = UserRelationSocialPeriod(
                    event_type=main_cat_value,
                    month_week=related_cat,
                    user_id=user_id,
                    value=avr
                )

            self.repository.save_entity(new_avr) 

    def get_month_week(self, date: datetime) -> int:
        first_day_of_month = date.replace(day=1)
        day_of_month = date.day
        adjusted_day_of_month = day_of_month + first_day_of_month.day
        week_of_month = (adjusted_day_of_month - 1) // 7 + 1

        return week_of_month