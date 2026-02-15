from abc import ABCMeta, abstractmethod
from user.domain.user import User


# 객체지향 인터페이스로 선언하기 위해 ABCMeta 클래스를 사용합니다.
class IUserRepository(metaclass=ABCMeta):
  @abstractmethod
  def save(self, user: User):
    raise NotImplementedError

  @abstractmethod
  def find_by_email(self, email: str) -> User:
    """
    이메일로 유저를 검색한다.
    검새한 유저가 없을 경우 422 에러를 발생시킨다.
    """
    raise NotImplementedError

