# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/evolve_pokemon_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.inventory.item import item_id_pb2 as pogoprotos_dot_inventory_dot_item_dot_item__id__pb2
from pogoprotos.enums import pokemon_id_pb2 as pogoprotos_dot_enums_dot_pokemon__id__pb2
from pogoprotos.enums import form_pb2 as pogoprotos_dot_enums_dot_form__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/evolve_pokemon_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nDpogoprotos/networking/requests/messages/evolve_pokemon_message.proto\x12\'pogoprotos.networking.requests.messages\x1a\'pogoprotos/inventory/item/item_id.proto\x1a!pogoprotos/enums/pokemon_id.proto\x1a\x1bpogoprotos/enums/form.proto\"\xf3\x01\n\x14\x45volvePokemonMessage\x12\x12\n\npokemon_id\x18\x01 \x01(\x06\x12\x45\n\x1a\x65volution_item_requirement\x18\x02 \x01(\x0e\x32!.pogoprotos.inventory.item.ItemId\x12\x36\n\x11target_pokemon_id\x18\x03 \x01(\x0e\x32\x1b.pogoprotos.enums.PokemonId\x12\x33\n\x13target_pokemon_form\x18\x04 \x01(\x0e\x32\x16.pogoprotos.enums.Form\x12\x13\n\x0buse_special\x18\x05 \x01(\x08\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_inventory_dot_item_dot_item__id__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_pokemon__id__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_form__pb2.DESCRIPTOR,])




_EVOLVEPOKEMONMESSAGE = _descriptor.Descriptor(
  name='EvolvePokemonMessage',
  full_name='pogoprotos.networking.requests.messages.EvolvePokemonMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon_id', full_name='pogoprotos.networking.requests.messages.EvolvePokemonMessage.pokemon_id', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='evolution_item_requirement', full_name='pogoprotos.networking.requests.messages.EvolvePokemonMessage.evolution_item_requirement', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_pokemon_id', full_name='pogoprotos.networking.requests.messages.EvolvePokemonMessage.target_pokemon_id', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_pokemon_form', full_name='pogoprotos.networking.requests.messages.EvolvePokemonMessage.target_pokemon_form', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='use_special', full_name='pogoprotos.networking.requests.messages.EvolvePokemonMessage.use_special', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=219,
  serialized_end=462,
)

_EVOLVEPOKEMONMESSAGE.fields_by_name['evolution_item_requirement'].enum_type = pogoprotos_dot_inventory_dot_item_dot_item__id__pb2._ITEMID
_EVOLVEPOKEMONMESSAGE.fields_by_name['target_pokemon_id'].enum_type = pogoprotos_dot_enums_dot_pokemon__id__pb2._POKEMONID
_EVOLVEPOKEMONMESSAGE.fields_by_name['target_pokemon_form'].enum_type = pogoprotos_dot_enums_dot_form__pb2._FORM
DESCRIPTOR.message_types_by_name['EvolvePokemonMessage'] = _EVOLVEPOKEMONMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EvolvePokemonMessage = _reflection.GeneratedProtocolMessageType('EvolvePokemonMessage', (_message.Message,), dict(
  DESCRIPTOR = _EVOLVEPOKEMONMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.evolve_pokemon_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.EvolvePokemonMessage)
  ))
_sym_db.RegisterMessage(EvolvePokemonMessage)


# @@protoc_insertion_point(module_scope)
