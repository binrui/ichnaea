from ichnaea.models.transform import ReportTransform
from ichnaea.service.base_submit import BaseSubmitView
from ichnaea.service.geosubmit2.schema import GeoSubmit2Schema


class GeoSubmit2Transform(ReportTransform):
    # the connection section is not mapped on purpose

    time_id = 'timestamp'
    toplevel_map = [
        'carrier',
        'homeMobileCountryCode',
        'homeMobileNetworkCode',
    ]

    position_id = ('position', 'position')
    position_map = [
        'latitude',
        'longitude',
        'accuracy',
        'altitude',
        'altitudeAccuracy',
        'age',
        'heading',
        'pressure',
        'speed',
        'source',
    ]

    blue_id = ('bluetoothBeacons', 'bluetoothBeacons')
    blue_map = [
        'macAddress',
        'name',
        'age',
        'signalStrength',
    ]

    radio_id = ('radioType', 'radioType')
    cell_id = ('cellTowers', 'cellTowers')
    cell_map = [
        'radioType',
        'mobileCountryCode',
        'mobileNetworkCode',
        'locationAreaCode',
        'cellId',
        'age',
        'asu',
        'primaryScramblingCode',
        'serving',
        'signalStrength',
        'timingAdvance',
    ]

    wifi_id = ('wifiAccessPoints', 'wifiAccessPoints')
    wifi_map = [
        # ssid is not mapped on purpose, we never want to store it
        'macAddress',
        'radioType',
        'age',
        'channel',
        'frequency',
        'signalToNoiseRatio',
        'signalStrength',
    ]


class GeoSubmit2View(BaseSubmitView):

    route = '/v2/geosubmit'
    schema = GeoSubmit2Schema
    transform = GeoSubmit2Transform
    view_name = 'geosubmit2'
