# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/game/gameanticheat/responses/acknowledge_warnings_response.proto

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
  name='pogoprotos/networking/responses/game/gameanticheat/responses/acknowledge_warnings_response.proto',
  package='pogoprotos.networking.responses.game.gameanticheat.responses',
  syntax='proto3',
  serialized_pb=_b('\n`pogoprotos/networking/responses/game/gameanticheat/responses/acknowledge_warnings_response.proto\x12<pogoprotos.networking.responses.game.gameanticheat.responses\".\n\x1b\x41\x63knowledgeWarningsResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ACKNOWLEDGEWARNINGSRESPONSE = _descriptor.Descriptor(
  name='AcknowledgeWarningsResponse',
  full_name='pogoprotos.networking.responses.game.gameanticheat.responses.AcknowledgeWarningsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='pogoprotos.networking.responses.game.gameanticheat.responses.AcknowledgeWarningsResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=162,
  serialized_end=208,
)

DESCRIPTOR.message_types_by_name['AcknowledgeWarningsResponse'] = _ACKNOWLEDGEWARNINGSRESPONSE

AcknowledgeWarningsResponse = _reflection.GeneratedProtocolMessageType('AcknowledgeWarningsResponse', (_message.Message,), dict(
  DESCRIPTOR = _ACKNOWLEDGEWARNINGSRESPONSE,
  __module__ = 'pogoprotos.networking.responses.game.gameanticheat.responses.acknowledge_warnings_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.game.gameanticheat.responses.AcknowledgeWarningsResponse)
  ))
_sym_db.RegisterMessage(AcknowledgeWarningsResponse)


# @@protoc_insertion_point(module_scope)
