# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/inventory/egg_incubator.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.inventory.item import item_id_pb2 as pogoprotos_dot_inventory_dot_item_dot_item__id__pb2
from pogoprotos.inventory import egg_incubator_type_pb2 as pogoprotos_dot_inventory_dot_egg__incubator__type__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/inventory/egg_incubator.proto',
  package='pogoprotos.inventory',
  syntax='proto3',
  serialized_pb=_b('\n(pogoprotos/inventory/egg_incubator.proto\x12\x14pogoprotos.inventory\x1a\'pogoprotos/inventory/item/item_id.proto\x1a-pogoprotos/inventory/egg_incubator_type.proto\"\xed\x01\n\x0c\x45ggIncubator\x12\n\n\x02id\x18\x01 \x01(\t\x12\x32\n\x07item_id\x18\x02 \x01(\x0e\x32!.pogoprotos.inventory.item.ItemId\x12>\n\x0eincubator_type\x18\x03 \x01(\x0e\x32&.pogoprotos.inventory.EggIncubatorType\x12\x16\n\x0euses_remaining\x18\x04 \x01(\x05\x12\x12\n\npokemon_id\x18\x05 \x01(\x03\x12\x17\n\x0fstart_km_walked\x18\x06 \x01(\x01\x12\x18\n\x10target_km_walked\x18\x07 \x01(\x01\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_inventory_dot_item_dot_item__id__pb2.DESCRIPTOR,pogoprotos_dot_inventory_dot_egg__incubator__type__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_EGGINCUBATOR = _descriptor.Descriptor(
  name='EggIncubator',
  full_name='pogoprotos.inventory.EggIncubator',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='pogoprotos.inventory.EggIncubator.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_id', full_name='pogoprotos.inventory.EggIncubator.item_id', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='incubator_type', full_name='pogoprotos.inventory.EggIncubator.incubator_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uses_remaining', full_name='pogoprotos.inventory.EggIncubator.uses_remaining', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_id', full_name='pogoprotos.inventory.EggIncubator.pokemon_id', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_km_walked', full_name='pogoprotos.inventory.EggIncubator.start_km_walked', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_km_walked', full_name='pogoprotos.inventory.EggIncubator.target_km_walked', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=155,
  serialized_end=392,
)

_EGGINCUBATOR.fields_by_name['item_id'].enum_type = pogoprotos_dot_inventory_dot_item_dot_item__id__pb2._ITEMID
_EGGINCUBATOR.fields_by_name['incubator_type'].enum_type = pogoprotos_dot_inventory_dot_egg__incubator__type__pb2._EGGINCUBATORTYPE
DESCRIPTOR.message_types_by_name['EggIncubator'] = _EGGINCUBATOR

EggIncubator = _reflection.GeneratedProtocolMessageType('EggIncubator', (_message.Message,), dict(
  DESCRIPTOR = _EGGINCUBATOR,
  __module__ = 'pogoprotos.inventory.egg_incubator_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.inventory.EggIncubator)
  ))
_sym_db.RegisterMessage(EggIncubator)


# @@protoc_insertion_point(module_scope)
