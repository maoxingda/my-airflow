from airflow.decorators import dag, task
from airflow.utils.dates import days_ago, datetime


@task()
def print_today():
    print(datetime.today())


@dag(start_date=datetime(year=2021, month=6, day=27),
     schedule_interval='@daily'
     )
def daily_days_ago_2():
    print_today()


dag = daily_days_ago_2()
