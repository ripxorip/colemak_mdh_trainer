import argparse

class Trainer():
    def __init__(self):
        pass

def main():
    parser = argparse.ArgumentParser(description='Tool to practice touch typing on my new ergo..')
    parser.add_argument('-b', '--buildcmd', help='Command used to build the project', required=False, nargs='+')

if __name__ == "__main__":
    main()
