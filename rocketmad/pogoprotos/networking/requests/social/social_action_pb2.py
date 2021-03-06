# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/social/social_action.proto

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
  name='pogoprotos/networking/requests/social/social_action.proto',
  package='pogoprotos.networking.requests.social',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n9pogoprotos/networking/requests/social/social_action.proto\x12%pogoprotos.networking.requests.social*\xc4\x06\n\x0cSocialAction\x12\x19\n\x15UNKNOWN_SOCIAL_ACTION\x10\x00\x12\x12\n\rSEARCH_PLAYER\x10\x90N\x12\x17\n\x12SEND_FRIEND_INVITE\x10\x92N\x12\x19\n\x14\x43\x41NCEL_FRIEND_INVITE\x10\x93N\x12\x19\n\x14\x41\x43\x43\x45PT_FRIEND_INVITE\x10\x94N\x12\x1a\n\x15\x44\x45\x43LINE_FRIEND_INVITE\x10\x95N\x12\x11\n\x0cLIST_FRIENDS\x10\x96N\x12!\n\x1cLIST_OUTGOING_FRIEND_INVITES\x10\x97N\x12!\n\x1cLIST_INCOMING_FRIEND_INVITES\x10\x98N\x12\x12\n\rREMOVE_FRIEND\x10\x99N\x12\x17\n\x12LIST_FRIEND_STATUS\x10\x9aN\x12 \n\x1bSEND_FACEBOOK_FRIEND_INVITE\x10\x9bN\x12\x11\n\x0cIS_MY_FRIEND\x10\x9cN\x12\x17\n\x12\x43REATE_INVITE_CODE\x10\x9dN\x12\x1d\n\x18GET_FACEBOOK_FRIEND_LIST\x10\x9eN\x12\x1b\n\x16UPDATE_FACEBOOK_STATUS\x10\x9fN\x12\x19\n\x14SAVE_PLAYER_SETTINGS\x10\xa0N\x12\x18\n\x13GET_PLAYER_SETTINGS\x10\xa1N\x12\x1c\n\x17GET_NIANTIC_FRIEND_LIST\x10\xa2N\x12\x1f\n\x1aGET_NIANTIC_FRIEND_DETAILS\x10\xa3N\x12\x1f\n\x1aSEND_NIANTIC_FRIEND_INVITE\x10\xa4N\x12\x19\n\x14SET_ACCOUNT_SETTINGS\x10\xa5N\x12\x19\n\x14GET_ACCOUNT_SETTINGS\x10\xa6N\x12-\n(REGISTER_PUSH_NOTIFICATION_SOCIAL_ACTION\x10\xf5N\x12/\n*UNREGISTER_PUSH_NOTIFICATION_SOCIAL_ACTION\x10\xf6N\x12\x18\n\x13UPDATE_NOTIFICATION\x10\xf7N\x12\x35\n0OPT_OUT_PUSH_NOTIFICATION_CATEGORY_SOCIAL_ACTION\x10\xf8N\x12\x0e\n\tGET_INBOX\x10\xf9Nb\x06proto3')
)

_SOCIALACTION = _descriptor.EnumDescriptor(
  name='SocialAction',
  full_name='pogoprotos.networking.requests.social.SocialAction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_SOCIAL_ACTION', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEARCH_PLAYER', index=1, number=10000,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEND_FRIEND_INVITE', index=2, number=10002,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANCEL_FRIEND_INVITE', index=3, number=10003,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACCEPT_FRIEND_INVITE', index=4, number=10004,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DECLINE_FRIEND_INVITE', index=5, number=10005,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIST_FRIENDS', index=6, number=10006,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIST_OUTGOING_FRIEND_INVITES', index=7, number=10007,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIST_INCOMING_FRIEND_INVITES', index=8, number=10008,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOVE_FRIEND', index=9, number=10009,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIST_FRIEND_STATUS', index=10, number=10010,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEND_FACEBOOK_FRIEND_INVITE', index=11, number=10011,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IS_MY_FRIEND', index=12, number=10012,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CREATE_INVITE_CODE', index=13, number=10013,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_FACEBOOK_FRIEND_LIST', index=14, number=10014,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_FACEBOOK_STATUS', index=15, number=10015,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SAVE_PLAYER_SETTINGS', index=16, number=10016,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_PLAYER_SETTINGS', index=17, number=10017,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_NIANTIC_FRIEND_LIST', index=18, number=10018,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_NIANTIC_FRIEND_DETAILS', index=19, number=10019,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEND_NIANTIC_FRIEND_INVITE', index=20, number=10020,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_ACCOUNT_SETTINGS', index=21, number=10021,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_ACCOUNT_SETTINGS', index=22, number=10022,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGISTER_PUSH_NOTIFICATION_SOCIAL_ACTION', index=23, number=10101,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNREGISTER_PUSH_NOTIFICATION_SOCIAL_ACTION', index=24, number=10102,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_NOTIFICATION', index=25, number=10103,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPT_OUT_PUSH_NOTIFICATION_CATEGORY_SOCIAL_ACTION', index=26, number=10104,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_INBOX', index=27, number=10105,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=101,
  serialized_end=937,
)
_sym_db.RegisterEnumDescriptor(_SOCIALACTION)

SocialAction = enum_type_wrapper.EnumTypeWrapper(_SOCIALACTION)
UNKNOWN_SOCIAL_ACTION = 0
SEARCH_PLAYER = 10000
SEND_FRIEND_INVITE = 10002
CANCEL_FRIEND_INVITE = 10003
ACCEPT_FRIEND_INVITE = 10004
DECLINE_FRIEND_INVITE = 10005
LIST_FRIENDS = 10006
LIST_OUTGOING_FRIEND_INVITES = 10007
LIST_INCOMING_FRIEND_INVITES = 10008
REMOVE_FRIEND = 10009
LIST_FRIEND_STATUS = 10010
SEND_FACEBOOK_FRIEND_INVITE = 10011
IS_MY_FRIEND = 10012
CREATE_INVITE_CODE = 10013
GET_FACEBOOK_FRIEND_LIST = 10014
UPDATE_FACEBOOK_STATUS = 10015
SAVE_PLAYER_SETTINGS = 10016
GET_PLAYER_SETTINGS = 10017
GET_NIANTIC_FRIEND_LIST = 10018
GET_NIANTIC_FRIEND_DETAILS = 10019
SEND_NIANTIC_FRIEND_INVITE = 10020
SET_ACCOUNT_SETTINGS = 10021
GET_ACCOUNT_SETTINGS = 10022
REGISTER_PUSH_NOTIFICATION_SOCIAL_ACTION = 10101
UNREGISTER_PUSH_NOTIFICATION_SOCIAL_ACTION = 10102
UPDATE_NOTIFICATION = 10103
OPT_OUT_PUSH_NOTIFICATION_CATEGORY_SOCIAL_ACTION = 10104
GET_INBOX = 10105


DESCRIPTOR.enum_types_by_name['SocialAction'] = _SOCIALACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
