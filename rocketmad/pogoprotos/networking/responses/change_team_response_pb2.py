# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/change_team_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data import player_data_pb2 as pogoprotos_dot_data_dot_player__data__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/change_team_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n:pogoprotos/networking/responses/change_team_response.proto\x12\x1fpogoprotos.networking.responses\x1a!pogoprotos/data/player_data.proto\"\x96\x02\n\x12\x43hangeTeamResponse\x12J\n\x06status\x18\x01 \x01(\x0e\x32:.pogoprotos.networking.responses.ChangeTeamResponse.Status\x12\x33\n\x0eupdated_player\x18\x02 \x01(\x0b\x32\x1b.pogoprotos.data.PlayerData\"\x7f\n\x06Status\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x13\n\x0f\x45RROR_SAME_TEAM\x10\x02\x12\x1f\n\x1b\x45RROR_ITEM_NOT_IN_INVENTORY\x10\x03\x12\x14\n\x10\x45RROR_WRONG_ITEM\x10\x04\x12\x11\n\rERROR_UNKNOWN\x10\x05\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_player__data__pb2.DESCRIPTOR,])



_CHANGETEAMRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='pogoprotos.networking.responses.ChangeTeamResponse.Status',
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
      name='ERROR_SAME_TEAM', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_ITEM_NOT_IN_INVENTORY', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_WRONG_ITEM', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_UNKNOWN', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=282,
  serialized_end=409,
)
_sym_db.RegisterEnumDescriptor(_CHANGETEAMRESPONSE_STATUS)


_CHANGETEAMRESPONSE = _descriptor.Descriptor(
  name='ChangeTeamResponse',
  full_name='pogoprotos.networking.responses.ChangeTeamResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pogoprotos.networking.responses.ChangeTeamResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_player', full_name='pogoprotos.networking.responses.ChangeTeamResponse.updated_player', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CHANGETEAMRESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=131,
  serialized_end=409,
)

_CHANGETEAMRESPONSE.fields_by_name['status'].enum_type = _CHANGETEAMRESPONSE_STATUS
_CHANGETEAMRESPONSE.fields_by_name['updated_player'].message_type = pogoprotos_dot_data_dot_player__data__pb2._PLAYERDATA
_CHANGETEAMRESPONSE_STATUS.containing_type = _CHANGETEAMRESPONSE
DESCRIPTOR.message_types_by_name['ChangeTeamResponse'] = _CHANGETEAMRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ChangeTeamResponse = _reflection.GeneratedProtocolMessageType('ChangeTeamResponse', (_message.Message,), dict(
  DESCRIPTOR = _CHANGETEAMRESPONSE,
  __module__ = 'pogoprotos.networking.responses.change_team_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.ChangeTeamResponse)
  ))
_sym_db.RegisterMessage(ChangeTeamResponse)


# @@protoc_insertion_point(module_scope)
