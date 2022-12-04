
class Tdot():
    def __init__(self, key: str, label: str):
        self.key = key
        self.label = label

    def __str__(self):
        return f"Tdot({self.key}, {self.label})"

    def __repr__(self):
        return f"Tdot({self.key}, {self.label})"
