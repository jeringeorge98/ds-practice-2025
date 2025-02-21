# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: suggestions.proto
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
    'suggestions.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11suggestions.proto\x12\tbookstore\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"c\n\x0cOrderedBooks\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x10\n\x08\x62ook_ids\x18\x02 \x03(\t\x12\x1c\n\x0fmax_suggestions\x18\x03 \x01(\x05H\x00\x88\x01\x01\x42\x12\n\x10_max_suggestions\"\x8c\x01\n\x13SuggestionsResponse\x12.\n\x0bsuggestions\x18\x01 \x03(\x0b\x32\x19.bookstore.BookSuggestion\x12\x15\n\rsuggestion_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x93\x01\n\x0e\x42ookSuggestion\x12\x0f\n\x07\x62ook_id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\r\n\x05price\x18\x05 \x01(\x01\x12\x10\n\x08\x63urrency\x18\x06 \x01(\t\x12\x1b\n\x13matching_categories\x18\t \x03(\t\x12\x13\n\x0b\x64\x65scription\x18\x0b \x01(\t2_\n\x12SuggestionsService\x12I\n\x0egetSuggestions\x12\x17.bookstore.OrderedBooks\x1a\x1e.bookstore.SuggestionsResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'suggestions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ORDEREDBOOKS']._serialized_start=94
  _globals['_ORDEREDBOOKS']._serialized_end=193
  _globals['_SUGGESTIONSRESPONSE']._serialized_start=196
  _globals['_SUGGESTIONSRESPONSE']._serialized_end=336
  _globals['_BOOKSUGGESTION']._serialized_start=339
  _globals['_BOOKSUGGESTION']._serialized_end=486
  _globals['_SUGGESTIONSSERVICE']._serialized_start=488
  _globals['_SUGGESTIONSSERVICE']._serialized_end=583
# @@protoc_insertion_point(module_scope)
