# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/leave_buddy_multiplayer_session_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/leave_buddy_multiplayer_session_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_pb=_b('\nNpogoprotos/networking/responses/leave_buddy_multiplayer_session_response.proto\x12\x1fpogoprotos.networking.responses\"\xed\x01\n$LeaveBuddyMultiplayerSessionResponse\x12\\\n\x06result\x18\x01 \x01(\x0e\x32L.pogoprotos.networking.responses.LeaveBuddyMultiplayerSessionResponse.Result\"g\n\x06Result\x12\x11\n\rLEAVE_SUCCESS\x10\x00\x12\x16\n\x12LEAVE_NOT_IN_LOBBY\x10\x01\x12\x19\n\x15LEAVE_LOBBY_NOT_FOUND\x10\x02\x12\x17\n\x13LEAVE_UNKNOWN_ERROR\x10\x03\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_LEAVEBUDDYMULTIPLAYERSESSIONRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.LeaveBuddyMultiplayerSessionResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LEAVE_SUCCESS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEAVE_NOT_IN_LOBBY', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEAVE_LOBBY_NOT_FOUND', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEAVE_UNKNOWN_ERROR', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=250,
  serialized_end=353,
)
_sym_db.RegisterEnumDescriptor(_LEAVEBUDDYMULTIPLAYERSESSIONRESPONSE_RESULT)


_LEAVEBUDDYMULTIPLAYERSESSIONRESPONSE = _descriptor.Descriptor(
  name='LeaveBuddyMultiplayerSessionResponse',
  full_name='pogoprotos.networking.responses.LeaveBuddyMultiplayerSessionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.LeaveBuddyMultiplayerSessionResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LEAVEBUDDYMULTIPLAYERSESSIONRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=116,
  serialized_end=353,
)

_LEAVEBUDDYMULTIPLAYERSESSIONRESPONSE.fields_by_name['result'].enum_type = _LEAVEBUDDYMULTIPLAYERSESSIONRESPONSE_RESULT
_LEAVEBUDDYMULTIPLAYERSESSIONRESPONSE_RESULT.containing_type = _LEAVEBUDDYMULTIPLAYERSESSIONRESPONSE
DESCRIPTOR.message_types_by_name['LeaveBuddyMultiplayerSessionResponse'] = _LEAVEBUDDYMULTIPLAYERSESSIONRESPONSE

LeaveBuddyMultiplayerSessionResponse = _reflection.GeneratedProtocolMessageType('LeaveBuddyMultiplayerSessionResponse', (_message.Message,), dict(
  DESCRIPTOR = _LEAVEBUDDYMULTIPLAYERSESSIONRESPONSE,
  __module__ = 'pogoprotos.networking.responses.leave_buddy_multiplayer_session_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.LeaveBuddyMultiplayerSessionResponse)
  ))
_sym_db.RegisterMessage(LeaveBuddyMultiplayerSessionResponse)


# @@protoc_insertion_point(module_scope)
