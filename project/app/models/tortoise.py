from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class User(models.Model):
    username = fields.CharField(max_length=255, unique=True)
    password = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255, unique=True)
    full_name = fields.CharField(max_length=255, null=True)
    disabled = fields.BooleanField(default=False)


class Budget(models.Model):
    month = fields.IntField(required=True)
    year = fields.IntField(required=True)
    amount = fields.DecimalField(max_digits=9, decimal_places=2)
    user_id = fields.BigIntField(required=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.month}-{self.year} - {self.amount} - {self.user_id}"


BudgetSchema = pydantic_model_creator(Budget)
UserSchema = pydantic_model_creator(User)
