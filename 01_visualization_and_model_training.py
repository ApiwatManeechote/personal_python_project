# As I'm coding Python in Google Colab, I need to upload my file here before I start doing anything.
# Once I run this 2 lines, the platform will allow me to click and upload the file.

from google.colab import files
uploaded = files.upload()

# There's some library that should be imported to ease our tasks just like in R that we installed many packages.
import sqlite3
import pandas as pd
import numpy as np

# Make a connection to the file that I have just uploaded.
con = sqlite3.connect("chinook_updated.db")

query = """
SELECT
    ar.Name AS artist_name,
    (SELECT COUNT(t.TrackId)
        FROM albums al
        JOIN tracks t ON al.AlbumId = t.AlbumId
        WHERE al.ArtistId = ar.ArtistId) AS track_count,
    (SELECT SUM(il.UnitPrice * il.Quantity)
        FROM albums al
        JOIN tracks t ON al.AlbumId = t.AlbumId
        JOIN invoicelines il ON il.TrackId = t.TrackId
        WHERE al.ArtistId = ar.ArtistId) AS total_sales
FROM artists ar
WHERE total_sales IS NOT NULL AND track_count IS NOT NULL;
"""

df = pd.read_sql_query(query, con)

# We can plot a graph with Python as well.
# Here I try scatter plot.
import matplotlib.pyplot as plt

df.plot(x = "total_sales", y = "track_count", kind = "scatter", color = "red")
plt.title("Track Count vs Total Sales")
plt.show()

# If we'd like to know the correlation between the total_sales and the track_count, we can find out by using this.
cor = df["total_sales"].corr(df["track_count"])


# Model Training in Python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 1. Split Data
x = df[["track_count"]]
y = df["total_sales"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 99)

# 2. Train Model
model = LinearRegression()
model.fit(x_train, y_train)

# 3. Score
p = model.predict(x_test)

# 4. Evaluate
rmse = mean_squared_error(y_test, p)
