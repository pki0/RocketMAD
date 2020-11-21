# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/telemetry/boot_telemetry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/telemetry/boot_telemetry.proto',
  package='pogoprotos.data.telemetry',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n.pogoprotos/data/telemetry/boot_telemetry.proto\x12\x19pogoprotos.data.telemetry\"N\n\rBootTelemetry\x12\x1c\n\x14nearest_poi_distance\x18\x01 \x01(\x02\x12\x1f\n\x17poi_within_one_km_count\x18\x02 \x01(\x05\x62\x06proto3')
)




_BOOTTELEMETRY = _descriptor.Descriptor(
  name='BootTelemetry',
  full_name='pogoprotos.data.telemetry.BootTelemetry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nearest_poi_distance', full_name='pogoprotos.data.telemetry.BootTelemetry.nearest_poi_distance', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='poi_within_one_km_count', full_name='pogoprotos.data.telemetry.BootTelemetry.poi_within_one_km_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=77,
  serialized_end=155,
)

DESCRIPTOR.message_types_by_name['BootTelemetry'] = _BOOTTELEMETRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BootTelemetry = _reflection.GeneratedProtocolMessageType('BootTelemetry', (_message.Message,), dict(
  DESCRIPTOR = _BOOTTELEMETRY,
  __module__ = 'pogoprotos.data.telemetry.boot_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.BootTelemetry)
  ))
_sym_db.RegisterMessage(BootTelemetry)


# @@protoc_insertion_point(module_scope)
