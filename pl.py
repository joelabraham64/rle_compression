import numpy as np
import matplotlib . pyplot as plt
plt . figure ()
plt . xlim (0 , 5 )
plt . ylim (0 , 5 )
plt . grid (True , which ='both')
x = np . linspace (0 ,5 , 100 )
plt . plot (x , x-1 )
plt . savefig (" Question7Output .pdf ")