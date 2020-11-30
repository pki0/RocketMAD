# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/inventory/candy.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import pokemon_family_id_pb2 as pogoprotos_dot_enums_dot_pokemon__family__id__pb2
from pogoprotos.enums import temporary_evolution_id_pb2 as pogoprotos_dot_enums_dot_temporary__evolution__id__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/inventory/candy.proto',
  package='pogoprotos.inventory',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n pogoprotos/inventory/candy.proto\x12\x14pogoprotos.inventory\x1a(pogoprotos/enums/pokemon_family_id.proto\x1a-pogoprotos/enums/temporary_evolution_id.proto\"\xcf\x02\n\x05\x43\x61ndy\x12\x34\n\tfamily_id\x18\x01 \x01(\x0e\x32!.pogoprotos.enums.PokemonFamilyId\x12\r\n\x05\x63\x61ndy\x18\x02 \x01(\x05\x12X\n\x18mega_evolution_resources\x18\x03 \x03(\x0b\x32\x36.pogoprotos.inventory.Candy.TemporaryEvolutionResource\x12\x10\n\x08xl_candy\x18\x04 \x01(\x05\x1a\x94\x01\n\x1aTemporaryEvolutionResource\x12\x46\n\x16temporary_evolution_id\x18\x01 \x01(\x0e\x32&.pogoprotos.enums.TemporaryEvolutionId\x12\x14\n\x0c\x65nergy_count\x18\x02 \x01(\x05\x12\x18\n\x10max_energy_count\x18\x03 \x01(\x05\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_pokemon__family__id__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_temporary__evolution__id__pb2.DESCRIPTOR,])




_CANDY_TEMPORARYEVOLUTIONRESOURCE = _descriptor.Descriptor(
  name='TemporaryEvolutionResource',
  full_name='pogoprotos.inventory.Candy.TemporaryEvolutionResource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='temporary_evolution_id', full_name='pogoprotos.inventory.Candy.TemporaryEvolutionResource.temporary_evolution_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='energy_count', full_name='pogoprotos.inventory.Candy.TemporaryEvolutionResource.energy_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_energy_count', full_name='pogoprotos.inventory.Candy.TemporaryEvolutionResource.max_energy_count', index=2,
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
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=335,
  serialized_end=483,
)

_CANDY = _descriptor.Descriptor(
  name='Candy',
  full_name='pogoprotos.inventory.Candy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='family_id', full_name='pogoprotos.inventory.Candy.family_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='candy', full_name='pogoprotos.inventory.Candy.candy', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mega_evolution_resources', full_name='pogoprotos.inventory.Candy.mega_evolution_resources', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='xl_candy', full_name='pogoprotos.inventory.Candy.xl_candy', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CANDY_TEMPORARYEVOLUTIONRESOURCE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=148,
  serialized_end=483,
)

_CANDY_TEMPORARYEVOLUTIONRESOURCE.fields_by_name['temporary_evolution_id'].enum_type = pogoprotos_dot_enums_dot_temporary__evolution__id__pb2._TEMPORARYEVOLUTIONID
_CANDY_TEMPORARYEVOLUTIONRESOURCE.containing_type = _CANDY
_CANDY.fields_by_name['family_id'].enum_type = pogoprotos_dot_enums_dot_pokemon__family__id__pb2._POKEMONFAMILYID
_CANDY.fields_by_name['mega_evolution_resources'].message_type = _CANDY_TEMPORARYEVOLUTIONRESOURCE
DESCRIPTOR.message_types_by_name['Candy'] = _CANDY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Candy = _reflection.GeneratedProtocolMessageType('Candy', (_message.Message,), dict(

  TemporaryEvolutionResource = _reflection.GeneratedProtocolMessageType('TemporaryEvolutionResource', (_message.Message,), dict(
    DESCRIPTOR = _CANDY_TEMPORARYEVOLUTIONRESOURCE,
    __module__ = 'pogoprotos.inventory.candy_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.inventory.Candy.TemporaryEvolutionResource)
    ))
  ,
  DESCRIPTOR = _CANDY,
  __module__ = 'pogoprotos.inventory.candy_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.inventory.Candy)
  ))
_sym_db.RegisterMessage(Candy)
_sym_db.RegisterMessage(Candy.TemporaryEvolutionResource)


# @@protoc_insertion_point(module_scope)
