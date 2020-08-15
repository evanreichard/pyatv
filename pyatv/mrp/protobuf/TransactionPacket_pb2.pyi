# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from pyatv.mrp.protobuf.TransactionKey_pb2 import (
    TransactionKey as pyatv___mrp___protobuf___TransactionKey_pb2___TransactionKey,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class TransactionPacket(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    packetData: builtin___bytes = ...
    identifier: typing___Text = ...
    totalLength: builtin___int = ...
    totalWritePosition: builtin___int = ...

    @property
    def key(self) -> pyatv___mrp___protobuf___TransactionKey_pb2___TransactionKey: ...

    def __init__(self,
        *,
        key : typing___Optional[pyatv___mrp___protobuf___TransactionKey_pb2___TransactionKey] = None,
        packetData : typing___Optional[builtin___bytes] = None,
        identifier : typing___Optional[typing___Text] = None,
        totalLength : typing___Optional[builtin___int] = None,
        totalWritePosition : typing___Optional[builtin___int] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"identifier",b"identifier",u"key",b"key",u"packetData",b"packetData",u"totalLength",b"totalLength",u"totalWritePosition",b"totalWritePosition"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"identifier",b"identifier",u"key",b"key",u"packetData",b"packetData",u"totalLength",b"totalLength",u"totalWritePosition",b"totalWritePosition"]) -> None: ...
type___TransactionPacket = TransactionPacket
