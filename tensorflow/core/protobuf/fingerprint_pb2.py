# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/protobuf/fingerprint.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/core/protobuf/fingerprint.proto',
  package='tensorflow',
  syntax='proto3',
  serialized_options=_b('\n\030org.tensorflow.frameworkB\021FingerprintProtosP\001ZUgithub.com/tensorflow/tensorflow/tensorflow/go/core/protobuf/for_core_protos_go_proto\370\001\001'),
  serialized_pb=_b('\n*tensorflow/core/protobuf/fingerprint.proto\x12\ntensorflow\"(\n\x0e\x46ingerprintDef\x12\x16\n\x0egraph_def_hash\x18\x01 \x01(\x04\x42\x89\x01\n\x18org.tensorflow.frameworkB\x11\x46ingerprintProtosP\x01ZUgithub.com/tensorflow/tensorflow/tensorflow/go/core/protobuf/for_core_protos_go_proto\xf8\x01\x01\x62\x06proto3')
)




_FINGERPRINTDEF = _descriptor.Descriptor(
  name='FingerprintDef',
  full_name='tensorflow.FingerprintDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='graph_def_hash', full_name='tensorflow.FingerprintDef.graph_def_hash', index=0,
      number=1, type=4, cpp_type=4, label=1,
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
  serialized_start=58,
  serialized_end=98,
)

DESCRIPTOR.message_types_by_name['FingerprintDef'] = _FINGERPRINTDEF
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FingerprintDef = _reflection.GeneratedProtocolMessageType('FingerprintDef', (_message.Message,), {
  'DESCRIPTOR' : _FINGERPRINTDEF,
  '__module__' : 'tensorflow.core.protobuf.fingerprint_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.FingerprintDef)
  })
_sym_db.RegisterMessage(FingerprintDef)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)