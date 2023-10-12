from src.modules.m_execute.execute import init
try:
    import rich
except ImportError:
    print('import error')


def main():
    init()

if __name__ == '__main__':
    main()
