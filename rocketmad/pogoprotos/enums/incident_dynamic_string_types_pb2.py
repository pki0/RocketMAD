# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/incident_dynamic_string_types.proto

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
  name='pogoprotos/enums/incident_dynamic_string_types.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n4pogoprotos/enums/incident_dynamic_string_types.proto\x12\x10pogoprotos.enums*\x8b\x02\n\x1aIncidentDynamicStringTypes\x12\x0c\n\x08GREETING\x10\x00\x12\r\n\tCHALLENGE\x10\x01\x12\n\n\x06\x44\x45\x46\x45\x41T\x10\x02\x12\x0b\n\x07VICTORY\x10\x03\x12\x0e\n\nPRE_BATTLE\x10\x04\x12\x0f\n\x0bPOST_BATTLE\x10\x05\x12\x10\n\x0cITEMS_STOLEN\x10\x06\x12\x0c\n\x08TUTORIAL\x10\x07\x12\x10\n\x0c\x43OMBAT_QUOTE\x10\x08\x12\x13\n\x0f\x43\x41NDELA_INSPIRE\x10\t\x12\x13\n\x0f\x42LANCHE_INSPIRE\x10\n\x12\x11\n\rSPARK_INSPIRE\x10\x0b\x12\x0f\n\x0bGRUNT_DECOY\x10\x0c\x12\x16\n\x12\x43OMBAT_DECOY_QUOTE\x10\rb\x06proto3')
)

_INCIDENTDYNAMICSTRINGTYPES = _descriptor.EnumDescriptor(
  name='IncidentDynamicStringTypes',
  full_name='pogoprotos.enums.IncidentDynamicStringTypes',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GREETING', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHALLENGE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEFEAT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VICTORY', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRE_BATTLE', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POST_BATTLE', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEMS_STOLEN', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TUTORIAL', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMBAT_QUOTE', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANDELA_INSPIRE', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLANCHE_INSPIRE', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPARK_INSPIRE', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GRUNT_DECOY', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMBAT_DECOY_QUOTE', index=13, number=13,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=75,
  serialized_end=342,
)
_sym_db.RegisterEnumDescriptor(_INCIDENTDYNAMICSTRINGTYPES)

IncidentDynamicStringTypes = enum_type_wrapper.EnumTypeWrapper(_INCIDENTDYNAMICSTRINGTYPES)
GREETING = 0
CHALLENGE = 1
DEFEAT = 2
VICTORY = 3
PRE_BATTLE = 4
POST_BATTLE = 5
ITEMS_STOLEN = 6
TUTORIAL = 7
COMBAT_QUOTE = 8
CANDELA_INSPIRE = 9
BLANCHE_INSPIRE = 10
SPARK_INSPIRE = 11
GRUNT_DECOY = 12
COMBAT_DECOY_QUOTE = 13


DESCRIPTOR.enum_types_by_name['IncidentDynamicStringTypes'] = _INCIDENTDYNAMICSTRINGTYPES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
