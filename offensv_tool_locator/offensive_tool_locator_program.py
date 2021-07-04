from offensive_tool_locator import gh_api_search_for_cves, gh_api_search_for_rats
import click
import sys


class style():
    RED = '\033[31m'
    GREEN = '\033[32m'
    IGREEN = '\033[92m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    PURPLE = '\033[1;35m'
    GRAY = '\033[1;30m'
    WHITE = '\033[37m'
    END = '\033[0m'


print(style.BLUE + '1 ' + style.MAGENTA+'Retrieve recently updated CVE-2021* related repos')
print(style.BLUE + '2 ' + style.MAGENTA+'Retrieve recently updated remote access tool/trojan')
print(style.RED + '9 ' + style.RED + 'Quit Program' + style.END)
print('\n')


@click.command()
@click.option('--m', prompt="Enter your selection from the above menu: ", type=int)
def main(m):
    print('\n')
    while True:
        if m == 9:
            sys.exit('Exiting program...')
       
        elif m == 1:
            gh_api_search_for_cves()
            break
         
        elif m == 2:
            gh_api_search_for_rats()
            break
        else:
            sys.exit("Sorry, didn't understand your selection, try again. Exiting...")


if __name__ == '__main__':
    main()
