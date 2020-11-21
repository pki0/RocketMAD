# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/friends/friend_details.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.player import player_summary_pb2 as pogoprotos_dot_data_dot_player_dot_player__summary__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/friends/friend_details.proto',
  package='pogoprotos.data.friends',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n,pogoprotos/data/friends/friend_details.proto\x12\x17pogoprotos.data.friends\x1a+pogoprotos/data/player/player_summary.proto\"\xaa\x02\n\rFriendDetails\x12\x35\n\x06player\x18\x01 \x01(\x0b\x32%.pogoprotos.data.player.PlayerSummary\x12\x1b\n\x13\x66riend_visible_data\x18\x02 \x01(\x0c\x12\r\n\x05score\x18\x03 \x01(\x05\x12\x14\n\x0c\x64\x61ta_with_me\x18\x04 \x01(\x0c\x12J\n\ronline_status\x18\x05 \x01(\x0e\x32\x33.pogoprotos.data.friends.FriendDetails.OnlineStatus\"T\n\x0cOnlineStatus\x12\t\n\x05UNSET\x10\x00\x12\x12\n\x0eSTATUS_UNKNOWN\x10\x01\x12\x11\n\rSTATUS_ONLINE\x10\x02\x12\x12\n\x0eSTATUS_OFFLINE\x10\x03\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_player_dot_player__summary__pb2.DESCRIPTOR,])



_FRIENDDETAILS_ONLINESTATUS = _descriptor.EnumDescriptor(
  name='OnlineStatus',
  full_name='pogoprotos.data.friends.FriendDetails.OnlineStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS_ONLINE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS_OFFLINE', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=333,
  serialized_end=417,
)
_sym_db.RegisterEnumDescriptor(_FRIENDDETAILS_ONLINESTATUS)


_FRIENDDETAILS = _descriptor.Descriptor(
  name='FriendDetails',
  full_name='pogoprotos.data.friends.FriendDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='player', full_name='pogoprotos.data.friends.FriendDetails.player', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='friend_visible_data', full_name='pogoprotos.data.friends.FriendDetails.friend_visible_data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='score', full_name='pogoprotos.data.friends.FriendDetails.score', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_with_me', full_name='pogoprotos.data.friends.FriendDetails.data_with_me', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='online_status', full_name='pogoprotos.data.friends.FriendDetails.online_status', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FRIENDDETAILS_ONLINESTATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=119,
  serialized_end=417,
)

_FRIENDDETAILS.fields_by_name['player'].message_type = pogoprotos_dot_data_dot_player_dot_player__summary__pb2._PLAYERSUMMARY
_FRIENDDETAILS.fields_by_name['online_status'].enum_type = _FRIENDDETAILS_ONLINESTATUS
_FRIENDDETAILS_ONLINESTATUS.containing_type = _FRIENDDETAILS
DESCRIPTOR.message_types_by_name['FriendDetails'] = _FRIENDDETAILS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FriendDetails = _reflection.GeneratedProtocolMessageType('FriendDetails', (_message.Message,), dict(
  DESCRIPTOR = _FRIENDDETAILS,
  __module__ = 'pogoprotos.data.friends.friend_details_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.friends.FriendDetails)
  ))
_sym_db.RegisterMessage(FriendDetails)


# @@protoc_insertion_point(module_scope)
