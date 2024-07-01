import pathlib


def tryingToSleep(test_case_file):
    
    cases=0
    try:
        cases = [num.rstrip().lower() for num in open(pathlib.Path(__file__).parent.resolve().joinpath(test_case_file))]
    except(FileNotFoundError):
        raise Exception(f'The "{test_case_file}" file must exist in the directory: {pathlib.Path(__file__).parent.resolve()}.')

    number_of_cases=int(cases[0])

    #Some validations
    if number_of_cases != (cases.__len__()-1):
        raise Exception(f'The number of cases specified ({number_of_cases}) in the "{test_case_file}" file does not match the actual number ({cases.__len__()-1})')
    elif number_of_cases >100:
        raise Exception(f'The number of cases is greater than allowed (100)')
    elif number_of_cases < 1:
        raise Exception(f'The number of cases is less than allowed (1)')

    cases.pop(0) #removing the number of cases from the list 
    case_number=1
    for num in cases:
        number=int(num)
        if number < 0:
            raise Exception(f'The case #{case_number} is less than 0')
        elif number > 200:
            Exception(f'The case #{case_number} is greater than 200')
        elif number==0:
            print(f'Case #{case_number}: INSOMNIA')  
        else:
            digits=set()
            i=0
            while(digits.__len__()<10):
                i=i+1
                digits=digits.union(set(list(str(number*i))))

            print(f'Case #{case_number}: {number*i}')
                
        case_number=case_number+1
            


if __name__ == "__main__":
    tryingToSleep('c-input.in')