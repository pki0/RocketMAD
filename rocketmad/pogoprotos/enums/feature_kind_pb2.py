# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/feature_kind.proto

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
  name='pogoprotos/enums/feature_kind.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n#pogoprotos/enums/feature_kind.proto\x12\x10pogoprotos.enums*\xcd\x0c\n\x0b\x46\x65\x61tureKind\x12\x12\n\x0eKIND_UNDEFINED\x10\x00\x12\x0e\n\nKIND_BASIN\x10\x01\x12\x0e\n\nKIND_CANAL\x10\x02\x12\x11\n\rKIND_CEMETERY\x10\x03\x12\x0f\n\x0bKIND_CINEMA\x10\x04\x12\x10\n\x0cKIND_COLLEGE\x10\x05\x12\x13\n\x0fKIND_COMMERCIAL\x10\x06\x12\x0f\n\x0bKIND_COMMON\x10\x07\x12\x0c\n\x08KIND_DAM\x10\x08\x12\x0e\n\nKIND_DITCH\x10\t\x12\r\n\tKIND_DOCK\x10\n\x12\x0e\n\nKIND_DRAIN\x10\x0b\x12\r\n\tKIND_FARM\x10\x0c\x12\x11\n\rKIND_FARMLAND\x10\r\x12\x11\n\rKIND_FARMYARD\x10\x0e\x12\x10\n\x0cKIND_FOOTWAY\x10\x0f\x12\x0f\n\x0bKIND_FOREST\x10\x10\x12\x0f\n\x0bKIND_GARDEN\x10\x11\x12\x10\n\x0cKIND_GLACIER\x10\x12\x12\x14\n\x10KIND_GOLF_COURSE\x10\x13\x12\x0e\n\nKIND_GRASS\x10\x14\x12\x10\n\x0cKIND_HIGHWAY\x10\x15\x12\x11\n\rKIND_HOSPITAL\x10\x16\x12\x0e\n\nKIND_HOTEL\x10\x17\x12\x13\n\x0fKIND_INDUSTRIAL\x10\x18\x12\r\n\tKIND_LAKE\x10\x19\x12\r\n\tKIND_LAND\x10\x1a\x12\x10\n\x0cKIND_LIBRARY\x10\x1b\x12\x13\n\x0fKIND_MAJOR_ROAD\x10\x1c\x12\x0f\n\x0bKIND_MEADOW\x10\x1d\x12\x13\n\x0fKIND_MINOR_ROAD\x10\x1e\x12\x17\n\x13KIND_NATURE_RESERVE\x10\x1f\x12\x0e\n\nKIND_OCEAN\x10 \x12\r\n\tKIND_PARK\x10!\x12\x10\n\x0cKIND_PARKING\x10\"\x12\r\n\tKIND_PATH\x10#\x12\x13\n\x0fKIND_PEDESTRIAN\x10$\x12\x0e\n\nKIND_PITCH\x10%\x12\x19\n\x15KIND_PLACE_OF_WORSHIP\x10&\x12\x0e\n\nKIND_PLAYA\x10\'\x12\x13\n\x0fKIND_PLAYGROUND\x10(\x12\x0f\n\x0bKIND_QUARRY\x10)\x12\x10\n\x0cKIND_RAILWAY\x10*\x12\x18\n\x14KIND_RECREATION_AREA\x10+\x12\x12\n\x0eKIND_RESERVOIR\x10,\x12\x14\n\x10KIND_RESIDENTIAL\x10-\x12\x0f\n\x0bKIND_RETAIL\x10.\x12\x0e\n\nKIND_RIVER\x10/\x12\x12\n\x0eKIND_RIVERBANK\x10\x30\x12\x0f\n\x0bKIND_RUNWAY\x10\x31\x12\x0f\n\x0bKIND_SCHOOL\x10\x32\x12\x16\n\x12KIND_SPORTS_CENTER\x10\x33\x12\x10\n\x0cKIND_STADIUM\x10\x34\x12\x0f\n\x0bKIND_STREAM\x10\x35\x12\x10\n\x0cKIND_TAXIWAY\x10\x36\x12\x10\n\x0cKIND_THEATRE\x10\x37\x12\x13\n\x0fKIND_UNIVERSITY\x10\x38\x12\x13\n\x0fKIND_URBAN_AREA\x10\x39\x12\x0e\n\nKIND_WATER\x10:\x12\x10\n\x0cKIND_WETLAND\x10;\x12\r\n\tKIND_WOOD\x10<\x12\x1b\n\x17KIND_DEBUG_TILE_OUTLINE\x10=\x12\x1b\n\x17KIND_DEBUG_TILE_SURFACE\x10>\x12\x0e\n\nKIND_OTHER\x10?\x12\x10\n\x0cKIND_COUNTRY\x10@\x12\x0f\n\x0bKIND_REGION\x10\x41\x12\r\n\tKIND_CITY\x10\x42\x12\r\n\tKIND_TOWN\x10\x43\x12\x10\n\x0cKIND_AIRPORT\x10\x44\x12\x0c\n\x08KIND_BAY\x10\x45\x12\x10\n\x0cKIND_BOROUGH\x10\x46\x12\x0e\n\nKIND_FJORD\x10G\x12\x0f\n\x0bKIND_HAMLET\x10H\x12\x11\n\rKIND_MILITARY\x10I\x12\x16\n\x12KIND_NATIONAL_PARK\x10J\x12\x15\n\x11KIND_NEIGHBORHOOD\x10K\x12\r\n\tKIND_PEAK\x10L\x12\x0f\n\x0bKIND_PRISON\x10M\x12\x17\n\x13KIND_PROTECTED_AREA\x10N\x12\r\n\tKIND_REEF\x10O\x12\r\n\tKIND_ROCK\x10P\x12\r\n\tKIND_SAND\x10Q\x12\x0e\n\nKIND_SCRUB\x10R\x12\x0c\n\x08KIND_SEA\x10S\x12\x0f\n\x0bKIND_STRAIT\x10T\x12\x0f\n\x0bKIND_VALLEY\x10U\x12\x10\n\x0cKIND_VILLAGE\x10V\x12\r\n\x08KIND_ANY\x10\xd0\x0f\x62\x06proto3')
)

_FEATUREKIND = _descriptor.EnumDescriptor(
  name='FeatureKind',
  full_name='pogoprotos.enums.FeatureKind',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='KIND_UNDEFINED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_BASIN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_CANAL', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_CEMETERY', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_CINEMA', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_COLLEGE', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_COMMERCIAL', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_COMMON', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_DAM', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_DITCH', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_DOCK', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_DRAIN', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_FARM', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_FARMLAND', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_FARMYARD', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_FOOTWAY', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_FOREST', index=16, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_GARDEN', index=17, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_GLACIER', index=18, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_GOLF_COURSE', index=19, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_GRASS', index=20, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_HIGHWAY', index=21, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_HOSPITAL', index=22, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_HOTEL', index=23, number=23,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_INDUSTRIAL', index=24, number=24,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_LAKE', index=25, number=25,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_LAND', index=26, number=26,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_LIBRARY', index=27, number=27,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_MAJOR_ROAD', index=28, number=28,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_MEADOW', index=29, number=29,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_MINOR_ROAD', index=30, number=30,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_NATURE_RESERVE', index=31, number=31,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_OCEAN', index=32, number=32,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_PARK', index=33, number=33,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_PARKING', index=34, number=34,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_PATH', index=35, number=35,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_PEDESTRIAN', index=36, number=36,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_PITCH', index=37, number=37,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_PLACE_OF_WORSHIP', index=38, number=38,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_PLAYA', index=39, number=39,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_PLAYGROUND', index=40, number=40,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_QUARRY', index=41, number=41,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_RAILWAY', index=42, number=42,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_RECREATION_AREA', index=43, number=43,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_RESERVOIR', index=44, number=44,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_RESIDENTIAL', index=45, number=45,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_RETAIL', index=46, number=46,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_RIVER', index=47, number=47,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_RIVERBANK', index=48, number=48,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_RUNWAY', index=49, number=49,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_SCHOOL', index=50, number=50,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_SPORTS_CENTER', index=51, number=51,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_STADIUM', index=52, number=52,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_STREAM', index=53, number=53,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_TAXIWAY', index=54, number=54,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_THEATRE', index=55, number=55,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_UNIVERSITY', index=56, number=56,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_URBAN_AREA', index=57, number=57,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_WATER', index=58, number=58,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_WETLAND', index=59, number=59,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_WOOD', index=60, number=60,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_DEBUG_TILE_OUTLINE', index=61, number=61,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_DEBUG_TILE_SURFACE', index=62, number=62,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_OTHER', index=63, number=63,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_COUNTRY', index=64, number=64,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_REGION', index=65, number=65,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_CITY', index=66, number=66,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_TOWN', index=67, number=67,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_AIRPORT', index=68, number=68,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_BAY', index=69, number=69,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_BOROUGH', index=70, number=70,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_FJORD', index=71, number=71,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_HAMLET', index=72, number=72,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_MILITARY', index=73, number=73,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_NATIONAL_PARK', index=74, number=74,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_NEIGHBORHOOD', index=75, number=75,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_PEAK', index=76, number=76,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_PRISON', index=77, number=77,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_PROTECTED_AREA', index=78, number=78,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_REEF', index=79, number=79,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_ROCK', index=80, number=80,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_SAND', index=81, number=81,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_SCRUB', index=82, number=82,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_SEA', index=83, number=83,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_STRAIT', index=84, number=84,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_VALLEY', index=85, number=85,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_VILLAGE', index=86, number=86,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_ANY', index=87, number=2000,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=58,
  serialized_end=1671,
)
_sym_db.RegisterEnumDescriptor(_FEATUREKIND)

FeatureKind = enum_type_wrapper.EnumTypeWrapper(_FEATUREKIND)
KIND_UNDEFINED = 0
KIND_BASIN = 1
KIND_CANAL = 2
KIND_CEMETERY = 3
KIND_CINEMA = 4
KIND_COLLEGE = 5
KIND_COMMERCIAL = 6
KIND_COMMON = 7
KIND_DAM = 8
KIND_DITCH = 9
KIND_DOCK = 10
KIND_DRAIN = 11
KIND_FARM = 12
KIND_FARMLAND = 13
KIND_FARMYARD = 14
KIND_FOOTWAY = 15
KIND_FOREST = 16
KIND_GARDEN = 17
KIND_GLACIER = 18
KIND_GOLF_COURSE = 19
KIND_GRASS = 20
KIND_HIGHWAY = 21
KIND_HOSPITAL = 22
KIND_HOTEL = 23
KIND_INDUSTRIAL = 24
KIND_LAKE = 25
KIND_LAND = 26
KIND_LIBRARY = 27
KIND_MAJOR_ROAD = 28
KIND_MEADOW = 29
KIND_MINOR_ROAD = 30
KIND_NATURE_RESERVE = 31
KIND_OCEAN = 32
KIND_PARK = 33
KIND_PARKING = 34
KIND_PATH = 35
KIND_PEDESTRIAN = 36
KIND_PITCH = 37
KIND_PLACE_OF_WORSHIP = 38
KIND_PLAYA = 39
KIND_PLAYGROUND = 40
KIND_QUARRY = 41
KIND_RAILWAY = 42
KIND_RECREATION_AREA = 43
KIND_RESERVOIR = 44
KIND_RESIDENTIAL = 45
KIND_RETAIL = 46
KIND_RIVER = 47
KIND_RIVERBANK = 48
KIND_RUNWAY = 49
KIND_SCHOOL = 50
KIND_SPORTS_CENTER = 51
KIND_STADIUM = 52
KIND_STREAM = 53
KIND_TAXIWAY = 54
KIND_THEATRE = 55
KIND_UNIVERSITY = 56
KIND_URBAN_AREA = 57
KIND_WATER = 58
KIND_WETLAND = 59
KIND_WOOD = 60
KIND_DEBUG_TILE_OUTLINE = 61
KIND_DEBUG_TILE_SURFACE = 62
KIND_OTHER = 63
KIND_COUNTRY = 64
KIND_REGION = 65
KIND_CITY = 66
KIND_TOWN = 67
KIND_AIRPORT = 68
KIND_BAY = 69
KIND_BOROUGH = 70
KIND_FJORD = 71
KIND_HAMLET = 72
KIND_MILITARY = 73
KIND_NATIONAL_PARK = 74
KIND_NEIGHBORHOOD = 75
KIND_PEAK = 76
KIND_PRISON = 77
KIND_PROTECTED_AREA = 78
KIND_REEF = 79
KIND_ROCK = 80
KIND_SAND = 81
KIND_SCRUB = 82
KIND_SEA = 83
KIND_STRAIT = 84
KIND_VALLEY = 85
KIND_VILLAGE = 86
KIND_ANY = 2000


DESCRIPTOR.enum_types_by_name['FeatureKind'] = _FEATUREKIND
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
