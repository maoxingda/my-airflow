import pendulum
from airflow.decorators import dag, task
from airflow.utils.dates import days_ago, datetime

locale_tz = pendulum.timezone('Asia/Shanghai')


@task()
def print_today():
    print(datetime.today())


@dag(start_date=datetime(year=2021, month=6, day=26, tzinfo=locale_tz),
     schedule_interval='@daily'
     )
def daily_days_ago_0():
    print_today()


dag = daily_days_ago_0()
