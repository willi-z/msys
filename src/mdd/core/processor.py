from .module import Module


class Processor(Module):
    def __init__(self, inputs=[], outputs=[], options=[], modules=[]):
        super().__init__(inputs, outputs, options)
        self.modules = modules

    def getchilds(self) -> []:
        return self.inputs + self.outputs + self.modules
