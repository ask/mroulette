from __future__ import absolute_import

from binascii import hexlify

AUPRESET_FMT = """\
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
    "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>data</key>
    <data>
    </data>
    <key>manufacturer</key>
    <integer>{manufacturer}</integer>
    <key>name</key>
    <string>{name}</string>
    <key>subtype</key>
    <integer>{subtype}</integer>
    <key>type</key>
    <integer>{type}</integer>
    <key>version</key>
    <integer>{version}</integer>
</dict>
</plist>
"""


def to_integer(x):
    if not isinstance(x, int):
        return int(hexlify(x), 16)
    return x


def aupreset(manufacturer, subtype, type, name='mroulette', version=0):
    return AUPRESET_FMT.format(
        manufacturer=to_integer(manufacturer),
        subtype=to_integer(subtype),
        type=to_integer(type),
        name=name,
        version=version,
    )
