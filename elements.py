from periodic_table import PeriodicTable


class Element:
    def __init__(
        self,
        name,
        symbol,
        summary,
        appearance,
        category,
        phase,
        period,
        group,
        electron_configuration,
    ):
        self.name = name
        self.symbol = symbol
        self.summary = summary
        self.appearance = appearance
        self.category = category
        self.phase = phase
        self.period = period
        self.group = group
        self.electron_configuration = electron_configuration

    def __repr__(self):
        return f"{self.name} ({self.symbol})"


pt = PeriodicTable()

# Creates the Periodic Table
ptable = []

for element in pt.elements:
    ptable.append(
        Element(
            element.name,
            element.symbol,
            element.summary,
            element.appearance,
            element.category,
            element.phase,
            element.period,
            element.group,
            element.electron_configuration,
        )
    )

ptable = tuple(ptable)

ELEMENTS = 119  # == len(ptable), the number of elements in the Periodic Table
