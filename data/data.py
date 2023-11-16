import csv

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
        self.config = cnf


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
        with open(self.config["file"], 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            for index, entry in enumerate(self.history, 1):
                data = f"{index}) {entry}"
                btn = self.DPLHistory.getChild()[index - 1]
                btn.set(data)
                csvwriter.writerow([data])
            
        self.data = ""
        self.result.set(self.data)

    def Load(self):
        """
        Load the data from the history and sent to display. 
    
        """
        try:
            with open(self.config["file"], 'r') as csvfile:
                    csvreader = csv.reader(csvfile)
                    loaded_data = [row[0] for row in csvreader]
                    self.history = loaded_data
                    for index, entry in enumerate(loaded_data, 1):
                        btn = self.DPLHistory.getChild()[index - 1]
                        btn.set(entry)
        except FileNotFoundError:
            print(f"File not found.")

if __name__ == "__main__":
    db = DATA()
    print(db.read())