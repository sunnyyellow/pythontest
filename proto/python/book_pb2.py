# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: book.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='book.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\nbook.proto\"\x14\n\x04\x42ook\x12\x0c\n\x04name\x18\x01 \x02(\t')
)




_BOOK = _descriptor.Descriptor(
  name='Book',
  full_name='Book',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Book.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=34,
)

DESCRIPTOR.message_types_by_name['Book'] = _BOOK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Book = _reflection.GeneratedProtocolMessageType('Book', (_message.Message,), dict(
  DESCRIPTOR = _BOOK,
  __module__ = 'book_pb2'
  # @@protoc_insertion_point(class_scope:Book)
  ))
_sym_db.RegisterMessage(Book)


# @@protoc_insertion_point(module_scope)
