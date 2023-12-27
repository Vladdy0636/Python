class CollisionCheck():
    
    @staticmethod
    def within_x(co1, co2):
        if (co2.x1 < co1.x1 < co2.x2) \
                or (co2.x1 < co1.x2 < co2.x2) \
                or (co1.x1 < co2.x1 < co1.x2) \
                or (co1.x1 < co2.x2 < co1.x2):
            return True
        else:
            return False

    @staticmethod
    def within_y(co1, co2):
        if (co2.y1 < co1.y1 < co2.y2) \
                or (co2.y1 < co1.y2 < co2.y2) \
                or (co1.y1 < co2.y1 < co1.y2) \
                or (co1.y1 < co2.y2 < co1.y2):
            return True
        else:
            return False

    @staticmethod
    def collided_left(co1, co2):
        if CollisionCheck.within_y(co1, co2):
            if co2.x2 >= co1.x1 >= co2.x1:
                return True
        return False

    @staticmethod
    def collided_right(co1, co2):
        if CollisionCheck.within_y(co1, co2):
            if co2.x1 <= co1.x2 <= co2.x2:
                return True
        return False

    @staticmethod
    def collided_top(co1, co2):
        if CollisionCheck.within_x(co1, co2):
            if co2.y2 >= co1.y1 >= co2.y1:
                return True
        return False

    @staticmethod
    def collided_bottom(y, co1, co2):
        if CollisionCheck.within_x(co1, co2):
            y_calc = co1.y2 + y
            if y_calc >= co2.y1 >= co1.y2:
                return True
        return False
