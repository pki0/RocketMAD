# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/telemetry/change_online_status_telemetry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/telemetry/change_online_status_telemetry.proto',
  package='pogoprotos.data.telemetry',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n>pogoprotos/data/telemetry/change_online_status_telemetry.proto\x12\x19pogoprotos.data.telemetry\":\n\x1b\x43hangeOnlineStatusTelemetry\x12\x1b\n\x13is_online_status_on\x18\x01 \x01(\x08\x62\x06proto3')
)




_CHANGEONLINESTATUSTELEMETRY = _descriptor.Descriptor(
  name='ChangeOnlineStatusTelemetry',
  full_name='pogoprotos.data.telemetry.ChangeOnlineStatusTelemetry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_online_status_on', full_name='pogoprotos.data.telemetry.ChangeOnlineStatusTelemetry.is_online_status_on', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=93,
  serialized_end=151,
)

DESCRIPTOR.message_types_by_name['ChangeOnlineStatusTelemetry'] = _CHANGEONLINESTATUSTELEMETRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ChangeOnlineStatusTelemetry = _reflection.GeneratedProtocolMessageType('ChangeOnlineStatusTelemetry', (_message.Message,), dict(
  DESCRIPTOR = _CHANGEONLINESTATUSTELEMETRY,
  __module__ = 'pogoprotos.data.telemetry.change_online_status_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.ChangeOnlineStatusTelemetry)
  ))
_sym_db.RegisterMessage(ChangeOnlineStatusTelemetry)


# @@protoc_insertion_point(module_scope)
