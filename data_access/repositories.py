from sqlalchemy.orm import Session
from typing import Type, TypeVar, List
from data_access.interfaces import (
    IBaseRepository,
    IOrderRepository,
    IPaymentRepository,
    ISubscriberRepository,
    ITariffRepository,
)
from data_access.models import Order, Payment, Subscriber, TariffPlan

T = TypeVar("T")


class BaseRepository(IBaseRepository[T]):
    def __init__(self, session: Session, model: Type[T]):
        self.session = session
        self.model = model

    def add(self, entity: T) -> T:
        self.session.add(entity)
        self.session.commit()
        return entity

    def get_by_id(self, entity_id: int) -> T | None:
        return self.session.query(self.model).filter_by(id=entity_id).first()

    def get_all(self, **kwargs) -> List[T]:
        query = self.session.query(self.model)
        for key, value in kwargs.items():
            query = query.filter(getattr(self.model, key) == value)
        return query.all()

    def update(self, entity: T) -> T:
        self.session.commit()
        return entity

    def delete(self, entity: T) -> None:
        self.session.delete(entity)
        self.session.commit()


class SubscriberRepository(BaseRepository[Subscriber], ISubscriberRepository):
    def __init__(self, session: Session):
        super().__init__(session, Subscriber)


class TariffRepository(BaseRepository[TariffPlan], ITariffRepository):
    def __init__(self, session: Session):
        super().__init__(session, TariffPlan)


class OrderRepository(BaseRepository[Order], IOrderRepository):
    def __init__(self, session: Session):
        super().__init__(session, Order)


class PaymentRepository(BaseRepository[Payment], IPaymentRepository):
    def __init__(self, session: Session):
        super().__init__(session, Payment)
