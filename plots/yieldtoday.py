import sqlite3, pandas, matplotlib.pyplot as plt

con = sqlite3.connect("../solar_data.db")

sql = """select
            yieldtoday
        from
            DOWNLOADED_SOLAX_INFO
        order by
            time_of_request desc
        limit 50;
        """

data = pandas.read_sql(sql, con)

plt.plot(data.yieldtoday, label = "Yield today")
plt.grid()
plt.legend()
plt.title("Yield Today")
#plt.show()
#plt.savefig('/var/www/html/proto/cheese.png')
plt.savefig('yieldtoday0.png')
