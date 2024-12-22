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

    pairwise_comparison_session = PairwiseComparisonSession()
    pairwise_comparison_session.store_options(options)

    print(pairwise_comparison_session.option_map)

    for i in range(0, len(options)):
        for j in range(i + 1, len(options)):
            option1 = pairwise_comparison_session.get_option(i)
            option2 = pairwise_comparison_session.get_option(j)
            
            print(f"\nComparing: {option1} vs {option2}")
            while True:
                choice = input(f"Which do you prefer? (1 for {option1}, 2 for {option2}): ").strip()
                if choice in ('1', '2'):
                    break
                print("Please enter 1 or 2")
            
            if choice == '1':
                pairwise_comparison_session.store_result_from_user(i)
            else:
                pairwise_comparison_session.store_result_from_user(j)

    results = pairwise_comparison_session.generate_results()
    print("\nResults:")
    print("-" * 40)
    for index, option, score in results:
        print(f"Index: {index:2d} | Option: {option:15s} | Score: {score}")
    print("-" * 40)

if __name__ == "__main__":
    main()