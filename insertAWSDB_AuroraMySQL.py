import insertUtil as ut
import MySQLdb


#Tạo kết nối với RDS Aurora MySQL và thêm dữ liệu vào
conn = MySQLdb.connect(host='db-aurora.cluster-ro-ctbqd9rtrx3c.us-east-1.rds.amazonaws.com', 
user='admin',
passwd='nhat123456',
db='covid19_aurora', 
port='3306')
print('Open DB successfully')
ut.insert(conn)
ut.select(conn)
conn.close()    
print('Successfully')


