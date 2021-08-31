class Cpu:
    def __init__(self, cache, memory):
        self.reads = 0
        self.writes = 0
        self.hits = 0
        self.misses = 0
        self.hitRate = 0
        self.missRate = 0
        self.cache = cache
        self.memory = memory
    
    def process(self, instruction):
        if (instruction.isOpWrite()):
            self.writes += 1
            instruction.result = "W"
            self.cache.write(instruction.adr, instruction.data)
        else:
            self.reads += 1
            result = self.cache.read(instruction.adr)
            if(result):
                instruction.result = "H"
            else:
                instruction.result = "M"
            #add logic to check hit and miss