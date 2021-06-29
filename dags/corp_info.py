import os
from subprocess import Popen, PIPE, check_output

from airflow.decorators import dag, task
from airflow.utils.dates import days_ago


# @task()
# def do_datax_job():
#     # python3 bin/datax.py /tmp/datax-job-dim.corp_info-to-corp_info.json
#     cmd = [
#         'python3',
#         '/Users/maoxd/open-source/DataX/target/archive-tmp/datax/bin/datax.py',
#         '/tmp/datax-job-dim.corp_info-to-corp_info.json'
#     ]
#     # with Popen(cmd, text=True, shell=True) as child_proc:
#     out = check_output(cmd, shell=True, text=True)
#     print(out)
#
#
# @dag(start_date=days_ago(0),
#      schedule_interval='@once',
#      tags=[os.path.basename(__file__).split('.')[0]])
# def corp_info():
#     do_datax_job()


# dag = corp_info()
# import subprocess as sp
# cmd = [
#     'python3',
#     '/Users/maoxd/open-source/DataX/target/archive-tmp/datax/bin/datax.py',
#     '/tmp/datax-job-dim.corp_info-to-corp_info.json'
# ]
# # with Popen(cmd, text=True, shell=True) as child_proc:
# out = sp.run(cmd, shell=True, text=True,
#              stdout=sp.PIPE, stderr=sp.STDOUT)
# print(out)
#
