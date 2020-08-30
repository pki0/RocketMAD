# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/get_rocket_balloon_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.rocket import rocket_balloon_display_pb2 as pogoprotos_dot_data_dot_rocket_dot_rocket__balloon__display__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/get_rocket_balloon_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_pb=_b('\nApogoprotos/networking/responses/get_rocket_balloon_response.proto\x12\x1fpogoprotos.networking.responses\x1a\x33pogoprotos/data/rocket/rocket_balloon_display.proto\"\xc7\x02\n\x18GetRocketBalloonResponse\x12P\n\x06status\x18\x01 \x01(\x0e\x32@.pogoprotos.networking.responses.GetRocketBalloonResponse.Status\x12=\n\x07\x64isplay\x18\x02 \x01(\x0b\x32,.pogoprotos.data.rocket.RocketBalloonDisplay\"\x99\x01\n\x06Status\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x10\n\x0cIN_COOL_DOWN\x10\x02\x12\x18\n\x14NO_BALLOON_AVAILABLE\x10\x03\x12\x0c\n\x08\x44ISABLED\x10\x04\x12\x19\n\x15\x45QUIPPED_ITEM_INVALID\x10\x05\x12\"\n\x1eSUCCESS_BALLOON_ALREADY_EXISTS\x10\x06\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_rocket_dot_rocket__balloon__display__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_GETROCKETBALLOONRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='pogoprotos.networking.responses.GetRocketBalloonResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IN_COOL_DOWN', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_BALLOON_AVAILABLE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISABLED', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EQUIPPED_ITEM_INVALID', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS_BALLOON_ALREADY_EXISTS', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=330,
  serialized_end=483,
)
_sym_db.RegisterEnumDescriptor(_GETROCKETBALLOONRESPONSE_STATUS)


_GETROCKETBALLOONRESPONSE = _descriptor.Descriptor(
  name='GetRocketBalloonResponse',
  full_name='pogoprotos.networking.responses.GetRocketBalloonResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pogoprotos.networking.responses.GetRocketBalloonResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='display', full_name='pogoprotos.networking.responses.GetRocketBalloonResponse.display', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GETROCKETBALLOONRESPONSE_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=156,
  serialized_end=483,
)

_GETROCKETBALLOONRESPONSE.fields_by_name['status'].enum_type = _GETROCKETBALLOONRESPONSE_STATUS
_GETROCKETBALLOONRESPONSE.fields_by_name['display'].message_type = pogoprotos_dot_data_dot_rocket_dot_rocket__balloon__display__pb2._ROCKETBALLOONDISPLAY
_GETROCKETBALLOONRESPONSE_STATUS.containing_type = _GETROCKETBALLOONRESPONSE
DESCRIPTOR.message_types_by_name['GetRocketBalloonResponse'] = _GETROCKETBALLOONRESPONSE

GetRocketBalloonResponse = _reflection.GeneratedProtocolMessageType('GetRocketBalloonResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETROCKETBALLOONRESPONSE,
  __module__ = 'pogoprotos.networking.responses.get_rocket_balloon_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.GetRocketBalloonResponse)
  ))
_sym_db.RegisterMessage(GetRocketBalloonResponse)


# @@protoc_insertion_point(module_scope)
