# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/social/requests/get_niantic_friend_details_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/social/requests/get_niantic_friend_details_message.proto',
  package='pogoprotos.networking.requests.social.requests',
  syntax='proto3',
  serialized_pb=_b('\nWpogoprotos/networking/requests/social/requests/get_niantic_friend_details_message.proto\x12.pogoprotos.networking.requests.social.requests\"3\n\x1eGetNianticFriendDetailsMessage\x12\x11\n\tplayer_id\x18\x01 \x03(\tb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GETNIANTICFRIENDDETAILSMESSAGE = _descriptor.Descriptor(
  name='GetNianticFriendDetailsMessage',
  full_name='pogoprotos.networking.requests.social.requests.GetNianticFriendDetailsMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_id', full_name='pogoprotos.networking.requests.social.requests.GetNianticFriendDetailsMessage.player_id', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=139,
  serialized_end=190,
)

DESCRIPTOR.message_types_by_name['GetNianticFriendDetailsMessage'] = _GETNIANTICFRIENDDETAILSMESSAGE

GetNianticFriendDetailsMessage = _reflection.GeneratedProtocolMessageType('GetNianticFriendDetailsMessage', (_message.Message,), dict(
  DESCRIPTOR = _GETNIANTICFRIENDDETAILSMESSAGE,
  __module__ = 'pogoprotos.networking.requests.social.requests.get_niantic_friend_details_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.social.requests.GetNianticFriendDetailsMessage)
  ))
_sym_db.RegisterMessage(GetNianticFriendDetailsMessage)


# @@protoc_insertion_point(module_scope)
