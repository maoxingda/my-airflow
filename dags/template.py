import os

from datetime import datetime as dt

from airflow.operators.bash import BashOperator
from airflow.models import DAG

with DAG(
        dag_id=os.path.basename(__file__),
        start_date=dt(year=2021, month=6, day=27),
        schedule_interval='@once'
) as dag:
    print_cur_date = BashOperator(task_id='print_cur_date',
                                  bash_command='/tmp/print_cur_date.sh ',
                                  env={
                                      'cur_date': '{{ ds }}'
                                  }
                                  )
