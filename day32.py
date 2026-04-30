'''
import matplotlib.pyplot as plt
plt.bar([2024,2025,2026],[67,89,50],color = "blue")
plt.title("Car Sales")
plt.xlabel("Years")
plt.ylabel("Number of cars sold")
plt.show()
'''
'''
import matplotlib.pyplot as plt
plt.pie([40,15,35,20],labels=["Backend(Python)","Frontend(HTML,CSS)","Database(MySQL)","Testing"])
plt.title("ATM Application(Project)")
plt.legend(["Raj","Sumesh","Ansh","Yan"])
plt.show()

import matplotlib.pyplot as plt
plt.scatter([1,2,3,4],[200,400,100,800],color="Yellow",s=200)
plt.title("Swift Car Sales")
plt.xlabel("Years")
plt.ylabel("Number of Sales")
plt.show()
'''
'''
import matplotlib.pyplot as plt

# Book names
books = ["The Alchemist", "Velvet", "Mission", "Objects","Think and Grow", "The Red", "Dream Job","Voodoo", "Olympics", "Black Maria"]

# Prices (example data – meeru change cheyochu)
prices = [51, 52, 48, 45, 51, 22, 32, 18, 22, 46]

# Plot bar chart
plt.figure(figsize=(10,6))
plt.bar(books, prices)

# Titles and labels
plt.title("Book Prices (Top 10)")
plt.xlabel("Books")
plt.ylabel("Price")

# Rotate x labels (important)
plt.xticks(rotation=90)

# Show graph
plt.tight_layout()
plt.show()
'''



