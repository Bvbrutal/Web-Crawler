from colorama import init, Fore

def print_formatted_info(name, age):
    # 初始化 colorama 库，使彩色输出生效
    init(autoreset=True)

    # 使用 f-string 格式化输出
    print(f"姓名: {Fore.GREEN}{name}{Fore.RESET}")
    print(f"年龄: {Fore.BLUE}{age}{Fore.RESET}")

from termcolor import colored

def print_colored_text():
    text = "Hello, World!"
    colored_text = colored(text, 'red', 'on_yellow')
    print(colored_text)

print_colored_text()

from colorama import init, Fore, Back, Style

def print_styled_text():
    init(autoreset=True)
    text = "Hello, World!"
    styled_text = f"{Fore.RED}{Back.YELLOW}{Style.BRIGHT}{text}"
    print(styled_text)

print_styled_text()

from tabulate import tabulate
def show():
    data = [
        ["John Doe", 30],
        ["Jane Smith", 25],
        ["Michael Johnson", 35]
    ]

    headers = ["Name", "Age"]

    print(tabulate(data, headers=headers, tablefmt="grid"))


name = "John Doe"
age = 30
print_formatted_info(name, age)
print_colored_text()
print_styled_text()
show()
from colorama import init, Fore

def print_colored_message(message):
    # 初始化 colorama 库，使彩色输出生效
    init(autoreset=True)

    # 使用 f-string 格式化输出，添加颜色
    colored_message = f"{Fore.GREEN}{message}{Fore.RESET}"
    print(colored_message)

if __name__ == "__main__":
    message = "上传结束！"
    print_colored_message(message)
