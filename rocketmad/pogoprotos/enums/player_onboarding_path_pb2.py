# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/player_onboarding_path.proto

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
  name='pogoprotos/enums/player_onboarding_path.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_pb=_b('\n-pogoprotos/enums/player_onboarding_path.proto\x12\x10pogoprotos.enums*v\n\x14PlayerOnboardingPath\x12 \n\x1cUNSET_PLAYER_ONBOARDING_PATH\x10\x00\x12\x1d\n\x19V1_PLAYER_ONBOARDING_PATH\x10\x01\x12\x1d\n\x19V2_PLAYER_ONBOARDING_PATH\x10\x02\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_PLAYERONBOARDINGPATH = _descriptor.EnumDescriptor(
  name='PlayerOnboardingPath',
  full_name='pogoprotos.enums.PlayerOnboardingPath',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET_PLAYER_ONBOARDING_PATH', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='V1_PLAYER_ONBOARDING_PATH', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='V2_PLAYER_ONBOARDING_PATH', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=67,
  serialized_end=185,
)
_sym_db.RegisterEnumDescriptor(_PLAYERONBOARDINGPATH)

PlayerOnboardingPath = enum_type_wrapper.EnumTypeWrapper(_PLAYERONBOARDINGPATH)
UNSET_PLAYER_ONBOARDING_PATH = 0
V1_PLAYER_ONBOARDING_PATH = 1
V2_PLAYER_ONBOARDING_PATH = 2


DESCRIPTOR.enum_types_by_name['PlayerOnboardingPath'] = _PLAYERONBOARDINGPATH


# @@protoc_insertion_point(module_scope)
