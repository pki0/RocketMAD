# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/mega_evolve_pokemon_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import temporary_evolution_id_pb2 as pogoprotos_dot_enums_dot_temporary__evolution__id__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/mega_evolve_pokemon_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nIpogoprotos/networking/requests/messages/mega_evolve_pokemon_message.proto\x12\'pogoprotos.networking.requests.messages\x1a-pogoprotos/enums/temporary_evolution_id.proto\"k\n\x18MegaEvolvePokemonMessage\x12\x12\n\npokemon_id\x18\x01 \x01(\x06\x12;\n\x0btemp_evo_id\x18\x02 \x01(\x0e\x32&.pogoprotos.enums.TemporaryEvolutionIdb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_temporary__evolution__id__pb2.DESCRIPTOR,])




_MEGAEVOLVEPOKEMONMESSAGE = _descriptor.Descriptor(
  name='MegaEvolvePokemonMessage',
  full_name='pogoprotos.networking.requests.messages.MegaEvolvePokemonMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon_id', full_name='pogoprotos.networking.requests.messages.MegaEvolvePokemonMessage.pokemon_id', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='temp_evo_id', full_name='pogoprotos.networking.requests.messages.MegaEvolvePokemonMessage.temp_evo_id', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=165,
  serialized_end=272,
)

_MEGAEVOLVEPOKEMONMESSAGE.fields_by_name['temp_evo_id'].enum_type = pogoprotos_dot_enums_dot_temporary__evolution__id__pb2._TEMPORARYEVOLUTIONID
DESCRIPTOR.message_types_by_name['MegaEvolvePokemonMessage'] = _MEGAEVOLVEPOKEMONMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MegaEvolvePokemonMessage = _reflection.GeneratedProtocolMessageType('MegaEvolvePokemonMessage', (_message.Message,), dict(
  DESCRIPTOR = _MEGAEVOLVEPOKEMONMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.mega_evolve_pokemon_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.MegaEvolvePokemonMessage)
  ))
_sym_db.RegisterMessage(MegaEvolvePokemonMessage)


# @@protoc_insertion_point(module_scope)
