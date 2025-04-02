from abc import ABC, abstractmethod
from typing import List, Optional
from data_access.models import Subscriber, TariffPlan, Order, Payment


class ISubscriberController(ABC):
    @abstractmethod
    def get_subscriber(self, subscriber_id: int) -> Optional[Subscriber]:
        pass

    @abstractmethod
    def create_subscriber(self, name: str, tariff_plan_id: int) -> Subscriber:
        pass

    @abstractmethod
    def update_balance(self, subscriber_id: int, amount: float) -> Subscriber:
        pass

    @abstractmethod
    def change_tariff(self, subscriber_id: int, new_tariff_plan_id: int) -> Order:
        pass


class ITariffController(ABC):
    @abstractmethod
    def get_tariff(self, tariff_id: int) -> Optional[TariffPlan]:
        pass

    @abstractmethod
    def get_all_tariffs(self) -> List[TariffPlan]:
        pass

    @abstractmethod
    def create_tariff(self, name: str, price: float) -> TariffPlan:
        pass

    @abstractmethod
    def update_tariff(self, tariff_id: int, name: Optional[str], price: Optional[float]) -> TariffPlan:
        pass

    @abstractmethod
    def delete_tariff(self, tariff_id: int) -> bool:
        pass


class IOrderController(ABC):
    @abstractmethod
    def get_subscriber_orders(self, subscriber_id: int) -> List[Order]:
        pass


class IPaymentController(ABC):
    @abstractmethod
    def pay(self, payment_id: int) -> Payment:
        pass
