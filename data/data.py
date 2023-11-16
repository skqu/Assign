import mysql.connector


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
        self.mydb = mysql.connector.connect(
        host=self.config["host"],
        user=self.config["user"],
        password=self.config["password"],
        database=self.config["database"]
        )   

        self.mycursor = self.mydb.cursor()

        self.mycursor.execute("SHOW TABLES")

        tables = []

        for x in self.mycursor:
            tables.append(x[0])
        
        if "history" not in tables:
                self.mycursor.execute("CREATE TABLE history (`ID` INT NOT NULL AUTO_INCREMENT, `equation` VARCHAR(45) NOT NULL, PRIMARY KEY (`ID`));")
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
        for index, entry in enumerate(self.history, 1):
            btn = self.DPLHistory.getChild()[index - 1]
            btn.set(str(index) + ") " + entry)


        
        sql = "INSERT INTO `calculator`.`history` (`equation`) VALUES ('" + self.data + "');"
        self.mycursor.execute(sql)
        self.mydb.commit()
            
            
        self.data = ""
        self.result.set(self.data)

    def Load(self):
        """
        Load the data from the history and sent to display. 
    
        """
        self.mycursor.execute("SELECT equation FROM history")

        myresult = self.mycursor.fetchall()

        for index, entry in enumerate(myresult, 1):
            self.history.insert(0, entry[0])

        for index, entry in enumerate(self.history, 1):
            btn = self.DPLHistory.getChild()[index - 1]
            btn.set(str(index) + ") " + entry)
        
if __name__ == "__main__":
    db = DATA()
    print(db.read())
