from contextlib import contextmanager
from datetime import datetime
import gzip
from io import BytesIO
import shutil
import struct
import tempfile
import zlib

from pytz import UTC

from ichnaea.exceptions import GZIPDecodeError


@contextmanager
def gzip_open(filename, mode, compresslevel=6):  # pragma: no cover
    """Open a gzip file.

    :param mode: Either `r` or `w` for read or write access.
    """
    with open(filename, mode + 'b') as fd:
        with gzip.open(fd, mode=mode + 't',
                       compresslevel=compresslevel,
                       encoding='utf-8') as gzip_file:
            yield gzip_file


def encode_gzip(data, compresslevel=6, encoding='utf-8'):
    """Encode the passed in data with gzip."""
    if encoding and isinstance(data, str):
        data = data.encode(encoding)
    out = BytesIO()
    with gzip.GzipFile(None, 'wb',
                       compresslevel=compresslevel, fileobj=out) as gzip_file:
        gzip_file.write(data)
    return out.getvalue()


def decode_gzip(data, encoding='utf-8'):
    """Decode the bytes data and return a Unicode string.

    :raises: :exc:`~ichnaea.exceptions.GZIPDecodeError`
    """
    try:
        with gzip.GzipFile(None, mode='rb',
                           fileobj=BytesIO(data)) as gzip_file:
            out = gzip_file.read()
        if encoding:
            return out.decode(encoding)
        return out
    except (IOError, OSError, EOFError, struct.error, zlib.error) as exc:
        raise GZIPDecodeError(repr(exc))


@contextmanager
def selfdestruct_tempdir():
    base_path = tempfile.mkdtemp()
    try:
        yield base_path
    finally:
        shutil.rmtree(base_path)


def utcnow():
    """Return the current time in UTC with a UTC timezone set."""
    return datetime.utcnow().replace(microsecond=0, tzinfo=UTC)
