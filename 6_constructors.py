# 6. constructors and destructors 

class Logger:
    def __init__(self):
        # constructors message
        print("Logger object created.")
        
    def __del__(self):
        print("Logger object destructors.")
        
logger1 = Logger()
del logger1