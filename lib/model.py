import abc
from typing import ClassVar

from pydantic import BaseModel
from devtools import debug

class Model(BaseModel, ABC):
    @property
    @abc.abstractmethod
    def item_type(self) -> str:
        pass
