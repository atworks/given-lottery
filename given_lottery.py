import secrets
import sys

def draw_lots(data=None):
    if data is None:
        return -1
    
    lot_member = data.split(',')
    r = secrets.randbelow(len(lot_member))

    return lot_member[r]

if __name__ == '__main__':
    args = sys.argv
    print(draw_lots(args[1]))
