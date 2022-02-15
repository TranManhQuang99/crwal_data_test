import xlrd
import MySQLdb

# Open the workbook and define the worksheet
book = xlrd.open_workbook('Xuất file từ máy chấm công tuần 2 tháng 4 (3).xlsx')
sheet = book.sheet_by_name("Xuất lưới")

# Establish a MySQL connection
database = MySQLdb.connect (host="103.226.248.168", user = "root", passwd = "admin1234", db = "quangdb")

# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()

# Create the INSERT INTO sql query
query = """INSERT INTO orders (Ngày, Thứ, Mã_NV, Tên_nhân_viên, Phòng_ban, Chức_vụ, Vào_1 , Ra_1 , Vào_2 , Ra_2 , Vào_3 , Ra_3 , Tổng_giờ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

# Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
for r in range(1, sheet.nrows):
		Ngày		= sheet.cell(r,0).value
		Thứ	= sheet.cell(r,1).value
		Mã_NV			= sheet.cell(r,2).value
		Tên_nhân_viên		= sheet.cell(r,3).value
		Phòng_ban		= sheet.cell(r,4).value
		Chức_vụ	= sheet.cell(r,5).value
		Vào_1		= sheet.cell(r,6).value
		Ra_1		= sheet.cell(r,7).value
		Vào_2		= sheet.cell(r,8).value
		Ra_2		= sheet.cell(r,9).value
		Vào_3			= sheet.cell(r,10).value
		Ra_3			= sheet.cell(r,11).value
		Tổng_giờ	= sheet.cell(r,12).value

		# Assign values from each row
		values = (Ngày, Thứ, Mã_NV, Tên_nhân_viên, Phòng_ban, Chức_vụ, Vào_1, Ra_1, Vào_2, Ra_2, Vào_3, Ra_3, Tổng_giờ)

		# Execute sql Query
		try:
			cursor.execute(query, values)
		except:
			continue


# Close the cursor
cursor.close()

# Commit the transaction
database.commit()

# Close the database connection
database.close()

# Print results
# print ""
# print "All Done! Bye, for now."
# print ""
# columns = str(sheet.ncols)
# rows = str(sheet.nrows)
# print "I just imported " %2B columns %2B " columns and " %2B rows %2B " rows to MySQL!"