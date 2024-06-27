wget is a command-line utility for downloading files from the web. It supports downloading via HTTP, HTTPS, and FTP protocols.

https://lnkd.in/gfENQi7K- shortended url

https://raw.githubusercontent.com/LinkedInLearning/hands-on-introduction-data-engineering-4395021/main/data/top-level-domain-names.csv - link of the csv file to be downloaded

create a folder named manual in lab

$ wget -c https://raw.githubusercontent.com/LinkedInLearning/hands-on-introduction-data-engineering-4395021/main/data/top-level-domain-names.csv -O /workspaces/AIRFLOW-HANDSON/airflow/lab/manual/manual-extract-data.csv

wget: The command to download files from the web.
-c: This option allows you to continue getting a partially-downloaded file.
https://raw.githubusercontent.com/LinkedInLearning/hands-on-introduction-data-engineering-4395021/main/data/top-level-domain-names.csv: The URL of the file to be downloaded.
-O /workspaces/hands-on-introduction-data-engineering-4395021/lab/manual/manual-extract-data.csv: This option specifies the output file path and name where the downloaded file will be saved.