from pairwise_comparison_session import PairwiseComparisonSession
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Pairwise comparison tool')
    parser.add_argument('--options', nargs='+', help='List of options to compare')
    return parser.parse_args()

def get_user_options():
    options = []
    print("Enter options one by one (press enter to finish):")
    while True:
        option = input("Option: ").strip()
        if not option:
            break
        options.append(option)
    return options

def main():
    args = parse_arguments()
    
    if args.options:
        options = args.options
    else:
        options = get_user_options()
        
    if not options:
        print("No options provided!")
        return
        
    print(f"Working with options: {options}")

if __name__ == "__main__":
    main()