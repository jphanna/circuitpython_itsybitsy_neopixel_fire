import board
import pwmio
import supervisor
import random
from micropython import const


class Fire:
    def __init__(self, pin, fType):
        self.ItsyBitsy_Pins = {
            0: board.D0,
            1: board.D1,
            7: board.D7,
            9: board.D9,
            10: board.D10,
            11: board.D11,
            12: board.D12,
        }
        self.led = pwmio.PWMOut(self.ItsyBitsy_Pins[pin], frequency=500, duty_cycle=0)
        self.fire_type = fType
        self.brightness = self._get_brightness()
        self.flicker_duration = self._get_flicker_duration()
        self.current_moment = supervisor.ticks_ms()
        # For Time Comparison
        self._TICKS_PERIOD = const(1 << 29)
        self._TICKS_MAX = const(self._TICKS_PERIOD - 1)
        self._TICKS_HALFPERIOD = const(self._TICKS_PERIOD // 2)

    def _get_brightness(self):
        if self.fire_type == "lantern":
            return random.randrange(30000, 65535)
        else:
            return random.randrange(8000, 20000)

    @staticmethod
    def _get_flicker_duration():
        return random.randrange(25, 200)

    def ticks_diff(self, ticks1, ticks2):
        # "Compute the signed difference between two ticks values, assuming that they are within 2**28 ticks"
        self.diff = (ticks1 - ticks2) & self._TICKS_MAX
        self.diff = (
            (self.diff + self._TICKS_HALFPERIOD) & self._TICKS_MAX
        ) - self._TICKS_HALFPERIOD
        return self.diff

    def flicker(self):
        if (
            self.ticks_diff(supervisor.ticks_ms(), self.current_moment)
            >= self.flicker_duration
        ):
            self.led.duty_cycle = self.brightness
            self.current_moment = supervisor.ticks_ms()
            self.brightness = self._get_brightness()
            self.flicker_duration = self._get_flicker_duration()
