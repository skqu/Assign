class DATA:
    _instance = None


    def __new__(cls):
        """
        Initialize a singleton instance of the data class.

        """
        if cls._instance is None:
            cls._instance = super(DATA, cls).__new__(cls)
        return cls._instance


    def __init__(self):
        """
        Initialiserer en instans af data class.

        """
        pass


    def _DataInit(self):
        """
        Initialize the data class, from singleton. 
        This inititialize the first instance. 
        
        """
        self.data = ""
        self.history = []
        self.result = None
        self.DPLHistory = None
        

    def Config(self, cnf):
        """
        Configure the data class. 
    
        :param cnf: The config for the data connection
        :type cnf: dict
        """


    def read(self) -> str:
        """
        Read function to get the current data. 

        :return: Return the current data.
        :rtype: str
        """
        return self.data


    def connect(self) -> int:
        """
        Dependent on the configuration make the connect. 
    
        :return: 0 for everything is fine, and the connection is established.
                If error see error codes. 
        :rtype: int
        """
        return 0
    

    def write(self, content) -> None:
        """
        Write data to current buffer. 
    
        :param content: content to be written to the data
        :type content: str
        :return: None
        :rtype: None
        """
        self.data = content
        self.result.set(self.data)

    
    def SetDisplay(self, display, function):
        """
        Configure the display for the data. 
    
        :param display: The obj from a display class. 
        :type display: obj
        :param function: The function of the display. 
        :type function: str
        """

        if function == "Result": 
            self.result = display
        elif function == "History":
            self.DPLHistory = display
        else:
            self.result = None
            self.DPLHistory = None


    def Save(self):
        """
        Save the data to the history. 
    
        """
        self.history.insert(0, self.data)
        for his in self.history:
            btn = self.DPLHistory.getChild()[self.history.index(his)] 
            data =  str(self.history.index(his) + 1) + ") " + his
            btn.set(data)
        self.data = ""
        self.result.set(self.data)

    def Load(self):
        """
        Load the data from the history and sent to display. 
    
        """

if __name__ == "__main__":
    db = DATA()
    print(db.read())