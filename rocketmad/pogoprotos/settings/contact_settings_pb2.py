# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/contact_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/contact_settings.proto',
  package='pogoprotos.settings',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n*pogoprotos/settings/contact_settings.proto\x12\x13pogoprotos.settings\"Q\n\x0f\x43ontactSettings\x12\x1d\n\x15send_marketing_emails\x18\x01 \x01(\x08\x12\x1f\n\x17send_push_notifications\x18\x02 \x01(\x08\x62\x06proto3')
)




_CONTACTSETTINGS = _descriptor.Descriptor(
  name='ContactSettings',
  full_name='pogoprotos.settings.ContactSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='send_marketing_emails', full_name='pogoprotos.settings.ContactSettings.send_marketing_emails', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='send_push_notifications', full_name='pogoprotos.settings.ContactSettings.send_push_notifications', index=1,
      number=2, type=8, cpp_type=7, label=1,
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
  serialized_start=67,
  serialized_end=148,
)

DESCRIPTOR.message_types_by_name['ContactSettings'] = _CONTACTSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ContactSettings = _reflection.GeneratedProtocolMessageType('ContactSettings', (_message.Message,), dict(
  DESCRIPTOR = _CONTACTSETTINGS,
  __module__ = 'pogoprotos.settings.contact_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.ContactSettings)
  ))
_sym_db.RegisterMessage(ContactSettings)


# @@protoc_insertion_point(module_scope)
