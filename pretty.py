import sys
import ujson as json
from structlog.dev import ConsoleRenderer

def main():
    c = ConsoleRenderer()
    for line in sys.stdin:
        d = json.loads(line)
        print(c(None, None, d))

if __name__ == '__main__':
    main()
