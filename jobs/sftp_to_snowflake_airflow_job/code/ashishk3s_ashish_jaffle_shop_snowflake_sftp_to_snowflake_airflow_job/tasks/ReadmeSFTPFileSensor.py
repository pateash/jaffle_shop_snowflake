from ashishk3s_ashish_jaffle_shop_snowflake_sftp_to_snowflake_airflow_job.utils import *

def ReadmeSFTPFileSensor():
    from airflow.providers.sftp.sensors.sftp import SFTPSensor

    return SFTPSensor(
        task_id = "ReadmeSFTPFileSensor",
        path = "{{ params.SFTP_FILE_LOCATION }}",
        sftp_conn_id = "sftp_prophecy",
        poke_interval = 60,
        timeout = 600,
    )
