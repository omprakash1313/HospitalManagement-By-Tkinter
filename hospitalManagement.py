from tkinter import * 
import tkinter                       #importing gui tkinter library 
from tkinter import ttk  #tkinter.ttk module provides access to the Tk themed widget set
import random            # to generate random number 
import time              #for getting time            
import datetime          #for getting datetime
from tkinter import messagebox   #for message box
import mysql.connector
from mysql.connector import cursor           # My sql Connector for data managent 

#Creating a class hospital 

class hospital:
        def __init__(self,root) :   
                self.root=root
                # root is the name of the wondow   #__init__ method is similar to constructors 
        # Constructors are used to initialize the object’s state
                self.root.title("Hospital Management System of Patient ")  # Title of the project .
                self.root.geometry("1500x800+0+0")       #1500-width,length-800 # Geometry of the window title 

                self.NameOftablet=StringVar()
                self.Ref=StringVar()
                self.Dose=StringVar()
                self.NumberOfTablets=StringVar()
                self.Lot=StringVar()
                self.IssueDate=StringVar()
                self.ExpDate=StringVar()
                self.DailyDose=StringVar()
                self.sideEffect=StringVar()
                self.FurtherInformation=StringVar()
                self.DrivingUsingMachine=StringVar()
                self.HowToUseMedication=StringVar()   
                self.PatientId=StringVar()
                self.StoringDevice=StringVar() 
                self.PatientName=StringVar() 
                self.NhsNumber=StringVar()
                self.Patientname=StringVar()
                self.DateOfBirth=StringVar()
                self.PatientAddress=StringVar()
        ################Text Taking vairable ############################################################

        #setting the label box size, font , foreground color, background color
        
                lbltitle=Label(self.root,bd=15,relief=RIDGE,text="Hospital Management System of Patient",fg="black",bg="red",font=("times new roman",50,"bold"))
        
        # now we will pack the the lable to the root window 
                lbltitle.pack(side=TOP,fill=X)   # we need to give the size and need t pack till complete x axis

        ##############################################################################################################
        #creating the dialog box for data frame [Left side]. 
                Dataframe= Frame(self.root,bd=15,relief=RIDGE)
                Dataframe.place(x=0,y=100,width=1300,height=400)

                Dataframeleft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",20,"bold"),text="Patient Information")
                Dataframeleft.place(x=0,y=5,width=980,height=350)


                #creating the dialog box/dataframe for data frame [Right side]. 
                DataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",20,"bold"),text="Patient Prescription")
                DataframeRight.place(x=990,y=5,width=270,height=350)
        ##############################################################################################################
                Buttonframe= Frame(self.root,bd=15,relief=RIDGE)
                Buttonframe.place(x=0,y=530,width=1300,height=50)
         ## frame panel that will show button top ,,, and information below framen label
                Detailframe= Frame(self.root,bd=15,relief=RIDGE)
                Detailframe.place(x=0,y=580,width=1300,height=100)
        #########################################DETAIL FRAME PANEL####################################################################
                lblNameTablet=Label(Dataframeleft,text="Medicine Name",font=("times new roman",14,"bold"),padx=2,pady=6)  
        
        # in parent label we will put the another child label 
       
                lblNameTablet.grid(row=0,column=0) #Position a widget in the parent widget in a grid.
     
        # we will now create a comboBox , we will use [ttk ] module from tkinter for comboBox
        #combobox is a type of pick list which is for selection a user option
        
                combNametablet=ttk.Combobox(Dataframeleft,textvariable=self.NameOftablet,state="normal",font=("times new roman",15,"bold"),width=33)
        
        ## we will pass the tupple as the values and list of medicine
        
                combNametablet["values"]=("Acetaminophen","Adderall","Amitriptyline","Amlodipine""Amoxicillin","Ativan","Atorvastatin","Azithromycin","Benzonatate","Brilinta","Bunavail","Buprenorphine","Cephalexin","Citalopram","Clindamycin","Clonazepam")
                combNametablet.current(0)
                combNametablet.grid(row=0,column=1)



                labrefe=Label(Dataframeleft,font=("arial",12,"bold"),text="Reerence fNo.",padx=2)
                labrefe.grid(row=1,column=0,sticky=W)
                txtref=Entry(Dataframeleft,font=("arial",12,"bold"),textvariable=self.Ref,width=35)
                txtref.grid(row=1,column=1)


                lblDose=Label(Dataframeleft,font=("Arial",12,"bold"),text=" Dose.",padx=2,pady=4)
                lblDose.grid(row=2,column=0,sticky=W)
                txtDose=Entry(Dataframeleft,font=("arial",12,"bold"),textvariable=self.Dose,width=35)
                txtDose.grid(row=2,column=1)

                lblNoOftablets=Label(Dataframeleft,font=("arial",12,"bold"),text="Number of Tablets.",padx=2,pady=6)
                lblNoOftablets.grid(row=3,column=0,sticky=W)
                txtNoOftablets=Entry(Dataframeleft,font=("arial",12,"bold"),textvariable=self.NumberOfTablets,width=35)
                txtNoOftablets.grid(row=3,column=1)


                lblLot=Label(Dataframeleft,font=("arial",12,"bold"),text="LOT.",padx=2,pady=6)
                lblLot.grid(row=4,column=0,sticky=W)
                txtLot=Entry(Dataframeleft,font=("arial",12,"bold"),textvariable=self.Lot,width=35)
                txtLot.grid(row=4,column=1)

                lblissueDate=Label(Dataframeleft,font=("arial",12,"bold"),text="Issue Date",padx=2,pady=6)
                lblissueDate.grid(row=5,column=0,sticky=W)
                txtissueDate=Entry(Dataframeleft,font=("arial",12,"bold"),textvariable=self.IssueDate,width=35)
                txtissueDate.grid(row=5,column=1)


                lblExpDate=Label(Dataframeleft,font=("arial",12,"bold"),text="Expiry Date.",padx=2,pady=6)
                lblExpDate.grid(row=6,column=0,sticky=W)
                txtExpDate=Entry(Dataframeleft,font=("arial",12,"bold"),textvariable=self.ExpDate,width=35)
                txtExpDate.grid(row=6,column=1)

                

                lblDailyDose=Label(Dataframeleft,font=("arial",12,"bold"),text="Daily Dose.",padx=2,pady=4)
                lblDailyDose.grid(row=7,column=0,sticky=W)
                txtDailyDose=Entry(Dataframeleft,font=("arial",12,"bold"),textvariable=self.DailyDose,width=35)
                txtDailyDose.grid(row=7,column=1)

                lblSideEffect=Label(Dataframeleft,font=("arial",12,"bold"),text="SideEffect.",padx=2,pady=6)
                lblSideEffect.grid(row=8,column=0,sticky=W)
                txtSideEffect=Entry(Dataframeleft,font=("arial",12,"bold"),textvariable=self.sideEffect,width=35)
                txtSideEffect.grid(row=8,column=1)



                
                lblfurtherinfo=Label(Dataframeleft,font=("arial",12,"bold"),text="txturtherInfo.",padx=2)
                lblfurtherinfo.grid(row=0,column=2,sticky=W)
                txtfurtherinfo=Entry(Dataframeleft,font=("arial",12,"bold"),textvariable=self.FurtherInformation,width=35)
                txtfurtherinfo.grid(row=0,column=3)


                lblBloodPressure=Label(Dataframeleft,font=("arial",12,"bold"),text="Blood Pressure.",padx=2,pady=6)
                lblBloodPressure.grid(row=1,column=2,sticky=W)
                txtBloodPressure=Entry(Dataframeleft,font=("arial",12,"bold"),textvariable=self.DrivingUsingMachine,width=35)
                txtBloodPressure.grid(row=1,column=3)


                lblStorage=Label(Dataframeleft,font=("arial",12,"bold"),text="Storage Deice.",padx=2,pady=6)
                lblStorage.grid(row=2,column=2,sticky=W)
                txtStorage=Entry(Dataframeleft,font=("arial",12,"bold"),textvariable=self.StoringDevice,width=35)
                txtStorage.grid(row=2,column=3)


                lblMedicine=Label(Dataframeleft,font=("arial",12,"bold"),text="Medication.",padx=2,pady=6)
                lblMedicine.grid(row=3,column=2,sticky=W)
                txtMedicine=Entry(Dataframeleft,font=("arial",12,"bold"),textvariable=self.HowToUseMedication,width=35)
                txtMedicine.grid(row=3,column=3)

                lblPatientId=Label(Dataframeleft,font=("arial",12,"bold"),text="_Patient_Id",padx=2,pady=6)
                lblPatientId.grid(row=4,column=2,sticky=W)
                txtPatientId=Entry(Dataframeleft,font=("arial",12,"bold"),textvariable=self.IssueDate,width=35)
                txtPatientId.grid(row=4,column=3)


                lblNHSNumber=Label(Dataframeleft,font=("arial",12,"bold"),text="NHS Number.",padx=2,pady=6)
                lblNHSNumber.grid(row=5,column=2,sticky=W)
                txtNHSNumber=Entry(Dataframeleft,font=("arial",12,"bold"),textvariable=self.NhsNumber,width=35)
                txtNHSNumber.grid(row=5,column=3)
        
        
                lblPatientname=Label(Dataframeleft,font=("arial",12,"bold"),text="Email.",padx=2,pady=6)
                lblPatientname.grid(row=6,column=2,sticky=W)
                txtPatientname=Entry(Dataframeleft,font=("arial",12,"bold"),textvariable=self.Patientname,width=35)
                txtPatientname.grid(row=6,column=3)

                lblDateOfBirth=Label(Dataframeleft,font=("arial",12,"bold"),text="DOB.",padx=2,pady=6)
                lblDateOfBirth.grid(row=7,column=2,sticky=W)
                txtDateOfBirth=Entry(Dataframeleft,font=("arial",12,"bold"),textvariable=self.DateOfBirth,width=35)
                txtDateOfBirth.grid(row=7,column=3)
        
                lblpatientAddress=Label(Dataframeleft,font=("arial",12,"bold"),text="patient_Address.",padx=2,pady=6)
                lblpatientAddress.grid(row=8,column=2,sticky=W)
                txtNopatientAddress=Entry(Dataframeleft,font=("arial",12,"bold"),textvariable=self.PatientAddress,width=35)
                txtNopatientAddress.grid(row=8,column=3)


#   ##############################################################################################################
#                 # now we will create the priscription of the pateint in the right dataframe
#                 #using the [Text feild ]
        
        
                self.textprecription=Text(DataframeRight,font=("arial",12,"bold"),width=25,height=15,padx=2,pady=6)
                self.textprecription.grid(row=0,column=0)

# ################################################BUTTONS##############################################################

# now we will create the button for in the navigation bar below

                        #   Button 1

                btnPrescription=Button(Buttonframe,command=self.iPriscription(),text="Prescription",bg="black",fg="white",font=("arial",12,"bold"),width=20,height=1,padx=2,pady=5)
                btnPrescription.grid(row=0,column=0)

                        #   Button 2

                btnPrescriptionData=Button(Buttonframe,command=self.iPriscriptionData,text="Prescription Data",bg="black",fg="white",font=("arial",12,"bold"),width=20,height=1,padx=2,pady=5)
                btnPrescriptionData.grid(row=0,column=1)

                        #   Button 3

                btnUpdate=Button(Buttonframe,command=self.update_data,text="Update",bg="black",fg="white",font=("arial",12,"bold"),width=20,height=1,padx=2,pady=5)
                btnUpdate.grid(row=0,column=2)

                        #   Button 4

                btnDelete=Button(Buttonframe,command=self.idelete,text="Delete",bg="black",fg="white",font=("arial",12,"bold"),width=20,height=1,padx=2,pady=5)
                btnDelete.grid(row=0,column=3)

                        #   Button 5

                btnClear=Button(Buttonframe,command=self.clear,text="Clear",bg="black",fg="white",font=("arial",12,"bold"),width=20,height=1,padx=2,pady=5)
                btnClear.grid(row=0,column=4)

                        #   Button 6

                btnExit=Button(Buttonframe,command=self.iexit,text="Exit",bg="black",fg="white",font=("arial",12,"bold"),width=20,height=1,padx=2,pady=5)
                btnExit.grid(row=0,column=5)


################################################Table for veiewing the Data ##############################################################
# Now we will create a table to show the data of the patient .

        ########################################## Scroll Bar ###################################################

                scroll_x=ttk.Scrollbar(Detailframe,orient=HORIZONTAL)  # we will create scroll bar for both 
                # horizontal and vertica(x,y)respectively
                scroll_y=ttk.Scrollbar(Detailframe,orient=VERTICAL)

                self.hospital_table=ttk.Treeview(Detailframe,columns=("nameOftabelts","ref","dose","nooftablets","lot","issuedate","expdate","dailydose","storage","nhsNumber","pname","DOB","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_x.pack(side=BOTTOM,fill=X)

                scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
                scroll_x=ttk.Scrollbar(command=self.hospital_table.yview)

                # we will have the below heading of the table 
        
                self.hospital_table.heading("nameOftabelts",text="Name of Table")
                self.hospital_table.heading("ref",text="Reference No")
                self.hospital_table.heading("dose",text="Dose")
                self.hospital_table.heading("nooftablets",text="Name of Tablets")
                self.hospital_table.heading("lot",text="LOT")
                self.hospital_table.heading("issuedate",text="Issue Date")
                self.hospital_table.heading("expdate",text="Exp Date") 
                self.hospital_table.heading("dailydose",text="DailyDose") 
                self.hospital_table.heading("storage",text="Storage") 
                self.hospital_table.heading("nhsNumber",text="nhsNumber")
                self.hospital_table.heading("pname",text="pname")
                self.hospital_table.heading("DOB",text="DOB")
                self.hospital_table.heading("Address",text="Address")
                
                
                self.hospital_table["show"]="headings"  # display of the heading 

                # following are the columns of the table which we will have 

                self.hospital_table.column("nameOftabelts",width=105)
                self.hospital_table.column("ref",width=105)
                self.hospital_table.column("dose",width=105)
                self.hospital_table.column("nooftablets",width=105)
                self.hospital_table.column("issuedate",width=105)
                self.hospital_table.column("expdate",width=105)
                self.hospital_table.column("dailydose",width=105)
                self.hospital_table.column("storage",width=105)
                self.hospital_table.column("nhsNumber",width=105)
                self.hospital_table.column("pname",width=105)
                self.hospital_table.column("DOB",width=105)
                self.hospital_table.column("Address",width=105)
                
                self.hospital_table.pack(fill=BOTH,expand=1)
                self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
                self.fatch_data()
                
####################################FUNCTIONALITY DETAIL ########################################################
        
        # the follwing will display data in priscription box

        def iPrescriptionData(self):
                if self.NameOftablets.get()=="" or self.ref.get()=="":
                        messagebox.showerror("Error" ,"All Feilds are Required")
                else:
                        conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="mydata")
                        my_cursor=conn.cursor()
                        my_cursor.execute("insert into hospital values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(


                                                                                                self.NameOftablet.get(),
                                                                                                self.Ref.get(),
                                                                                                self.Dose.get(),
                                                                                                self.NumberOfTablets.get(),
                                                                                                self.Lot.get(),
                                                                                                self.IssueDate.get(),
                                                                                                self.ExpDate.get(),
                                                                                                self.DailyDose.get(),
                                                                                                self.StoringAdevice.get() ,
                                                                                                self.PatientName.get() ,
                                                                                                self.NhsNumber.get(),
                                                                                                self.Patientname.get(),
                                                                                                self.DateOfBirth.get(),
                                                                                                self.PatientAddress.get(),
                        
                                                                                                ))

                        # the following will automatically commit and close the conn.
                        conn.autocommit()
                        self.fatch_data()
                        conn.close()
                        messagebox.showinfo("Succes ", " Record has been inserted")

        
        # we need to update the record so we need to create the the update function
        
        def update_data(self):
                conn=mysql.connector.connect(host='localhost',username='root',password='123456',database='mydata')
                my_cursor=conn.cursor()
                my_cursor.execute("update hospital set Nameoftablets=%s,dose=%s,nooftablets=%s,lot=%s,issuedate=%s,expdate=%s,dailydose=%s,storage=%s,nhsNumber=%s,pname,DOB=%s,Address=%s where Reference_No=%s",(


## here we will set the data to the columns
                                                                                        self.NameOftablet.get(),
                                                                                        self.Ref.get(),
                                                                                        self.Dose.get(),
                                                                                        self.NumberOfTablets.get(),
                                                                                        self.Lot.get(),
                                                                                        self.IssueDate.get(),
                                                                                        self.ExpDate.get(),
                                                                                        self.DailyDose.get(),
                                                                                        self.StoringDevice.get() ,
                                                                                        self.PatientName.get() ,
                                                                                        self.NhsNumber.get(),
                                                                                        self.Patientname.get(),
                                                                                        self.DateOfBirth.get(),
                                                                                        self.PatientAddress.get(),
                ) )

                # now we need to fetch the data from the sql we need to create a database and
                # a table to put the data in the table wheneer the record is being updated

        def fatch_data(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="mydata")
                my_cursor=conn.cursor()
                my_cursor.execute("select  * from hospital")
                rows=my_cursor.fecthall()
                if len(rows)!=0:
                        self.hospital_table.delete(*self.hospital_table.get_children())
                        for i in rows:
                                self.hospital_table.insert("",END,values=i)
                conn.commit()
                conn.close() 

                ## putting the values to the particular rows
        def get_cursor(self,events=""):
                cursor_row=self.hospital_table.focus()
                content=self.hospital_table.item(cursor_row)
                row=content["values"]
                self.Ref.set(row[0]),
                self.Dose.set(row[1]),
                self.NumberOfTablets.set(row[2]),
                self.Lot.set(row[3]),
                self.IssueDate.set(row[4]),
                self.ExpDate.set(row[5]),
                self.DailyDose.set(row[6]),
                self.StoringDevice.set(row[7]) ,
                self.PatientName.set(row[8]) ,
                self.NhsNumber.set(row[9]),
                self.Patientname.set(row[10]),
                self.DateOfBirth.set(row[11]),
                self.PatientAddress.set(row[12])
        
        def iPriscription(self):
                self.NameOftablet.insert(END,"name if Tablests:\t\t\t"+   self.NameOftablet.get(),+"\n")
                self.Ref.insert(END,"name if Tablests:\t\t\t"+            self.Ref.get(),+"\n")
                self.Dose.insert(END,"name if Tablests:\t\t\t"+           self.Dose.get(),+"\n")
                self.Lot.insert(END,"name if Tablests:\t\t\t"+self.NumberOfTablets.get(),+"\n")
                self.IssueDate.insert(END,"name if Tablests:\t\t\t"+            self.Lot.get(),+"\n")
                self.IssueDate.insert(END,"name if Tablests:\t\t\t"+      self.IssueDate.get(),+"\n")
                self.ExpDate.insert(END,"name if Tablests:\t\t\t"+        self.ExpDate.get(),+"\n")
                self.DailyDose.insert(END,"name if Tablests:\t\t\t"+      self.DailyDose.get(),+"\n")
                self.StoringDevice.insert(END,"name if Tablests:\t\t\t"+ self.StoringDevice.get() ,+"\n")
                self.PatientName.insert(END,"name if Tablests:\t\t\t"+   self.PatientName.get() ,+"\n")
                self.NhsNumber.insert(END,"name if Tablests:\t\t\t"+      self.NhsNumber.get(),+"\n")
                self.Patientname.insert(END,"name if Tablests:\t\t\t"+    self.Patientname.get(),+"\n")
                self.DateOfBirth.insert(END,"name if Tablests:\t\t\t"+    self.DateOfBirth.get(),+"\n")
                self.PatientAddress.insert(END,"name if Tablests:\t\t\t"+ self.PatientAddress.get(),+"\n")
        def idelete(self):
                conn=mysql.connector.connect(host='localhost',username='root',password='123456',database='hospital')
                my_cursor=conn.connect()
                query="delete from hospital where Reference_No=%s"
                values=(self.ref.get(),)
                my_cursor.execute(query,values)

                conn.commit()
                conn.close()
                messagebox.showinfo("Delet","Pateint Record has been succesfully deleted")
        def clear(self):
                self.Ref.set(""),          
                self.Dose.set(""),                        
                self.NumberOfTablets.set(""),
                self.Lot.set(""),                        
                self.IssueDate.set(""),                
                self.ExpDate.set(""),                
                self.DailyDose.set(""),                
                self.StoringDevice.set("") ,
                self.PatientName.set("") ,                
                self.NhsNumber.set(""),                
                self.Patientname.set(""),                
                self.DateOfBirth.set(""),                
                self.PatientAddress.set("")
                self.textprecription.delete("1.0",END)
        def iexit(self):
                iexit=messagebox.askyesno(("Hospital Management ","You want to exit"))
                if(exit>0):
                        root.destroy()
                        return



                                
                
                
                
                
                
                
                
                
                
                 
                
                
                
                
                
                
                
                
        

      







root=Tk()
ob=hospital(root)
root.mainloop()
