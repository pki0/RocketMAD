# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/social/requests/list_friends_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/social/requests/list_friends_message.proto',
  package='pogoprotos.networking.requests.social.requests',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nIpogoprotos/networking/requests/social/requests/list_friends_message.proto\x12.pogoprotos.networking.requests.social.requests\"\x14\n\x12ListFriendsMessageb\x06proto3')
)




_LISTFRIENDSMESSAGE = _descriptor.Descriptor(
  name='ListFriendsMessage',
  full_name='pogoprotos.networking.requests.social.requests.ListFriendsMessage',
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
  serialized_start=125,
  serialized_end=145,
)

DESCRIPTOR.message_types_by_name['ListFriendsMessage'] = _LISTFRIENDSMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListFriendsMessage = _reflection.GeneratedProtocolMessageType('ListFriendsMessage', (_message.Message,), dict(
  DESCRIPTOR = _LISTFRIENDSMESSAGE,
  __module__ = 'pogoprotos.networking.requests.social.requests.list_friends_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.social.requests.ListFriendsMessage)
  ))
_sym_db.RegisterMessage(ListFriendsMessage)


# @@protoc_insertion_point(module_scope)
