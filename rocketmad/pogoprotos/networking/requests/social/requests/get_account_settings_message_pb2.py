# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/social/requests/get_account_settings_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/social/requests/get_account_settings_message.proto',
  package='pogoprotos.networking.requests.social.requests',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nQpogoprotos/networking/requests/social/requests/get_account_settings_message.proto\x12.pogoprotos.networking.requests.social.requests\"\x1b\n\x19GetAccountSettingsMessageb\x06proto3')
)




_GETACCOUNTSETTINGSMESSAGE = _descriptor.Descriptor(
  name='GetAccountSettingsMessage',
  full_name='pogoprotos.networking.requests.social.requests.GetAccountSettingsMessage',
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
  serialized_start=133,
  serialized_end=160,
)

DESCRIPTOR.message_types_by_name['GetAccountSettingsMessage'] = _GETACCOUNTSETTINGSMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetAccountSettingsMessage = _reflection.GeneratedProtocolMessageType('GetAccountSettingsMessage', (_message.Message,), dict(
  DESCRIPTOR = _GETACCOUNTSETTINGSMESSAGE,
  __module__ = 'pogoprotos.networking.requests.social.requests.get_account_settings_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.social.requests.GetAccountSettingsMessage)
  ))
_sym_db.RegisterMessage(GetAccountSettingsMessage)


# @@protoc_insertion_point(module_scope)
