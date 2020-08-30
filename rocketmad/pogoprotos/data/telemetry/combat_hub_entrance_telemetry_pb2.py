# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/telemetry/combat_hub_entrance_telemetry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import telemetry_ids_pb2 as pogoprotos_dot_enums_dot_telemetry__ids__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/telemetry/combat_hub_entrance_telemetry.proto',
  package='pogoprotos.data.telemetry',
  syntax='proto3',
  serialized_pb=_b('\n=pogoprotos/data/telemetry/combat_hub_entrance_telemetry.proto\x12\x19pogoprotos.data.telemetry\x1a$pogoprotos/enums/telemetry_ids.proto\"n\n\x1a\x43ombatHubEntranceTelemetry\x12P\n\x17\x63ombat_hub_telemetry_id\x18\x01 \x01(\x0e\x32/.pogoprotos.enums.CombatHubEntranceTelemetryIdsb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_telemetry__ids__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_COMBATHUBENTRANCETELEMETRY = _descriptor.Descriptor(
  name='CombatHubEntranceTelemetry',
  full_name='pogoprotos.data.telemetry.CombatHubEntranceTelemetry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='combat_hub_telemetry_id', full_name='pogoprotos.data.telemetry.CombatHubEntranceTelemetry.combat_hub_telemetry_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
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
  serialized_start=130,
  serialized_end=240,
)

_COMBATHUBENTRANCETELEMETRY.fields_by_name['combat_hub_telemetry_id'].enum_type = pogoprotos_dot_enums_dot_telemetry__ids__pb2._COMBATHUBENTRANCETELEMETRYIDS
DESCRIPTOR.message_types_by_name['CombatHubEntranceTelemetry'] = _COMBATHUBENTRANCETELEMETRY

CombatHubEntranceTelemetry = _reflection.GeneratedProtocolMessageType('CombatHubEntranceTelemetry', (_message.Message,), dict(
  DESCRIPTOR = _COMBATHUBENTRANCETELEMETRY,
  __module__ = 'pogoprotos.data.telemetry.combat_hub_entrance_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.CombatHubEntranceTelemetry)
  ))
_sym_db.RegisterMessage(CombatHubEntranceTelemetry)


# @@protoc_insertion_point(module_scope)
