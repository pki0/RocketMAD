# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/route/route_checkpoint.proto

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
  name='pogoprotos/data/route/route_checkpoint.proto',
  package='pogoprotos.data.route',
  syntax='proto3',
  serialized_pb=_b('\n,pogoprotos/data/route/route_checkpoint.proto\x12\x15pogoprotos.data.route\"\x96\x03\n\x0fRouteCheckpoint\x12>\n\x03poi\x18\x01 \x01(\x0b\x32/.pogoprotos.data.route.RouteCheckpoint.RoutePoiH\x00\x12J\n\tguidepost\x18\x02 \x01(\x0b\x32\x35.pogoprotos.data.route.RouteCheckpoint.RouteGuidepostH\x00\x1a\x1a\n\x08RoutePoi\x12\x0e\n\x06poi_id\x18\x01 \x01(\t\x1aU\n\x0eRouteGuidepost\x12\x43\n\x08location\x18\x01 \x01(\x0b\x32\x31.pogoprotos.data.route.RouteCheckpoint.LocationE6\x1a\x43\n\nRouteImage\x12\x12\n\x08image_id\x18\x01 \x01(\tH\x00\x12\x17\n\rimage_context\x18\x02 \x01(\tH\x00\x42\x08\n\x06Source\x1a\x37\n\nLocationE6\x12\x13\n\x0blatitude_e6\x18\x01 \x01(\x05\x12\x14\n\x0clongitude_e6\x18\x02 \x01(\x05\x42\x06\n\x04Typeb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ROUTECHECKPOINT_ROUTEPOI = _descriptor.Descriptor(
  name='RoutePoi',
  full_name='pogoprotos.data.route.RouteCheckpoint.RoutePoi',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='poi_id', full_name='pogoprotos.data.route.RouteCheckpoint.RoutePoi.poi_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=231,
  serialized_end=257,
)

_ROUTECHECKPOINT_ROUTEGUIDEPOST = _descriptor.Descriptor(
  name='RouteGuidepost',
  full_name='pogoprotos.data.route.RouteCheckpoint.RouteGuidepost',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='location', full_name='pogoprotos.data.route.RouteCheckpoint.RouteGuidepost.location', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=259,
  serialized_end=344,
)

_ROUTECHECKPOINT_ROUTEIMAGE = _descriptor.Descriptor(
  name='RouteImage',
  full_name='pogoprotos.data.route.RouteCheckpoint.RouteImage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='image_id', full_name='pogoprotos.data.route.RouteCheckpoint.RouteImage.image_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='image_context', full_name='pogoprotos.data.route.RouteCheckpoint.RouteImage.image_context', index=1,
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
    _descriptor.OneofDescriptor(
      name='Source', full_name='pogoprotos.data.route.RouteCheckpoint.RouteImage.Source',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=346,
  serialized_end=413,
)

_ROUTECHECKPOINT_LOCATIONE6 = _descriptor.Descriptor(
  name='LocationE6',
  full_name='pogoprotos.data.route.RouteCheckpoint.LocationE6',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='latitude_e6', full_name='pogoprotos.data.route.RouteCheckpoint.LocationE6.latitude_e6', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude_e6', full_name='pogoprotos.data.route.RouteCheckpoint.LocationE6.longitude_e6', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=415,
  serialized_end=470,
)

_ROUTECHECKPOINT = _descriptor.Descriptor(
  name='RouteCheckpoint',
  full_name='pogoprotos.data.route.RouteCheckpoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='poi', full_name='pogoprotos.data.route.RouteCheckpoint.poi', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='guidepost', full_name='pogoprotos.data.route.RouteCheckpoint.guidepost', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ROUTECHECKPOINT_ROUTEPOI, _ROUTECHECKPOINT_ROUTEGUIDEPOST, _ROUTECHECKPOINT_ROUTEIMAGE, _ROUTECHECKPOINT_LOCATIONE6, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='Type', full_name='pogoprotos.data.route.RouteCheckpoint.Type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=72,
  serialized_end=478,
)

_ROUTECHECKPOINT_ROUTEPOI.containing_type = _ROUTECHECKPOINT
_ROUTECHECKPOINT_ROUTEGUIDEPOST.fields_by_name['location'].message_type = _ROUTECHECKPOINT_LOCATIONE6
_ROUTECHECKPOINT_ROUTEGUIDEPOST.containing_type = _ROUTECHECKPOINT
_ROUTECHECKPOINT_ROUTEIMAGE.containing_type = _ROUTECHECKPOINT
_ROUTECHECKPOINT_ROUTEIMAGE.oneofs_by_name['Source'].fields.append(
  _ROUTECHECKPOINT_ROUTEIMAGE.fields_by_name['image_id'])
_ROUTECHECKPOINT_ROUTEIMAGE.fields_by_name['image_id'].containing_oneof = _ROUTECHECKPOINT_ROUTEIMAGE.oneofs_by_name['Source']
_ROUTECHECKPOINT_ROUTEIMAGE.oneofs_by_name['Source'].fields.append(
  _ROUTECHECKPOINT_ROUTEIMAGE.fields_by_name['image_context'])
_ROUTECHECKPOINT_ROUTEIMAGE.fields_by_name['image_context'].containing_oneof = _ROUTECHECKPOINT_ROUTEIMAGE.oneofs_by_name['Source']
_ROUTECHECKPOINT_LOCATIONE6.containing_type = _ROUTECHECKPOINT
_ROUTECHECKPOINT.fields_by_name['poi'].message_type = _ROUTECHECKPOINT_ROUTEPOI
_ROUTECHECKPOINT.fields_by_name['guidepost'].message_type = _ROUTECHECKPOINT_ROUTEGUIDEPOST
_ROUTECHECKPOINT.oneofs_by_name['Type'].fields.append(
  _ROUTECHECKPOINT.fields_by_name['poi'])
_ROUTECHECKPOINT.fields_by_name['poi'].containing_oneof = _ROUTECHECKPOINT.oneofs_by_name['Type']
_ROUTECHECKPOINT.oneofs_by_name['Type'].fields.append(
  _ROUTECHECKPOINT.fields_by_name['guidepost'])
_ROUTECHECKPOINT.fields_by_name['guidepost'].containing_oneof = _ROUTECHECKPOINT.oneofs_by_name['Type']
DESCRIPTOR.message_types_by_name['RouteCheckpoint'] = _ROUTECHECKPOINT

RouteCheckpoint = _reflection.GeneratedProtocolMessageType('RouteCheckpoint', (_message.Message,), dict(

  RoutePoi = _reflection.GeneratedProtocolMessageType('RoutePoi', (_message.Message,), dict(
    DESCRIPTOR = _ROUTECHECKPOINT_ROUTEPOI,
    __module__ = 'pogoprotos.data.route.route_checkpoint_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.data.route.RouteCheckpoint.RoutePoi)
    ))
  ,

  RouteGuidepost = _reflection.GeneratedProtocolMessageType('RouteGuidepost', (_message.Message,), dict(
    DESCRIPTOR = _ROUTECHECKPOINT_ROUTEGUIDEPOST,
    __module__ = 'pogoprotos.data.route.route_checkpoint_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.data.route.RouteCheckpoint.RouteGuidepost)
    ))
  ,

  RouteImage = _reflection.GeneratedProtocolMessageType('RouteImage', (_message.Message,), dict(
    DESCRIPTOR = _ROUTECHECKPOINT_ROUTEIMAGE,
    __module__ = 'pogoprotos.data.route.route_checkpoint_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.data.route.RouteCheckpoint.RouteImage)
    ))
  ,

  LocationE6 = _reflection.GeneratedProtocolMessageType('LocationE6', (_message.Message,), dict(
    DESCRIPTOR = _ROUTECHECKPOINT_LOCATIONE6,
    __module__ = 'pogoprotos.data.route.route_checkpoint_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.data.route.RouteCheckpoint.LocationE6)
    ))
  ,
  DESCRIPTOR = _ROUTECHECKPOINT,
  __module__ = 'pogoprotos.data.route.route_checkpoint_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.route.RouteCheckpoint)
  ))
_sym_db.RegisterMessage(RouteCheckpoint)
_sym_db.RegisterMessage(RouteCheckpoint.RoutePoi)
_sym_db.RegisterMessage(RouteCheckpoint.RouteGuidepost)
_sym_db.RegisterMessage(RouteCheckpoint.RouteImage)
_sym_db.RegisterMessage(RouteCheckpoint.LocationE6)


# @@protoc_insertion_point(module_scope)