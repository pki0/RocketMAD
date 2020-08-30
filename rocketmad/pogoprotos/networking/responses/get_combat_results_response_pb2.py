# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/get_combat_results_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import combat_reward_status_pb2 as pogoprotos_dot_enums_dot_combat__reward__status__pb2
from pogoprotos.inventory import loot_pb2 as pogoprotos_dot_inventory_dot_loot__pb2
from pogoprotos.data.friends import leveled_up_friends_pb2 as pogoprotos_dot_data_dot_friends_dot_leveled__up__friends__pb2
from pogoprotos.enums import combat_player_finish_state_pb2 as pogoprotos_dot_enums_dot_combat__player__finish__state__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/get_combat_results_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_pb=_b('\nApogoprotos/networking/responses/get_combat_results_response.proto\x12\x1fpogoprotos.networking.responses\x1a+pogoprotos/enums/combat_reward_status.proto\x1a\x1fpogoprotos/inventory/loot.proto\x1a\x30pogoprotos/data/friends/leveled_up_friends.proto\x1a\x31pogoprotos/enums/combat_player_finish_state.proto\"\xb5\x05\n\x18GetCombatResultsResponse\x12P\n\x06result\x18\x01 \x01(\x0e\x32@.pogoprotos.networking.responses.GetCombatResultsResponse.Result\x12;\n\rreward_status\x18\x02 \x01(\x0e\x32$.pogoprotos.enums.CombatRewardStatus\x12+\n\x07rewards\x18\x03 \x01(\x0b\x32\x1a.pogoprotos.inventory.Loot\x12\x42\n\x0f\x66riend_level_up\x18\x04 \x01(\x0b\x32).pogoprotos.data.friends.LeveledUpFriends\x12%\n\x1dnumber_rewarded_battles_today\x18\x05 \x01(\x05\x12M\n\x1a\x63ombat_player_finish_state\x18\x06 \x01(\x0e\x32).pogoprotos.enums.CombatPlayerFinishState\x12_\n\x0e\x63ombat_rematch\x18\x07 \x01(\x0b\x32G.pogoprotos.networking.responses.GetCombatResultsResponse.CombatRematch\x1aM\n\rCombatRematch\x12\x19\n\x11\x63ombat_rematch_id\x18\x01 \x01(\t\x12!\n\x19\x63ombat_league_template_id\x18\x02 \x01(\t\"s\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x1e\n\x1a\x45RROR_INVALID_COMBAT_STATE\x10\x02\x12\x1a\n\x16\x45RROR_COMBAT_NOT_FOUND\x10\x03\x12\x15\n\x11\x45RROR_PLAYER_QUIT\x10\x04\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_combat__reward__status__pb2.DESCRIPTOR,pogoprotos_dot_inventory_dot_loot__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_friends_dot_leveled__up__friends__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_combat__player__finish__state__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_GETCOMBATRESULTSRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.GetCombatResultsResponse.Result',
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
      name='ERROR_INVALID_COMBAT_STATE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_COMBAT_NOT_FOUND', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PLAYER_QUIT', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=860,
  serialized_end=975,
)
_sym_db.RegisterEnumDescriptor(_GETCOMBATRESULTSRESPONSE_RESULT)


_GETCOMBATRESULTSRESPONSE_COMBATREMATCH = _descriptor.Descriptor(
  name='CombatRematch',
  full_name='pogoprotos.networking.responses.GetCombatResultsResponse.CombatRematch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='combat_rematch_id', full_name='pogoprotos.networking.responses.GetCombatResultsResponse.CombatRematch.combat_rematch_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='combat_league_template_id', full_name='pogoprotos.networking.responses.GetCombatResultsResponse.CombatRematch.combat_league_template_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=781,
  serialized_end=858,
)

_GETCOMBATRESULTSRESPONSE = _descriptor.Descriptor(
  name='GetCombatResultsResponse',
  full_name='pogoprotos.networking.responses.GetCombatResultsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.GetCombatResultsResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reward_status', full_name='pogoprotos.networking.responses.GetCombatResultsResponse.reward_status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rewards', full_name='pogoprotos.networking.responses.GetCombatResultsResponse.rewards', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='friend_level_up', full_name='pogoprotos.networking.responses.GetCombatResultsResponse.friend_level_up', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='number_rewarded_battles_today', full_name='pogoprotos.networking.responses.GetCombatResultsResponse.number_rewarded_battles_today', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='combat_player_finish_state', full_name='pogoprotos.networking.responses.GetCombatResultsResponse.combat_player_finish_state', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='combat_rematch', full_name='pogoprotos.networking.responses.GetCombatResultsResponse.combat_rematch', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_GETCOMBATRESULTSRESPONSE_COMBATREMATCH, ],
  enum_types=[
    _GETCOMBATRESULTSRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=282,
  serialized_end=975,
)

_GETCOMBATRESULTSRESPONSE_COMBATREMATCH.containing_type = _GETCOMBATRESULTSRESPONSE
_GETCOMBATRESULTSRESPONSE.fields_by_name['result'].enum_type = _GETCOMBATRESULTSRESPONSE_RESULT
_GETCOMBATRESULTSRESPONSE.fields_by_name['reward_status'].enum_type = pogoprotos_dot_enums_dot_combat__reward__status__pb2._COMBATREWARDSTATUS
_GETCOMBATRESULTSRESPONSE.fields_by_name['rewards'].message_type = pogoprotos_dot_inventory_dot_loot__pb2._LOOT
_GETCOMBATRESULTSRESPONSE.fields_by_name['friend_level_up'].message_type = pogoprotos_dot_data_dot_friends_dot_leveled__up__friends__pb2._LEVELEDUPFRIENDS
_GETCOMBATRESULTSRESPONSE.fields_by_name['combat_player_finish_state'].enum_type = pogoprotos_dot_enums_dot_combat__player__finish__state__pb2._COMBATPLAYERFINISHSTATE
_GETCOMBATRESULTSRESPONSE.fields_by_name['combat_rematch'].message_type = _GETCOMBATRESULTSRESPONSE_COMBATREMATCH
_GETCOMBATRESULTSRESPONSE_RESULT.containing_type = _GETCOMBATRESULTSRESPONSE
DESCRIPTOR.message_types_by_name['GetCombatResultsResponse'] = _GETCOMBATRESULTSRESPONSE

GetCombatResultsResponse = _reflection.GeneratedProtocolMessageType('GetCombatResultsResponse', (_message.Message,), dict(

  CombatRematch = _reflection.GeneratedProtocolMessageType('CombatRematch', (_message.Message,), dict(
    DESCRIPTOR = _GETCOMBATRESULTSRESPONSE_COMBATREMATCH,
    __module__ = 'pogoprotos.networking.responses.get_combat_results_response_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.GetCombatResultsResponse.CombatRematch)
    ))
  ,
  DESCRIPTOR = _GETCOMBATRESULTSRESPONSE,
  __module__ = 'pogoprotos.networking.responses.get_combat_results_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.GetCombatResultsResponse)
  ))
_sym_db.RegisterMessage(GetCombatResultsResponse)
_sym_db.RegisterMessage(GetCombatResultsResponse.CombatRematch)


# @@protoc_insertion_point(module_scope)
