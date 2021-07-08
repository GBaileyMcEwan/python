import sys
import logging
import rds_config
import pymysql
# rds settings

rds_host = "[yourRDSendpoint]"
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(host=rds_host, user=name,
                           passwd=password, db=db_name, connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error(
        "ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")


def handler(event, context):
    """
    This function fetches content from MySQL RDS instance
    """

    item_count = 0
    #myNameIs = "\'\' or 1=1"
    myNameIs = "'Joe'"

    with conn.cursor() as cur:
        #cur.execute("create table Employee ( EmpID  int NOT NULL, Name varchar(255) NOT NULL, PRIMARY KEY (EmpID))")
        #cur.execute('insert into Employee (EmpID, Name) values(1, "Joe")')
        #cur.execute('insert into Employee (EmpID, Name) values(2, "Bob")')
        #cur.execute('insert into Employee (EmpID, Name) values(3, "Mary")')
        # conn.commit()
        select_statement = "SELECT * FROM Employee WHERE Name = " + myNameIs
        #select_statement = "SELECT * FROM Employee WHERE Name = %s"

        #cur.execute(f"select * from Employee where name contains {myName}")
        cur.execute(select_statement)
        # cur.execute(select_statement,myNameIs)
        # logger.info(myNameIs)
        # cur.execute("select * from Employee where name = '' or 1=1#")
        for row in cur:
            item_count += 1
            logger.info(row)
            # print(row)
    conn.commit()

    return "Added %d items from RDS MySQL table" % (item_count)
