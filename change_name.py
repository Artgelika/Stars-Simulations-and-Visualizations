# necessary library:
import os


pathh = r".../Stars/input" 
filenames = os.listdir(pathh)
print(filenames)


# create a list from 0 to amount of filenames - 1
# I want to create an iterator which iter step by step over files 
order = [x for x in range(len(filenames))]
iterator = iter(order)


for filename in filenames:
    try:   
        os.rename(os.path.join(pathh, filename), # <- old name, below new name
                  os.path.join(pathh, "C" + str(next(iterator)) + ".csv"))
    except:
        pass
