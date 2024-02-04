from signal import raise_signal
import sys, argparse


class Main():

    def __init__(self):
        self.handle_args()
        if self.args.v:
            print("Number of players:", self.args.num_players)
        if self.args.t:
            test()
    
    def handle_args(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument(
            "-v",
            help="increase output verbosity",
            action=argparse.BooleanOptionalAction,
            default=False
        )
        self.parser.add_argument(
            "-n",
            help="Number of players for the games",
            default=2,
            type=int
        )
        self.parser.add_argument(
            "-t",
            help="test func",
            action=argparse.BooleanOptionalAction
        )
        self.args = self.parser.parse_args()

def test():
    print("""
        
    Turno de: JP1 (X)
            
        #############
        # x # 0 # 0 #
        #############
        #   # x # x #
        #############
        # x # 0 # 0 #
        #############    

Inserta tu
    jugada (1-9): 1
    """)


if __name__ == "__main__":
    Main()
