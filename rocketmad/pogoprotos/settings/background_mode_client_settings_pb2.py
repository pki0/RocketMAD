# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/background_mode_client_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/background_mode_client_settings.proto',
  package='pogoprotos.settings',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n9pogoprotos/settings/background_mode_client_settings.proto\x12\x13pogoprotos.settings\"\xb3\x02\n\x1c\x42\x61\x63kgroundModeClientSettings\x12\x1d\n\x15maximum_sample_age_ms\x18\x01 \x01(\x03\x12%\n\x1d\x61\x63\x63\x65pt_manual_fitness_samples\x18\x02 \x01(\x08\x12(\n minimum_location_accuracy_meters\x18\x03 \x01(\x01\x12+\n#background_wake_up_interval_minutes\x18\x04 \x01(\x05\x12 \n\x18max_upload_size_in_bytes\x18\x05 \x01(\x05\x12\'\n\x1fmin_enclosing_geofence_radius_m\x18\x06 \x01(\x01\x12+\n#background_token_refresh_interval_s\x18\x07 \x01(\x03\x62\x06proto3')
)




_BACKGROUNDMODECLIENTSETTINGS = _descriptor.Descriptor(
  name='BackgroundModeClientSettings',
  full_name='pogoprotos.settings.BackgroundModeClientSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='maximum_sample_age_ms', full_name='pogoprotos.settings.BackgroundModeClientSettings.maximum_sample_age_ms', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accept_manual_fitness_samples', full_name='pogoprotos.settings.BackgroundModeClientSettings.accept_manual_fitness_samples', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minimum_location_accuracy_meters', full_name='pogoprotos.settings.BackgroundModeClientSettings.minimum_location_accuracy_meters', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='background_wake_up_interval_minutes', full_name='pogoprotos.settings.BackgroundModeClientSettings.background_wake_up_interval_minutes', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_upload_size_in_bytes', full_name='pogoprotos.settings.BackgroundModeClientSettings.max_upload_size_in_bytes', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_enclosing_geofence_radius_m', full_name='pogoprotos.settings.BackgroundModeClientSettings.min_enclosing_geofence_radius_m', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='background_token_refresh_interval_s', full_name='pogoprotos.settings.BackgroundModeClientSettings.background_token_refresh_interval_s', index=6,
      number=7, type=3, cpp_type=2, label=1,
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
  serialized_start=83,
  serialized_end=390,
)

DESCRIPTOR.message_types_by_name['BackgroundModeClientSettings'] = _BACKGROUNDMODECLIENTSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BackgroundModeClientSettings = _reflection.GeneratedProtocolMessageType('BackgroundModeClientSettings', (_message.Message,), dict(
  DESCRIPTOR = _BACKGROUNDMODECLIENTSETTINGS,
  __module__ = 'pogoprotos.settings.background_mode_client_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.BackgroundModeClientSettings)
  ))
_sym_db.RegisterMessage(BackgroundModeClientSettings)


# @@protoc_insertion_point(module_scope)
