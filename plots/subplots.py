import sqlite3, pandas, matplotlib.pyplot as plt

con = sqlite3.connect("../solar_data.db")

sql = """select
            acpower
        from
            DOWNLOADED_SOLAX_INFO
        order by
            time_of_request desc
        limit 50;
        """

data = pandas.read_sql(sql, con)

plt.plot(data.acpower, label = "AC Power")
plt.grid()
plt.legend()
plt.title("AC Power")
#plt.show()
#plt.savefig('/var/www/html/proto/cheese.png')
plt.savefig('cheese2.png')
