

class PilotSubmarine:
    
    def __init__(self, input: str):
        self.depths = [(direction, int(unit)) for d.split() in input]
        print(self.depths)