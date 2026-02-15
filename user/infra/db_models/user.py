from datetime import datetime

from sqlalchemy import String, DateTime, Column
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


# database 모듈에서 declarative_base 함수에 의해 생성된 Base 클래스를 상속받는다.
# declarative_base 함수는 선언형 클래스를 정의하기 위한 기본 클래스를 생성한다.
# 생성된 기본 클래스는 메타클래스를 얻게 되는데, 이는 적합한 Table 객체를 생성하고,
# 클레스 내에서 선언된 정보와 클래스의 하위 클래스로부터 제공된 정보를 기반으로 적절한 메퍼를 생성한다.
class User(Base):
  __tablename__ = "User"

  id: Mapped[str] = Column(String(36), primary_key=True)
  name: Mapped[str] = Column(String(36), nullable=False)
  email: Mapped[str] = Column(String(36), nullable=False)
  password: Mapped[str] = Column(String(36), nullable=False)
  created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
  updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
