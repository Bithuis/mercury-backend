from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Budget(models.Model):
    month = fields.IntField(required=True)
    year = fields.IntField(required=True)
    amount = fields.DecimalField(max_digits=9, decimal_places=2)
    user_id = fields.BigIntField(required=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.month}-{self.year} - {self.amount} - {self.user_id}"


BudgetSchema = pydantic_model_creator(Budget)
