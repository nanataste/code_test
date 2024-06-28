# The code you provided is creating a line plot using the `matplotlib` library in Python. Here's a
# breakdown of what each part of the code is doing:
# import matplotlib.pyplot as plt


# X = [ "Mon", "Tue", "Wed", "Thur", "Fri",  "Sat", "Sun" ] 
# Y1 = [15.6, 14.2, 16.3, 18.2, 17.1, 20.2, 22.4]
# Y2 = [20.1, 23.1, 23.8, 25.9, 23.4, 25.1, 26.3]

# plt.plot(X, Y1, label="Seoul")		
# plt.plot(X, Y2, label="Busan")		
# plt.xlabel("day")
# plt.ylabel("temperature")
# plt.legend(loc="upper left")
# plt.title("Temperatures of Cities")
# plt.show()


# import matplotlib.pyplot as plt


# X = [ "Mon", "Tue", "Wed", "Thur", "Fri",  "Sat", "Sun" ] 
# plt.plot(X, [15.6, 14.2, 16.3, 18.2, 17.1, 20.2, 22.4], "sm")
# plt.show()

# import matplotlib.pyplot as plt


# X = [ "Mon", "Tue", "Wed", "Thur", "Fri",  "Sat", "Sun" ] 
# Y = [15.6, 14.2, 16.3, 18.2, 17.1, 20.2, 22.4]
# plt.bar(X, Y)
# plt.show()

import matplotlib.pyplot as plt
import numpy as np

numbers = np.random.normal(size=10000)

plt.hist(numbers)
plt.xlabel("value")
plt.ylabel("freq")
plt.show()
