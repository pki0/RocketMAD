# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/telemetry/common_telemetry_shop_view.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/telemetry/common_telemetry_shop_view.proto',
  package='pogoprotos.data.telemetry',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n:pogoprotos/data/telemetry/common_telemetry_shop_view.proto\x12\x19pogoprotos.data.telemetry\"\xbf\x01\n\x17\x43ommonTelemetryShopView\x12\"\n\x1ashopping_page_view_type_id\x18\x01 \x01(\t\x12\x1f\n\x17view_start_timestamp_ms\x18\x02 \x01(\x03\x12\x1d\n\x15view_end_timestamp_ms\x18\x03 \x01(\x03\x12\x1c\n\x14\x63onsolidated_item_id\x18\x04 \x03(\t\x12\"\n\x1aroot_store_page_session_id\x18\x05 \x01(\tb\x06proto3')
)




_COMMONTELEMETRYSHOPVIEW = _descriptor.Descriptor(
  name='CommonTelemetryShopView',
  full_name='pogoprotos.data.telemetry.CommonTelemetryShopView',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shopping_page_view_type_id', full_name='pogoprotos.data.telemetry.CommonTelemetryShopView.shopping_page_view_type_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='view_start_timestamp_ms', full_name='pogoprotos.data.telemetry.CommonTelemetryShopView.view_start_timestamp_ms', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='view_end_timestamp_ms', full_name='pogoprotos.data.telemetry.CommonTelemetryShopView.view_end_timestamp_ms', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='consolidated_item_id', full_name='pogoprotos.data.telemetry.CommonTelemetryShopView.consolidated_item_id', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='root_store_page_session_id', full_name='pogoprotos.data.telemetry.CommonTelemetryShopView.root_store_page_session_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=90,
  serialized_end=281,
)

DESCRIPTOR.message_types_by_name['CommonTelemetryShopView'] = _COMMONTELEMETRYSHOPVIEW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CommonTelemetryShopView = _reflection.GeneratedProtocolMessageType('CommonTelemetryShopView', (_message.Message,), dict(
  DESCRIPTOR = _COMMONTELEMETRYSHOPVIEW,
  __module__ = 'pogoprotos.data.telemetry.common_telemetry_shop_view_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.CommonTelemetryShopView)
  ))
_sym_db.RegisterMessage(CommonTelemetryShopView)


# @@protoc_insertion_point(module_scope)
