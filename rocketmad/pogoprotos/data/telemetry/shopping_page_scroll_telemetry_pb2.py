# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/telemetry/shopping_page_scroll_telemetry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/telemetry/shopping_page_scroll_telemetry.proto',
  package='pogoprotos.data.telemetry',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n>pogoprotos/data/telemetry/shopping_page_scroll_telemetry.proto\x12\x19pogoprotos.data.telemetry\"\x8b\x02\n\x1bShoppingPageScrollTelemetry\x12\x61\n\x0bscroll_type\x18\x01 \x01(\x0e\x32L.pogoprotos.data.telemetry.ShoppingPageScrollTelemetry.ShoppingPageScrollIds\x12\x12\n\nscroll_row\x18\x02 \x01(\x05\x12\x12\n\ntotal_rows\x18\x03 \x01(\x05\"a\n\x15ShoppingPageScrollIds\x12\'\n#UNDEFINED_SHOPPING_PAGE_SCROLL_TYPE\x10\x00\x12\x0f\n\x0bLAST_SCROLL\x10\x01\x12\x0e\n\nMAX_SCROLL\x10\x02\x62\x06proto3')
)



_SHOPPINGPAGESCROLLTELEMETRY_SHOPPINGPAGESCROLLIDS = _descriptor.EnumDescriptor(
  name='ShoppingPageScrollIds',
  full_name='pogoprotos.data.telemetry.ShoppingPageScrollTelemetry.ShoppingPageScrollIds',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED_SHOPPING_PAGE_SCROLL_TYPE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LAST_SCROLL', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAX_SCROLL', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=264,
  serialized_end=361,
)
_sym_db.RegisterEnumDescriptor(_SHOPPINGPAGESCROLLTELEMETRY_SHOPPINGPAGESCROLLIDS)


_SHOPPINGPAGESCROLLTELEMETRY = _descriptor.Descriptor(
  name='ShoppingPageScrollTelemetry',
  full_name='pogoprotos.data.telemetry.ShoppingPageScrollTelemetry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scroll_type', full_name='pogoprotos.data.telemetry.ShoppingPageScrollTelemetry.scroll_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scroll_row', full_name='pogoprotos.data.telemetry.ShoppingPageScrollTelemetry.scroll_row', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_rows', full_name='pogoprotos.data.telemetry.ShoppingPageScrollTelemetry.total_rows', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SHOPPINGPAGESCROLLTELEMETRY_SHOPPINGPAGESCROLLIDS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=94,
  serialized_end=361,
)

_SHOPPINGPAGESCROLLTELEMETRY.fields_by_name['scroll_type'].enum_type = _SHOPPINGPAGESCROLLTELEMETRY_SHOPPINGPAGESCROLLIDS
_SHOPPINGPAGESCROLLTELEMETRY_SHOPPINGPAGESCROLLIDS.containing_type = _SHOPPINGPAGESCROLLTELEMETRY
DESCRIPTOR.message_types_by_name['ShoppingPageScrollTelemetry'] = _SHOPPINGPAGESCROLLTELEMETRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ShoppingPageScrollTelemetry = _reflection.GeneratedProtocolMessageType('ShoppingPageScrollTelemetry', (_message.Message,), dict(
  DESCRIPTOR = _SHOPPINGPAGESCROLLTELEMETRY,
  __module__ = 'pogoprotos.data.telemetry.shopping_page_scroll_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.ShoppingPageScrollTelemetry)
  ))
_sym_db.RegisterMessage(ShoppingPageScrollTelemetry)


# @@protoc_insertion_point(module_scope)
