from .game_interface import GameInterface


class VariableHolder:
    def __init__(self):
        self.SIZE = 8
        self.QUALITY = "low"
        self.ANIMATIONS = True
        self.TOTAL_TICKS = {
            "low": 5,
            "medium": 10,
            "high": 20,
            "ultra": 40
        }
        self.TICKS_INTERVAL = {
            "low": 200,
            "medium": 100,
            "high": 50,
            "ultra": 30,
        }
        self.SCALE = 1
        self.GAME_INTERFACE = GameInterface()
        self.TYPES = ['CCCCCC', 'CCCGCC', 'CCCPCC', 'CCCRGR', 'CGGCGG',
                      'CGGGCC', 'CGGPPG', 'CPGPCC', 'CRCCRC', 'GCCRPG',
                      'GGCGGC', 'GGGGGC', 'GGGGGG', 'GGGGGR', 'GGGPPG',
                      'GGPGPP', 'GGRGGG', 'GGRGRG', 'GPRGPR', 'GRGGRG',
                      'GRPGRG', 'PGGPGG', 'PPGPPG', 'PPGRRG']
        self.COLORS = ["red", "blue"]


variables = VariableHolder()
