from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from data_access.repositories import (
    SubscriberRepository,
    TariffRepository,
    OrderRepository,
    PaymentRepository,
)
from business_logic.services import (
    SubscriberService,
    TariffService,
    OrderService,
    PaymentService,
)

DATABASE_URL = "sqlite:///operator.db"


class DIContainer:
    def __init__(self):

        self.engine = create_engine(DATABASE_URL)
        self.SessionLocal = sessionmaker(bind=self.engine)

        self.subscriber_repo = None
        self.tariff_repo = None
        self.order_repo = None
        self.payment_repo = None

        self.subscriber_service = None
        self.tariff_service = None
        self.order_service = None
        self.payment_service = None

    def init_services(self):
        session = self.SessionLocal()

        self.subscriber_repo = SubscriberRepository(session)
        self.tariff_repo = TariffRepository(session)
        self.order_repo = OrderRepository(session)
        self.payment_repo = PaymentRepository(session)

        self.subscriber_service = SubscriberService(
            self.subscriber_repo, self.order_repo, self.payment_repo, self.tariff_repo
        )
        self.tariff_service = TariffService(self.tariff_repo)
        self.order_service = OrderService(
            self.order_repo, self.payment_repo, self.subscriber_repo
        )
        self.payment_service = PaymentService(
            self.payment_repo, self.subscriber_repo, self.order_repo, self.tariff_repo
        )

    def get_session(self) -> Session:
        return self.SessionLocal()


container = DIContainer()
container.init_services()
