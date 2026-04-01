from http import HTTPStatus
from typing import Generic, Literal, MutableMapping, Optional, TypeVar

from attrs import define


class Unset:
    def __bool__(self) -> Literal[False]:
        return False


UNSET: Unset = Unset()
T = TypeVar("T")


@define
class Response(Generic[T]):
    status_code: HTTPStatus
    content: bytes
    headers: MutableMapping[str, str]
    parsed: Optional[T]

    __all__ = ["Response", "Unset", "UNSET"]
