# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/buddy_activity_category.proto

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
  name='pogoprotos/enums/buddy_activity_category.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_pb=_b('\n.pogoprotos/enums/buddy_activity_category.proto\x12\x10pogoprotos.enums*\xea\x01\n\x15\x42uddyActivityCategory\x12\x18\n\x14\x42UDDY_CATEGORY_UNSET\x10\x00\x12\x17\n\x13\x42UDDY_CATEGORY_FEED\x10\x01\x12\x17\n\x13\x42UDDY_CATEGORY_CARE\x10\x02\x12\x1b\n\x17\x42UDDY_CATEGORY_SNAPSHOT\x10\x03\x12\x17\n\x13\x42UDDY_CATEGORY_WALK\x10\x04\x12\x19\n\x15\x42UDDY_CATEGORY_BATTLE\x10\x05\x12\x1a\n\x16\x42UDDY_CATEGORY_EXPLORE\x10\x06\x12\x18\n\x14\x42UDDY_CATEGORY_BONUS\x10\x07\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_BUDDYACTIVITYCATEGORY = _descriptor.EnumDescriptor(
  name='BuddyActivityCategory',
  full_name='pogoprotos.enums.BuddyActivityCategory',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BUDDY_CATEGORY_UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_CATEGORY_FEED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_CATEGORY_CARE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_CATEGORY_SNAPSHOT', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_CATEGORY_WALK', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_CATEGORY_BATTLE', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_CATEGORY_EXPLORE', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_CATEGORY_BONUS', index=7, number=7,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=69,
  serialized_end=303,
)
_sym_db.RegisterEnumDescriptor(_BUDDYACTIVITYCATEGORY)

BuddyActivityCategory = enum_type_wrapper.EnumTypeWrapper(_BUDDYACTIVITYCATEGORY)
BUDDY_CATEGORY_UNSET = 0
BUDDY_CATEGORY_FEED = 1
BUDDY_CATEGORY_CARE = 2
BUDDY_CATEGORY_SNAPSHOT = 3
BUDDY_CATEGORY_WALK = 4
BUDDY_CATEGORY_BATTLE = 5
BUDDY_CATEGORY_EXPLORE = 6
BUDDY_CATEGORY_BONUS = 7


DESCRIPTOR.enum_types_by_name['BuddyActivityCategory'] = _BUDDYACTIVITYCATEGORY


# @@protoc_insertion_point(module_scope)
