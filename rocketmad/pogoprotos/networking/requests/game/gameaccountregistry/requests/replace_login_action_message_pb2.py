# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/game/gameaccountregistry/requests/replace_login_action_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import identity_provider_pb2 as pogoprotos_dot_enums_dot_identity__provider__pb2
from pogoprotos.networking.requests.platform.requests import add_login_action_message_pb2 as pogoprotos_dot_networking_dot_requests_dot_platform_dot_requests_dot_add__login__action__message__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/game/gameaccountregistry/requests/replace_login_action_message.proto',
  package='pogoprotos.networking.requests.game.gameaccountregistry.requests',
  syntax='proto3',
  serialized_pb=_b('\ncpogoprotos/networking/requests/game/gameaccountregistry/requests/replace_login_action_message.proto\x12@pogoprotos.networking.requests.game.gameaccountregistry.requests\x1a(pogoprotos/enums/identity_provider.proto\x1aOpogoprotos/networking/requests/platform/requests/add_login_action_message.proto\"\xd9\x01\n\x19ReplaceLoginActionMessage\x12\x46\n\x1a\x65xisting_identity_provider\x18\x01 \x01(\x0e\x32\".pogoprotos.enums.IdentityProvider\x12Z\n\tnew_login\x18\x02 \x01(\x0b\x32G.pogoprotos.networking.requests.platform.requests.AddLoginActionMessage\x12\x18\n\x10\x61uth_provider_id\x18\x03 \x01(\tb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_identity__provider__pb2.DESCRIPTOR,pogoprotos_dot_networking_dot_requests_dot_platform_dot_requests_dot_add__login__action__message__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_REPLACELOGINACTIONMESSAGE = _descriptor.Descriptor(
  name='ReplaceLoginActionMessage',
  full_name='pogoprotos.networking.requests.game.gameaccountregistry.requests.ReplaceLoginActionMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='existing_identity_provider', full_name='pogoprotos.networking.requests.game.gameaccountregistry.requests.ReplaceLoginActionMessage.existing_identity_provider', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='new_login', full_name='pogoprotos.networking.requests.game.gameaccountregistry.requests.ReplaceLoginActionMessage.new_login', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='auth_provider_id', full_name='pogoprotos.networking.requests.game.gameaccountregistry.requests.ReplaceLoginActionMessage.auth_provider_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=293,
  serialized_end=510,
)

_REPLACELOGINACTIONMESSAGE.fields_by_name['existing_identity_provider'].enum_type = pogoprotos_dot_enums_dot_identity__provider__pb2._IDENTITYPROVIDER
_REPLACELOGINACTIONMESSAGE.fields_by_name['new_login'].message_type = pogoprotos_dot_networking_dot_requests_dot_platform_dot_requests_dot_add__login__action__message__pb2._ADDLOGINACTIONMESSAGE
DESCRIPTOR.message_types_by_name['ReplaceLoginActionMessage'] = _REPLACELOGINACTIONMESSAGE

ReplaceLoginActionMessage = _reflection.GeneratedProtocolMessageType('ReplaceLoginActionMessage', (_message.Message,), dict(
  DESCRIPTOR = _REPLACELOGINACTIONMESSAGE,
  __module__ = 'pogoprotos.networking.requests.game.gameaccountregistry.requests.replace_login_action_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.game.gameaccountregistry.requests.ReplaceLoginActionMessage)
  ))
_sym_db.RegisterMessage(ReplaceLoginActionMessage)


# @@protoc_insertion_point(module_scope)
