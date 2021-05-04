from ..unit import UniqueUnit
from .connectable import ConnectableInterface


class Input(UniqueUnit, ConnectableInterface):
    def __init__(self, default_value=[0.0], output=None, optimized=False, generator=None):
        super().__init__()
        self.generator = generator
        self.static_value = default_value
        self.output = output
        self.optimized = optimized
        self.__changed = True

    def get_value(self):
        if self.output:
            return self.output.get_value()
        return self.static_value

    def set_value(self, val: []) -> bool:
        if self.output:
            return False
        else:
            if self.static_value != val:
                self.static_value = val
                self.__changed = True
            return True

    def is_optimized(self) -> bool:
        if self.output:
            return False
        return self.optimized

    def set_optimized(self, optimized: bool) -> bool:
        self.optimized = optimized
        return self.is_optimized()

    def changed(self) ->bool:
        if self.output:
            return self.output.changed()
        return self.__changed

    def connect(self, connectable, both=True) -> bool:
        from .output import Output
        if not isinstance(connectable, Output):
            return False
        if self.output:
            if not self.disconnect():
                return False
        if both:
            if not connectable.connect(self, False):
                return False

        self.output = connectable
        return True

    def disconnect(self, connectable=None, both=True) -> bool:
        if not self.output:
            return False

        if both:
            if not self.output.disconnect(self, False):
                return False
        self.output = None
        return True

    def update(self) -> bool:
        result = self.changed()
        self.__changed = False
        return result

