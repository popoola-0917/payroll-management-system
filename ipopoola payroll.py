from tkinter import*
import random
import time
import datetime


#first stop at 27:57
#second stop at 1:20:30


payroll = Tk()
payroll.geometry("1300x600+0+0")
payroll.title("Payroll Management Systems")

def Exit():
	payroll.destroy()



def Reset():

	EmployeeName.set("")
	Address.set("")
	Reference.set("")
	EmployerName.set("")
	CityWeighting.set("")
	BasicSalary.set("")
	OverTime.set("")
	GrossPay.set("")
	NetPay.set("")
	Tax.set("")
	Pension.set("")
	StudentLoan.set("")
	NIPayment.set("")
	Deductions.set("")
	PostCode.set("")
	Gender.set("")
	PayDate.set("")
	TaxPeriod.set("")
	NINumber.set("")
	NICode.set("")
	TaxablePay.set("")
	PensionablePay.set("")
	OtherPaymentDue.set("")

def PayRef():
	PayDate.set(time.strftime("%d/%m/%Y"))
	#PayDate.set(time,strftime("%x"))
	Refpay=random.randint(20000,709467)
	Refpaid=str("PR" + str(Refpay))
	Reference.set(Refpaid)


	NIpay=random.randint(4200,9467)
	NIpaid=str("NI" + str(NIpay))
	NINumber.set(NIpaid)


def PayPeriod():
	i=datetime.datetime.now()
	TaxPeriod.set(i.month)



	NCode=random.randint(1200,4467)
	CodeNI=str("NICode" + str(NCode))
	NICode.set(CodeNI)

def MonthlySalary():
	BS = float(BasicSalary.get())
	CW = float(CityWeighting.get())
	OT = float(OverTime.get())

	MTax=((BS +CW + OT) * 0.3)
	TTax="$", str('%.2f'%(MTax))
	Tax.set(TTax)


	M_Pension=((BS +CW + OT) * 0.02)
	MM_Pension="$", str('%.2f'%(M_Pension))
	Pension.set(TTax)


	M_StudentLoan=((BS +CW + OT) * 0.012)
	MM_StudentLoan="$", str('%.2f'%(M_StudentLoan))
	StudentLoan.set(MM_StudentLoan)


	M_NIPayment=((BS +CW + OT) * 0.012)
	MM_NIPayment="$", str('%.2f'%(M_NIPayment))
	NIPayment.set(MM_NIPayment)



	Deduct= (MTax + M_Pension + M_StudentLoan + M_NIPayment)
	Deduct_Payment = "$", str('%.2f'%(Deduct))
	Deductions.set(Deduct_Payment)



	Gross_Pay = "$", str('%.2f' % (BS +CW + OT))
	GrossPay.set(Gross_Pay)


	NetPayAfter = (BS +CW + OT) - Deduct
	NetAfter = "$", str('%.2f' %(NetPayAfter))
	NetPay.set(NetAfter)


	TaxablePay.set(TTax)
	PensionablePay.set(MM_Pension)
	OtherPaymentDue.set("0.00")







EmployeeName=StringVar()
Address=StringVar()
Reference=StringVar()
EmployerName=StringVar()
CityWeighting=StringVar()
BasicSalary=StringVar()
OverTime=StringVar()
GrossPay=StringVar()
NetPay=StringVar()
Tax=StringVar()
Pension=StringVar()
StudentLoan=StringVar()
NIPayment=StringVar()
Deductions=StringVar()
PostCode=StringVar()
Gender=StringVar()
PayDate=StringVar()
TaxPeriod=StringVar()
NINumber=StringVar()
NICode=StringVar()
TaxablePay=StringVar()
PensionablePay=StringVar()
OtherPaymentDue=StringVar()





Tops=Frame(payroll, width=1350, height=50, bd=5, relief="groove")
Tops.pack(side=TOP)


LF=Frame(payroll, width=700,  height=650, bd=8, relief="groove")
LF.pack(side=LEFT)


RF=Frame(payroll, width=700,  height=650, bd=8, relief="groove")
RF.pack(side=RIGHT)



lblInfo=Label(Tops, font=('Banchscrift',36), text="ipopoola Payroll Management Systems",
	fg="steel blue",bg="white", bd=1) 
lblInfo.grid(row=0, column=0)










LeftInsideLF=Frame(LF, bg="white",width=700, height=200,bd=5, relief="groove")
LeftInsideLF.pack(side=TOP)


LeftInsideLFLF=Frame(LF, bg="white", width=325, height=400, bd=5, relief="groove" )
LeftInsideLFLF.pack(side=LEFT)


LeftInsideRFRF=Frame(LF, bg="white",  width=325, height=400, bd=5, relief="groove")
LeftInsideRFRF.pack(side=RIGHT)




RightInsideLF=Frame(RF,bg="white", width=600, height=200,  bd=8, relief="groove" )
RightInsideLF.pack(side=TOP)


RightInsideLFLF=Frame(RF,bg="white", width=300, height=400,  bd=8, relief="groove")
RightInsideLFLF.pack(side=LEFT)


RightInsideRFRF=Frame(RF, width=300, height=500, bd=8, relief="groove")
RightInsideRFRF.pack(side=RIGHT)





###################################LeftSide#######################################
lblEmployeeName=Label(LeftInsideLF, font=('Montserrat',14), text="Employee Name",
	fg="Steel Blue",bg="white", bd=10, anchor='w') 
lblEmployeeName.grid(row=0, column=0)
txtEmployeeName=Entry(LeftInsideLF, font=('Montserrat',14), bd=5, width=36,
	bg="powder blue", justify='right', textvariable=EmployeeName)
txtEmployeeName.grid(row=0, column=1)


lblAddress=Label(LeftInsideLF, font=('Montserrat',14), text="Address",
	fg="Steel Blue",bg="white", bd=10, anchor='w') 
lblAddress.grid(row=1, column=0)
txtAddress=Entry(LeftInsideLF, font=('Montserrat',14),bd=5, width=36,
	bg="powder blue", justify='right',textvariable=Address)
txtAddress.grid(row=1, column=1)


lblReference=Label(LeftInsideLF, font=('Montserrat',14), text="Reference",
	fg="Steel Blue",bg="white", bd=1, anchor='e') 
lblReference.grid(row=2, column=0)
txtReference=Entry(LeftInsideLF, font=('Montserrat',14),bd=5, width=36,
	bg="powder blue", justify='left', textvariable=Reference)
txtReference.grid(row=2, column=1)


lblEmployerName=Label(LeftInsideLF, font=('Montserrat',14), text="Employer Name",
	fg="Steel Blue",bg="white", bd=10, anchor='w') 
lblEmployerName.grid(row=3, column=0)
txtEmployerName=Entry(LeftInsideLF, font=('Montserrat',14), bd=5, width=36,
	bg="powder blue", justify='right', textvariable=EmployerName)
txtEmployerName.grid(row=3, column=1)


#######################################################
lblCity=Label(LeftInsideLFLF, font=('Montserrat',14), text="City Weighting",
	fg="Steel Blue", bg="white", bd=10, anchor='w', justify='right') 
lblCity.grid(row=0, column=0)
txtCity=Entry(LeftInsideLFLF, font=('Montserrat',14), bd=5, width=9,
	bg="powder blue", justify='right', textvariable=CityWeighting)
txtCity.grid(row=0, column=1)

########################################################
lblBasicSalary=Label(LeftInsideLFLF, font=('Montserrat',14), text="Basic Salary",
	fg="Steel Blue",bg="white", bd=1, anchor='w') 
lblBasicSalary.grid(row=1, column=0)
txtBasicSalary=Entry(LeftInsideLFLF, font=('Montserrat',14), bd=5, width=9,
	bg="powder blue", justify='left', textvariable=BasicSalary)
txtBasicSalary.grid(row=1, column=1)


#########################################################
lblOverTime=Label(LeftInsideLFLF, font=('Montserrat',14), text="Over Time",
	fg="Steel Blue",bg="white", bd=1, anchor='w') 
lblOverTime.grid(row=2, column=0)
txtOverTime=Entry(LeftInsideLFLF, font=('Montserrat',14), bd=5, width=9,
	bg="powder blue", justify='left', textvariable=OverTime)
txtOverTime.grid(row=2, column=1)

#########################################################
lblGrossPay=Label(LeftInsideLFLF, font=('Montserrat',14), text="Gross Pay",
	fg="Steel Blue",bg="white", bd=1, anchor='w') 
lblGrossPay.grid(row=3, column=0)
txtGrossPay=Entry(LeftInsideLFLF, font=('Montserrat',14), bd=5, width=9,
	bg="powder blue", justify='left', textvariable=GrossPay)
txtGrossPay.grid(row=3, column=1)


lblNetPay=Label(LeftInsideLFLF, font=('Montserrat',14), text="Net Pay",
	fg="Steel Blue",bg="white", bd=1, anchor='w') 
lblNetPay.grid(row=4, column=0)
txtNetPay=Entry(LeftInsideLFLF, font=('Montserrat',14), bd=5, width=9,
	bg="powder blue", justify='left', textvariable=NetPay )
txtNetPay.grid(row=4, column=1)



#######################################################
#################
lblTax=Label(LeftInsideRFRF, font=('Montserrat',14), text="Tax",
	fg="Steel Blue",bg="white", bd=1, anchor='w') 
lblTax.grid(row=0, column=0)
txtTax=Entry(LeftInsideRFRF, font=('Montserrat',14), bd=5, width=9,
	bg="powder blue", justify='right',textvariable=Tax)
txtTax.grid(row=0, column=1)

########################################################
lblPension=Label(LeftInsideRFRF, font=('Montserrat',14), text="Pension",
	fg="Steel Blue",bg="white", bd=1, anchor='w') 
lblPension.grid(row=1, column=0)
txtPension=Entry(LeftInsideRFRF, font=('Montserrat',14), bd=5, width=9,
	bg="powder blue", justify='right',textvariable=Pension)
txtPension.grid(row=1, column=1)


#########################################################
lblStudentLoan=Label(LeftInsideRFRF, font=('Montserrat',14), text="Student Loan",
	fg="Steel Blue",bg="white", bd=1, anchor='w') 
lblStudentLoan.grid(row=2, column=0)
txtStudentLoan=Entry(LeftInsideRFRF, font=('Montserrat',14), bd=5, width=9,
	bg="powder blue", justify='right', textvariable=StudentLoan)
txtStudentLoan.grid(row=2, column=1)

#########################################################
lblNIPayment=Label(LeftInsideRFRF, font=('Montserrat',14), text="NI Payment",
	fg="Steel Blue",bg="white", bd=1, anchor='w') 
lblNIPayment.grid(row=3, column=0)
txtNIPayment=Entry(LeftInsideRFRF, font=('Montserrat',14), bd=5, width=9,
	bg="powder blue", justify='right',textvariable=NIPayment)
txtNIPayment.grid(row=3, column=1)



lblDeductions=Label(LeftInsideRFRF, font=('Montserrat',14), text="Deductions",
	fg="Steel Blue",bg="white", bd=1, anchor='w') 
lblDeductions.grid(row=4, column=0)
txtDeductions=Entry(LeftInsideRFRF, font=('Montserrat',14), bd=5, width=9,
	bg="powder blue", justify='right',textvariable=Deductions)
txtDeductions.grid(row=4, column=1)


#######################################################Rightside###################


lblPostCode=Label(RightInsideLF, font=('Montserrat',14), text="Post Code",
	fg="Steel Blue",bg="white", bd=1, anchor='w') 
lblPostCode.grid(row=0, column=0)
txtPostCode=Entry(RightInsideLF, font=('Montserrat',14), bd=5, width=36,
	bg="powder blue", justify='right',textvariable=PostCode)
txtPostCode.grid(row=0, column=1)


lblGender=Label(RightInsideLF, font=('Montserrat',14), text="Gender",
	fg="Steel Blue",bg="white",bd=1, anchor='w') 
lblGender.grid(row=1, column=0)
txtGender=Entry(RightInsideLF, font=('Montserrat',14), bd=5, width=36,
	bg="powder blue", justify='right',textvariable=Gender)
txtGender.grid(row=1, column=1)




###################################RightinnserSide#######################################
lblPayDate=Label(RightInsideLFLF, font=('Montserrat',14), text="Pay Date",
	fg="Steel Blue",bg="white", bd=10, anchor='w') 
lblPayDate.grid(row=0, column=0)
txtPayDate=Entry(RightInsideLFLF, font=('Montserrat',14), bd=5, width=9,
	bg="powder blue", justify='left',textvariable=PayDate)
txtPayDate.grid(row=0, column=1)



lblTaxPeriod=Label(RightInsideLFLF, font=('Montserrat',14), text="Tax Period",
	fg="Steel Blue",bg="white", bd=10, anchor='w') 
lblTaxPeriod.grid(row=1, column=0)
txtTaxPeriod=Entry(RightInsideLFLF, font=('Montserrat',14), bd=5, width=9,
	bg="powder blue", justify='left',textvariable=TaxPeriod )
txtTaxPeriod.grid(row=1, column=1)

##################################

lblNINumber=Label(RightInsideLFLF, font=('Montserrat',14), text="NI Number",
	fg="Steel Blue",bg="white", bd=10, anchor='w') 
lblNINumber.grid(row=2, column=0)
txtNINumber=Entry(RightInsideLFLF, font=('Montserrat',14), bd=5, width=9,
	bg="powder blue", justify='left',textvariable=NINumber )
txtNINumber.grid(row=2, column=1)


lblNICode=Label(RightInsideLFLF, font=('Montserrat',14), text="NI Code",
	fg="Steel Blue",bg="white", bd=10, anchor='w') 
lblNICode.grid(row=3, column=0)
txtNICode=Entry(RightInsideLFLF, font=('Montserrat',14), bd=5, width=9,
	bg="powder blue", justify='left',textvariable=NICode )
txtNICode.grid(row=3, column=1)


########################################
lblTaxablePay=Label(RightInsideLFLF, font=('Montserrat',14), text="Taxable Pay",
	fg="Steel Blue",bg="white", bd=10, anchor='w') 
lblTaxablePay.grid(row=4, column=0)
txtTaxablePay=Entry(RightInsideLFLF, font=('Montserrat',14), bd=5, width=9,
	bg="powder blue", justify='left',textvariable=TaxablePay)
txtTaxablePay.grid(row=4, column=1)


lblPensionablePay=Label(RightInsideLFLF, font=('Montserrat',14), text="Pensionable Pay",
	fg="Steel Blue", bg="white", bd=10, anchor='w') 
lblPensionablePay.grid(row=5, column=0)
txtPensionablePay=Entry(RightInsideLFLF, font=('Montserrat',14), bd=5, width=9,
	bg="powder blue", justify='left',textvariable=PensionablePay)
txtPensionablePay.grid(row=5, column=1)


lblOtherPaymentDue=Label(RightInsideLFLF, font=('Montserrat',14), text="Other Payment Due",
	fg="Steel Blue",bg="white", bd=10, anchor='w') 
lblOtherPaymentDue.grid(row=6, column=0)
txtOtherPaymentDue=Entry(RightInsideLFLF, font=('Montserrat',14), bd=5, width=9,
	bg="powder blue", justify='left',textvariable=OtherPaymentDue)
txtOtherPaymentDue.grid(row=6, column=1)







btnWagePayment=Button(RightInsideRFRF, padx=8, bd=8, fg="white",
	font=('Montserrat',14), width=14, text="Wage Payment", 
	bg="steel blue", command=MonthlySalary).grid(row=0,column=0)

btnReset=Button(RightInsideRFRF, padx=8, bd=8, fg="white",
	font=('Montserrat',14), width=14, text="Reset System", 
	bg="steel blue", command=Reset).grid(row=1,column=0)

btnPayRef=Button(RightInsideRFRF, padx=8, bd=8, fg="white",
	font=('Montserrat',14), width=14, text="Pay Reference", 
	bg="steel blue", command=PayRef).grid(row=2,column=0)

btnPayCode=Button(RightInsideRFRF, padx=8, bd=8, fg="white",
	font=('Montserrat',14), width=14, text="Pay Code", 
	bg="steel blue", command=PayPeriod).grid(row=3,column=0)

btnExit=Button(RightInsideRFRF, padx=8, bd=8, fg="white",
	font=('Montserrat',14), width=14, text="Exit", 
	bg="steel blue", command=Exit).grid(row=4,column=0)



payroll.mainloop()