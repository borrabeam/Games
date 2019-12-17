# define Python user-defined exceptions

class Error(Exception):
   """Base class for other exceptions"""
   pass
class InvalidCardRank(Error):
   """Raised when the input card rank is not a valid rank"""
   pass
class InvalidCardSuit(Error):
   """Raised when the input card suit is not a valid suit"""
   pass
class InvalidInput(Error):
   """Raised when the input option is not Yes or Not """