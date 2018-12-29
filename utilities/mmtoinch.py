import sys
import pandas as pd
while True:
    number = input("mm?")
    if number == 'c':
        sys.exit(0)
    else:
        clip = f"{round((float(number)/25.4),4)}" 
        df=pd.DataFrame([clip])
        df.to_clipboard(index=False,header=False)
        print(clip)
        continue
   
