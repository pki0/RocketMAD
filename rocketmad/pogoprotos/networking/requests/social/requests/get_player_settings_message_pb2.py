# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/social/requests/get_player_settings_message.proto

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
  name='pogoprotos/networking/requests/social/requests/get_player_settings_message.proto',
  package='pogoprotos.networking.requests.social.requests',
  syntax='proto3',
  serialized_pb=_b('\nPpogoprotos/networking/requests/social/requests/get_player_settings_message.proto\x12.pogoprotos.networking.requests.social.requests\"\x1a\n\x18GetPlayerSettingsMessageb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GETPLAYERSETTINGSMESSAGE = _descriptor.Descriptor(
  name='GetPlayerSettingsMessage',
  full_name='pogoprotos.networking.requests.social.requests.GetPlayerSettingsMessage',
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=132,
  serialized_end=158,
)

DESCRIPTOR.message_types_by_name['GetPlayerSettingsMessage'] = _GETPLAYERSETTINGSMESSAGE

GetPlayerSettingsMessage = _reflection.GeneratedProtocolMessageType('GetPlayerSettingsMessage', (_message.Message,), dict(
  DESCRIPTOR = _GETPLAYERSETTINGSMESSAGE,
  __module__ = 'pogoprotos.networking.requests.social.requests.get_player_settings_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.social.requests.GetPlayerSettingsMessage)
  ))
_sym_db.RegisterMessage(GetPlayerSettingsMessage)


# @@protoc_insertion_point(module_scope)
