# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/buddy_activity_category_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import buddy_activity_category_pb2 as pogoprotos_dot_enums_dot_buddy__activity__category__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/master/buddy_activity_category_settings.proto',
  package='pogoprotos.settings.master',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nApogoprotos/settings/master/buddy_activity_category_settings.proto\x12\x1apogoprotos.settings.master\x1a.pogoprotos/enums/buddy_activity_category.proto\"\x7f\n\x1d\x42uddyActivityCategorySettings\x12\x42\n\x11\x61\x63tivity_category\x18\x01 \x01(\x0e\x32\'.pogoprotos.enums.BuddyActivityCategory\x12\x1a\n\x12max_points_per_day\x18\x02 \x01(\x05\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_buddy__activity__category__pb2.DESCRIPTOR,])




_BUDDYACTIVITYCATEGORYSETTINGS = _descriptor.Descriptor(
  name='BuddyActivityCategorySettings',
  full_name='pogoprotos.settings.master.BuddyActivityCategorySettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='activity_category', full_name='pogoprotos.settings.master.BuddyActivityCategorySettings.activity_category', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_points_per_day', full_name='pogoprotos.settings.master.BuddyActivityCategorySettings.max_points_per_day', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=145,
  serialized_end=272,
)

_BUDDYACTIVITYCATEGORYSETTINGS.fields_by_name['activity_category'].enum_type = pogoprotos_dot_enums_dot_buddy__activity__category__pb2._BUDDYACTIVITYCATEGORY
DESCRIPTOR.message_types_by_name['BuddyActivityCategorySettings'] = _BUDDYACTIVITYCATEGORYSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BuddyActivityCategorySettings = _reflection.GeneratedProtocolMessageType('BuddyActivityCategorySettings', (_message.Message,), dict(
  DESCRIPTOR = _BUDDYACTIVITYCATEGORYSETTINGS,
  __module__ = 'pogoprotos.settings.master.buddy_activity_category_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.BuddyActivityCategorySettings)
  ))
_sym_db.RegisterMessage(BuddyActivityCategorySettings)


# @@protoc_insertion_point(module_scope)
