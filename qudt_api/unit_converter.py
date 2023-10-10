## unit_converter.py

from pint import UnitRegistry

class UnitConverter:
    def __init__(self):
        self.ureg = UnitRegistry()

    def extend_unit(self, unit: str, scaling_factor: float, label: str):
        base_unit = self.ureg.Unit(unit)
        new_unit = base_unit * scaling_factor
        self.ureg.define(f'{label} = {new_unit} {unit}')
        return self.ureg.Quantity(1, label)
