# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_test_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17grpc_test_service.proto\x12\x10grpc_test_server\"\x1f\n\x0fgRPCTestMessage\x12\x0c\n\x04text\x18\x01 \x01(\t2d\n\x0fgRPCTestService\x12Q\n\tTestServe\x12!.grpc_test_server.gRPCTestMessage\x1a!.grpc_test_server.gRPCTestMessageb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'grpc_test_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GRPCTESTMESSAGE._serialized_start=45
  _GRPCTESTMESSAGE._serialized_end=76
  _GRPCTESTSERVICE._serialized_start=78
  _GRPCTESTSERVICE._serialized_end=178
# @@protoc_insertion_point(module_scope)
