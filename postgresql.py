# postgresql python client library
import psycopg2

# Heroku hosted postgresql database sesion credentials
HOSTNAME= 'ec2-44-206-214-233.compute-1.amazonaws.com'
DB='deivb838l9grl2'
USR='bhzvirilzchnmu'
PSWRD=''#
PORT=5432

# sql routines
def create_table(connection):
    connection.execute('CREATE TABLE IF NOT EXISTS JOBS("Company" text COLLATE pg_catalog."default","Location" text COLLATE pg_catalog."default","Title" text COLLATE pg_catalog."default","Description_link" text COLLATE pg_catalog."default","Description" text COLLATE pg_catalog."default","Job_type" text COLLATE pg_catalog."default","Posted_date" date,"Id" bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 0 MINVALUE 0 MAXVALUE 9223372036854775807 CACHE 1 ),CONSTRAINT jobs_pkey PRIMARY KEY ("Id"));COMMIT;'
)

def insert_row(connection,company:str,location:str,title:str,desc_link:str,desc:str,job_type:str,post_date:str)->None:

    insert_cmd = 'INSERT INTO JOBS ("Company","Location","Title","Description_link","Description","Job_type","Posted_date") VALUES (%s,%s,%s,%s,%s,%s,%s);COMMIT;'
    values = (company,location,title,desc_link,desc,job_type,post_date)
    connection.execute(insert_cmd,values)

# Connect to db
try:
    conn =psycopg2.connect(
        host=HOSTNAME,
        dbname=DB,
        user=USR,
        password=PSWRD,
        port=PORT
    )

    cur = conn.cursor()

    # insert row test
    insert_row(cur,'Visa','Buenos aires','Executive manager','https://...','descr...','full-time',None)

# close connection
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()