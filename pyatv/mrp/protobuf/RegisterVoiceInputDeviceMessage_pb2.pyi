# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FieldDescriptor as google___protobuf___descriptor___FieldDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from pyatv.mrp.protobuf.VoiceInputDeviceDescriptorMessage_pb2 import (
    VoiceInputDeviceDescriptor as pyatv___mrp___protobuf___VoiceInputDeviceDescriptorMessage_pb2___VoiceInputDeviceDescriptor,
)

from typing import (
    Optional as typing___Optional,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class RegisterVoiceInputDeviceMessage(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def deviceDescriptor(self) -> pyatv___mrp___protobuf___VoiceInputDeviceDescriptorMessage_pb2___VoiceInputDeviceDescriptor: ...

    def __init__(self,
        *,
        deviceDescriptor : typing___Optional[pyatv___mrp___protobuf___VoiceInputDeviceDescriptorMessage_pb2___VoiceInputDeviceDescriptor] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"deviceDescriptor",b"deviceDescriptor"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"deviceDescriptor",b"deviceDescriptor"]) -> None: ...
type___RegisterVoiceInputDeviceMessage = RegisterVoiceInputDeviceMessage

registerVoiceInputDeviceMessage: google___protobuf___descriptor___FieldDescriptor = ...
