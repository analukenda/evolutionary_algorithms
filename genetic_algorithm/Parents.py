class Parents:
    def __init__(self,parent_1,parent_2):
        self.parent_1=parent_1
        self.parent_2=parent_2
    def __eq__(self, other):
        if self.parent_1 == other.parent_1:
            if self.parent_2 == other.parent_2:
                return True
            return False
        if self.parent_1 == other.parent_2:
            if self.parent_2 == other.parent_1:
                return True
            return False