from ichnaea.models.transform import ReportTransform
from ichnaea.service.base_submit import BaseSubmitView
from ichnaea.service.geosubmit.schema import GeoSubmitSchema


class GeoSubmitTransform(ReportTransform):

    time_id = 'timestamp'
    toplevel_map = [
        'carrier',
        'homeMobileCountryCode',
        'homeMobileNetworkCode',
    ]

    position_id = (None, 'position')
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
        ('psc', 'primaryScramblingCode'),
        'serving',
        'signalStrength',
        'timingAdvance',
    ]

    wifi_id = ('wifiAccessPoints', 'wifiAccessPoints')
    wifi_map = [
        # ssid is not mapped on purpose, we never want to store it
        'macAddress',
        'age',
        'channel',
        'frequency',
        'radioType',
        'signalToNoiseRatio',
        'signalStrength',
    ]


class GeoSubmitView(BaseSubmitView):

    route = '/v1/geosubmit'
    schema = GeoSubmitSchema
    transform = GeoSubmitTransform
    view_name = 'geosubmit'
