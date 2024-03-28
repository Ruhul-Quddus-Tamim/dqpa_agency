**Data Quality Check Pipeline**

- This pipeline is build for checking any data quality checks which supports csv file
- Ready for use in production
- Can easily integrate into any Data Engineering pipeline
- Data from raw source and the data which already resides in production clusters like AWS Redshift or BigQuery can be pulled and compare quality checks between two sources
- If there is any mismatch between two sources it will trigger an alert by the Alert Agent to send an email through SMPT server with detailed information which/what is having issue
