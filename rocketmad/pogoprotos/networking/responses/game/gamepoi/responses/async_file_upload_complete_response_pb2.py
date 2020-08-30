# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/game/gamepoi/responses/async_file_upload_complete_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import player_submission_type_pb2 as pogoprotos_dot_enums_dot_player__submission__type__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/game/gamepoi/responses/async_file_upload_complete_response.proto',
  package='pogoprotos.networking.responses.game.gamepoi.responses',
  syntax='proto3',
  serialized_pb=_b('\n`pogoprotos/networking/responses/game/gamepoi/responses/async_file_upload_complete_response.proto\x12\x36pogoprotos.networking.responses.game.gamepoi.responses\x1a-pogoprotos/enums/player_submission_type.proto\"\xee\x02\n\x1f\x41syncFileUploadCompleteResponse\x12r\n\x05\x65rror\x18\x01 \x01(\x0e\x32\x63.pogoprotos.networking.responses.game.gamepoi.responses.AsyncFileUploadCompleteResponse.ErrorStatus\x12?\n\x0fsubmission_type\x18\x02 \x01(\x0e\x32&.pogoprotos.enums.PlayerSubmissionType\x12\x0e\n\x06poi_id\x18\x03 \x01(\t\"\x85\x01\n\x0b\x45rrorStatus\x12\t\n\x05UNSET\x10\x00\x12\x18\n\x14SERVER_UPDATE_FAILED\x10\x01\x12\x19\n\x15MISSING_SUBMISSION_ID\x10\x02\x12\x1b\n\x17MISSING_SUBMISSION_TYPE\x10\x03\x12\x19\n\x15MISSING_UPLOAD_STATUS\x10\x04\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_player__submission__type__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_ASYNCFILEUPLOADCOMPLETERESPONSE_ERRORSTATUS = _descriptor.EnumDescriptor(
  name='ErrorStatus',
  full_name='pogoprotos.networking.responses.game.gamepoi.responses.AsyncFileUploadCompleteResponse.ErrorStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SERVER_UPDATE_FAILED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_SUBMISSION_ID', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_SUBMISSION_TYPE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_UPLOAD_STATUS', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=437,
  serialized_end=570,
)
_sym_db.RegisterEnumDescriptor(_ASYNCFILEUPLOADCOMPLETERESPONSE_ERRORSTATUS)


_ASYNCFILEUPLOADCOMPLETERESPONSE = _descriptor.Descriptor(
  name='AsyncFileUploadCompleteResponse',
  full_name='pogoprotos.networking.responses.game.gamepoi.responses.AsyncFileUploadCompleteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='pogoprotos.networking.responses.game.gamepoi.responses.AsyncFileUploadCompleteResponse.error', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='submission_type', full_name='pogoprotos.networking.responses.game.gamepoi.responses.AsyncFileUploadCompleteResponse.submission_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='poi_id', full_name='pogoprotos.networking.responses.game.gamepoi.responses.AsyncFileUploadCompleteResponse.poi_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ASYNCFILEUPLOADCOMPLETERESPONSE_ERRORSTATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=204,
  serialized_end=570,
)

_ASYNCFILEUPLOADCOMPLETERESPONSE.fields_by_name['error'].enum_type = _ASYNCFILEUPLOADCOMPLETERESPONSE_ERRORSTATUS
_ASYNCFILEUPLOADCOMPLETERESPONSE.fields_by_name['submission_type'].enum_type = pogoprotos_dot_enums_dot_player__submission__type__pb2._PLAYERSUBMISSIONTYPE
_ASYNCFILEUPLOADCOMPLETERESPONSE_ERRORSTATUS.containing_type = _ASYNCFILEUPLOADCOMPLETERESPONSE
DESCRIPTOR.message_types_by_name['AsyncFileUploadCompleteResponse'] = _ASYNCFILEUPLOADCOMPLETERESPONSE

AsyncFileUploadCompleteResponse = _reflection.GeneratedProtocolMessageType('AsyncFileUploadCompleteResponse', (_message.Message,), dict(
  DESCRIPTOR = _ASYNCFILEUPLOADCOMPLETERESPONSE,
  __module__ = 'pogoprotos.networking.responses.game.gamepoi.responses.async_file_upload_complete_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.game.gamepoi.responses.AsyncFileUploadCompleteResponse)
  ))
_sym_db.RegisterMessage(AsyncFileUploadCompleteResponse)


# @@protoc_insertion_point(module_scope)
