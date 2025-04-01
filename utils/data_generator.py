import csv
from faker import Faker
import random


fake = Faker()


def generate_csv():
    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            'subscriber_name', 'subscriber_balance', 'tariff_plan_id',
            'tariff_plan_name', 'tariff_plan_price', 
            'order_type', 'order_amount',
            'payment_amount', 'payment_status'
        ])

        
        tariff_plans = [
            {'id': 1, 'name': 'Basic Plan', 'price': 10.0},
            {'id': 2, 'name': 'Premium Plan', 'price': 20.0},
            {'id': 3, 'name': 'Family Plan', 'price': 15.0},
        ]

        
        for _ in range(1000):
            subscriber_name = fake.name()
            subscriber_balance = round(random.uniform(0, 1000), 2)
            tariff_plan = random.choice(tariff_plans)
            order_type = random.choice(['change_tariff', 'top_up'])
            order_amount = round(random.uniform(5, 100), 2)
            payment_status = random.choice(['pending', 'completed'])
            payment_amount = round(random.uniform(5, 100), 2)

            
            writer.writerow([
                subscriber_name, subscriber_balance,
                tariff_plan['id'], tariff_plan['name'], tariff_plan['price'],
                order_type, order_amount,
                payment_amount, payment_status
            ])


generate_csv()
