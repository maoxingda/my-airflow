from datetime import datetime as dt

from airflow.decorators import dag, task
from airflow.hooks.subprocess import SubprocessHook


@task()
def gen_datax_jobs_file():
    return {
        "jobs": [
            "/tmp/datax-job-dim.corp_info-to-corp_info.json",
            "/tmp/datax-job-dim.corp_info-to-corp_info.json"
        ]
    }


@task()
def do_datax_jobs(jobs_conf):
    SubprocessHook().run_command(command=[
        'bash',
        '-c',
        f'/usr/local/bin/python3 '
        f'/Users/maoxd/open-source/DataX/target/archive-tmp/datax/'
        f'bin/datax.py {jobs_conf["jobs"][0]}'
    ])


@dag(start_date=dt(year=2021, month=6, day=27),
     schedule_interval='@once', tags=['datax-tool'])
def redshift_to_es():
    jobs_conf = gen_datax_jobs_file()
    do_datax_jobs(jobs_conf)


dag = redshift_to_es()
