import secrets
import sys

def draw_lots(data=None):
    if data is None:
        return -1
    
    return secrets.choice(data.split(','))

if __name__ == '__main__':
    args = sys.argv
    print(draw_lots(args[1]))
