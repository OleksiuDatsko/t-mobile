import csv
from faker import Faker
import random

fake = Faker()

def generate_csv():
    with open("data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                "subscriber_name",
                "subscriber_balance",
                "subscriber_phone_number",
                "tariff_plan_id",
                "tariff_plan_name",
                "tariff_plan_price",
                "order_amount",
                "payment_amount",
                "payment_status",
            ]
        )

        tariff_plans = [
            {"id": 1, "name": "Basic Plan", "price": 10.0},
            {"id": 2, "name": "Premium Plan", "price": 20.0},
            {"id": 3, "name": "Family Plan", "price": 15.0},
        ]

        for _ in range(500):
            subscriber_name = fake.name()
            subscriber_balance = round(random.uniform(0, 1000), 2)
            subscriber_phone_number = fake.phone_number()
            tariff_plan = random.choice(tariff_plans)

            order_amount1 = round(random.uniform(5, 100), 2)
            payment_status1 = "completed"
            payment_amount1 = order_amount1

            writer.writerow(
                [
                    subscriber_name,
                    subscriber_balance,
                    subscriber_phone_number,
                    tariff_plan["id"],
                    tariff_plan["name"],
                    tariff_plan["price"],
                    order_amount1,
                    payment_amount1,
                    payment_status1,
                ]
            )

            order_amount2 = round(random.uniform(5, 100), 2)
            payment_status2 = random.choice(["pending", "completed"])
            payment_amount2 = order_amount2

            writer.writerow(
                [
                    subscriber_name,
                    subscriber_balance,
                    subscriber_phone_number,
                    tariff_plan["id"],
                    tariff_plan["name"],
                    tariff_plan["price"],
                    order_amount2,
                    payment_amount2,
                    payment_status2,
                ]
            )

generate_csv()
