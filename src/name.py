class Name:
    __MIN_LENGTH: int = 4
    
    def __init__(self, initial_name:str = None) -> None:
        #self.__name = self.__query_name()
        self.__name = initial_name if initial_name else self.__query_name()
    
    def __query_name(self) -> str:
        while True:
            name_input = input("What's your name? ").strip()
            if len(name_input) >= self.__MIN_LENGTH and name_input.isalnum():
                return name_input
            else:
                print("Wrong name")
    
    def rename(self) -> None:
        self.__name = self.__query_name()
    
    def __str__(self) -> str:
        return self.__name
    
    # Added for GUI compatibility
    @property
    def name(self) -> str:
        return self.__name