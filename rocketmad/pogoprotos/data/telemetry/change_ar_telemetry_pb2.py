# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/telemetry/change_ar_telemetry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/telemetry/change_ar_telemetry.proto',
  package='pogoprotos.data.telemetry',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n3pogoprotos/data/telemetry/change_ar_telemetry.proto\x12\x19pogoprotos.data.telemetry\"@\n\x11\x43hangeArTelemetry\x12\x12\n\nar_enabled\x18\x01 \x01(\x08\x12\x17\n\x0f\x61r_plus_enabled\x18\x02 \x01(\x08\x62\x06proto3')
)




_CHANGEARTELEMETRY = _descriptor.Descriptor(
  name='ChangeArTelemetry',
  full_name='pogoprotos.data.telemetry.ChangeArTelemetry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ar_enabled', full_name='pogoprotos.data.telemetry.ChangeArTelemetry.ar_enabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ar_plus_enabled', full_name='pogoprotos.data.telemetry.ChangeArTelemetry.ar_plus_enabled', index=1,
      number=2, type=8, cpp_type=7, label=1,
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
  serialized_start=82,
  serialized_end=146,
)

DESCRIPTOR.message_types_by_name['ChangeArTelemetry'] = _CHANGEARTELEMETRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ChangeArTelemetry = _reflection.GeneratedProtocolMessageType('ChangeArTelemetry', (_message.Message,), dict(
  DESCRIPTOR = _CHANGEARTELEMETRY,
  __module__ = 'pogoprotos.data.telemetry.change_ar_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.ChangeArTelemetry)
  ))
_sym_db.RegisterMessage(ChangeArTelemetry)


# @@protoc_insertion_point(module_scope)
