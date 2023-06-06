import sqlite3, pandas, matplotlib.pyplot as plt

con = sqlite3.connect("../solar_data.db")

sql = """select
            acpower, yieldtoday, consumeenergy, batPower
        from
            DOWNLOADED_SOLAX_INFO
        where
            date(time_of_request, 'localtime') = current_date;
        """

data = pandas.read_sql(sql, con)

# AC Power
plt.subplot(2, 2, 1)
plt.plot(data.acpower, label = "AC Power")
plt.title("AC Power")

# Yield Today
plt.subplot(2, 2, 2)
plt.plot(data.yieldtoday, label = "Yield Today")
plt.title("Yield Today")

# Consume Energy
plt.subplot(2, 2, 3)
plt.plot(data.consumeenergy, label = "Consume Energy")
plt.title("Consume Energy")

# Battery Power
plt.subplot(2, 2, 4)
plt.plot(data.batPower, label = "Battery Power")
plt.title("Battery Power")

plt.savefig('sub0.png', dpi=400)
