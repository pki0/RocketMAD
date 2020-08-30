# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/trading/excluded_pokemon.proto

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
  name='pogoprotos/data/trading/excluded_pokemon.proto',
  package='pogoprotos.data.trading',
  syntax='proto3',
  serialized_pb=_b('\n.pogoprotos/data/trading/excluded_pokemon.proto\x12\x17pogoprotos.data.trading\"\xb3\x03\n\x0f\x45xcludedPokemon\x12\x12\n\npokemon_id\x18\x01 \x01(\x06\x12R\n\x10\x65xclusion_reason\x18\x02 \x01(\x0e\x32\x38.pogoprotos.data.trading.ExcludedPokemon.ExclusionReason\"\xb7\x02\n\x0f\x45xclusionReason\x12\t\n\x05UNSET\x10\x00\x12\x14\n\x10MYTHICAL_POKEMON\x10\x01\x12\x0b\n\x07SLASHED\x10\x02\x12\x10\n\x0cGYM_DEPLOYED\x10\x03\x12\t\n\x05\x42UDDY\x10\x04\x12\x14\n\x10STAMINA_NOT_FULL\x10\x05\x12\x13\n\x0f\x45GG_NOT_HATCHED\x10\x06\x12\x18\n\x14\x46RIENDSHIP_LEVEL_LOW\x10\x07\x12\x18\n\x14\x46RIEND_CANNOT_AFFORD\x10\x08\x12\x1e\n\x1a\x46RIEND_REACHED_DAILY_LIMIT\x10\t\x12\x12\n\x0e\x41LREADY_TRADED\x10\n\x12\x18\n\x14PLAYER_CANNOT_AFFORD\x10\x0b\x12\x1e\n\x1aPLAYER_REACHED_DAILY_LIMIT\x10\x0c\x12\x0c\n\x08\x46\x41VORITE\x10\rb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_EXCLUDEDPOKEMON_EXCLUSIONREASON = _descriptor.EnumDescriptor(
  name='ExclusionReason',
  full_name='pogoprotos.data.trading.ExcludedPokemon.ExclusionReason',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MYTHICAL_POKEMON', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SLASHED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GYM_DEPLOYED', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STAMINA_NOT_FULL', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EGG_NOT_HATCHED', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FRIENDSHIP_LEVEL_LOW', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FRIEND_CANNOT_AFFORD', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FRIEND_REACHED_DAILY_LIMIT', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALREADY_TRADED', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLAYER_CANNOT_AFFORD', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLAYER_REACHED_DAILY_LIMIT', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAVORITE', index=13, number=13,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=200,
  serialized_end=511,
)
_sym_db.RegisterEnumDescriptor(_EXCLUDEDPOKEMON_EXCLUSIONREASON)


_EXCLUDEDPOKEMON = _descriptor.Descriptor(
  name='ExcludedPokemon',
  full_name='pogoprotos.data.trading.ExcludedPokemon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon_id', full_name='pogoprotos.data.trading.ExcludedPokemon.pokemon_id', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exclusion_reason', full_name='pogoprotos.data.trading.ExcludedPokemon.exclusion_reason', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _EXCLUDEDPOKEMON_EXCLUSIONREASON,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=76,
  serialized_end=511,
)

_EXCLUDEDPOKEMON.fields_by_name['exclusion_reason'].enum_type = _EXCLUDEDPOKEMON_EXCLUSIONREASON
_EXCLUDEDPOKEMON_EXCLUSIONREASON.containing_type = _EXCLUDEDPOKEMON
DESCRIPTOR.message_types_by_name['ExcludedPokemon'] = _EXCLUDEDPOKEMON

ExcludedPokemon = _reflection.GeneratedProtocolMessageType('ExcludedPokemon', (_message.Message,), dict(
  DESCRIPTOR = _EXCLUDEDPOKEMON,
  __module__ = 'pogoprotos.data.trading.excluded_pokemon_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.trading.ExcludedPokemon)
  ))
_sym_db.RegisterMessage(ExcludedPokemon)


# @@protoc_insertion_point(module_scope)
