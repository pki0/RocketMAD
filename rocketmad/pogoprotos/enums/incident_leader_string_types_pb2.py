# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/incident_leader_string_types.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/enums/incident_leader_string_types.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_pb=_b('\n3pogoprotos/enums/incident_leader_string_types.proto\x12\x10pogoprotos.enums*\xec\x01\n\x19IncidentLeaderStringTypes\x12\x1b\n\x17ONBOARDING_INTRODUCTION\x10\x00\x12\x18\n\x14ONBOARDING_ENCOUNTER\x10\x01\x12\x15\n\x11ONBOARDING_SHADOW\x10\x02\x12\x1b\n\x17ONBOARDING_MAP_FRAGMENT\x10\x03\x12\x14\n\x10ONBOARDING_MAP_1\x10\x04\x12\x14\n\x10ONBOARDING_MAP_2\x10\x05\x12\x0b\n\x07INSPIRE\x10\x06\x12\x14\n\x10MAP_TIME_WARNING\x10\x07\x12\x15\n\x11MAP_EMPTY_WARNING\x10\x08\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_INCIDENTLEADERSTRINGTYPES = _descriptor.EnumDescriptor(
  name='IncidentLeaderStringTypes',
  full_name='pogoprotos.enums.IncidentLeaderStringTypes',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ONBOARDING_INTRODUCTION', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ONBOARDING_ENCOUNTER', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ONBOARDING_SHADOW', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ONBOARDING_MAP_FRAGMENT', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ONBOARDING_MAP_1', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ONBOARDING_MAP_2', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INSPIRE', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAP_TIME_WARNING', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAP_EMPTY_WARNING', index=8, number=8,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=74,
  serialized_end=310,
)
_sym_db.RegisterEnumDescriptor(_INCIDENTLEADERSTRINGTYPES)

IncidentLeaderStringTypes = enum_type_wrapper.EnumTypeWrapper(_INCIDENTLEADERSTRINGTYPES)
ONBOARDING_INTRODUCTION = 0
ONBOARDING_ENCOUNTER = 1
ONBOARDING_SHADOW = 2
ONBOARDING_MAP_FRAGMENT = 3
ONBOARDING_MAP_1 = 4
ONBOARDING_MAP_2 = 5
INSPIRE = 6
MAP_TIME_WARNING = 7
MAP_EMPTY_WARNING = 8


DESCRIPTOR.enum_types_by_name['IncidentLeaderStringTypes'] = _INCIDENTLEADERSTRINGTYPES


# @@protoc_insertion_point(module_scope)
