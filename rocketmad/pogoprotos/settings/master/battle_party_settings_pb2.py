# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/battle_party_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/master/battle_party_settings.proto',
  package='pogoprotos.settings.master',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n6pogoprotos/settings/master/battle_party_settings.proto\x12\x1apogoprotos.settings.master\"r\n\x13\x42\x61ttlePartySettings\x12\"\n\x1a\x65nable_battle_party_saving\x18\x01 \x01(\x08\x12\x1a\n\x12max_battle_parties\x18\x02 \x01(\x05\x12\x1b\n\x13overall_parties_cap\x18\x03 \x01(\x05\x62\x06proto3')
)




_BATTLEPARTYSETTINGS = _descriptor.Descriptor(
  name='BattlePartySettings',
  full_name='pogoprotos.settings.master.BattlePartySettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enable_battle_party_saving', full_name='pogoprotos.settings.master.BattlePartySettings.enable_battle_party_saving', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_battle_parties', full_name='pogoprotos.settings.master.BattlePartySettings.max_battle_parties', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='overall_parties_cap', full_name='pogoprotos.settings.master.BattlePartySettings.overall_parties_cap', index=2,
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
  serialized_start=86,
  serialized_end=200,
)

DESCRIPTOR.message_types_by_name['BattlePartySettings'] = _BATTLEPARTYSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BattlePartySettings = _reflection.GeneratedProtocolMessageType('BattlePartySettings', (_message.Message,), dict(
  DESCRIPTOR = _BATTLEPARTYSETTINGS,
  __module__ = 'pogoprotos.settings.master.battle_party_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.BattlePartySettings)
  ))
_sym_db.RegisterMessage(BattlePartySettings)


# @@protoc_insertion_point(module_scope)
