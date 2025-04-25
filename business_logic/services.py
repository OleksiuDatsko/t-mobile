from business_logic.interfaces import (
    IOrderService,
    IPaymentService,
    ISubscriberService,
    ITariffService,
)
from data_access.interfaces import (
    ISubscriberRepository,
    ITariffRepository,
    IOrderRepository,
    IPaymentRepository,
)
from data_access.models import Subscriber, TariffPlan, Order, Payment


class SubscriberService(ISubscriberService):
    def __init__(
        self,
        subscriber_repo: ISubscriberRepository,
        order_repo: IOrderRepository,
        payment_repo: IPaymentRepository,
        tariff_repo: ITariffRepository,
    ):
        self.subscriber_repo = subscriber_repo
        self.order_repo = order_repo
        self.payment_repo = payment_repo
        self.tariff_repo = tariff_repo
        
    def get_all_subscribers(self) -> list[Subscriber]:
        return self.subscriber_repo.get_all()

    def get_subscriber(self, subscriber_id: int) -> Subscriber | None:
        return self.subscriber_repo.get_by_id(subscriber_id)

    def create_subscriber(self, name: str, tariff_plan_id: int, phone_number: str) -> Subscriber:
        new_subscriber = Subscriber(name=name, tariff_plan_id=tariff_plan_id, phone_number=phone_number)
        return self.subscriber_repo.add(new_subscriber)

    def update_balance(self, subscriber_id: int, amount: float) -> Subscriber:
        subscriber = self.subscriber_repo.get_by_id(subscriber_id)
        if not subscriber:
            raise ValueError("Subscriber not found")

        subscriber.balance += amount
        self.subscriber_repo.update(subscriber)
        return subscriber

    def change_tariff(self, subscriber_id: int, new_tariff_plan_id: int) -> tuple[Order, Payment]:
        subscriber = self.subscriber_repo.get_by_id(subscriber_id)
        if not subscriber:
            raise ValueError("Subscriber not found")

        new_tariff_plan = self.tariff_repo.get_by_id(new_tariff_plan_id)
        if not new_tariff_plan:
            raise ValueError("New tariff plan not found")

        if new_tariff_plan_id == subscriber.tariff_plan_id:
            raise ValueError("The subscriber is already on this tariff plan")

        order = Order(
            subscriber_id=subscriber_id,
            amount=new_tariff_plan.price,
            tariff_plan_id=new_tariff_plan_id,
        )
        self.order_repo.add(order)

        payment = Payment(order_id=order.id, amount=order.amount, status="pending")
        self.payment_repo.add(payment)
        return order, payment


class TariffService(ITariffService):
    def __init__(self, tariff_repo: ITariffRepository):
        self.tariff_repo = tariff_repo

    def get_tariff(self, tariff_id: int) -> TariffPlan | None:
        return self.tariff_repo.get_by_id(tariff_id)

    def get_all_tariffs(self) -> list[TariffPlan]:
        return self.tariff_repo.get_all()

    def create_tariff(self, name: str, price: float) -> TariffPlan:
        new_tariff = TariffPlan(name=name, price=price)
        return self.tariff_repo.add(new_tariff)

    def update_tariff(
        self, tariff_id: int, name: str | None = None, price: float | None = None
    ):
        tariff = self.tariff_repo.get_by_id(tariff_id)
        if not tariff:
            raise ValueError("Tariff plan not found")

        if name:
            tariff.name = name
        if price:
            tariff.price = price

        return self.tariff_repo.update(tariff)

    def delete_tariff(self, tariff_id: int) -> bool:
        return self.tariff_repo.delete(tariff_id)


class OrderService(IOrderService):
    def __init__(
        self,
        order_repo: IOrderRepository,
        payment_repo: IPaymentRepository,
        subscriber_repo: ISubscriberRepository,
    ):
        self.order_repo = order_repo
        self.payment_repo = payment_repo
        self.subscriber_repo = subscriber_repo

    def get_subscriber_orders(self, subscriber_id: int) -> list[Order]:
        return self.order_repo.get_all(subscriber_id=subscriber_id)


class PaymentService(IPaymentService):
    def __init__(
        self,
        payment_repo: IPaymentRepository,
        subscriber_repo: ISubscriberRepository,
        order_repo: IOrderRepository,
        tariff_repo: ITariffRepository,
    ):
        self.payment_repo = payment_repo
        self.subscriber_repo = subscriber_repo
        self.order_repo = order_repo
        self.tariff_repo = tariff_repo

    def pay(self, payment_id: int) -> Payment:
        payment = self.payment_repo.get_by_id(payment_id)
        if not payment:
            raise ValueError("Payment not found")

        order = self.order_repo.get_by_id(payment.order_id)
        if not order:
            raise ValueError("Order not found")

        subscriber = self.subscriber_repo.get_by_id(order.subscriber_id)
        if not subscriber:
            raise ValueError("Subscriber not found")

        if subscriber.balance < payment.amount:
            raise ValueError("Insufficient balance")

        subscriber.balance -= payment.amount
        payment.status = "completed"

        tariff_plan = self.tariff_repo.get_by_id(order.tariff_plan_id)
        if not tariff_plan:
            raise ValueError("The specified tariff plan does not exist")
        subscriber.tariff_plan_id = order.tariff_plan_id

        self.payment_repo.update(payment)
        self.subscriber_repo.update(subscriber)

        return payment
