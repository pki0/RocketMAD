# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/incident_global_settings.proto

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
  name='pogoprotos/settings/incident_global_settings.proto',
  package='pogoprotos.settings',
  syntax='proto3',
  serialized_pb=_b('\n2pogoprotos/settings/incident_global_settings.proto\x12\x13pogoprotos.settings\"S\n\x16IncidentGlobalSettings\x12\x18\n\x10min_player_level\x18\x01 \x01(\x05\x12\x1f\n\x17min_player_level_for_v2\x18\x02 \x01(\x05\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_INCIDENTGLOBALSETTINGS = _descriptor.Descriptor(
  name='IncidentGlobalSettings',
  full_name='pogoprotos.settings.IncidentGlobalSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min_player_level', full_name='pogoprotos.settings.IncidentGlobalSettings.min_player_level', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_player_level_for_v2', full_name='pogoprotos.settings.IncidentGlobalSettings.min_player_level_for_v2', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=75,
  serialized_end=158,
)

DESCRIPTOR.message_types_by_name['IncidentGlobalSettings'] = _INCIDENTGLOBALSETTINGS

IncidentGlobalSettings = _reflection.GeneratedProtocolMessageType('IncidentGlobalSettings', (_message.Message,), dict(
  DESCRIPTOR = _INCIDENTGLOBALSETTINGS,
  __module__ = 'pogoprotos.settings.incident_global_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.IncidentGlobalSettings)
  ))
_sym_db.RegisterMessage(IncidentGlobalSettings)


# @@protoc_insertion_point(module_scope)
