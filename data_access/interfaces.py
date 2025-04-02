from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List
from data_access.models import Subscriber, TariffPlan, Order, Payment

T = TypeVar("T")


class IBaseRepository(ABC, Generic[T]):
    @abstractmethod
    def get_by_id(self, entity_id: int) -> T | None:
        pass

    @abstractmethod
    def get_all(self) -> List[T]:
        pass

    @abstractmethod
    def add(self, entity: T) -> T:
        pass

    @abstractmethod
    def update(self, entity: T) -> T:
        pass

    @abstractmethod
    def delete(self, entity: T) -> None:
        pass


class ISubscriberRepository(IBaseRepository[Subscriber], ABC):
    pass


class ITariffRepository(IBaseRepository[TariffPlan], ABC):
    pass


class IOrderRepository(IBaseRepository[Order], ABC):
    pass


class IPaymentRepository(IBaseRepository[Payment], ABC):
    pass
