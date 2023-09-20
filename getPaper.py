import argparse

from editors.HAL import getHAL
from editors.arXiv import getArXiv


parser = argparse.ArgumentParser(description="PaperPulse")
parser.add_argument("--keys", type=str, default="keywords.yaml", help='path to the keywords')
parser.add_argument("-X","--arXiv", action = 'store_true', default=False, help='Get articles from arXiv')
parser.add_argument("-H","--HAL", action='store_true', default=False, help='Get articles from HAL')
parser.add_argument('--nb', type=int, default=1, help='Number of articles you are getting from all publishers')
opt = parser.parse_args()

   
def main(arg):
    if arg.HAL :
        print("Articles from HAL : \n")
        getHAL(arg.keys, arg.nb)
    if arg.arXiv:
        print("Articles from arXiv : \n")
        getArXiv(arg.keys, arg.nb)
    
    if not arg.arXiv and not arg.HAL : 
        print("No publishers selected")

if __name__ == "__main__":
    main(opt)