# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/telemetry/common_telemetry_boot_time.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/telemetry/common_telemetry_boot_time.proto',
  package='pogoprotos.data.telemetry',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n:pogoprotos/data/telemetry/common_telemetry_boot_time.proto\x12\x19pogoprotos.data.telemetry\"B\n\x17\x43ommonTelemetryBootTime\x12\x12\n\nboot_phase\x18\x01 \x01(\t\x12\x13\n\x0b\x64uration_ms\x18\x02 \x01(\x03\x62\x06proto3')
)




_COMMONTELEMETRYBOOTTIME = _descriptor.Descriptor(
  name='CommonTelemetryBootTime',
  full_name='pogoprotos.data.telemetry.CommonTelemetryBootTime',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='boot_phase', full_name='pogoprotos.data.telemetry.CommonTelemetryBootTime.boot_phase', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration_ms', full_name='pogoprotos.data.telemetry.CommonTelemetryBootTime.duration_ms', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=89,
  serialized_end=155,
)

DESCRIPTOR.message_types_by_name['CommonTelemetryBootTime'] = _COMMONTELEMETRYBOOTTIME
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CommonTelemetryBootTime = _reflection.GeneratedProtocolMessageType('CommonTelemetryBootTime', (_message.Message,), dict(
  DESCRIPTOR = _COMMONTELEMETRYBOOTTIME,
  __module__ = 'pogoprotos.data.telemetry.common_telemetry_boot_time_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.CommonTelemetryBootTime)
  ))
_sym_db.RegisterMessage(CommonTelemetryBootTime)


# @@protoc_insertion_point(module_scope)
