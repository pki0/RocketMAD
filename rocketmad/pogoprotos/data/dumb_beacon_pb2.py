# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/dumb_beacon.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/dumb_beacon.proto',
  package='pogoprotos.data',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n!pogoprotos/data/dumb_beacon.proto\x12\x0fpogoprotos.data\"\x0c\n\nDumbBeaconb\x06proto3')
)




_DUMBBEACON = _descriptor.Descriptor(
  name='DumbBeacon',
  full_name='pogoprotos.data.DumbBeacon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=54,
  serialized_end=66,
)

DESCRIPTOR.message_types_by_name['DumbBeacon'] = _DUMBBEACON
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DumbBeacon = _reflection.GeneratedProtocolMessageType('DumbBeacon', (_message.Message,), dict(
  DESCRIPTOR = _DUMBBEACON,
  __module__ = 'pogoprotos.data.dumb_beacon_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.DumbBeacon)
  ))
_sym_db.RegisterMessage(DumbBeacon)


# @@protoc_insertion_point(module_scope)
