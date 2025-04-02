import csv
from data_access.models import Subscriber, TariffPlan, Order, Payment
from utils.di_container import container


subscriber_repo = container.subscriber_repo
tariff_repo = container.tariff_repo
order_repo = container.order_repo
payment_repo = container.payment_repo


def load_data_from_csv():
    with open("data.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:

            tariff_plan = tariff_repo.get_by_id(int(row["tariff_plan_id"]))
            if not tariff_plan:
                tariff_plan = TariffPlan(
                    name=row["tariff_plan_name"], price=row["tariff_plan_price"]
                )
                tariff_plan = tariff_repo.add(tariff_plan)
            
            subscriber = subscriber_repo.get_all(phone_number=row["subscriber_phone_number"])
            if not subscriber:
                subscriber = Subscriber(
                    name=row["subscriber_name"],
                    balance=row["subscriber_balance"],
                    phone_number=row["subscriber_phone_number"],
                    tariff_plan_id=tariff_plan.id,
                )
                subscriber_repo.add(subscriber)
            else:
                subscriber = subscriber[0]

            order = Order(
                subscriber_id=subscriber.id,
                amount=row["order_amount"],
                tariff_plan_id=row["tariff_plan_id"],
            )
            order_repo.add(order)

            payment = Payment(
                order_id=order.id,
                amount=row["payment_amount"],
                status=row["payment_status"],
            )
            payment_repo.add(payment)


load_data_from_csv()
