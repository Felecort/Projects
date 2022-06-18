import matplotlib.pyplot as plt 
from random import random

percent_1_to_2 = 0.2
percent_2_to_1 = 0.3
current_stage = 1
stages = []
srages_append = stages.append

for i in range(100):
    if current_stage == 1:
        if random() < percent_1_to_2:
            current_stage = 2
            srages_append(current_stage)
        else:
            srages_append(current_stage)
            
    else:
        if random() < percent_2_to_1:
            current_stage = 1
            srages_append(current_stage)
        else:
            srages_append(current_stage)
            
            
plt.stem(stages)
plt.show()

