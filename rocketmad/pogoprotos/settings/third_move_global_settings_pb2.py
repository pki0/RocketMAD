# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/third_move_global_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/third_move_global_settings.proto',
  package='pogoprotos.settings',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n4pogoprotos/settings/third_move_global_settings.proto\x12\x13pogoprotos.settings\"1\n\x17ThirdMoveGlobalSettings\x12\x16\n\x0eunlock_enabled\x18\x01 \x01(\x08\x62\x06proto3')
)




_THIRDMOVEGLOBALSETTINGS = _descriptor.Descriptor(
  name='ThirdMoveGlobalSettings',
  full_name='pogoprotos.settings.ThirdMoveGlobalSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unlock_enabled', full_name='pogoprotos.settings.ThirdMoveGlobalSettings.unlock_enabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
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
  serialized_start=77,
  serialized_end=126,
)

DESCRIPTOR.message_types_by_name['ThirdMoveGlobalSettings'] = _THIRDMOVEGLOBALSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ThirdMoveGlobalSettings = _reflection.GeneratedProtocolMessageType('ThirdMoveGlobalSettings', (_message.Message,), dict(
  DESCRIPTOR = _THIRDMOVEGLOBALSETTINGS,
  __module__ = 'pogoprotos.settings.third_move_global_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.ThirdMoveGlobalSettings)
  ))
_sym_db.RegisterMessage(ThirdMoveGlobalSettings)


# @@protoc_insertion_point(module_scope)
