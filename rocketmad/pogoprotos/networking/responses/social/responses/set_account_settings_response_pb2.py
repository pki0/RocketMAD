# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/social/responses/set_account_settings_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/social/responses/set_account_settings_response.proto',
  package='pogoprotos.networking.responses.social.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nTpogoprotos/networking/responses/social/responses/set_account_settings_response.proto\x12\x30pogoprotos.networking.responses.social.responses\"\xb6\x01\n\x1aSetAccountSettingsResponse\x12\x63\n\x06result\x18\x01 \x01(\x0e\x32S.pogoprotos.networking.responses.social.responses.SetAccountSettingsResponse.Result\"3\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x11\n\rERROR_UNKNOWN\x10\x02\x62\x06proto3')
)



_SETACCOUNTSETTINGSRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.social.responses.SetAccountSettingsResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_UNKNOWN', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=270,
  serialized_end=321,
)
_sym_db.RegisterEnumDescriptor(_SETACCOUNTSETTINGSRESPONSE_RESULT)


_SETACCOUNTSETTINGSRESPONSE = _descriptor.Descriptor(
  name='SetAccountSettingsResponse',
  full_name='pogoprotos.networking.responses.social.responses.SetAccountSettingsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.social.responses.SetAccountSettingsResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SETACCOUNTSETTINGSRESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=139,
  serialized_end=321,
)

_SETACCOUNTSETTINGSRESPONSE.fields_by_name['result'].enum_type = _SETACCOUNTSETTINGSRESPONSE_RESULT
_SETACCOUNTSETTINGSRESPONSE_RESULT.containing_type = _SETACCOUNTSETTINGSRESPONSE
DESCRIPTOR.message_types_by_name['SetAccountSettingsResponse'] = _SETACCOUNTSETTINGSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SetAccountSettingsResponse = _reflection.GeneratedProtocolMessageType('SetAccountSettingsResponse', (_message.Message,), dict(
  DESCRIPTOR = _SETACCOUNTSETTINGSRESPONSE,
  __module__ = 'pogoprotos.networking.responses.social.responses.set_account_settings_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.social.responses.SetAccountSettingsResponse)
  ))
_sym_db.RegisterMessage(SetAccountSettingsResponse)


# @@protoc_insertion_point(module_scope)
