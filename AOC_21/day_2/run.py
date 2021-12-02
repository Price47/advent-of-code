from .submarine import Submarine

if __name__ == '__main__':
    test = [
        'forward 5',
        'down 5',
        'forward 8',
        'up 3',
        'down 8',
        'forward 2'
    ]
    s = Submarine()
    s.run()
