# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/calendar_add_result.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/calendar_add_result.proto',
  package='pogoprotos.data',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n)pogoprotos/data/calendar_add_result.proto\x12\x0fpogoprotos.data*c\n\x11\x43\x61lendarAddResult\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x1e\n\x11PERMISSION_DENIED\x10\xfe\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x16\n\tNOT_ADDED\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\t\n\x05\x41\x44\x44\x45\x44\x10\x01\x62\x06proto3')
)

_CALENDARADDRESULT = _descriptor.EnumDescriptor(
  name='CalendarAddResult',
  full_name='pogoprotos.data.CalendarAddResult',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERMISSION_DENIED', index=1, number=-2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_ADDED', index=2, number=-1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADDED', index=3, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=62,
  serialized_end=161,
)
_sym_db.RegisterEnumDescriptor(_CALENDARADDRESULT)

CalendarAddResult = enum_type_wrapper.EnumTypeWrapper(_CALENDARADDRESULT)
UNKNOWN = 0
PERMISSION_DENIED = -2
NOT_ADDED = -1
ADDED = 1


DESCRIPTOR.enum_types_by_name['CalendarAddResult'] = _CALENDARADDRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
