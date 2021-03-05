import FAIRNessInfo

class Standard:
    TYPE = None
    TITLE = None
    DESCRIPTION = None
    FAIRNESS_INFO = None

    def __init__(self, type, title, description):
        self.TYPE = type
        self.TITLE = title
        self.DESCRIPTION = description