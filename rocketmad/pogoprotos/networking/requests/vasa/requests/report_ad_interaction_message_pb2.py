# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/vasa/requests/report_ad_interaction_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/vasa/requests/report_ad_interaction_message.proto',
  package='pogoprotos.networking.requests.vasa.requests',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nPpogoprotos/networking/requests/vasa/requests/report_ad_interaction_message.proto\x12,pogoprotos.networking.requests.vasa.requests\"\xaf\x07\n\x1aReportAdInteractionMessage\x12\x0f\n\x07game_id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x0c\n\x04guid\x18\x03 \x01(\t\x12\x1a\n\x12\x65ncrypted_ad_token\x18\x04 \x01(\x0c\x12}\n\x0fview_impression\x18\x05 \x01(\x0b\x32\x62.pogoprotos.networking.requests.vasa.requests.ReportAdInteractionMessage.ViewImpressionInteractionH\x00\x12}\n\x0fview_fullscreen\x18\x06 \x01(\x0b\x32\x62.pogoprotos.networking.requests.vasa.requests.ReportAdInteractionMessage.ViewFullscreenInteractionH\x00\x12\x80\x01\n\x16\x66ullscreen_interaction\x18\x07 \x01(\x0b\x32^.pogoprotos.networking.requests.vasa.requests.ReportAdInteractionMessage.FullScreenInteractionH\x00\x12s\n\x0b\x63ta_clicked\x18\x08 \x01(\x0b\x32\\.pogoprotos.networking.requests.vasa.requests.ReportAdInteractionMessage.CTAClickInteractionH\x00\x1a&\n\x13\x43TAClickInteraction\x12\x0f\n\x07\x63ta_url\x18\x06 \x01(\t\x1a\x85\x01\n\x15\x46ullScreenInteraction\x12\x1c\n\x14\x66ullscreen_image_url\x18\x01 \x01(\t\x12\x1f\n\x17total_residence_time_ms\x18\x02 \x01(\x03\x12\x14\n\x0ctime_away_ms\x18\x03 \x01(\x03\x12\x17\n\x0ftook_screenshot\x18\x04 \x01(\x08\x1a\x39\n\x19ViewFullscreenInteraction\x12\x1c\n\x14\x66ullscreen_image_url\x18\x01 \x01(\t\x1aQ\n\x19ViewImpressionInteraction\x12\x19\n\x11preview_image_url\x18\x01 \x01(\t\x12\x19\n\x11is_persisted_gift\x18\x02 \x01(\x08\x42\x11\n\x0fInteractionTypeb\x06proto3')
)




_REPORTADINTERACTIONMESSAGE_CTACLICKINTERACTION = _descriptor.Descriptor(
  name='CTAClickInteraction',
  full_name='pogoprotos.networking.requests.vasa.requests.ReportAdInteractionMessage.CTAClickInteraction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cta_url', full_name='pogoprotos.networking.requests.vasa.requests.ReportAdInteractionMessage.CTAClickInteraction.cta_url', index=0,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=739,
  serialized_end=777,
)

_REPORTADINTERACTIONMESSAGE_FULLSCREENINTERACTION = _descriptor.Descriptor(
  name='FullScreenInteraction',
  full_name='pogoprotos.networking.requests.vasa.requests.ReportAdInteractionMessage.FullScreenInteraction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fullscreen_image_url', full_name='pogoprotos.networking.requests.vasa.requests.ReportAdInteractionMessage.FullScreenInteraction.fullscreen_image_url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_residence_time_ms', full_name='pogoprotos.networking.requests.vasa.requests.ReportAdInteractionMessage.FullScreenInteraction.total_residence_time_ms', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_away_ms', full_name='pogoprotos.networking.requests.vasa.requests.ReportAdInteractionMessage.FullScreenInteraction.time_away_ms', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='took_screenshot', full_name='pogoprotos.networking.requests.vasa.requests.ReportAdInteractionMessage.FullScreenInteraction.took_screenshot', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=780,
  serialized_end=913,
)

_REPORTADINTERACTIONMESSAGE_VIEWFULLSCREENINTERACTION = _descriptor.Descriptor(
  name='ViewFullscreenInteraction',
  full_name='pogoprotos.networking.requests.vasa.requests.ReportAdInteractionMessage.ViewFullscreenInteraction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fullscreen_image_url', full_name='pogoprotos.networking.requests.vasa.requests.ReportAdInteractionMessage.ViewFullscreenInteraction.fullscreen_image_url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=915,
  serialized_end=972,
)

_REPORTADINTERACTIONMESSAGE_VIEWIMPRESSIONINTERACTION = _descriptor.Descriptor(
  name='ViewImpressionInteraction',
  full_name='pogoprotos.networking.requests.vasa.requests.ReportAdInteractionMessage.ViewImpressionInteraction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='preview_image_url', full_name='pogoprotos.networking.requests.vasa.requests.ReportAdInteractionMessage.ViewImpressionInteraction.preview_image_url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_persisted_gift', full_name='pogoprotos.networking.requests.vasa.requests.ReportAdInteractionMessage.ViewImpressionInteraction.is_persisted_gift', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=974,
  serialized_end=1055,
)

_REPORTADINTERACTIONMESSAGE = _descriptor.Descriptor(
  name='ReportAdInteractionMessage',
  full_name='pogoprotos.networking.requests.vasa.requests.ReportAdInteractionMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='game_id', full_name='pogoprotos.networking.requests.vasa.requests.ReportAdInteractionMessage.game_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='pogoprotos.networking.requests.vasa.requests.ReportAdInteractionMessage.user_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='guid', full_name='pogoprotos.networking.requests.vasa.requests.ReportAdInteractionMessage.guid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encrypted_ad_token', full_name='pogoprotos.networking.requests.vasa.requests.ReportAdInteractionMessage.encrypted_ad_token', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='view_impression', full_name='pogoprotos.networking.requests.vasa.requests.ReportAdInteractionMessage.view_impression', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='view_fullscreen', full_name='pogoprotos.networking.requests.vasa.requests.ReportAdInteractionMessage.view_fullscreen', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fullscreen_interaction', full_name='pogoprotos.networking.requests.vasa.requests.ReportAdInteractionMessage.fullscreen_interaction', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cta_clicked', full_name='pogoprotos.networking.requests.vasa.requests.ReportAdInteractionMessage.cta_clicked', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_REPORTADINTERACTIONMESSAGE_CTACLICKINTERACTION, _REPORTADINTERACTIONMESSAGE_FULLSCREENINTERACTION, _REPORTADINTERACTIONMESSAGE_VIEWFULLSCREENINTERACTION, _REPORTADINTERACTIONMESSAGE_VIEWIMPRESSIONINTERACTION, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='InteractionType', full_name='pogoprotos.networking.requests.vasa.requests.ReportAdInteractionMessage.InteractionType',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=131,
  serialized_end=1074,
)

_REPORTADINTERACTIONMESSAGE_CTACLICKINTERACTION.containing_type = _REPORTADINTERACTIONMESSAGE
_REPORTADINTERACTIONMESSAGE_FULLSCREENINTERACTION.containing_type = _REPORTADINTERACTIONMESSAGE
_REPORTADINTERACTIONMESSAGE_VIEWFULLSCREENINTERACTION.containing_type = _REPORTADINTERACTIONMESSAGE
_REPORTADINTERACTIONMESSAGE_VIEWIMPRESSIONINTERACTION.containing_type = _REPORTADINTERACTIONMESSAGE
_REPORTADINTERACTIONMESSAGE.fields_by_name['view_impression'].message_type = _REPORTADINTERACTIONMESSAGE_VIEWIMPRESSIONINTERACTION
_REPORTADINTERACTIONMESSAGE.fields_by_name['view_fullscreen'].message_type = _REPORTADINTERACTIONMESSAGE_VIEWFULLSCREENINTERACTION
_REPORTADINTERACTIONMESSAGE.fields_by_name['fullscreen_interaction'].message_type = _REPORTADINTERACTIONMESSAGE_FULLSCREENINTERACTION
_REPORTADINTERACTIONMESSAGE.fields_by_name['cta_clicked'].message_type = _REPORTADINTERACTIONMESSAGE_CTACLICKINTERACTION
_REPORTADINTERACTIONMESSAGE.oneofs_by_name['InteractionType'].fields.append(
  _REPORTADINTERACTIONMESSAGE.fields_by_name['view_impression'])
_REPORTADINTERACTIONMESSAGE.fields_by_name['view_impression'].containing_oneof = _REPORTADINTERACTIONMESSAGE.oneofs_by_name['InteractionType']
_REPORTADINTERACTIONMESSAGE.oneofs_by_name['InteractionType'].fields.append(
  _REPORTADINTERACTIONMESSAGE.fields_by_name['view_fullscreen'])
_REPORTADINTERACTIONMESSAGE.fields_by_name['view_fullscreen'].containing_oneof = _REPORTADINTERACTIONMESSAGE.oneofs_by_name['InteractionType']
_REPORTADINTERACTIONMESSAGE.oneofs_by_name['InteractionType'].fields.append(
  _REPORTADINTERACTIONMESSAGE.fields_by_name['fullscreen_interaction'])
_REPORTADINTERACTIONMESSAGE.fields_by_name['fullscreen_interaction'].containing_oneof = _REPORTADINTERACTIONMESSAGE.oneofs_by_name['InteractionType']
_REPORTADINTERACTIONMESSAGE.oneofs_by_name['InteractionType'].fields.append(
  _REPORTADINTERACTIONMESSAGE.fields_by_name['cta_clicked'])
_REPORTADINTERACTIONMESSAGE.fields_by_name['cta_clicked'].containing_oneof = _REPORTADINTERACTIONMESSAGE.oneofs_by_name['InteractionType']
DESCRIPTOR.message_types_by_name['ReportAdInteractionMessage'] = _REPORTADINTERACTIONMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReportAdInteractionMessage = _reflection.GeneratedProtocolMessageType('ReportAdInteractionMessage', (_message.Message,), dict(

  CTAClickInteraction = _reflection.GeneratedProtocolMessageType('CTAClickInteraction', (_message.Message,), dict(
    DESCRIPTOR = _REPORTADINTERACTIONMESSAGE_CTACLICKINTERACTION,
    __module__ = 'pogoprotos.networking.requests.vasa.requests.report_ad_interaction_message_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.vasa.requests.ReportAdInteractionMessage.CTAClickInteraction)
    ))
  ,

  FullScreenInteraction = _reflection.GeneratedProtocolMessageType('FullScreenInteraction', (_message.Message,), dict(
    DESCRIPTOR = _REPORTADINTERACTIONMESSAGE_FULLSCREENINTERACTION,
    __module__ = 'pogoprotos.networking.requests.vasa.requests.report_ad_interaction_message_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.vasa.requests.ReportAdInteractionMessage.FullScreenInteraction)
    ))
  ,

  ViewFullscreenInteraction = _reflection.GeneratedProtocolMessageType('ViewFullscreenInteraction', (_message.Message,), dict(
    DESCRIPTOR = _REPORTADINTERACTIONMESSAGE_VIEWFULLSCREENINTERACTION,
    __module__ = 'pogoprotos.networking.requests.vasa.requests.report_ad_interaction_message_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.vasa.requests.ReportAdInteractionMessage.ViewFullscreenInteraction)
    ))
  ,

  ViewImpressionInteraction = _reflection.GeneratedProtocolMessageType('ViewImpressionInteraction', (_message.Message,), dict(
    DESCRIPTOR = _REPORTADINTERACTIONMESSAGE_VIEWIMPRESSIONINTERACTION,
    __module__ = 'pogoprotos.networking.requests.vasa.requests.report_ad_interaction_message_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.vasa.requests.ReportAdInteractionMessage.ViewImpressionInteraction)
    ))
  ,
  DESCRIPTOR = _REPORTADINTERACTIONMESSAGE,
  __module__ = 'pogoprotos.networking.requests.vasa.requests.report_ad_interaction_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.vasa.requests.ReportAdInteractionMessage)
  ))
_sym_db.RegisterMessage(ReportAdInteractionMessage)
_sym_db.RegisterMessage(ReportAdInteractionMessage.CTAClickInteraction)
_sym_db.RegisterMessage(ReportAdInteractionMessage.FullScreenInteraction)
_sym_db.RegisterMessage(ReportAdInteractionMessage.ViewFullscreenInteraction)
_sym_db.RegisterMessage(ReportAdInteractionMessage.ViewImpressionInteraction)


# @@protoc_insertion_point(module_scope)
