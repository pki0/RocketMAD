# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/buddy/buddy_encounter_help_telemetry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import encounter_type_pb2 as pogoprotos_dot_enums_dot_encounter__type__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/buddy/buddy_encounter_help_telemetry.proto',
  package='pogoprotos.data.buddy',
  syntax='proto3',
  serialized_pb=_b('\n:pogoprotos/data/buddy/buddy_encounter_help_telemetry.proto\x12\x15pogoprotos.data.buddy\x1a%pogoprotos/enums/encounter_type.proto\"\xbe\x01\n\x1b\x42uddyEncounterHelpTelemetry\x12\x12\n\npokemon_id\x18\x01 \x01(\x05\x12\n\n\x02\x63p\x18\x02 \x01(\x05\x12\x16\n\x0e\x65ncounter_type\x18\x03 \x01(\t\x12\x1a\n\x12\x61r_classic_enabled\x18\x04 \x01(\x08\x12\x17\n\x0f\x61r_plus_enabled\x18\x05 \x01(\x08\x12\x32\n\tencounter\x18\x06 \x01(\x0e\x32\x1f.pogoprotos.enums.EncounterTypeb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_encounter__type__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_BUDDYENCOUNTERHELPTELEMETRY = _descriptor.Descriptor(
  name='BuddyEncounterHelpTelemetry',
  full_name='pogoprotos.data.buddy.BuddyEncounterHelpTelemetry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon_id', full_name='pogoprotos.data.buddy.BuddyEncounterHelpTelemetry.pokemon_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cp', full_name='pogoprotos.data.buddy.BuddyEncounterHelpTelemetry.cp', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encounter_type', full_name='pogoprotos.data.buddy.BuddyEncounterHelpTelemetry.encounter_type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ar_classic_enabled', full_name='pogoprotos.data.buddy.BuddyEncounterHelpTelemetry.ar_classic_enabled', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ar_plus_enabled', full_name='pogoprotos.data.buddy.BuddyEncounterHelpTelemetry.ar_plus_enabled', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encounter', full_name='pogoprotos.data.buddy.BuddyEncounterHelpTelemetry.encounter', index=5,
      number=6, type=14, cpp_type=8, label=1,
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
  serialized_start=125,
  serialized_end=315,
)

_BUDDYENCOUNTERHELPTELEMETRY.fields_by_name['encounter'].enum_type = pogoprotos_dot_enums_dot_encounter__type__pb2._ENCOUNTERTYPE
DESCRIPTOR.message_types_by_name['BuddyEncounterHelpTelemetry'] = _BUDDYENCOUNTERHELPTELEMETRY

BuddyEncounterHelpTelemetry = _reflection.GeneratedProtocolMessageType('BuddyEncounterHelpTelemetry', (_message.Message,), dict(
  DESCRIPTOR = _BUDDYENCOUNTERHELPTELEMETRY,
  __module__ = 'pogoprotos.data.buddy.buddy_encounter_help_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.buddy.BuddyEncounterHelpTelemetry)
  ))
_sym_db.RegisterMessage(BuddyEncounterHelpTelemetry)


# @@protoc_insertion_point(module_scope)
