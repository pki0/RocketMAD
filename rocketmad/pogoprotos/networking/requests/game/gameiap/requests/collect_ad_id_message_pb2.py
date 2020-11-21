# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/game/gameiap/requests/collect_ad_id_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/game/gameiap/requests/collect_ad_id_message.proto',
  package='pogoprotos.networking.requests.game.gameiap.requests',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nPpogoprotos/networking/requests/game/gameiap/requests/collect_ad_id_message.proto\x12\x34pogoprotos.networking.requests.game.gameiap.requests\"\xba\x03\n\x12\x43ollectAdIdMessage\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\r\n\x05\x61\x64_id\x18\x02 \x01(\t\x12p\n\x0f\x64\x65vice_platform\x18\x03 \x01(\x0e\x32W.pogoprotos.networking.requests.game.gameiap.requests.CollectAdIdMessage.DevicePlatform\x12v\n\rfailed_reason\x18\x04 \x01(\x0e\x32_.pogoprotos.networking.requests.game.gameiap.requests.CollectAdIdMessage.CollectionFailedReason\x12\x14\n\x0ctimestamp_ms\x18\x05 \x01(\x04\"F\n\x16\x43ollectionFailedReason\x12\x12\n\x0eREASON_INVALID\x10\x00\x12\x18\n\x14\x41\x44_TRACKING_DISABLED\x10\x01\"<\n\x0e\x44\x65vicePlatform\x12\x14\n\x10PLATFORM_INVALID\x10\x00\x12\x0b\n\x07\x41NDROID\x10\x01\x12\x07\n\x03IOS\x10\x02\x62\x06proto3')
)



_COLLECTADIDMESSAGE_COLLECTIONFAILEDREASON = _descriptor.EnumDescriptor(
  name='CollectionFailedReason',
  full_name='pogoprotos.networking.requests.game.gameiap.requests.CollectAdIdMessage.CollectionFailedReason',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='REASON_INVALID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AD_TRACKING_DISABLED', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=449,
  serialized_end=519,
)
_sym_db.RegisterEnumDescriptor(_COLLECTADIDMESSAGE_COLLECTIONFAILEDREASON)

_COLLECTADIDMESSAGE_DEVICEPLATFORM = _descriptor.EnumDescriptor(
  name='DevicePlatform',
  full_name='pogoprotos.networking.requests.game.gameiap.requests.CollectAdIdMessage.DevicePlatform',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PLATFORM_INVALID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ANDROID', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IOS', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=521,
  serialized_end=581,
)
_sym_db.RegisterEnumDescriptor(_COLLECTADIDMESSAGE_DEVICEPLATFORM)


_COLLECTADIDMESSAGE = _descriptor.Descriptor(
  name='CollectAdIdMessage',
  full_name='pogoprotos.networking.requests.game.gameiap.requests.CollectAdIdMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='pogoprotos.networking.requests.game.gameiap.requests.CollectAdIdMessage.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ad_id', full_name='pogoprotos.networking.requests.game.gameiap.requests.CollectAdIdMessage.ad_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_platform', full_name='pogoprotos.networking.requests.game.gameiap.requests.CollectAdIdMessage.device_platform', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='failed_reason', full_name='pogoprotos.networking.requests.game.gameiap.requests.CollectAdIdMessage.failed_reason', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp_ms', full_name='pogoprotos.networking.requests.game.gameiap.requests.CollectAdIdMessage.timestamp_ms', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _COLLECTADIDMESSAGE_COLLECTIONFAILEDREASON,
    _COLLECTADIDMESSAGE_DEVICEPLATFORM,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=139,
  serialized_end=581,
)

_COLLECTADIDMESSAGE.fields_by_name['device_platform'].enum_type = _COLLECTADIDMESSAGE_DEVICEPLATFORM
_COLLECTADIDMESSAGE.fields_by_name['failed_reason'].enum_type = _COLLECTADIDMESSAGE_COLLECTIONFAILEDREASON
_COLLECTADIDMESSAGE_COLLECTIONFAILEDREASON.containing_type = _COLLECTADIDMESSAGE
_COLLECTADIDMESSAGE_DEVICEPLATFORM.containing_type = _COLLECTADIDMESSAGE
DESCRIPTOR.message_types_by_name['CollectAdIdMessage'] = _COLLECTADIDMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CollectAdIdMessage = _reflection.GeneratedProtocolMessageType('CollectAdIdMessage', (_message.Message,), dict(
  DESCRIPTOR = _COLLECTADIDMESSAGE,
  __module__ = 'pogoprotos.networking.requests.game.gameiap.requests.collect_ad_id_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.game.gameiap.requests.CollectAdIdMessage)
  ))
_sym_db.RegisterMessage(CollectAdIdMessage)


# @@protoc_insertion_point(module_scope)
