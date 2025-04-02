from abc import ABC, abstractmethod

from data_access.models import Order, Payment, Subscriber, TariffPlan


class ISubscriberService(ABC):
    @abstractmethod
    def get_subscriber(self, subscriber_id: str) -> Subscriber | None:
        pass

    @abstractmethod
    def create_subscriber(self, name: str, tariff_plan_id: int, phone_number: str) -> Subscriber:
        pass

    @abstractmethod
    def update_balance(self, subscriber_id: int, amount: float) -> Subscriber:
        pass

    @abstractmethod
    def change_tariff(self, subscriber_id: int, new_tariff_plan_id: int) -> tuple[Order, Payment]:
        pass


class ITariffService(ABC):
    @abstractmethod
    def get_tariff(self, tariff_id: int) -> TariffPlan | None:
        pass

    @abstractmethod
    def get_all_tariffs(self) -> list[TariffPlan]:
        pass

    @abstractmethod
    def create_tariff(self, name: str, price: float) -> TariffPlan:
        pass

    @abstractmethod
    def update_tariff(
        self, tariff_id: int, name: str = None, price: float = None
    ) -> TariffPlan:
        pass

    @abstractmethod
    def delete_tariff(self, tariff_id: int) -> bool:
        pass


class IOrderService(ABC):
    @abstractmethod
    def get_subscriber_orders(self, subscriber_id: int) -> list[Order]:
        pass


class IPaymentService(ABC):
    @abstractmethod
    def pay(self, payment_id: int) -> Payment:
        pass
