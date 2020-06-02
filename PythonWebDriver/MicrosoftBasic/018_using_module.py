# This is a script that is importing a method from a different file and showing the way to import it

import helpers_018                              #Importing everything under the module
from helpers_018 import *                       #Importing everything under the module
from helpers_018 import display                 #Importing a function from a module

helpers_018.display('Not a warning' ,True)            #import helpers_018


display('Not a warning')                        #from helpers_018 import *


display('Not a warning ')                        #from helpers_018 import display
