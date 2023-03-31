from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import *
import datetime


class First():
    def __init__(self):
        # self.Now = datetime.datetime.now()
        self.Now = datetime.date(2023, 3, 20)
        self.Date = f"{self.Now.day}.{self.Now.month}.{self.Now.year}"
        self.listDaysWeek = []
        self.Monday=[]; self.Tuesday=[]; self.Wednesday=[]; self.Thursday=[]; self.Friday=[]; self.Saturday=[]
        self.ML=""; self.VL=""; self.SL=""; self.HL=""; self.PL=""; self.SUL=""
        self.MondayHome=[]; self.TuesdayHome=[]; self.WednesdayHome=[]; self.ThursdayHome=[]; self.FridayHome=[]; self.SaturdayHome=[]
        self.MD=""; self.VD=""; self.SD=""; self.HD=""; self.PD=""; self.SUD=""
        self.MondayNumber=[]; self.TuesdayNumber=[]; self.WednesdayNumber=[]; self.ThursdayNumber=[]; self.FridayNumber=[]; self.SaturdayNumber=[]
        self.GradeLessons=[]; self.GradeMarks=[]; self.GradeBall=[]
        self.ArrHomeToday=""; self.ArrHomeTomorrow=""

        self.url = "https://edu.gounn.ru/authorize"
        self.driver = webdriver.Chrome(executable_path=r"D:\Python\ProectSel\chromedriver.exe")


    def authorization(self):
        self.driver.get(self.url)
        sleep(2)
        login = self.driver.find_element("xpath", '/html/body/div/div/main/div/div/div/div[1]/form/div[1]/div[1]/div/input')
        login.send_keys("temgaev_e")
        password = self.driver.find_element("xpath", '/html/body/div/div/main/div/div/div/div[1]/form/div[1]/div[2]/div/input')
        password.send_keys("02092005t")
        login.submit()
        self.Dnevnik()
        self.Grade()
        
        


    def Dnevnik(self):
        sleep(1)
        clickDiary = self.driver.find_element("xpath", "/html/body/div[1]/div/header/div/div/nav/div[2]/a[2]")
        clickDiary.click()
        
        # 
        next = self.driver.find_element("xpath", "/html/body/div[1]/div/main/div/nav/div/div/div[2]/a[1]")
        next.click()
        # 

        for day in range(1, 7):
            calendar = self.driver.find_element("xpath", f"/html/body/div[1]/div/main/div/div[2]/div/div/div/div[2]/div[{day}]/div[1]/div")
            c = calendar.text
            if (str(c.partition(',')[2]) == " " + str(self.Now.day) + ".03"):
                for x in range(1, 9):
                    try: 
                        lesson = self.driver.find_element("xpath", f"/html/body/div[1]/div/main/div/div[2]/div/div/div/div[2]/div[{day}]/div[2]/div[{x}]/div[2]/span")
                        home = self.driver.find_element("xpath", f"/html/body/div[1]/div/main/div/div[2]/div/div/div/div[2]/div[{day}]/div[2]/div[{x}]/div[4]/div")
                        self.ArrHomeToday += f"{lesson.text} | {home.text}" + "\n"
                    except: pass
                for x in range(1, 9):
                    try: 
                        lesson = self.driver.find_element("xpath", f"/html/body/div[1]/div/main/div/div[2]/div/div/div/div[2]/div[{day+1}]/div[2]/div[{x}]/div[2]/span")
                        home = self.driver.find_element("xpath", f"/html/body/div[1]/div/main/div/div[2]/div/div/div/div[2]/div[{day+1}]/div[2]/div[{x}]/div[4]/div")
                        self.ArrHomeTomorrow += f"{lesson.text} | {home.text}" + "\n"
                    except: pass


        wholeWeek = self.driver.find_element("xpath", "/html/body/div[1]/div/main/div/div[2]/div/div/div/div[2]")
        for countDay in range(1, 7):
            day = wholeWeek.find_element("xpath", f"/html/body/div[1]/div/main/div/div[2]/div/div/div/div[2]/div[{countDay}]")
            for countForLesson in range(1, 9):
                try: number = day.find_element("xpath", f"/html/body/div[1]/div/main/div/div[2]/div/div/div/div[2]/div[{countDay}]/div[2]/div[{countForLesson}]/div[1]").text
                except: number = ""
                try: lesson = day.find_element("xpath", f"/html/body/div[1]/div/main/div/div[2]/div/div/div/div[2]/div[{countDay}]/div[2]/div[{countForLesson}]/div[2]/span").text
                except: lesson = ""
                try: homework = day.find_element("xpath", f"/html/body/div[1]/div/main/div/div[2]/div/div/div/div[2]/div[{countDay}]/div[2]/div[{countForLesson}]/div[3]/div/div").text
                except: homework = ""

                if (countDay==1):
                    self.MondayNumber.append(number)
                    self.Monday.append(lesson)
                    self.MondayHome.append(homework)
                if (countDay==2):
                    self.TuesdayNumber.append(number)
                    self.Tuesday.append(lesson)
                    self.TuesdayHome.append(homework)
                if (countDay==3):
                    self.WednesdayNumber.append(number)
                    self.Wednesday.append(lesson)
                    self.WednesdayHome.append(homework)
                if (countDay==4):
                    self.ThursdayNumber.append(number)
                    self.Thursday.append(lesson)
                    self.ThursdayHome.append(homework)
                if (countDay==5):
                    self.FridayNumber.append(number)
                    self.Friday.append(lesson)
                    self.FridayHome.append(homework)
                if (countDay==6):
                    self.SaturdayNumber.append(number)
                    self.Saturday.append(lesson)
                    self.SaturdayHome.append(homework)

    def Grade(self):
        strm = ""
        sleep(1)
        clickGrade = self.driver.find_element("xpath", "/html/body/div[1]/div/header/div/div/nav/div[2]/a[3]")
        clickGrade.click()
        for count in range(1, 100):
            if (strm!=""):
                self.GradeMarks.append(strm)
            strm = ""
            try:
                lesson = self.driver.find_element("xpath", f"/html/body/div[1]/div/main/div/div[2]/div/div[1]/div[2]/div[2]/div/div[1]/div[{count}]/div")
                averageScore = self.driver.find_element("xpath", f"/html/body/div[1]/div/main/div/div[2]/div/div[1]/div[2]/div[2]/div/div[5]/div[{count}]")
                self.GradeLessons.append(lesson.text)
                for mark in range(1, 100):
                    try:
                        marks = self.driver.find_element("xpath", f"/html/body/div[1]/div/main/div/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[{mark}]/div[{count}]/div[1]")
                        if (marks.text != ""): strm += marks.text + "    "
                    except:
                        self.GradeBall.append(averageScore.text)
                        break
            except: break



objectF = First()
objectF.authorization()