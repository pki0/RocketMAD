# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/game/gamepoi/requests/submit_sponsor_poi_report_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/game/gamepoi/requests/submit_sponsor_poi_report_message.proto',
  package='pogoprotos.networking.requests.game.gamepoi.requests',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\\pogoprotos/networking/requests/game/gamepoi/requests/submit_sponsor_poi_report_message.proto\x12\x34pogoprotos.networking.requests.game.gamepoi.requests\"\xd4\x03\n\x1dSubmitSponsorPoiReportMessage\x12\x0e\n\x06poi_id\x18\x01 \x01(\t\x12\x83\x01\n\x0einvalid_reason\x18\x02 \x01(\x0e\x32k.pogoprotos.networking.requests.game.gamepoi.requests.SubmitSponsorPoiReportMessage.SponsorPoiInvalidReason\x12\x1a\n\x12\x61\x64\x64itional_details\x18\x03 \x01(\t\"\x80\x02\n\x17SponsorPoiInvalidReason\x12\"\n\x1eSPONSOR_POI_REASON_UNSPECIFIED\x10\x00\x12%\n!SPONSOR_POI_REASON_DOES_NOT_EXIST\x10\x01\x12\x1f\n\x1bSPONSOR_POI_REASON_NOT_SAFE\x10\x02\x12#\n\x1fSPONSOR_POI_REASON_NOT_TRUTHFUL\x10\x03\x12*\n&SPONSOR_POI_REASON_NOT_FAMILY_FRIENDLY\x10\x04\x12(\n$SPONSOR_POI_REASON_OFFENSIVE_CONTENT\x10\x05\x62\x06proto3')
)



_SUBMITSPONSORPOIREPORTMESSAGE_SPONSORPOIINVALIDREASON = _descriptor.EnumDescriptor(
  name='SponsorPoiInvalidReason',
  full_name='pogoprotos.networking.requests.game.gamepoi.requests.SubmitSponsorPoiReportMessage.SponsorPoiInvalidReason',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SPONSOR_POI_REASON_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPONSOR_POI_REASON_DOES_NOT_EXIST', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPONSOR_POI_REASON_NOT_SAFE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPONSOR_POI_REASON_NOT_TRUTHFUL', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPONSOR_POI_REASON_NOT_FAMILY_FRIENDLY', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPONSOR_POI_REASON_OFFENSIVE_CONTENT', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=363,
  serialized_end=619,
)
_sym_db.RegisterEnumDescriptor(_SUBMITSPONSORPOIREPORTMESSAGE_SPONSORPOIINVALIDREASON)


_SUBMITSPONSORPOIREPORTMESSAGE = _descriptor.Descriptor(
  name='SubmitSponsorPoiReportMessage',
  full_name='pogoprotos.networking.requests.game.gamepoi.requests.SubmitSponsorPoiReportMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='poi_id', full_name='pogoprotos.networking.requests.game.gamepoi.requests.SubmitSponsorPoiReportMessage.poi_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='invalid_reason', full_name='pogoprotos.networking.requests.game.gamepoi.requests.SubmitSponsorPoiReportMessage.invalid_reason', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='additional_details', full_name='pogoprotos.networking.requests.game.gamepoi.requests.SubmitSponsorPoiReportMessage.additional_details', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SUBMITSPONSORPOIREPORTMESSAGE_SPONSORPOIINVALIDREASON,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=151,
  serialized_end=619,
)

_SUBMITSPONSORPOIREPORTMESSAGE.fields_by_name['invalid_reason'].enum_type = _SUBMITSPONSORPOIREPORTMESSAGE_SPONSORPOIINVALIDREASON
_SUBMITSPONSORPOIREPORTMESSAGE_SPONSORPOIINVALIDREASON.containing_type = _SUBMITSPONSORPOIREPORTMESSAGE
DESCRIPTOR.message_types_by_name['SubmitSponsorPoiReportMessage'] = _SUBMITSPONSORPOIREPORTMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SubmitSponsorPoiReportMessage = _reflection.GeneratedProtocolMessageType('SubmitSponsorPoiReportMessage', (_message.Message,), dict(
  DESCRIPTOR = _SUBMITSPONSORPOIREPORTMESSAGE,
  __module__ = 'pogoprotos.networking.requests.game.gamepoi.requests.submit_sponsor_poi_report_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.game.gamepoi.requests.SubmitSponsorPoiReportMessage)
  ))
_sym_db.RegisterMessage(SubmitSponsorPoiReportMessage)


# @@protoc_insertion_point(module_scope)
