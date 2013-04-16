import time

class CurrentTime():
    def __init__(self):
        pass
    
    def getyear(self):
        FirstTerm = "Sep Oct Nov Dec"
        SecondTerm = "Jan Feb Mar Apr"
        ThirdTerm = "May Jun Jul Aug"
        currentyear = time.ctime()[4:7]
        if currentyear in Firstterm.split():
            currentTerm = "First"
        if currentyear in Secondterm.split():
            currentTerm = "Second"
        if currentyear in ThirdTerm.split():
            currentTerm = "Third"
        return currentTerm
            
def getyear():
    FirstTerm = "Sep Oct Nov Dec"
    SecondTerm = "Jan Feb Mar Apr"
    ThirdTerm = "May Jun Jul Aug"
    currentyear = time.ctime()[4:7]
    if currentyear in FirstTerm.split():
        currentTerm = "First"
    if currentyear in SecondTerm.split():
        currentTerm = "Second"
    if currentyear in ThirdTerm.split():
        currentTerm = "Third"
    return currentTerm
            
        