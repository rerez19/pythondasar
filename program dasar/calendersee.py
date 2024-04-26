#program untuk melihat kalender
#import packages calendar
import calendar

yy = int(input("Masukkan tahun: "))
mm = int(input("Masukkan bulan (dalam angka): "))


# display the calendar
print(calendar.month(yy, mm))