# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/gui_transition_type.proto

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
  name='pogoprotos/enums/gui_transition_type.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n*pogoprotos/enums/gui_transition_type.proto\x12\x10pogoprotos.enums*L\n\x11GuiTransitionType\x12\x1a\n\x16GUI_TRANSITION_TYPE_IN\x10\x00\x12\x1b\n\x17GUI_TRANSITION_TYPE_OUT\x10\x01\x62\x06proto3')
)

_GUITRANSITIONTYPE = _descriptor.EnumDescriptor(
  name='GuiTransitionType',
  full_name='pogoprotos.enums.GuiTransitionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GUI_TRANSITION_TYPE_IN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GUI_TRANSITION_TYPE_OUT', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=64,
  serialized_end=140,
)
_sym_db.RegisterEnumDescriptor(_GUITRANSITIONTYPE)

GuiTransitionType = enum_type_wrapper.EnumTypeWrapper(_GUITRANSITIONTYPE)
GUI_TRANSITION_TYPE_IN = 0
GUI_TRANSITION_TYPE_OUT = 1


DESCRIPTOR.enum_types_by_name['GuiTransitionType'] = _GUITRANSITIONTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
