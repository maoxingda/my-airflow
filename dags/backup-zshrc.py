import os

from datetime import datetime as dt

from airflow.operators.bash import BashOperator
from airflow.models import DAG

with DAG(
        dag_id=os.path.basename(__file__),
        start_date=dt(year=2021, month=6, day=29),
        schedule_interval='@daily'
) as dag:
    BashOperator(task_id='backup',
                 bash_command='/Users/maoxd/open-source/zsh/cron-backup-zshrc.sh '
                 )
