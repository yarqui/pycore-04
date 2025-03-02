import sys
from pathlib import Path
from colorama import Fore

def visualize_structure():
    if len(sys.argv) > 1:
        path = Path(sys.argv[1])

        if not path.exists():
            print(f"{Fore.RED}Error: The path '{path}' does not exist.")
            return
        if not path.is_dir():
            print(f"{Fore.RED}Error: '{path}' is not a directory.")
            return

        def traverse_directory(directory, level=0):
            for item in sorted(directory.iterdir(), key=lambda x: (not x.is_dir(), x.name)):
                indent = "    " * level  # Indentation for visual structure
                if item.is_dir():
                    print(f"{indent}{Fore.BLUE}📂 {item.name}")
                    traverse_directory(item, level + 1)
                else:
                    print(f"{indent}{Fore.GREEN}📜 {item.name}")

    print(f"{Fore.YELLOW}📂 Root: {path.name}")
    traverse_directory(path)
        
if __name__ == '__main__':
    visualize_structure()