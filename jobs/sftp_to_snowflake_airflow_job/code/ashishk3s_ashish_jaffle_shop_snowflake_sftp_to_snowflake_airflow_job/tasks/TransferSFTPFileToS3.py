from ashishk3s_ashish_jaffle_shop_snowflake_sftp_to_snowflake_airflow_job.utils import *

def TransferSFTPFileToS3():
    from airflow.providers.amazon.aws.transfers.sftp_to_s3 import SFTPToS3Operator

    return SFTPToS3Operator(
        task_id = "TransferSFTPFileToS3",
        sftp_conn_id = "sftp_prophecy",
        sftp_path = "{{ params.SFTP_FILE_LOCATION }}",
        s3_key = "{{ params.S3_FULL_KEY_PATH }}",
        s3_bucket = "{{ params.S3_BUCKET }}",
        s3_conn_id = "aws_default",
        use_temp_file = True,
    )
