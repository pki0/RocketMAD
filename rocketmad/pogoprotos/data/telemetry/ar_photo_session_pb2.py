# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/telemetry/ar_photo_session.proto

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
  name='pogoprotos/data/telemetry/ar_photo_session.proto',
  package='pogoprotos.data.telemetry',
  syntax='proto3',
  serialized_pb=_b('\n0pogoprotos/data/telemetry/ar_photo_session.proto\x12\x19pogoprotos.data.telemetry\"\x9c\x0f\n\x0e\x41rPhotoSession\x12\x41\n\x07\x61r_type\x18\x01 \x01(\x0e\x32\x30.pogoprotos.data.telemetry.ArPhotoSession.ArType\x12O\n\x17\x66urthest_step_completed\x18\x02 \x01(\x0e\x32..pogoprotos.data.telemetry.ArPhotoSession.Step\x12\x18\n\x10num_photos_taken\x18\x03 \x01(\x05\x12\x19\n\x11num_photos_shared\x18\x04 \x01(\x05\x12#\n\x1bnum_photos_taken_occlusions\x18\x05 \x01(\x05\x12\x1e\n\x16num_occlusions_enabled\x18\x06 \x01(\x05\x12\x1f\n\x17num_occlusions_disabled\x18\x07 \x01(\x05\x12G\n\nar_context\x18\x08 \x01(\x0e\x32\x33.pogoprotos.data.telemetry.ArPhotoSession.ArContext\x12\x16\n\x0esession_length\x18\t \x01(\x03\x12!\n\x19session_length_occlusions\x18\n \x01(\x03\x12$\n\x1cnum_photos_shared_occlusions\x18\x0b \x01(\x05\x12\x11\n\tmodel_url\x18\x0c \x01(\t\x12\x14\n\x0c\x61rdk_version\x18\r \x01(\t\x12\x19\n\x11\x61verage_framerate\x18\x0e \x01(\x05\x12\x1f\n\x17\x61verage_battery_per_min\x18\x0f \x01(\x02\x12\x19\n\x11\x61verage_cpu_usage\x18\x10 \x01(\x02\x12\x19\n\x11\x61verage_gpu_usage\x18\x11 \x01(\x02\x12T\n\x11\x66ramerate_samples\x18\x12 \x03(\x0b\x32\x39.pogoprotos.data.telemetry.ArPhotoSession.FramerateSample\x12P\n\x0f\x62\x61ttery_samples\x18\x13 \x03(\x0b\x32\x37.pogoprotos.data.telemetry.ArPhotoSession.BatterySample\x12T\n\x11processor_samples\x18\x14 \x03(\x0b\x32\x39.pogoprotos.data.telemetry.ArPhotoSession.ProcessorSample\x12+\n#session_start_to_plane_detection_ms\x18\x15 \x01(\x05\x12.\n&plane_detection_to_user_interaction_ms\x18\x16 \x01(\x05\x1a\x86\x01\n\x0c\x41rConditions\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12\x1a\n\x12occlusions_enabled\x18\x02 \x01(\x08\x12G\n\x0f\x63urrent_ar_step\x18\x03 \x01(\x0e\x32..pogoprotos.data.telemetry.ArPhotoSession.Step\x1a\xbb\x01\n\rBatterySample\x12J\n\nconditions\x18\x01 \x01(\x0b\x32\x36.pogoprotos.data.telemetry.ArPhotoSession.ArConditions\x12\x15\n\rbattery_level\x18\x02 \x01(\x02\x12G\n\x06status\x18\x03 \x01(\x0e\x32\x37.pogoprotos.data.telemetry.ArPhotoSession.BatteryStatus\x1ap\n\x0f\x46ramerateSample\x12J\n\nconditions\x18\x01 \x01(\x0b\x32\x36.pogoprotos.data.telemetry.ArPhotoSession.ArConditions\x12\x11\n\tframerate\x18\x02 \x01(\x05\x1a\x83\x01\n\x0fProcessorSample\x12J\n\nconditions\x18\x01 \x01(\x0b\x32\x36.pogoprotos.data.telemetry.ArPhotoSession.ArConditions\x12\x11\n\tcpu_usage\x18\x02 \x01(\x02\x12\x11\n\tgpu_usage\x18\x03 \x01(\x02\"\\\n\rBatteryStatus\x12\x10\n\x0cUNDETERMINED\x10\x00\x12\x0c\n\x08\x43HARGING\x10\x01\x12\x0f\n\x0b\x44ISCHARGING\x10\x02\x12\x10\n\x0cNOT_CHARGING\x10\x03\x12\x08\n\x04\x46ULL\x10\x04\"g\n\tArContext\x12\x08\n\x04NONE\x10\x00\x12\x10\n\x0c\x41R_ENCOUNTER\x10\x01\x12\x0f\n\x0b\x41R_SNAPSHOT\x10\x02\x12\x16\n\x12SINGLEPLAYER_BUDDY\x10\x03\x12\x15\n\x11MULTIPLAYER_BUDDY\x10\x04\"*\n\x06\x41rType\x12\t\n\x05UNSET\x10\x00\x12\x08\n\x04PLUS\x10\x01\x12\x0b\n\x07\x43LASSIC\x10\x02\"\x88\x01\n\x04Step\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x1d\n\x19\x43\x41MERA_PERMISSION_GRANTED\x10\x01\x12\x16\n\x12\x41RPLUS_PLANE_FOUND\x10\x02\x12\x19\n\x15\x41RPLUS_POKEMON_PLACED\x10\x03\x12\x0f\n\x0bPHOTO_TAKEN\x10\x04\x12\x10\n\x0cPHOTO_SHARED\x10\x05\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_ARPHOTOSESSION_BATTERYSTATUS = _descriptor.EnumDescriptor(
  name='BatteryStatus',
  full_name='pogoprotos.data.telemetry.ArPhotoSession.BatteryStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDETERMINED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARGING', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISCHARGING', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_CHARGING', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FULL', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1648,
  serialized_end=1740,
)
_sym_db.RegisterEnumDescriptor(_ARPHOTOSESSION_BATTERYSTATUS)

_ARPHOTOSESSION_ARCONTEXT = _descriptor.EnumDescriptor(
  name='ArContext',
  full_name='pogoprotos.data.telemetry.ArPhotoSession.ArContext',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AR_ENCOUNTER', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AR_SNAPSHOT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SINGLEPLAYER_BUDDY', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MULTIPLAYER_BUDDY', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1742,
  serialized_end=1845,
)
_sym_db.RegisterEnumDescriptor(_ARPHOTOSESSION_ARCONTEXT)

_ARPHOTOSESSION_ARTYPE = _descriptor.EnumDescriptor(
  name='ArType',
  full_name='pogoprotos.data.telemetry.ArPhotoSession.ArType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLUS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLASSIC', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1847,
  serialized_end=1889,
)
_sym_db.RegisterEnumDescriptor(_ARPHOTOSESSION_ARTYPE)

_ARPHOTOSESSION_STEP = _descriptor.EnumDescriptor(
  name='Step',
  full_name='pogoprotos.data.telemetry.ArPhotoSession.Step',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAMERA_PERMISSION_GRANTED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARPLUS_PLANE_FOUND', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARPLUS_POKEMON_PLACED', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHOTO_TAKEN', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHOTO_SHARED', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1892,
  serialized_end=2028,
)
_sym_db.RegisterEnumDescriptor(_ARPHOTOSESSION_STEP)


_ARPHOTOSESSION_ARCONDITIONS = _descriptor.Descriptor(
  name='ArConditions',
  full_name='pogoprotos.data.telemetry.ArPhotoSession.ArConditions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='pogoprotos.data.telemetry.ArPhotoSession.ArConditions.timestamp', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='occlusions_enabled', full_name='pogoprotos.data.telemetry.ArPhotoSession.ArConditions.occlusions_enabled', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_ar_step', full_name='pogoprotos.data.telemetry.ArPhotoSession.ArConditions.current_ar_step', index=2,
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
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1074,
  serialized_end=1208,
)

_ARPHOTOSESSION_BATTERYSAMPLE = _descriptor.Descriptor(
  name='BatterySample',
  full_name='pogoprotos.data.telemetry.ArPhotoSession.BatterySample',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='conditions', full_name='pogoprotos.data.telemetry.ArPhotoSession.BatterySample.conditions', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battery_level', full_name='pogoprotos.data.telemetry.ArPhotoSession.BatterySample.battery_level', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='pogoprotos.data.telemetry.ArPhotoSession.BatterySample.status', index=2,
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
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1211,
  serialized_end=1398,
)

_ARPHOTOSESSION_FRAMERATESAMPLE = _descriptor.Descriptor(
  name='FramerateSample',
  full_name='pogoprotos.data.telemetry.ArPhotoSession.FramerateSample',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='conditions', full_name='pogoprotos.data.telemetry.ArPhotoSession.FramerateSample.conditions', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='framerate', full_name='pogoprotos.data.telemetry.ArPhotoSession.FramerateSample.framerate', index=1,
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
  serialized_start=1400,
  serialized_end=1512,
)

_ARPHOTOSESSION_PROCESSORSAMPLE = _descriptor.Descriptor(
  name='ProcessorSample',
  full_name='pogoprotos.data.telemetry.ArPhotoSession.ProcessorSample',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='conditions', full_name='pogoprotos.data.telemetry.ArPhotoSession.ProcessorSample.conditions', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cpu_usage', full_name='pogoprotos.data.telemetry.ArPhotoSession.ProcessorSample.cpu_usage', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gpu_usage', full_name='pogoprotos.data.telemetry.ArPhotoSession.ProcessorSample.gpu_usage', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=1515,
  serialized_end=1646,
)

_ARPHOTOSESSION = _descriptor.Descriptor(
  name='ArPhotoSession',
  full_name='pogoprotos.data.telemetry.ArPhotoSession',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ar_type', full_name='pogoprotos.data.telemetry.ArPhotoSession.ar_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='furthest_step_completed', full_name='pogoprotos.data.telemetry.ArPhotoSession.furthest_step_completed', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_photos_taken', full_name='pogoprotos.data.telemetry.ArPhotoSession.num_photos_taken', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_photos_shared', full_name='pogoprotos.data.telemetry.ArPhotoSession.num_photos_shared', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_photos_taken_occlusions', full_name='pogoprotos.data.telemetry.ArPhotoSession.num_photos_taken_occlusions', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_occlusions_enabled', full_name='pogoprotos.data.telemetry.ArPhotoSession.num_occlusions_enabled', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_occlusions_disabled', full_name='pogoprotos.data.telemetry.ArPhotoSession.num_occlusions_disabled', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ar_context', full_name='pogoprotos.data.telemetry.ArPhotoSession.ar_context', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session_length', full_name='pogoprotos.data.telemetry.ArPhotoSession.session_length', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session_length_occlusions', full_name='pogoprotos.data.telemetry.ArPhotoSession.session_length_occlusions', index=9,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_photos_shared_occlusions', full_name='pogoprotos.data.telemetry.ArPhotoSession.num_photos_shared_occlusions', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='model_url', full_name='pogoprotos.data.telemetry.ArPhotoSession.model_url', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ardk_version', full_name='pogoprotos.data.telemetry.ArPhotoSession.ardk_version', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='average_framerate', full_name='pogoprotos.data.telemetry.ArPhotoSession.average_framerate', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='average_battery_per_min', full_name='pogoprotos.data.telemetry.ArPhotoSession.average_battery_per_min', index=14,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='average_cpu_usage', full_name='pogoprotos.data.telemetry.ArPhotoSession.average_cpu_usage', index=15,
      number=16, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='average_gpu_usage', full_name='pogoprotos.data.telemetry.ArPhotoSession.average_gpu_usage', index=16,
      number=17, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='framerate_samples', full_name='pogoprotos.data.telemetry.ArPhotoSession.framerate_samples', index=17,
      number=18, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battery_samples', full_name='pogoprotos.data.telemetry.ArPhotoSession.battery_samples', index=18,
      number=19, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='processor_samples', full_name='pogoprotos.data.telemetry.ArPhotoSession.processor_samples', index=19,
      number=20, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session_start_to_plane_detection_ms', full_name='pogoprotos.data.telemetry.ArPhotoSession.session_start_to_plane_detection_ms', index=20,
      number=21, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='plane_detection_to_user_interaction_ms', full_name='pogoprotos.data.telemetry.ArPhotoSession.plane_detection_to_user_interaction_ms', index=21,
      number=22, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ARPHOTOSESSION_ARCONDITIONS, _ARPHOTOSESSION_BATTERYSAMPLE, _ARPHOTOSESSION_FRAMERATESAMPLE, _ARPHOTOSESSION_PROCESSORSAMPLE, ],
  enum_types=[
    _ARPHOTOSESSION_BATTERYSTATUS,
    _ARPHOTOSESSION_ARCONTEXT,
    _ARPHOTOSESSION_ARTYPE,
    _ARPHOTOSESSION_STEP,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=80,
  serialized_end=2028,
)

_ARPHOTOSESSION_ARCONDITIONS.fields_by_name['current_ar_step'].enum_type = _ARPHOTOSESSION_STEP
_ARPHOTOSESSION_ARCONDITIONS.containing_type = _ARPHOTOSESSION
_ARPHOTOSESSION_BATTERYSAMPLE.fields_by_name['conditions'].message_type = _ARPHOTOSESSION_ARCONDITIONS
_ARPHOTOSESSION_BATTERYSAMPLE.fields_by_name['status'].enum_type = _ARPHOTOSESSION_BATTERYSTATUS
_ARPHOTOSESSION_BATTERYSAMPLE.containing_type = _ARPHOTOSESSION
_ARPHOTOSESSION_FRAMERATESAMPLE.fields_by_name['conditions'].message_type = _ARPHOTOSESSION_ARCONDITIONS
_ARPHOTOSESSION_FRAMERATESAMPLE.containing_type = _ARPHOTOSESSION
_ARPHOTOSESSION_PROCESSORSAMPLE.fields_by_name['conditions'].message_type = _ARPHOTOSESSION_ARCONDITIONS
_ARPHOTOSESSION_PROCESSORSAMPLE.containing_type = _ARPHOTOSESSION
_ARPHOTOSESSION.fields_by_name['ar_type'].enum_type = _ARPHOTOSESSION_ARTYPE
_ARPHOTOSESSION.fields_by_name['furthest_step_completed'].enum_type = _ARPHOTOSESSION_STEP
_ARPHOTOSESSION.fields_by_name['ar_context'].enum_type = _ARPHOTOSESSION_ARCONTEXT
_ARPHOTOSESSION.fields_by_name['framerate_samples'].message_type = _ARPHOTOSESSION_FRAMERATESAMPLE
_ARPHOTOSESSION.fields_by_name['battery_samples'].message_type = _ARPHOTOSESSION_BATTERYSAMPLE
_ARPHOTOSESSION.fields_by_name['processor_samples'].message_type = _ARPHOTOSESSION_PROCESSORSAMPLE
_ARPHOTOSESSION_BATTERYSTATUS.containing_type = _ARPHOTOSESSION
_ARPHOTOSESSION_ARCONTEXT.containing_type = _ARPHOTOSESSION
_ARPHOTOSESSION_ARTYPE.containing_type = _ARPHOTOSESSION
_ARPHOTOSESSION_STEP.containing_type = _ARPHOTOSESSION
DESCRIPTOR.message_types_by_name['ArPhotoSession'] = _ARPHOTOSESSION

ArPhotoSession = _reflection.GeneratedProtocolMessageType('ArPhotoSession', (_message.Message,), dict(

  ArConditions = _reflection.GeneratedProtocolMessageType('ArConditions', (_message.Message,), dict(
    DESCRIPTOR = _ARPHOTOSESSION_ARCONDITIONS,
    __module__ = 'pogoprotos.data.telemetry.ar_photo_session_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.ArPhotoSession.ArConditions)
    ))
  ,

  BatterySample = _reflection.GeneratedProtocolMessageType('BatterySample', (_message.Message,), dict(
    DESCRIPTOR = _ARPHOTOSESSION_BATTERYSAMPLE,
    __module__ = 'pogoprotos.data.telemetry.ar_photo_session_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.ArPhotoSession.BatterySample)
    ))
  ,

  FramerateSample = _reflection.GeneratedProtocolMessageType('FramerateSample', (_message.Message,), dict(
    DESCRIPTOR = _ARPHOTOSESSION_FRAMERATESAMPLE,
    __module__ = 'pogoprotos.data.telemetry.ar_photo_session_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.ArPhotoSession.FramerateSample)
    ))
  ,

  ProcessorSample = _reflection.GeneratedProtocolMessageType('ProcessorSample', (_message.Message,), dict(
    DESCRIPTOR = _ARPHOTOSESSION_PROCESSORSAMPLE,
    __module__ = 'pogoprotos.data.telemetry.ar_photo_session_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.ArPhotoSession.ProcessorSample)
    ))
  ,
  DESCRIPTOR = _ARPHOTOSESSION,
  __module__ = 'pogoprotos.data.telemetry.ar_photo_session_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.ArPhotoSession)
  ))
_sym_db.RegisterMessage(ArPhotoSession)
_sym_db.RegisterMessage(ArPhotoSession.ArConditions)
_sym_db.RegisterMessage(ArPhotoSession.BatterySample)
_sym_db.RegisterMessage(ArPhotoSession.FramerateSample)
_sym_db.RegisterMessage(ArPhotoSession.ProcessorSample)


# @@protoc_insertion_point(module_scope)
