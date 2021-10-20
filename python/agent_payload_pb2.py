# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: agent_payload.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from github.com.gogo.protobuf.gogoproto import gogo_pb2 as github_dot_com_dot_gogo_dot_protobuf_dot_gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='agent_payload.proto',
  package='datadog.agentpayload',
  syntax='proto3',
  serialized_pb=_b('\n\x13\x61gent_payload.proto\x12\x14\x64\x61tadog.agentpayload\x1a-github.com/gogo/protobuf/gogoproto/gogo.proto\"\x89\x01\n\x0e\x43ommonMetadata\x12\x15\n\ragent_version\x18\x01 \x01(\t\x12\x10\n\x08timezone\x18\x02 \x01(\t\x12\x15\n\rcurrent_epoch\x18\x03 \x01(\x01\x12\x13\n\x0binternal_ip\x18\x04 \x01(\t\x12\x11\n\tpublic_ip\x18\x05 \x01(\t\x12\x0f\n\x07\x61pi_key\x18\x06 \x01(\t\"\xaa\x02\n\rEventsPayload\x12\x39\n\x06\x65vents\x18\x01 \x03(\x0b\x32).datadog.agentpayload.EventsPayload.Event\x12\x36\n\x08metadata\x18\x02 \x01(\x0b\x32$.datadog.agentpayload.CommonMetadata\x1a\xa5\x01\n\x05\x45vent\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\n\n\x02ts\x18\x03 \x01(\x03\x12\x10\n\x08priority\x18\x04 \x01(\t\x12\x0c\n\x04host\x18\x05 \x01(\t\x12\x0c\n\x04tags\x18\x06 \x03(\t\x12\x12\n\nalert_type\x18\x07 \x01(\t\x12\x17\n\x0f\x61ggregation_key\x18\x08 \x01(\t\x12\x18\n\x10source_type_name\x18\t \x01(\t\"\x9b\x05\n\rSketchPayload\x12\x42\n\x08sketches\x18\x01 \x03(\x0b\x32*.datadog.agentpayload.SketchPayload.SketchB\x04\xc8\xde\x1f\x00\x12<\n\x08metadata\x18\x02 \x01(\x0b\x32$.datadog.agentpayload.CommonMetadataB\x04\xc8\xde\x1f\x00\x1a\x87\x04\n\x06Sketch\x12\x0e\n\x06metric\x18\x01 \x01(\t\x12\x0c\n\x04host\x18\x02 \x01(\t\x12T\n\rdistributions\x18\x03 \x03(\x0b\x32\x37.datadog.agentpayload.SketchPayload.Sketch.DistributionB\x04\xc8\xde\x1f\x00\x12\x0c\n\x04tags\x18\x04 \x03(\t\x12O\n\x0b\x64ogsketches\x18\x07 \x03(\x0b\x32\x34.datadog.agentpayload.SketchPayload.Sketch.DogsketchB\x04\xc8\xde\x1f\x00\x1a\x8d\x01\n\x0c\x44istribution\x12\n\n\x02ts\x18\x01 \x01(\x03\x12\x0b\n\x03\x63nt\x18\x02 \x01(\x03\x12\x0b\n\x03min\x18\x03 \x01(\x01\x12\x0b\n\x03max\x18\x04 \x01(\x01\x12\x0b\n\x03\x61vg\x18\x05 \x01(\x01\x12\x0b\n\x03sum\x18\x06 \x01(\x01\x12\t\n\x01v\x18\x07 \x03(\x01\x12\t\n\x01g\x18\x08 \x03(\r\x12\r\n\x05\x64\x65lta\x18\t \x03(\r\x12\x0b\n\x03\x62uf\x18\n \x03(\x01\x1an\n\tDogsketch\x12\n\n\x02ts\x18\x01 \x01(\x03\x12\x0b\n\x03\x63nt\x18\x02 \x01(\x03\x12\x0b\n\x03min\x18\x03 \x01(\x01\x12\x0b\n\x03max\x18\x04 \x01(\x01\x12\x0b\n\x03\x61vg\x18\x05 \x01(\x01\x12\x0b\n\x03sum\x18\x06 \x01(\x01\x12\t\n\x01k\x18\x07 \x03(\x11\x12\t\n\x01n\x18\x08 \x03(\rJ\x04\x08\x05\x10\x06J\x04\x08\x06\x10\x07R\x0e\x64istributionsKR\x0e\x64istributionsC\"\xc2\x02\n\x12\x45\x43SMetadataPayload\x12<\n\x05tasks\x18\x01 \x03(\x0b\x32-.datadog.agentpayload.ECSMetadataPayload.Task\x1a\xaa\x01\n\x04Task\x12\x0b\n\x03\x61rn\x18\x01 \x01(\t\x12\x16\n\x0e\x64\x65sired_status\x18\x02 \x01(\t\x12\x14\n\x0cknown_status\x18\x03 \x01(\t\x12\x0e\n\x06\x66\x61mily\x18\x04 \x01(\t\x12\x0f\n\x07version\x18\x05 \x01(\t\x12\x46\n\ncontainers\x18\x06 \x03(\x0b\x32\x32.datadog.agentpayload.ECSMetadataPayload.Container\x1a\x41\n\tContainer\x12\x11\n\tdocker_id\x18\x01 \x01(\t\x12\x13\n\x0b\x64ocker_name\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\tB(Z&github.com/DataDog/agent-payload/gogenb\x06proto3')
  ,
  dependencies=[github_dot_com_dot_gogo_dot_protobuf_dot_gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_COMMONMETADATA = _descriptor.Descriptor(
  name='CommonMetadata',
  full_name='datadog.agentpayload.CommonMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent_version', full_name='datadog.agentpayload.CommonMetadata.agent_version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timezone', full_name='datadog.agentpayload.CommonMetadata.timezone', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='current_epoch', full_name='datadog.agentpayload.CommonMetadata.current_epoch', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='internal_ip', full_name='datadog.agentpayload.CommonMetadata.internal_ip', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='public_ip', full_name='datadog.agentpayload.CommonMetadata.public_ip', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='api_key', full_name='datadog.agentpayload.CommonMetadata.api_key', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=93,
  serialized_end=230,
)


_EVENTSPAYLOAD_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='datadog.agentpayload.EventsPayload.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='datadog.agentpayload.EventsPayload.Event.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='datadog.agentpayload.EventsPayload.Event.text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ts', full_name='datadog.agentpayload.EventsPayload.Event.ts', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='priority', full_name='datadog.agentpayload.EventsPayload.Event.priority', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='host', full_name='datadog.agentpayload.EventsPayload.Event.host', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='datadog.agentpayload.EventsPayload.Event.tags', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alert_type', full_name='datadog.agentpayload.EventsPayload.Event.alert_type', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aggregation_key', full_name='datadog.agentpayload.EventsPayload.Event.aggregation_key', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source_type_name', full_name='datadog.agentpayload.EventsPayload.Event.source_type_name', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=366,
  serialized_end=531,
)

_EVENTSPAYLOAD = _descriptor.Descriptor(
  name='EventsPayload',
  full_name='datadog.agentpayload.EventsPayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='events', full_name='datadog.agentpayload.EventsPayload.events', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='datadog.agentpayload.EventsPayload.metadata', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_EVENTSPAYLOAD_EVENT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=233,
  serialized_end=531,
)


_SKETCHPAYLOAD_SKETCH_DISTRIBUTION = _descriptor.Descriptor(
  name='Distribution',
  full_name='datadog.agentpayload.SketchPayload.Sketch.Distribution',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ts', full_name='datadog.agentpayload.SketchPayload.Sketch.Distribution.ts', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cnt', full_name='datadog.agentpayload.SketchPayload.Sketch.Distribution.cnt', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min', full_name='datadog.agentpayload.SketchPayload.Sketch.Distribution.min', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max', full_name='datadog.agentpayload.SketchPayload.Sketch.Distribution.max', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='avg', full_name='datadog.agentpayload.SketchPayload.Sketch.Distribution.avg', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sum', full_name='datadog.agentpayload.SketchPayload.Sketch.Distribution.sum', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='v', full_name='datadog.agentpayload.SketchPayload.Sketch.Distribution.v', index=6,
      number=7, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='g', full_name='datadog.agentpayload.SketchPayload.Sketch.Distribution.g', index=7,
      number=8, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='delta', full_name='datadog.agentpayload.SketchPayload.Sketch.Distribution.delta', index=8,
      number=9, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='buf', full_name='datadog.agentpayload.SketchPayload.Sketch.Distribution.buf', index=9,
      number=10, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=904,
  serialized_end=1045,
)

_SKETCHPAYLOAD_SKETCH_DOGSKETCH = _descriptor.Descriptor(
  name='Dogsketch',
  full_name='datadog.agentpayload.SketchPayload.Sketch.Dogsketch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ts', full_name='datadog.agentpayload.SketchPayload.Sketch.Dogsketch.ts', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cnt', full_name='datadog.agentpayload.SketchPayload.Sketch.Dogsketch.cnt', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min', full_name='datadog.agentpayload.SketchPayload.Sketch.Dogsketch.min', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max', full_name='datadog.agentpayload.SketchPayload.Sketch.Dogsketch.max', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='avg', full_name='datadog.agentpayload.SketchPayload.Sketch.Dogsketch.avg', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sum', full_name='datadog.agentpayload.SketchPayload.Sketch.Dogsketch.sum', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='k', full_name='datadog.agentpayload.SketchPayload.Sketch.Dogsketch.k', index=6,
      number=7, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='n', full_name='datadog.agentpayload.SketchPayload.Sketch.Dogsketch.n', index=7,
      number=8, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=1047,
  serialized_end=1157,
)

_SKETCHPAYLOAD_SKETCH = _descriptor.Descriptor(
  name='Sketch',
  full_name='datadog.agentpayload.SketchPayload.Sketch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metric', full_name='datadog.agentpayload.SketchPayload.Sketch.metric', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='host', full_name='datadog.agentpayload.SketchPayload.Sketch.host', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distributions', full_name='datadog.agentpayload.SketchPayload.Sketch.distributions', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='datadog.agentpayload.SketchPayload.Sketch.tags', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dogsketches', full_name='datadog.agentpayload.SketchPayload.Sketch.dogsketches', index=4,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SKETCHPAYLOAD_SKETCH_DISTRIBUTION, _SKETCHPAYLOAD_SKETCH_DOGSKETCH, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=682,
  serialized_end=1201,
)

_SKETCHPAYLOAD = _descriptor.Descriptor(
  name='SketchPayload',
  full_name='datadog.agentpayload.SketchPayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sketches', full_name='datadog.agentpayload.SketchPayload.sketches', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='datadog.agentpayload.SketchPayload.metadata', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SKETCHPAYLOAD_SKETCH, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=534,
  serialized_end=1201,
)


_ECSMETADATAPAYLOAD_TASK = _descriptor.Descriptor(
  name='Task',
  full_name='datadog.agentpayload.ECSMetadataPayload.Task',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='arn', full_name='datadog.agentpayload.ECSMetadataPayload.Task.arn', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='desired_status', full_name='datadog.agentpayload.ECSMetadataPayload.Task.desired_status', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='known_status', full_name='datadog.agentpayload.ECSMetadataPayload.Task.known_status', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='family', full_name='datadog.agentpayload.ECSMetadataPayload.Task.family', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='datadog.agentpayload.ECSMetadataPayload.Task.version', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='containers', full_name='datadog.agentpayload.ECSMetadataPayload.Task.containers', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=1289,
  serialized_end=1459,
)

_ECSMETADATAPAYLOAD_CONTAINER = _descriptor.Descriptor(
  name='Container',
  full_name='datadog.agentpayload.ECSMetadataPayload.Container',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='docker_id', full_name='datadog.agentpayload.ECSMetadataPayload.Container.docker_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='docker_name', full_name='datadog.agentpayload.ECSMetadataPayload.Container.docker_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='datadog.agentpayload.ECSMetadataPayload.Container.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=1461,
  serialized_end=1526,
)

_ECSMETADATAPAYLOAD = _descriptor.Descriptor(
  name='ECSMetadataPayload',
  full_name='datadog.agentpayload.ECSMetadataPayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tasks', full_name='datadog.agentpayload.ECSMetadataPayload.tasks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ECSMETADATAPAYLOAD_TASK, _ECSMETADATAPAYLOAD_CONTAINER, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1204,
  serialized_end=1526,
)

_EVENTSPAYLOAD_EVENT.containing_type = _EVENTSPAYLOAD
_EVENTSPAYLOAD.fields_by_name['events'].message_type = _EVENTSPAYLOAD_EVENT
_EVENTSPAYLOAD.fields_by_name['metadata'].message_type = _COMMONMETADATA
_SKETCHPAYLOAD_SKETCH_DISTRIBUTION.containing_type = _SKETCHPAYLOAD_SKETCH
_SKETCHPAYLOAD_SKETCH_DOGSKETCH.containing_type = _SKETCHPAYLOAD_SKETCH
_SKETCHPAYLOAD_SKETCH.fields_by_name['distributions'].message_type = _SKETCHPAYLOAD_SKETCH_DISTRIBUTION
_SKETCHPAYLOAD_SKETCH.fields_by_name['dogsketches'].message_type = _SKETCHPAYLOAD_SKETCH_DOGSKETCH
_SKETCHPAYLOAD_SKETCH.containing_type = _SKETCHPAYLOAD
_SKETCHPAYLOAD.fields_by_name['sketches'].message_type = _SKETCHPAYLOAD_SKETCH
_SKETCHPAYLOAD.fields_by_name['metadata'].message_type = _COMMONMETADATA
_ECSMETADATAPAYLOAD_TASK.fields_by_name['containers'].message_type = _ECSMETADATAPAYLOAD_CONTAINER
_ECSMETADATAPAYLOAD_TASK.containing_type = _ECSMETADATAPAYLOAD
_ECSMETADATAPAYLOAD_CONTAINER.containing_type = _ECSMETADATAPAYLOAD
_ECSMETADATAPAYLOAD.fields_by_name['tasks'].message_type = _ECSMETADATAPAYLOAD_TASK
DESCRIPTOR.message_types_by_name['CommonMetadata'] = _COMMONMETADATA
DESCRIPTOR.message_types_by_name['EventsPayload'] = _EVENTSPAYLOAD
DESCRIPTOR.message_types_by_name['SketchPayload'] = _SKETCHPAYLOAD
DESCRIPTOR.message_types_by_name['ECSMetadataPayload'] = _ECSMETADATAPAYLOAD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CommonMetadata = _reflection.GeneratedProtocolMessageType('CommonMetadata', (_message.Message,), dict(
  DESCRIPTOR = _COMMONMETADATA,
  __module__ = 'agent_payload_pb2'
  # @@protoc_insertion_point(class_scope:datadog.agentpayload.CommonMetadata)
  ))
_sym_db.RegisterMessage(CommonMetadata)

EventsPayload = _reflection.GeneratedProtocolMessageType('EventsPayload', (_message.Message,), dict(

  Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), dict(
    DESCRIPTOR = _EVENTSPAYLOAD_EVENT,
    __module__ = 'agent_payload_pb2'
    # @@protoc_insertion_point(class_scope:datadog.agentpayload.EventsPayload.Event)
    ))
  ,
  DESCRIPTOR = _EVENTSPAYLOAD,
  __module__ = 'agent_payload_pb2'
  # @@protoc_insertion_point(class_scope:datadog.agentpayload.EventsPayload)
  ))
_sym_db.RegisterMessage(EventsPayload)
_sym_db.RegisterMessage(EventsPayload.Event)

SketchPayload = _reflection.GeneratedProtocolMessageType('SketchPayload', (_message.Message,), dict(

  Sketch = _reflection.GeneratedProtocolMessageType('Sketch', (_message.Message,), dict(

    Distribution = _reflection.GeneratedProtocolMessageType('Distribution', (_message.Message,), dict(
      DESCRIPTOR = _SKETCHPAYLOAD_SKETCH_DISTRIBUTION,
      __module__ = 'agent_payload_pb2'
      # @@protoc_insertion_point(class_scope:datadog.agentpayload.SketchPayload.Sketch.Distribution)
      ))
    ,

    Dogsketch = _reflection.GeneratedProtocolMessageType('Dogsketch', (_message.Message,), dict(
      DESCRIPTOR = _SKETCHPAYLOAD_SKETCH_DOGSKETCH,
      __module__ = 'agent_payload_pb2'
      # @@protoc_insertion_point(class_scope:datadog.agentpayload.SketchPayload.Sketch.Dogsketch)
      ))
    ,
    DESCRIPTOR = _SKETCHPAYLOAD_SKETCH,
    __module__ = 'agent_payload_pb2'
    # @@protoc_insertion_point(class_scope:datadog.agentpayload.SketchPayload.Sketch)
    ))
  ,
  DESCRIPTOR = _SKETCHPAYLOAD,
  __module__ = 'agent_payload_pb2'
  # @@protoc_insertion_point(class_scope:datadog.agentpayload.SketchPayload)
  ))
_sym_db.RegisterMessage(SketchPayload)
_sym_db.RegisterMessage(SketchPayload.Sketch)
_sym_db.RegisterMessage(SketchPayload.Sketch.Distribution)
_sym_db.RegisterMessage(SketchPayload.Sketch.Dogsketch)

ECSMetadataPayload = _reflection.GeneratedProtocolMessageType('ECSMetadataPayload', (_message.Message,), dict(

  Task = _reflection.GeneratedProtocolMessageType('Task', (_message.Message,), dict(
    DESCRIPTOR = _ECSMETADATAPAYLOAD_TASK,
    __module__ = 'agent_payload_pb2'
    # @@protoc_insertion_point(class_scope:datadog.agentpayload.ECSMetadataPayload.Task)
    ))
  ,

  Container = _reflection.GeneratedProtocolMessageType('Container', (_message.Message,), dict(
    DESCRIPTOR = _ECSMETADATAPAYLOAD_CONTAINER,
    __module__ = 'agent_payload_pb2'
    # @@protoc_insertion_point(class_scope:datadog.agentpayload.ECSMetadataPayload.Container)
    ))
  ,
  DESCRIPTOR = _ECSMETADATAPAYLOAD,
  __module__ = 'agent_payload_pb2'
  # @@protoc_insertion_point(class_scope:datadog.agentpayload.ECSMetadataPayload)
  ))
_sym_db.RegisterMessage(ECSMetadataPayload)
_sym_db.RegisterMessage(ECSMetadataPayload.Task)
_sym_db.RegisterMessage(ECSMetadataPayload.Container)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z&github.com/DataDog/agent-payload/gogen'))
_SKETCHPAYLOAD_SKETCH.fields_by_name['distributions'].has_options = True
_SKETCHPAYLOAD_SKETCH.fields_by_name['distributions']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_SKETCHPAYLOAD_SKETCH.fields_by_name['dogsketches'].has_options = True
_SKETCHPAYLOAD_SKETCH.fields_by_name['dogsketches']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_SKETCHPAYLOAD.fields_by_name['sketches'].has_options = True
_SKETCHPAYLOAD.fields_by_name['sketches']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_SKETCHPAYLOAD.fields_by_name['metadata'].has_options = True
_SKETCHPAYLOAD.fields_by_name['metadata']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
# @@protoc_insertion_point(module_scope)
