from pathlib import Path

def total_salary(path: str) -> tuple | None:
    try:
        if type(path) is not str:
            raise TypeError('Path should be a string')

        with open(path, encoding='UTF-8') as fh:
            lines = [line.strip() for line in fh] #readlines is less efficient with memory as it loads all lines into memory at once
            number_of_employees = len(lines)
            total_salary = sum(int(line.split(',')[1]) for line in lines)
            average_salary = total_salary // number_of_employees if number_of_employees > 0 else 0

        return total_salary, average_salary 

    except Exception as err:
        print(f'{type(err)}: {err}')
        return None

def main():
    current_dir = Path(__file__).parent
    file_path = str(current_dir / 'employees.txt')
    print(total_salary(file_path))

if __name__ == '__main__':
    main()