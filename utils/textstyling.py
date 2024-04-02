class TextStyle:
    __FAIL = "\033[91m"
    __WARNING = "\033[93m"
    
    __OKGREEN = "\033[92m"
    __OKBLUE = "\033[94m"
    __OKCYAN = "\033[96m"
    
    __HEADER = "\033[95m"
    __BOLD = "\033[1m"
    __UNDERLINE = "\033[4m"
    
    __ENDC = "\033[0m"
    
    def fail(self, text: str) -> str:
        return str(f"{self.__FAIL}{text}{self.__ENDC}")
    
    def warning(self, text: str) -> str:
        return str(f"{self.__WARNING}{text}{self.__ENDC}")
    
    def okgreen(self, text: str) -> str:
        return str(f"{self.__OKGREEN}{text}{self.__ENDC}")
    
    def okblue(self, text: str) -> str:
        return str(f"{self.__OKBLUE}{text}{self.__ENDC}")

    def okcyan(self, text: str) -> str:
        return str(f"{self.__OKCYAN}{text}{self.__ENDC}")
    
    def header(self, text: str) -> str:
        return str(f"{self.__HEADER}{text}{self.__ENDC}")

    def bold(self, text: str) -> str:
        return str(f"{self.__BOLD}{text}{self.__ENDC}")

    def underline(self, text: str) -> str:
        return str(f"{self.__UNDERLINE}{text}{self.__ENDC}")
