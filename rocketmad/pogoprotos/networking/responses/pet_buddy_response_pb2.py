# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/pet_buddy_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.buddy import buddy_observed_data_pb2 as pogoprotos_dot_data_dot_buddy_dot_buddy__observed__data__pb2
from pogoprotos.data.buddy import buddy_stats_shown_hearts_pb2 as pogoprotos_dot_data_dot_buddy_dot_buddy__stats__shown__hearts__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/pet_buddy_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_pb=_b('\n8pogoprotos/networking/responses/pet_buddy_response.proto\x12\x1fpogoprotos.networking.responses\x1a/pogoprotos/data/buddy/buddy_observed_data.proto\x1a\x34pogoprotos/data/buddy/buddy_stats_shown_hearts.proto\"\xb2\x02\n\x10PetBuddyResponse\x12H\n\x06result\x18\x01 \x01(\x0e\x32\x38.pogoprotos.networking.responses.PetBuddyResponse.Result\x12?\n\robserved_data\x18\x02 \x01(\x0b\x32(.pogoprotos.data.buddy.BuddyObservedData\x12V\n\x0cshown_hearts\x18\x03 \x01(\x0e\x32@.pogoprotos.data.buddy.BuddyStatsShownHearts.BuddyShownHeartType\";\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x19\n\x15\x45RROR_BUDDY_NOT_VALID\x10\x02\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_buddy_dot_buddy__observed__data__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_buddy_dot_buddy__stats__shown__hearts__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_PETBUDDYRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.PetBuddyResponse.Result',
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
      name='ERROR_BUDDY_NOT_VALID', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=444,
  serialized_end=503,
)
_sym_db.RegisterEnumDescriptor(_PETBUDDYRESPONSE_RESULT)


_PETBUDDYRESPONSE = _descriptor.Descriptor(
  name='PetBuddyResponse',
  full_name='pogoprotos.networking.responses.PetBuddyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.PetBuddyResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='observed_data', full_name='pogoprotos.networking.responses.PetBuddyResponse.observed_data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shown_hearts', full_name='pogoprotos.networking.responses.PetBuddyResponse.shown_hearts', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PETBUDDYRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=197,
  serialized_end=503,
)

_PETBUDDYRESPONSE.fields_by_name['result'].enum_type = _PETBUDDYRESPONSE_RESULT
_PETBUDDYRESPONSE.fields_by_name['observed_data'].message_type = pogoprotos_dot_data_dot_buddy_dot_buddy__observed__data__pb2._BUDDYOBSERVEDDATA
_PETBUDDYRESPONSE.fields_by_name['shown_hearts'].enum_type = pogoprotos_dot_data_dot_buddy_dot_buddy__stats__shown__hearts__pb2._BUDDYSTATSSHOWNHEARTS_BUDDYSHOWNHEARTTYPE
_PETBUDDYRESPONSE_RESULT.containing_type = _PETBUDDYRESPONSE
DESCRIPTOR.message_types_by_name['PetBuddyResponse'] = _PETBUDDYRESPONSE

PetBuddyResponse = _reflection.GeneratedProtocolMessageType('PetBuddyResponse', (_message.Message,), dict(
  DESCRIPTOR = _PETBUDDYRESPONSE,
  __module__ = 'pogoprotos.networking.responses.pet_buddy_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.PetBuddyResponse)
  ))
_sym_db.RegisterMessage(PetBuddyResponse)


# @@protoc_insertion_point(module_scope)
