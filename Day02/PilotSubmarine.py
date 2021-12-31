

class PilotSubmarine:
    
    def __init__(self, input: str):
        self.depths = [tuple(d.split) for d in input]
        print(self.depths)