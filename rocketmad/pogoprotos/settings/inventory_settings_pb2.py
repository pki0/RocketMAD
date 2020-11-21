# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/inventory_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/inventory_settings.proto',
  package='pogoprotos.settings',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n,pogoprotos/settings/inventory_settings.proto\x12\x13pogoprotos.settings\"\x90\x02\n\x11InventorySettings\x12\x13\n\x0bmax_pokemon\x18\x01 \x01(\x05\x12\x15\n\rmax_bag_items\x18\x02 \x01(\x05\x12\x14\n\x0c\x62\x61se_pokemon\x18\x03 \x01(\x05\x12\x16\n\x0e\x62\x61se_bag_items\x18\x04 \x01(\x05\x12\x11\n\tbase_eggs\x18\x05 \x01(\x05\x12\x18\n\x10max_team_changes\x18\x06 \x01(\x05\x12-\n%team_change_item_reset_period_in_days\x18\x07 \x01(\x03\x12\"\n\x1amax_item_boost_duration_ms\x18\x08 \x01(\x03\x12!\n\x19\x64\x65\x66\x61ult_sticker_max_count\x18\t \x01(\x05\x62\x06proto3')
)




_INVENTORYSETTINGS = _descriptor.Descriptor(
  name='InventorySettings',
  full_name='pogoprotos.settings.InventorySettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_pokemon', full_name='pogoprotos.settings.InventorySettings.max_pokemon', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_bag_items', full_name='pogoprotos.settings.InventorySettings.max_bag_items', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='base_pokemon', full_name='pogoprotos.settings.InventorySettings.base_pokemon', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='base_bag_items', full_name='pogoprotos.settings.InventorySettings.base_bag_items', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='base_eggs', full_name='pogoprotos.settings.InventorySettings.base_eggs', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_team_changes', full_name='pogoprotos.settings.InventorySettings.max_team_changes', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='team_change_item_reset_period_in_days', full_name='pogoprotos.settings.InventorySettings.team_change_item_reset_period_in_days', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_item_boost_duration_ms', full_name='pogoprotos.settings.InventorySettings.max_item_boost_duration_ms', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default_sticker_max_count', full_name='pogoprotos.settings.InventorySettings.default_sticker_max_count', index=8,
      number=9, type=5, cpp_type=1, label=1,
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
  serialized_start=70,
  serialized_end=342,
)

DESCRIPTOR.message_types_by_name['InventorySettings'] = _INVENTORYSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InventorySettings = _reflection.GeneratedProtocolMessageType('InventorySettings', (_message.Message,), dict(
  DESCRIPTOR = _INVENTORYSETTINGS,
  __module__ = 'pogoprotos.settings.inventory_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.InventorySettings)
  ))
_sym_db.RegisterMessage(InventorySettings)


# @@protoc_insertion_point(module_scope)
