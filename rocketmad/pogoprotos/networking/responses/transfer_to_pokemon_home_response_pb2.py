# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/transfer_to_pokemon_home_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/transfer_to_pokemon_home_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nGpogoprotos/networking/responses/transfer_to_pokemon_home_response.proto\x12\x1fpogoprotos.networking.responses\"\xcb\x08\n\x1dTransferToPokemonHomeResponse\x12U\n\x06status\x18\x01 \x01(\x0e\x32\x45.pogoprotos.networking.responses.TransferToPokemonHomeResponse.Status\x12\x15\n\rcandy_awarded\x18\x02 \x01(\x05\x12\x18\n\x10xl_candy_awarded\x18\x03 \x01(\x05\"\xa1\x07\n\x06Status\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x1e\n\x1a\x45RROR_PLAYER_LEVEL_TOO_LOW\x10\x02\x12\x18\n\x14\x45RROR_NO_NAID_LINKED\x10\x03\x12\x1a\n\x16\x45RROR_TOO_MANY_POKEMON\x10\x04\x12,\n(ERROR_SERVER_CLIENT_ENERGY_COST_MISMATCH\x10\x05\x12\x1d\n\x19\x45RROR_INSUFFICIENT_ENERGY\x10\x06\x12\x1e\n\x1a\x45RROR_TRANSFER_IN_PROGRESS\x10\x07\x12\x1a\n\x16\x45RROR_POKEMON_DEPLOYED\x10\n\x12\x18\n\x14\x45RROR_POKEMON_IS_EGG\x10\x0b\x12\x1a\n\x16\x45RROR_POKEMON_IS_BUDDY\x10\x0c\x12\x15\n\x11\x45RROR_POKEMON_BAD\x10\r\x12\x19\n\x15\x45RROR_POKEMON_IS_MEGA\x10\x0e\x12\x1b\n\x17\x45RROR_POKEMON_FAVORITED\x10\x0f\x12\x1b\n\x17\x45RROR_POKEMON_NOT_FOUND\x10\x10\x12\x1c\n\x18\x45RROR_VALIDATION_UNKNOWN\x10\x11\x12\x1d\n\x19\x45RROR_POKEMON_HAS_COSTUME\x10\x15\x12\x1b\n\x17\x45RROR_POKEMON_IS_SHADOW\x10\x16\x12\x1c\n\x18\x45RROR_POKEMON_DISALLOWED\x10\x17\x12\"\n\x1e\x45RROR_PHAPI_REQUEST_BODY_FALSE\x10\x1e\x12&\n\"ERROR_PHAPI_REQUEST_PARAMETERS_DNE\x10\x1f\x12(\n$ERROR_PHAPI_REQUEST_PARAMETERS_FALSE\x10 \x12\x1b\n\x17\x45RROR_PHAPI_MAINTENANCE\x10!\x12\x1d\n\x19\x45RROR_PHAPI_SERVICE_ENDED\x10\"\x12\x17\n\x13\x45RROR_PHAPI_UNKNOWN\x10#\x12#\n\x1f\x45RROR_PHAPI_NAID_DOES_NOT_EXIST\x10$\x12\x1f\n\x1b\x45RROR_PHAPI_NO_SPACE_IN_BOX\x10%\x12\'\n#ERROR_PHAPI_DATA_CONVERSION_FAILURE\x10&\x12#\n\x1f\x45RROR_PHAPI_WAITING_FOR_RECEIPT\x10\'\x12\'\n#ERROR_PHAPI_PLAYER_NOT_USING_PH_APP\x10(b\x06proto3')
)



_TRANSFERTOPOKEMONHOMERESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='pogoprotos.networking.responses.TransferToPokemonHomeResponse.Status',
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
      name='ERROR_PLAYER_LEVEL_TOO_LOW', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_NO_NAID_LINKED', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_TOO_MANY_POKEMON', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_SERVER_CLIENT_ENERGY_COST_MISMATCH', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INSUFFICIENT_ENERGY', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_TRANSFER_IN_PROGRESS', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POKEMON_DEPLOYED', index=8, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POKEMON_IS_EGG', index=9, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POKEMON_IS_BUDDY', index=10, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POKEMON_BAD', index=11, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POKEMON_IS_MEGA', index=12, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POKEMON_FAVORITED', index=13, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POKEMON_NOT_FOUND', index=14, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_VALIDATION_UNKNOWN', index=15, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POKEMON_HAS_COSTUME', index=16, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POKEMON_IS_SHADOW', index=17, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POKEMON_DISALLOWED', index=18, number=23,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PHAPI_REQUEST_BODY_FALSE', index=19, number=30,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PHAPI_REQUEST_PARAMETERS_DNE', index=20, number=31,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PHAPI_REQUEST_PARAMETERS_FALSE', index=21, number=32,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PHAPI_MAINTENANCE', index=22, number=33,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PHAPI_SERVICE_ENDED', index=23, number=34,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PHAPI_UNKNOWN', index=24, number=35,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PHAPI_NAID_DOES_NOT_EXIST', index=25, number=36,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PHAPI_NO_SPACE_IN_BOX', index=26, number=37,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PHAPI_DATA_CONVERSION_FAILURE', index=27, number=38,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PHAPI_WAITING_FOR_RECEIPT', index=28, number=39,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PHAPI_PLAYER_NOT_USING_PH_APP', index=29, number=40,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=279,
  serialized_end=1208,
)
_sym_db.RegisterEnumDescriptor(_TRANSFERTOPOKEMONHOMERESPONSE_STATUS)


_TRANSFERTOPOKEMONHOMERESPONSE = _descriptor.Descriptor(
  name='TransferToPokemonHomeResponse',
  full_name='pogoprotos.networking.responses.TransferToPokemonHomeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pogoprotos.networking.responses.TransferToPokemonHomeResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='candy_awarded', full_name='pogoprotos.networking.responses.TransferToPokemonHomeResponse.candy_awarded', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='xl_candy_awarded', full_name='pogoprotos.networking.responses.TransferToPokemonHomeResponse.xl_candy_awarded', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TRANSFERTOPOKEMONHOMERESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=109,
  serialized_end=1208,
)

_TRANSFERTOPOKEMONHOMERESPONSE.fields_by_name['status'].enum_type = _TRANSFERTOPOKEMONHOMERESPONSE_STATUS
_TRANSFERTOPOKEMONHOMERESPONSE_STATUS.containing_type = _TRANSFERTOPOKEMONHOMERESPONSE
DESCRIPTOR.message_types_by_name['TransferToPokemonHomeResponse'] = _TRANSFERTOPOKEMONHOMERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TransferToPokemonHomeResponse = _reflection.GeneratedProtocolMessageType('TransferToPokemonHomeResponse', (_message.Message,), dict(
  DESCRIPTOR = _TRANSFERTOPOKEMONHOMERESPONSE,
  __module__ = 'pogoprotos.networking.responses.transfer_to_pokemon_home_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.TransferToPokemonHomeResponse)
  ))
_sym_db.RegisterMessage(TransferToPokemonHomeResponse)


# @@protoc_insertion_point(module_scope)
