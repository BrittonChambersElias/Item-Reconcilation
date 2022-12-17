import tkinter as tk
import customtkinter
import pandas as pd
import time
from time import sleep
from threading import Thread


customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
 

# Thread and function for small db
def threading1():
    # Call work function
    t1=Thread(target=smalldb)
    t1.start()
def threading3(self):
    t3 = Thread(target=self.loading)
    t3.start()

#Thread and function for large db
def threading2():
    # Call work function
    t2=Thread(target=largedb)
    t2.start()
def threading4(self):
    t4 = Thread(target=self.loadinglarge)
    t4.start()


#Database 
def smalldb():
    time_start = "["+(time.strftime('%a %H:%M:%S'))+"]"
    time_end = "["+(time.strftime('%a %H:%M:%S'))+"]"
    print(time_start+" running small")    
    smalldb.df = pd.read_html('*')[0]
    smalldb.mc = pd.read_html('*')[0]
    time_end = "["+(time.strftime('%a %H:%M:%S'))+"]"
    print(time_end+" finish small")   
def largedb():
    time_start = "["+(time.strftime('%a %H:%M:%S'))+"]"
    print(time_start+" running large")
    largedb.df = pd.read_html('*')[0]
    largedb.mc = pd.read_html('*')[0]
    time_end = "["+(time.strftime('%a %H:%M:%S'))+"]"
    print(time_end+" finish large")
    

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Tile Reconcilation GUI 2.0")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        
        self.envelope = tk.StringVar()

        #History Text Box
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
 

        #Left widget frame
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=5, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)
        
        
        #DataBase Options
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="DataBase Options", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame,text="Load Small Data Base", command=lambda:[threading1(),threading3(self)])
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame,text="Load Large Data Base", command=lambda:[threading2(), threading4(self)])
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame,text="Scan an Item", command=lambda:[self.mc_input(),self.find()])
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame,text="Clear TextBox", command=self.clearTextBox)
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)

        

        
        # Bottom Envelope Entry
        self.entry = customtkinter.CTkEntry(self, textvariable=self.envelope)
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        main_button_1 = customtkinter.CTkButton(self, text="Validate Envelope", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),command=lambda:[self.validate_clicked(),self.clearToTextInput()])
        main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")
        

        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("Line ID")
        self.tabview.add("Master Pack")
        self.tabview.add("Envelope")
        self.tabview.tab("Line ID").grid_columnconfigure(0, weight=0)  # configure grid of individual tabs
        self.tabview.tab("Envelope").grid_columnconfigure(0, weight=0)
    
    def mc_input(self):
        dialog = customtkinter.CTkInputDialog(text="Scan Tile, Envelope or Master Carton", title="CTkInputDialog")
        self.ask= dialog.get_input()
            

    

    def validate_clicked(self):
        """ callback when the validate button clicked
        """
        validate = ''
        print("before the while loop")
        while validate != False:
            validate = self.envelope.get()
            print("Right after dialogue pops up")
            if validate in self.valid:             
                self.textbox.insert("0.0",validate+" Belongs in "+self.ask+"\n")
                self.textbox.tag_add(validate,"1.0", "1.15")
                self.textbox.tag_config(validate,foreground="green")
                break
            else:
                notvalid = validate
                self.textbox.insert("0.0",notvalid+" Doesn't belong in "+self.ask+"\n")
                self.textbox.tag_add(validate,"1.0", "1.15")
                self.textbox.tag_config(validate,foreground="red")
                break
                
    def clearToTextInput(self):
        self.entry.delete(0,"end")

    def clearTextBox(self):
        self.textbox.delete("1.0","end")


    def find(self):
        self.time_stamp = "["+(time.strftime('%a %H:%M:%S'))+"]"
        if self.ask == None:
            print("Canceled")
        #Finding Tile
        while self.ask != None:
            if self.ask.startswith('C') == True:
                tile1 = self.ask
                try:
                    df2=smalldb.df[['line_id','envelope_id','case_sn']]
                    mc2=smalldb.mc[['line_id','envelope_id','mc_id']]
                except:
                    df2=largedb.df[['line_id','envelope_id','case_sn']]
                    mc2=largedb.mc[['line_id','envelope_id','mc_id']]
                
                
                
                #Pull all rows containing serial number
                try:
                    findTile_1 = df2.loc[df2['case_sn']==tile1]
                except:
                    self.textbox.insert("0.0","Couldn't find Tile: " +tile1+ " in Database\n\n")
                
                # Takes single oldest row
                try:
                    findEnv = findTile_1.iloc[[-1]] 
                except:
                    self.textbox.insert("0.0",self.time_stamp + "\nCouldn't find Tile: " +tile1+ " in Database\n\n")
                
                #If first envelope is null, get second envelope
                if findEnv.isnull().values.any() == True: # Checking to see if the first envelope in list is empty
                    try:
                        findEnv = findTile_1.iloc[[-2]] # If first envelope in list is empty, grab the second to last envelope
                    except:
                        self.textbox.insert("0.0","Run Envelope and Tile through QC \n")
                #Grabing the envelope id as a string
                try:
                    env1 = findEnv['envelope_id'].item()
                except:
                    self.textbox.insert("0.0",self.time_stamp + " NOTICE: Couldn't find envelope matching with Tile\n")
                    
                print("----------------------------------------------")

                #pull all rows containing envelope id in master pack database
                findCarton_1 = mc2.loc[mc2['envelope_id']==env1]
                try:
                    findCart_1 = findCarton_1.iloc[[-1]]
                except:
                    self.textbox.insert("0.0",self.time_stamp + "\nEnvelope " + env1 + " couldn't be found in any MC\nRun Envelope Through QC\n\n" )
                
                if findCart_1.isnull().values.any() == True:
                    self.textbox.insert("0.0","Run Envelope Through QC")

                try:
                    line_id = findCarton_1['line_id'].item()
                except:
                    self.textbox.insert("0.0",self.time_stamp + "\nNOTICE: Couldn't find line_id matching with Tile\n")
                
                try:
                    mc_id = findCarton_1['mc_id'].item()
                except:
                    self.textbox.insert("0.0",self.time_stamp + "\nNOTICE: Couldn't find mc_id matching with Tile\n")

                #Formating tabs on the right side
                self.label_tab_1 = customtkinter.CTkLabel(self.tabview.tab("Line ID"), text=self.time_stamp+"\n"+line_id)
                self.label_tab_1.grid(row=0, column=0, padx=20, pady=20)

                self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Master Pack"), text=self.time_stamp+"\n"+mc_id)
                self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

                self.label_tab_3 = customtkinter.CTkLabel(self.tabview.tab("Envelope"), text=self.time_stamp+"\n"+env1)
                self.label_tab_3.grid(row=0, column=0, padx=20, pady=20)

                self.textbox.insert("0.0",self.time_stamp + "\nTile: " + tile1 + "\nLine ID: " + line_id + "\nMaster Pack: " + mc_id + "\nEnvelope ID: " + env1+"\n\n")
                break
            #Finding Envelope
            if self.ask.startswith('F02') == True:
                env1 = self.ask
                #picking database
                try:
                    mc=smalldb.mc
                except:
                    mc=largedb.mc

                env1 = mc.loc[mc['envelope_id']==env1]

                try:
                    env = env1.iloc[[-1]]
                    env_id = env['envelope_id'].item()
                    mc_id = env['mc_id'].item()
                    line_id = env['line_id'].item()

                    self.label_tab_1 = customtkinter.CTkLabel(self.tabview.tab("Line ID"), text=self.time_stamp+"\n"+line_id)
                    self.label_tab_1.grid(row=0, column=0, padx=20, pady=20)

                    self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Master Pack"), text=self.time_stamp+"\n"+mc_id)
                    self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

                    self.label_tab_3 = customtkinter.CTkLabel(self.tabview.tab("Envelope"), text=self.time_stamp+"\n"+env_id)
                    self.label_tab_3.grid(row=0, column=0, padx=20, pady=20)
                    self.textbox.insert("0.0",self.time_stamp + "\nEnvelope: " + env_id + "\nLine ID: " + line_id + "\nMaster Pack: " + mc_id +"\n\n")
                except:
                    self.textbox.insert("0.0",self.time_stamp + "\nNOTICE: Envelope not in any Master Pack\n\n")
                break
            #Finding Wrong Envelope in MC
            if self.ask.startswith('F22') == True:
                
                mc1 = self.ask
                try:
                    mc=smalldb.mc
                except:
                    mc=largedb.mc
                
                mc1 = mc.loc[mc['mc_id']==self.ask]
                mc1 = mc1['envelope_id']
                self.valid = mc1.values.tolist()
                self.textbox.insert("0.1","NOTICE: \nScan Envelope ID in Search Bar Below to Validate Envelope\n\n")
                break
                
           

    #loading bar for small database
    def loading(self):
        

        self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.slider_progressbar_frame.grid(row=1, column=1, columnspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        
        self.logo_label = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Loading Small Database", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.progressbar_1 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        self.progressbar_1.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")


        self.progressbar_1.configure(mode="determinate")
        self.progressbar_1.start()
        sleep(15)
        self.logo_label = customtkinter.CTkLabel(self.slider_progressbar_frame, text=" Loaded Small Database ", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        self.progressbar_1.configure(mode="determinate",progress_color='green',determinate_speed=150)
        self.progressbar_1.step()
        self.progressbar_1.stop()

        

    #loading bar for large database
    def loadinglarge(self):
        

        self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.slider_progressbar_frame.grid(row=1, column=1, columnspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        
        self.logo_label = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Loading Large Database", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.progressbar_1 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        self.progressbar_1.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")


        self.progressbar_1.configure(mode="determinate")
        self.progressbar_1.start()
        sleep(40)
        self.logo_label = customtkinter.CTkLabel(self.slider_progressbar_frame, text=" Loaded Large Database ", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=25, pady=(20, 10))
        
        self.progressbar_1.configure(mode="determinate",progress_color='green',determinate_speed=150)
        self.progressbar_1.step()
        self.progressbar_1.stop()

       

    

    def loadingmc(self):
        

        self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.slider_progressbar_frame.grid(row=1, column=1, columnspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        
        self.logo_label = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Loading MC Database", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.progressbar_1 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        self.progressbar_1.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")


        self.progressbar_1.configure(mode="determinate")
        self.progressbar_1.start()
        sleep(6)
        self.progressbar_1.stop()
        self.logo_label = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Loaded MC Database", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        self.progressbar_1.configure(mode="determinate",progress_color='green',determinate_speed=100)
        self.progressbar_1.step()
        self.progressbar_1.stop()

       
        
        
          

if __name__ == "__main__":
    app = App()
    app.mainloop()
