# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/pokedex_generation_id.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/enums/pokedex_generation_id.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n,pogoprotos/enums/pokedex_generation_id.proto\x12\x10pogoprotos.enums*\xb7\x01\n\x13PokedexGenerationId\x12\x08\n\x04GEN1\x10\x00\x12\x08\n\x04GEN2\x10\x01\x12\x08\n\x04GEN3\x10\x02\x12\x08\n\x04GEN4\x10\x03\x12\x08\n\x04GEN5\x10\x04\x12\x08\n\x04GEN6\x10\x05\x12\x08\n\x04GEN7\x10\x06\x12\x08\n\x04GEN8\x10\x07\x12\x1a\n\x15POKEDEX_GEN_ID_MELTAN\x10\xe9\x07\x12\x1b\n\x16POKEDEX_GEN_ID_MEGAEVO\x10\xea\x07\x12\x17\n\x12POKEDEX_GEN_ID_ALL\x10\x89\'b\x06proto3')
)

_POKEDEXGENERATIONID = _descriptor.EnumDescriptor(
  name='PokedexGenerationId',
  full_name='pogoprotos.enums.PokedexGenerationId',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GEN1', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GEN2', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GEN3', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GEN4', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GEN5', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GEN6', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GEN7', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GEN8', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEDEX_GEN_ID_MELTAN', index=8, number=1001,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEDEX_GEN_ID_MEGAEVO', index=9, number=1002,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEDEX_GEN_ID_ALL', index=10, number=5001,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=67,
  serialized_end=250,
)
_sym_db.RegisterEnumDescriptor(_POKEDEXGENERATIONID)

PokedexGenerationId = enum_type_wrapper.EnumTypeWrapper(_POKEDEXGENERATIONID)
GEN1 = 0
GEN2 = 1
GEN3 = 2
GEN4 = 3
GEN5 = 4
GEN6 = 5
GEN7 = 6
GEN8 = 7
POKEDEX_GEN_ID_MELTAN = 1001
POKEDEX_GEN_ID_MEGAEVO = 1002
POKEDEX_GEN_ID_ALL = 5001


DESCRIPTOR.enum_types_by_name['PokedexGenerationId'] = _POKEDEXGENERATIONID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
