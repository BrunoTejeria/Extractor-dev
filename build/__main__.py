from src.modules.m_main.ex import init
import sys




sys.dont_write_bytecode = True
sys.py_cache_prefix = 'etc/cache'



def main():
    init()

if __name__ == '__main__':
    main()
