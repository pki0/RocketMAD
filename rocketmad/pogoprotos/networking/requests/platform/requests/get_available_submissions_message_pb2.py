# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/platform/requests/get_available_submissions_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import player_submission_type_pb2 as pogoprotos_dot_enums_dot_player__submission__type__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/platform/requests/get_available_submissions_message.proto',
  package='pogoprotos.networking.requests.platform.requests',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nXpogoprotos/networking/requests/platform/requests/get_available_submissions_message.proto\x12\x30pogoprotos.networking.requests.platform.requests\x1a-pogoprotos/enums/player_submission_type.proto\"\xa3\x01\n\x1eGetAvailableSubmissionsMessage\x12?\n\x0fsubmission_type\x18\x01 \x01(\x0e\x32&.pogoprotos.enums.PlayerSubmissionType\x12@\n\x10submission_types\x18\x02 \x03(\x0e\x32&.pogoprotos.enums.PlayerSubmissionTypeb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_player__submission__type__pb2.DESCRIPTOR,])




_GETAVAILABLESUBMISSIONSMESSAGE = _descriptor.Descriptor(
  name='GetAvailableSubmissionsMessage',
  full_name='pogoprotos.networking.requests.platform.requests.GetAvailableSubmissionsMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='submission_type', full_name='pogoprotos.networking.requests.platform.requests.GetAvailableSubmissionsMessage.submission_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='submission_types', full_name='pogoprotos.networking.requests.platform.requests.GetAvailableSubmissionsMessage.submission_types', index=1,
      number=2, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=190,
  serialized_end=353,
)

_GETAVAILABLESUBMISSIONSMESSAGE.fields_by_name['submission_type'].enum_type = pogoprotos_dot_enums_dot_player__submission__type__pb2._PLAYERSUBMISSIONTYPE
_GETAVAILABLESUBMISSIONSMESSAGE.fields_by_name['submission_types'].enum_type = pogoprotos_dot_enums_dot_player__submission__type__pb2._PLAYERSUBMISSIONTYPE
DESCRIPTOR.message_types_by_name['GetAvailableSubmissionsMessage'] = _GETAVAILABLESUBMISSIONSMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetAvailableSubmissionsMessage = _reflection.GeneratedProtocolMessageType('GetAvailableSubmissionsMessage', (_message.Message,), dict(
  DESCRIPTOR = _GETAVAILABLESUBMISSIONSMESSAGE,
  __module__ = 'pogoprotos.networking.requests.platform.requests.get_available_submissions_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.platform.requests.GetAvailableSubmissionsMessage)
  ))
_sym_db.RegisterMessage(GetAvailableSubmissionsMessage)


# @@protoc_insertion_point(module_scope)
