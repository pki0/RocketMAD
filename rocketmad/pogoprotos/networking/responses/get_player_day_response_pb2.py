# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/get_player_day_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/get_player_day_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n=pogoprotos/networking/responses/get_player_day_response.proto\x12\x1fpogoprotos.networking.responses\"\xa6\x01\n\x14GetPlayerDayResponse\x12L\n\x06result\x18\x01 \x01(\x0e\x32<.pogoprotos.networking.responses.GetPlayerDayResponse.Result\x12\x0b\n\x03\x64\x61y\x18\x02 \x01(\x03\"3\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x11\n\rERROR_UNKNOWN\x10\x02\x62\x06proto3')
)



_GETPLAYERDAYRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.GetPlayerDayResponse.Result',
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
  serialized_start=214,
  serialized_end=265,
)
_sym_db.RegisterEnumDescriptor(_GETPLAYERDAYRESPONSE_RESULT)


_GETPLAYERDAYRESPONSE = _descriptor.Descriptor(
  name='GetPlayerDayResponse',
  full_name='pogoprotos.networking.responses.GetPlayerDayResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.GetPlayerDayResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='day', full_name='pogoprotos.networking.responses.GetPlayerDayResponse.day', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GETPLAYERDAYRESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=99,
  serialized_end=265,
)

_GETPLAYERDAYRESPONSE.fields_by_name['result'].enum_type = _GETPLAYERDAYRESPONSE_RESULT
_GETPLAYERDAYRESPONSE_RESULT.containing_type = _GETPLAYERDAYRESPONSE
DESCRIPTOR.message_types_by_name['GetPlayerDayResponse'] = _GETPLAYERDAYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetPlayerDayResponse = _reflection.GeneratedProtocolMessageType('GetPlayerDayResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETPLAYERDAYRESPONSE,
  __module__ = 'pogoprotos.networking.responses.get_player_day_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.GetPlayerDayResponse)
  ))
_sym_db.RegisterMessage(GetPlayerDayResponse)


# @@protoc_insertion_point(module_scope)
