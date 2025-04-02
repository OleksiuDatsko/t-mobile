from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Subscriber(Base):
    __tablename__ = "subscribers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    balance = Column(Float, default=0.0)
    phone_number = Column(String, nullable=True)
    tariff_plan_id = Column(Integer, ForeignKey("tariff_plans.id"))

    tariff_plan = relationship("TariffPlan")

    def __repr__(self):

        return f"Subscriber(id={self.id}, name='{self.name}', balance={self.balance}, phone_number={self.phone_number}, tariff_plan={self.tariff_plan})"

    def __str__(self):
        return f"Subscriber(id={self.id}, name='{self.name}', balance={self.balance}, phone_number={self.phone_number}, tariff_plan={self.tariff_plan})"


class TariffPlan(Base):
    __tablename__ = "tariff_plans"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)

    def __repr__(self):
        return f"TariffPlan(id={self.id}, name='{self.name}', price={self.price})"

    def __str__(self):
        return f"TariffPlan(id={self.id}, name='{self.name}', price={self.price})"


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    subscriber_id = Column(Integer, ForeignKey("subscribers.id"))
    amount = Column(Float, nullable=True)
    tariff_plan_id = Column(Integer, ForeignKey("tariff_plans.id"), nullable=True)

    subscriber = relationship("Subscriber")
    tariff_plan = relationship("TariffPlan")

    def __repr__(self):
        return f"Order(id={self.id}, subscriber_id={self.subscriber_id}, amount={self.amount})"

    def __str__(self):
        return f"Order(id={self.id}, subscriber_id={self.subscriber_id}, amount={self.amount})"


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    amount = Column(Float, nullable=False)
    status = Column(String, default="pending")  # "pending", "completed"

    order = relationship("Order")

    def __repr__(self):
        return f"Payment(id={self.id}, order_id={self.order_id}, amount={self.amount}, status='{self.status}, order={self.order}')"

    def __str__(self):
        return f"Payment(id={self.id}, order_id={self.order_id}, amount={self.amount}, status='{self.status}, order={self.order}')"
