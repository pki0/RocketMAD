# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/social_notification_variable_name.proto

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
  name='pogoprotos/enums/social_notification_variable_name.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_pb=_b('\n8pogoprotos/enums/social_notification_variable_name.proto\x12\x10pogoprotos.enums*\xa4\x01\n\x1eSocialNotificationVariableName\x12+\n\'UNSET_SOCIAL_NOTIFICATION_VARIABLE_NAME\x10\x00\x12\x13\n\x0fSOCIAL_CODENAME\x10\x01\x12\x0f\n\x0bSOCIAL_TEAM\x10\x02\x12\x19\n\x15SOCIAL_PLAYER_SUMMARY\x10\x03\x12\x14\n\x10SOCIAL_FULL_NAME\x10\x04\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_SOCIALNOTIFICATIONVARIABLENAME = _descriptor.EnumDescriptor(
  name='SocialNotificationVariableName',
  full_name='pogoprotos.enums.SocialNotificationVariableName',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET_SOCIAL_NOTIFICATION_VARIABLE_NAME', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOCIAL_CODENAME', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOCIAL_TEAM', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOCIAL_PLAYER_SUMMARY', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOCIAL_FULL_NAME', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=79,
  serialized_end=243,
)
_sym_db.RegisterEnumDescriptor(_SOCIALNOTIFICATIONVARIABLENAME)

SocialNotificationVariableName = enum_type_wrapper.EnumTypeWrapper(_SOCIALNOTIFICATIONVARIABLENAME)
UNSET_SOCIAL_NOTIFICATION_VARIABLE_NAME = 0
SOCIAL_CODENAME = 1
SOCIAL_TEAM = 2
SOCIAL_PLAYER_SUMMARY = 3
SOCIAL_FULL_NAME = 4


DESCRIPTOR.enum_types_by_name['SocialNotificationVariableName'] = _SOCIALNOTIFICATIONVARIABLENAME


# @@protoc_insertion_point(module_scope)
