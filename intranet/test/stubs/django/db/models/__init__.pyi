from . import deletion

class Count:
  # FIXME: figure out args
  def __init__(self, *args, **kwargs): ...
class Field:
  # FIXME: actually figure out args
  def __init__(self, *args, **kwargs): ...
class AutoField(Field): ...
class CharField(Field): ...
class BooleanField(Field): ...
class ManyToManyField(Field): ...
class IntegerField(Field): ...
class DateField(Field): ...
class DateTimeField(Field): ...
class TextField(Field): ...
class URLField(Field): ...
class OneToOneField(Field): ...
class SmallIntegerField(Field): ...
class TimeField(Field): ...
class DecimalField(Field): ...
class FileField(Field): ...
class PositiveIntegerField(Field): ...
class ForeignKey:
  # FIXME: actually figure out args
  def __init__(self, *args, **kwargs): ...
class Model:
  def __init__(self, *args, **kwargs): ... # FIXME: figure out args
  def validate_unique(self, *args, **kwargs): ...  # FIXME: figure out args
  def save(self, *args, **kwargs): ...  # FIXME: figure out args
class Q:
  # FIXME: actually figure out args
  def __init__(self, *args, **kwargs): ...
class Manager:
  def all(self): ...
  def get_query_set(self): ...
  def select_related(self, *args, **kwargs): ...  # FIXME: figure out args
