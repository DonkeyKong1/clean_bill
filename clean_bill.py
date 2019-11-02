from sqlalchemy.engine import create_engine
import sqlalchemy as sql_db
from pandas import read_excel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class CleanBill:

    def __init__(self):
        self._engine = create_engine('sqlite:///:memory:', echo=True)

        self._session = sessionmaker(bind=self._engine)()
        self._connection = self._engine.connect()

        self._DBase = declarative_base()

        self.DayOfTheWeek = None
        self.Rate = None

    @property
    def session(self):
        return self._session

    @property
    def connection(self):
        return self._connection

    def make_database(self):
        class DayOfTheWeek(self._DBase):
            __tablename__ = 'Day_Of_The_Week'
            Day_Of_The_Week_ID = sql_db.Column(sql_db.Integer, autoincrement=False, nullable=False, primary_key=True)
            Day_Of_The_Week = sql_db.Column(sql_db.VARCHAR(15), nullable=False, unique=True)
            Is_Weekday = sql_db.Column(sql_db.Boolean, nullable=False)

        class Rate(self._DBase):
            __tablename__ = 'Rate'
            Rate_ID = sql_db.Column(sql_db.Integer, autoincrement=True, nullable=False, primary_key=True)
            Rate = sql_db.Column(sql_db.REAL, nullable=False)
            Hour = sql_db.Column(sql_db.Integer, nullable=True)
            Is_Weekday = sql_db.Column(sql_db.Boolean, nullable=True)
            Rate_Type = sql_db.Column(sql_db.VARCHAR(25), nullable=False)
            Number_Of_Times_Per_Month = sql_db.Column(sql_db.Integer, nullable=True)
            Units = sql_db.Column(sql_db.VARCHAR(5), nullable=False)

            __table_args__ = (sql_db.CheckConstraint('"Rate_Type" IN ("Standard", "Demand")'),
                              sql_db.CheckConstraint('"Units" IN ("kW", "kWh")'),
                              )

        self._DBase.metadata.create_all(self._engine)

        self.DayOfTheWeek = DayOfTheWeek
        self.Rate = Rate

    def load_data(self):
        self._load_day_of_the_week()
        self._load_rate()
        self._load_customer_data()

    def _load_rate(self):
        r, h, iw, rt, ntpm, u = 'Rate', \
                                'Hour', \
                                'Is_Weekday', \
                                'Rate_Type', \
                                'Number_Of_Times_Per_Month', \
                                'Units'

        self._session.add(self.Rate(**{r: 20, rt: 'Demand', ntpm: 1, u: 'kW'}))

        rate_type = 'Standard'
        ut = 'kWh'

        for hour in range(24):
            self._session.add(self.Rate(**{r: .05, h: hour, iw: 0, rt: rate_type, u: ut}))
            if 0 <= hour < 16:
                self._session.add(self.Rate(**{r: .2, h: hour, iw: 1, rt: rate_type, u: ut}))
            elif 16 <= hour < 21:
                self._session.add(self.Rate(**{r: .3, h: hour, iw: 1, rt: rate_type, u: ut}))
            else:
                self._session.add(self.Rate(**{r: .1, h: hour, iw: 1, rt: rate_type, u: ut}))
        self._session.commit()

    def _load_day_of_the_week(self):
        id = 'Day_Of_The_Week_ID'
        dow = 'Day_Of_The_Week'
        iw = 'Is_Weekday'
        self._session.add(self.DayOfTheWeek(**{id: 0, dow: 'Sunday', iw: 0}))
        self._session.add(self.DayOfTheWeek(**{id: 1, dow: 'Monday', iw: 1}))
        self._session.add(self.DayOfTheWeek(**{id: 2, dow: 'Tuesday', iw: 1}))
        self._session.add(self.DayOfTheWeek(**{id: 3, dow: 'Wednesday', iw: 1}))
        self._session.add(self.DayOfTheWeek(**{id: 4, dow: 'Thursday', iw: 1}))
        self._session.add(self.DayOfTheWeek(**{id: 5, dow: 'Friday', iw: 1}))
        self._session.add(self.DayOfTheWeek(**{id: 6, dow: 'Saturday', iw: 0}))
        self._session.commit()

    def _load_customer_data(self):
        read_excel(r'data.xlsx',
                   sheet_name='Sheet1').to_sql(name='Energy_Data',
                                               con=self._connection,
                                               if_exists='append',
                                               index_label='Reading_ID')

    def calculate_energy_cost(self):
        return self.connection.execute("""
            SELECT      SUM(ED.kWh * R.Rate)
            FROM        "Energy_Data"       AS  ED
            INNER JOIN  "Day_Of_The_Week"   AS  DOW ON  DOW.Day_Of_The_Week_ID  =   strftime('%w', DateTime)
            INNER JOIN  "Rate"              AS  R   ON  R.Hour                  =   strftime('%H', DateTime)
            GROUP BY    strftime('%Y%m', DateTime)
            """).fetchone()[0]

    def calculate_demand_cost(self):
        kwh = self.connection.execute("""
        SELECT      Max(ED.kWh)
        FROM        "Energy_Data"       AS  ED
        """).fetchone()[0]
        rate = self.connection.execute("""
        SELECT      Rate
        FROM        "Rate"
        """).fetchone()[0]

        return kwh * rate


if __name__ == '__main__':
    db = CleanBill()
    db.make_database()
    db.load_data()
    print(db.calculate_energy_cost())
    print(db.calculate_demand_cost())
