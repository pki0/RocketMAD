# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/platform/requests/update_adventure_sync_settings_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.settings import adventure_sync_settings_pb2 as pogoprotos_dot_settings_dot_adventure__sync__settings__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/platform/requests/update_adventure_sync_settings_message.proto',
  package='pogoprotos.networking.requests.platform.requests',
  syntax='proto3',
  serialized_pb=_b('\n]pogoprotos/networking/requests/platform/requests/update_adventure_sync_settings_message.proto\x12\x30pogoprotos.networking.requests.platform.requests\x1a\x31pogoprotos/settings/adventure_sync_settings.proto\"q\n\"UpdateAdventureSyncSettingsMessage\x12K\n\x17\x61\x64venture_sync_settings\x18\x01 \x01(\x0b\x32*.pogoprotos.settings.AdventureSyncSettingsb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_settings_dot_adventure__sync__settings__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_UPDATEADVENTURESYNCSETTINGSMESSAGE = _descriptor.Descriptor(
  name='UpdateAdventureSyncSettingsMessage',
  full_name='pogoprotos.networking.requests.platform.requests.UpdateAdventureSyncSettingsMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='adventure_sync_settings', full_name='pogoprotos.networking.requests.platform.requests.UpdateAdventureSyncSettingsMessage.adventure_sync_settings', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=198,
  serialized_end=311,
)

_UPDATEADVENTURESYNCSETTINGSMESSAGE.fields_by_name['adventure_sync_settings'].message_type = pogoprotos_dot_settings_dot_adventure__sync__settings__pb2._ADVENTURESYNCSETTINGS
DESCRIPTOR.message_types_by_name['UpdateAdventureSyncSettingsMessage'] = _UPDATEADVENTURESYNCSETTINGSMESSAGE

UpdateAdventureSyncSettingsMessage = _reflection.GeneratedProtocolMessageType('UpdateAdventureSyncSettingsMessage', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEADVENTURESYNCSETTINGSMESSAGE,
  __module__ = 'pogoprotos.networking.requests.platform.requests.update_adventure_sync_settings_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.platform.requests.UpdateAdventureSyncSettingsMessage)
  ))
_sym_db.RegisterMessage(UpdateAdventureSyncSettingsMessage)


# @@protoc_insertion_point(module_scope)
