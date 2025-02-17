from hivemind_bus_client.client import HiveMessageBusClient
from ovos_dinkum_listener.service import OVOSDinkumVoiceService
from ovos_utils.log import LOG


def on_ready():
    LOG.info('HiveMind Voice Satellite is ready.')


def on_started():
    LOG.info('HiveMind Voice Satellite started.')


def on_alive():
    LOG.info('HiveMind Voice Satellite alive.')


def on_stopping():
    LOG.info('HiveMind Voice Satellite is shutting down...')


def on_error(e='Unknown'):
    LOG.error(f'HiveMind Voice Satellite failed to launch ({e}).')


class VoiceClient(OVOSDinkumVoiceService):
    """HiveMind Voice Satellite, but bus is replaced with hivemind connection"""

    def __init__(self, bus: HiveMessageBusClient, on_ready=on_ready, on_error=on_error,
                 on_stopping=on_stopping, on_alive=on_alive,
                 on_started=on_started, watchdog=lambda: None, mic=None):
        super().__init__(on_ready, on_error, on_stopping, on_alive, on_started, watchdog, mic)
        self.bus = bus

    def _connect_to_bus(self):
        pass
