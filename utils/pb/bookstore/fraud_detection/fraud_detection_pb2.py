# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: fraud_detection.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'fraud_detection.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x66raud_detection.proto\x12\tbookstore\"\x85\x01\n\x0bUserRequest\x12\x1d\n\x04user\x18\x01 \x01(\x0b\x32\x0f.bookstore.User\x12*\n\x0b\x63redit_card\x18\x02 \x01(\x0b\x32\x15.bookstore.CreditCard\x12+\n\x0f\x62illing_address\x18\x03 \x01(\x0b\x32\x12.bookstore.Address\"%\n\x04User\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontact\x18\x02 \x01(\t\"A\n\nCreditCard\x12\x0e\n\x06number\x18\x01 \x01(\t\x12\x16\n\x0e\x65xpirationDate\x18\x02 \x01(\t\x12\x0b\n\x03\x63vv\x18\x03 \x01(\t\"T\n\x07\x41\x64\x64ress\x12\x0e\n\x06street\x18\x01 \x01(\t\x12\x0c\n\x04\x63ity\x18\x02 \x01(\t\x12\r\n\x05state\x18\x03 \x01(\t\x12\x0b\n\x03zip\x18\x04 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x05 \x01(\t\">\n\x16\x46raudDetectionResponse\x12\x14\n\x0cisFraudulent\x18\x01 \x01(\x08\x12\x0e\n\x06reason\x18\x02 \x01(\t2e\n\x15\x46raudDetectionService\x12L\n\x0f\x44\x65tectUserFraud\x12\x16.bookstore.UserRequest\x1a!.bookstore.FraudDetectionResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'fraud_detection_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_USERREQUEST']._serialized_start=37
  _globals['_USERREQUEST']._serialized_end=170
  _globals['_USER']._serialized_start=172
  _globals['_USER']._serialized_end=209
  _globals['_CREDITCARD']._serialized_start=211
  _globals['_CREDITCARD']._serialized_end=276
  _globals['_ADDRESS']._serialized_start=278
  _globals['_ADDRESS']._serialized_end=362
  _globals['_FRAUDDETECTIONRESPONSE']._serialized_start=364
  _globals['_FRAUDDETECTIONRESPONSE']._serialized_end=426
  _globals['_FRAUDDETECTIONSERVICE']._serialized_start=428
  _globals['_FRAUDDETECTIONSERVICE']._serialized_end=529
# @@protoc_insertion_point(module_scope)
