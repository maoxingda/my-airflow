from datetime import datetime as dt

from airflow.decorators import dag, task


@task()
def task1():
    return {
        'k1': 'v1'
    }


@task()
def task2(arg1):
    for k, v in arg1.items():
        print(k, v)


@dag(start_date=dt(year=2021, month=6, day=27),
     schedule_interval='@once'
     )
def xcom_type():
    task2(task1())


dag = xcom_type()
