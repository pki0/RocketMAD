# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/check_photobomb_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/check_photobomb_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nEpogoprotos/networking/requests/messages/check_photobomb_message.proto\x12\'pogoprotos.networking.requests.messages\"1\n\x15\x43heckPhotobombMessage\x12\x18\n\x10photo_pokemon_id\x18\x01 \x01(\x06\x62\x06proto3')
)




_CHECKPHOTOBOMBMESSAGE = _descriptor.Descriptor(
  name='CheckPhotobombMessage',
  full_name='pogoprotos.networking.requests.messages.CheckPhotobombMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='photo_pokemon_id', full_name='pogoprotos.networking.requests.messages.CheckPhotobombMessage.photo_pokemon_id', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=114,
  serialized_end=163,
)

DESCRIPTOR.message_types_by_name['CheckPhotobombMessage'] = _CHECKPHOTOBOMBMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CheckPhotobombMessage = _reflection.GeneratedProtocolMessageType('CheckPhotobombMessage', (_message.Message,), dict(
  DESCRIPTOR = _CHECKPHOTOBOMBMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.check_photobomb_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.CheckPhotobombMessage)
  ))
_sym_db.RegisterMessage(CheckPhotobombMessage)


# @@protoc_insertion_point(module_scope)
