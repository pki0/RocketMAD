# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/unclassed/poi_edit_image_entry_source.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/unclassed/poi_edit_image_entry_source.proto',
  package='pogoprotos.data.unclassed',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n;pogoprotos/data/unclassed/poi_edit_image_entry_source.proto\x12\x19pogoprotos.data.unclassed*s\n\x17PoiEditImageEntrySource\x12)\n%POI_EDIT_IMAGE_ENTRY_SOURCE_EDIT_MENU\x10\x00\x12-\n)POI_EDIT_IMAGE_ENTRY_SOURCE_IMAGE_GALLERY\x10\x01\x62\x06proto3')
)

_POIEDITIMAGEENTRYSOURCE = _descriptor.EnumDescriptor(
  name='PoiEditImageEntrySource',
  full_name='pogoprotos.data.unclassed.PoiEditImageEntrySource',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='POI_EDIT_IMAGE_ENTRY_SOURCE_EDIT_MENU', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POI_EDIT_IMAGE_ENTRY_SOURCE_IMAGE_GALLERY', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=90,
  serialized_end=205,
)
_sym_db.RegisterEnumDescriptor(_POIEDITIMAGEENTRYSOURCE)

PoiEditImageEntrySource = enum_type_wrapper.EnumTypeWrapper(_POIEDITIMAGEENTRYSOURCE)
POI_EDIT_IMAGE_ENTRY_SOURCE_EDIT_MENU = 0
POI_EDIT_IMAGE_ENTRY_SOURCE_IMAGE_GALLERY = 1


DESCRIPTOR.enum_types_by_name['PoiEditImageEntrySource'] = _POIEDITIMAGEENTRYSOURCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
