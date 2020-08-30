# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/gift/gift_box.proto

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
  name='pogoprotos/data/gift/gift_box.proto',
  package='pogoprotos.data.gift',
  syntax='proto3',
  serialized_pb=_b('\n#pogoprotos/data/gift/gift_box.proto\x12\x14pogoprotos.data.gift\"\xc3\x01\n\x07GiftBox\x12\x12\n\ngiftbox_id\x18\x01 \x01(\x04\x12\x11\n\tsender_id\x18\x02 \x01(\t\x12\x13\n\x0breceiver_id\x18\x03 \x01(\t\x12\x0f\n\x07\x66ort_id\x18\x04 \x01(\t\x12\x10\n\x08\x66ort_lat\x18\x05 \x01(\x01\x12\x10\n\x08\x66ort_lng\x18\x06 \x01(\x01\x12\x1a\n\x12\x63reation_timestamp\x18\x07 \x01(\x03\x12\x16\n\x0esent_timestamp\x18\x08 \x01(\x03\x12\x13\n\x0bsent_bucket\x18\t \x01(\x03\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GIFTBOX = _descriptor.Descriptor(
  name='GiftBox',
  full_name='pogoprotos.data.gift.GiftBox',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='giftbox_id', full_name='pogoprotos.data.gift.GiftBox.giftbox_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sender_id', full_name='pogoprotos.data.gift.GiftBox.sender_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='receiver_id', full_name='pogoprotos.data.gift.GiftBox.receiver_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fort_id', full_name='pogoprotos.data.gift.GiftBox.fort_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fort_lat', full_name='pogoprotos.data.gift.GiftBox.fort_lat', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fort_lng', full_name='pogoprotos.data.gift.GiftBox.fort_lng', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='creation_timestamp', full_name='pogoprotos.data.gift.GiftBox.creation_timestamp', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sent_timestamp', full_name='pogoprotos.data.gift.GiftBox.sent_timestamp', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sent_bucket', full_name='pogoprotos.data.gift.GiftBox.sent_bucket', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=62,
  serialized_end=257,
)

DESCRIPTOR.message_types_by_name['GiftBox'] = _GIFTBOX

GiftBox = _reflection.GeneratedProtocolMessageType('GiftBox', (_message.Message,), dict(
  DESCRIPTOR = _GIFTBOX,
  __module__ = 'pogoprotos.data.gift.gift_box_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.gift.GiftBox)
  ))
_sym_db.RegisterMessage(GiftBox)


# @@protoc_insertion_point(module_scope)
