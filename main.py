from utils.di_container import container

def main():
    subscriber_service = container.subscriber_service
    tariff_service = container.tariff_service
    order_service = container.order_service
    payment_service = container.payment_service

    print(subscriber_service.get_subscriber(1))
    print(subscriber_service.update_balance(1, 100.0))
    print(order_service.get_subscriber_orders(1))

    _, payment = subscriber_service.change_tariff(1, 2)
    print(payment)
    print(payment_service.pay(payment.id))
    print(subscriber_service.get_subscriber(1))

    # subscriber_service.create_subscriber("John Doe", 1)

    # print(tariff_service.create_tariff("Basic", 10.0))

    # print(order_service.create_order(1, "order_type", 100.0))

    # Приклад створення абонента
    # new_subscriber = subscriber_service.get_subscriber(1)
    # print(f"Створено абонента: {new_subscriber}")

    # Отримання списку тарифів
    tariffs = tariff_service.get_all_tariffs()
    print(f"Доступні тарифи: {str(tariffs)}")

if __name__ == "__main__":
    main()
