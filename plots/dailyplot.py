import sqlite3, pandas, matplotlib.pyplot as plt

con = sqlite3.connect("/home/kiwi/project/solar_data.db")

sql =   """select
                substr(time(time_of_request, 'localtime'), 1, 2) as hour,
                round(avg(acpower)) as ac,
                round(yieldtoday) as yieldtoday,
                round(consumeenergy, 1) as consume,
                round(feedinenergy, 1) as feedin
            from
                DOWNLOADED_SOLAX_INFO
            where
                date(time_of_request, 'localtime') = current_date
            group by
                substr(time(time_of_request, 'localtime'), 1, 2);
             """

data = pandas.read_sql(sql, con)

# AC Power
plt.subplot(2, 2, 1)
plt.plot(data.hour, data.ac)
plt.title("AC Leistung [W]")
plt.xticks(fontsize=5, rotation=90)
plt.xlabel("Uhrzeit")
plt.grid(linestyle = '--', linewidth = 0.5)

# Yield Today
plt.subplot(2, 2, 2)
plt.plot(data.hour, data.yieldtoday)
plt.xticks(fontsize=5, rotation=90)
plt.title("Tagesertrag [kWh]")
plt.xlabel("Uhrzeit")
plt.grid(linestyle = '--', linewidth = 0.5)

# Consume Energy
plt.subplot(2, 2, 3)
plt.plot(data.hour, data.consume)
plt.xticks(fontsize=5, rotation=90)
plt.title("Eigennutzung [kWh]")
plt.xlabel("Uhrzeit")
plt.grid(linestyle = '--', linewidth = 0.5)

# Battery Power
plt.subplot(2, 2, 4)
plt.plot(data.hour, data.feedin)
plt.xticks(fontsize=5, rotation=90)
plt.title("Einspeisung [kWh]")
plt.xlabel("Uhrzeit")
plt.grid(linestyle = '--', linewidth = 0.5)

plt.tight_layout()
plt.suptitle("Heutige Daten")
plt.subplots_adjust(top=0.85)
plt.savefig('/home/kiwi/project/plots/daily0.png', dpi=175)
