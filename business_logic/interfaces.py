
from abc import ABC, abstractmethod

class ISubscriberService(ABC):
    @abstractmethod
    def change_tariff(self, subscriber_id, new_tariff_id):
        pass

    @abstractmethod
    def top_up_balance(self, subscriber_id, amount):
        pass

class ITariffService(ABC):
    @abstractmethod
    def create_tariff(self, name, price):
        pass

    @abstractmethod
    def get_all_tariffs(self):
        pass

class IOrderService(ABC):
    @abstractmethod
    def create_order(self, subscriber_id, order_type, new_tariff_id=None):
        pass

class IPaymentService(ABC):
    @abstractmethod
    def pay(self, payment_id):
        pass
