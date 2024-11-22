
class User:

    __user_cntr = 0

    def __init__(self, frist_name, last_name):
        User.__user_cntr += 1
        self.id = User.__user_cntr
        self.first_name = frist_name
        self.last_name = last_name

    def __eq__(self, other):
        if self.first_name == other.first_name and self.last_name == other.last_name:
            return True
        return False