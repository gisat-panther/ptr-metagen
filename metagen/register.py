from abc import ABC, abstractmethod
from uuid import UUID
from typing import Type
from functools import wraps
from warnings import warn
from pandas import DataFrame
from pydantic import BaseModel, Field

from metagen.base import LeafABC


# TODO: Register name - check on name internal


class Register(BaseModel, ABC):

    @abstractmethod
    def add(self, element: Type[LeafABC]) -> None:
        pass

    @abstractmethod
    def check_register(self, element: Type[LeafABC]) -> bool:
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> Type[LeafABC]:
        pass

    @abstractmethod
    def get_by_hash(self, hash: int) -> Type[LeafABC]:
        pass

    @abstractmethod
    def get_by_uuid(self, uuid: UUID) -> Type[LeafABC]:
        pass


# register
class DictRegister(Register):
    hashs: dict = Field(default_factory=dict)
    uuid: dict = Field(default_factory=dict)
    name: dict = Field(default_factory=dict)

    def add(self, element: Type[LeafABC]) -> None:
        if not self.check_register(element):
            self.hashs.update({hash(element): element})
            self.uuid.update({str(element.key): element})
            self.name.update({element.nameInternal: element})
        else:
            raise ValueError(f'PTR element "{element.__class__.__name__}" with nameInternal: {element.nameInternal}, '
                             f'key: {element.key} and hash: {hash(element)} already exist')

    def check_register(self, element: Type[LeafABC]) -> bool:
        return all([self.hashs.get(hash(element)), self.name.get(element.nameInternal)])

    def get_by_name(self, name: str) -> Type[LeafABC]:
        return self.name.get(name)

    def get_by_hash(self, hash: int) -> Type[LeafABC]:
        return self.hashs.get(hash)

    def get_by_uuid(self, uuid: str) -> Type[LeafABC]:
        if UUID(uuid):
            return self.uuid.get(uuid)


class PandasRegister(Register):
    table: DataFrame = Field(default=DataFrame())

    def add(self, element: Type[LeafABC]) -> None:
        self.table()

    def check_register(self, element: Type[LeafABC]) -> bool:
        pass


    def get_by_name(self, name: str) -> Type[LeafABC]:
        pass


    def get_by_hash(self, hash: int) -> Type[LeafABC]:
        pass


    def get_by_uuid(self, uuid: UUID) -> Type[LeafABC]:
        pass


register = DictRegister()


def exist_in_register(element):
    @wraps(element)
    def checking_register(*args, **kwargs):
        instance = element(*args, **kwargs)
        if register.get_by_hash(hash(instance)):
            registered_element = register.get_by_hash(hash(instance))
            warn(f'Element duplication: Element {instance.__class__.__name__} with parameters: '
                 f'{"; ".join([f"{k}: {v}" for k, v in kwargs.items()])} found in register. Element '
                 f'{registered_element.__repr__()} returned instead')
            return registered_element
        else:
            register.add(instance)
            return instance
    return checking_register