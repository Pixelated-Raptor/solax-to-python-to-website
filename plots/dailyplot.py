import sqlite3, pandas, matplotlib.pyplot as plt

con = sqlite3.connect("/home/kiwi/project/solar_data.db")

sql =   """select
                round(avg(acpower)) as ac,
                round(yieldtoday) as yieldtoday,
                round(consumeenergy, 1) as consume,
                batPower
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
plt.plot(data.ac, label = "AC Power")
plt.title("AC Leistung [W]")
plt.xlabel("Uhrzeit")
plt.grid(linestyle = '--', linewidth = 0.5)

# Yield Today
plt.subplot(2, 2, 2)
plt.plot(data.yieldtoday, label = "Yield Today")
plt.title("Tagesertrag [kWh]")
plt.xlabel("Uhrzeit")
plt.grid(linestyle = '--', linewidth = 0.5)

# Consume Energy
plt.subplot(2, 2, 3)
plt.plot(data.consume, label = "Consume Energy")
plt.title("Eigennutzung [kWh]")
plt.xlabel("Uhrzeit")
plt.grid(linestyle = '--', linewidth = 0.5)

# Battery Power
plt.subplot(2, 2, 4)
plt.plot(data.batPower, label = "Battery Power")
plt.title("Batterieleistung [W]")
plt.xlabel("Uhrzeit")
plt.grid(linestyle = '--', linewidth = 0.5)

x_tick_labels = ['0 uhr', '1 Uhr', '2 Uhr', '3 Uhr', '4 Uhr', '5 Uhr', '6 Uhr', '7 Uhr', '8 Uhr', '9 Uhr', '10 Uhr', '11 Uhr', '12 Uhr', '13 Uhr', '14 Uhr', '15 Uhr', '16 Uhr', '17 Uhr', '18 Uhr', '19 Uhr', '20 Uhr', '21 Uhr', '22 Uhr', '23 Uhr']
plt.tight_layout()
#plt.set_xticklabels(x_tick_labels)
plt.suptitle("Heutige Daten")
plt.subplots_adjust(top=0.85)
plt.savefig('/home/kiwi/project/plots/daily0.png', dpi=150)
