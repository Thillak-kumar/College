from tkinter import *
from time import sleep
import turtle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from PIL import ImageTk, Image

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(r"D:\Final year Project\finalized project\Code\Driver\chromedriver.exe",options=options)
# GUI
sleep(4)
root = Tk()
root.title("Chatbot")
root['background']='#000000'
BG_GRAY = "turquoise"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"
global roll
print("1.parent")
print("2.student")
choice=str(input("enter your choice"))
if choice=="1":
	input("Enter Your name:")
	print("login success chatbot opened")
elif choice=="2":
	roll=str(input("Enter Your roll:"))
	roll.lower()
	if len(roll)==10 and roll[0:6]=="19f61a" or roll[0:6]=="19F61A" or roll[0:6]=="19F61a"  or roll[0:6]=="19f61A" :
		print("Login sucess and chatbot is opened")
		print(roll[0]+roll[1])
		
	else:
		print("invalid input run the application again")
		sleep(4)
		quit()
else:
	print("invalid input run the application again")
	sleep(4)
	quit()

def Display_img(p,c):
	im = Image.open(p)
	im.show()
def StudentMark(url):
	lis=[]
	try:
		driver.get(url)
		sleep(4)
		driver.find_element(By.NAME, "htno").send_keys(roll)
		sleep(4)
		driver.find_element(By.NAME, "submit").click()
		sleep(4)
		d=driver.find_element(By.XPATH,"/html/body/main/section/span").text
		n=driver.find_element(By.XPATH,'/html/body/main/section/center[2]/div/b/font[2]').text
		if(n=='1'):
			n=driver.find_element(By.XPATH,'/html/body/main/section/center[2]/div/b/span[1]/font').text
		lis.append(d)
		lis.append(n)

	except:
		lis.append("Check the path in the website ")
		lis.append("Check your internet connection or ")
	return lis

def send():
	send = " You -> " + e.get()
	txt.insert(END, "\n" + send)
	user = e.get()
	user=user.lower()
	if (user == "hello"):
		txt.insert(END, "\n" + "Sietk -> Hi there, how can I help?")

	elif (user == "hi" or user == "hii" or user == "hiiii"):
		txt.insert(END, "\n" + "Sietk -> Hi there, what can I do for you?")

	elif (user == "how are you"):
		txt.insert(END, "\n" + "Sietk -> fine! and you")

	elif (user == "fine" or user == "i am good" or user == "i am doing good"):
		txt.insert(END, "\n" + "Sietk -> Great! how can I help you.")

	elif (user == "thanks" or user == "thank you" or user == "now its my time"):
		txt.insert(END, "\n" + "Sietk -> My pleasure !")

	elif (user == "what can you do for me" or user == "what kinds of items are there" or user == "have you something?" or user=="What do you do for me"):
		txt.insert(END, "\n")
		txt.insert(END, "\n" + "Sietk ->I was desined to show the following options")
		txt.insert(END, "\n" + "About Siddharth college")
		txt.insert(END, "\n" + "About Chairman")
		txt.insert(END, "\n" + "About principal")
		txt.insert(END, "\n" + "Student marks")
		txt.insert(END, "\n" + "Admission process")
		txt.insert(END, "\n" + "Placements")
		txt.insert(END, "\n" + "College and classroom photos")
		txt.insert(END, "\n" + "HOD & Counselor Details")
		txt.insert(END, "\n" + "facilities of the college")
		txt.insert(END, "\n" + "")
	elif(user=="about college" or user=="college" or user=="siddharth college"):
		txt.insert(END, "\n")
		txt.insert(END, "\n"+"Sietk -> Siddharth Institute of Engineering & Technology (SIETK) is an emerging center"" for excellence in Engineering & Management education, boast of energetic &"" experienced faculty successful students, great infrastructure and"" excellent placements record. ")
		txt.insert(END, "\n"+"The management encourages the students and the faculty to “Dare to Dream ""and Strive to Achieve”.")
		txt.insert(END, "\n"+"The institutes are indeed “dream come true” for many aspiring youngsters from rural"" areas in Chittoor District and Southern Andhra Pradesh")
		txt.insert(END, "\n"+"For more details plesase visit http://www.sietk.org/"+"\n")
		txt.insert(END, "\n" + "")
	elif(user=="about admission" or user=="college admission" or user=="admission"):
		txt.insert(END, "\n")
		txt.insert(END,"\n"+ "Our college as following U.G Courses "+"\n")
		txt.insert(END, "1.Computer Science & Information Technology (CIT)"+"\n")
		txt.insert(END, "2.Civil Engineering (CIV)"+"\n")
		txt.insert(END, "3.Electrical and Electronics Engineering (EEE)"+"\n")
		txt.insert(END, "4.Mechanical Engineering (MEC) "+"\n")
		txt.insert(END, "5.Electronics & Communication Engineering"+"\n")
		txt.insert(END, "6.Computer Science and Engineering (CSE)"+"\n")
		txt.insert(END, "7.CSE - Artificial Intelligence & Data Science (CAD)"+"\n")
		txt.insert(END, "8.CSE- Artificial Intelligence and Machine Learning (CSM)"+"\n")
		txt.insert(END, "9.Computer Science Engineering with Specialisation in Cloud Computing (CCC)"+"\n")
		txt.insert(END, "10.CSE - Internet of Things and Cyber Security Including Block Chain Technology (CIC)"+"\n")
		txt.insert(END, "11.Computer Science Engineering (Artificial Intelligence) (CAI)"+"\n")
		txt.insert(END, "12.Computer Science Engineering (Artificial Intelligence) (CAI)"+"\n")
		txt.insert(END, "13.Agriculture Engineering (AGR)"+"\n")
		txt.insert(END, "college ug admission is based on EAPCET or Management""\n"
		"70% of the seats are allotted based on the merit in the APEAPCET."
		"30% of the seats are earmarked for Management candidates. (CAT-B)"
		"For more details please visit http://sietk.org/ug_admissions.php")
		txt.insert(END,"\n"+ "following are the M.TECH PROGRAMMES OFFERED "+"\n")
		txt.insert(END,"\n"+ "All programmes are approved by AICTE"+"\n")
		txt.insert(END,"\n"+ "1.Structural Engineering"+"\n")
		txt.insert(END,"\n"+ "2.Power Electronics "+"\n")
		txt.insert(END,"\n"+ "3.Thermal Engineering"+"\n")
		txt.insert(END,"\n"+ "4.VLSI"+"\n")
		txt.insert(END,"\n"+ "4.Computer Science and Engineering"+"\n")
		txt.insert(END,"\n"+ "M.Tech admission is based on GATE, OR PGECET""For more details please visit http://sietk.org/pg_admissions.php")
		txt.insert(END,"\n"+"Master of Business Administration (MBA)")
		txt.insert(END,"\n"+"Master of Computer Applications (MCA))")
		txt.insert(END, "\n"+"MBA and MCA admission is based on""\n"
		" 70% of the seats are allotted based on the merit in the ICET.""\n"
		"30% of the seats are earmarked for Management candidates.""\n"
		"For more details please visit http://sietk.org/pg_admissions.php")
		txt.insert(END, "\n" + "")
	elif (user == "about chairman" or user == "chairman" or user == "college chairman"):
		txt.insert(END, "\n")
		txt.insert(END, "\n" +" The Chairman of the Board, Dr. Ashok Raju Konduru, an educationist and philanthropist, spearheaded the Siddharth Group of Engineering Institutions to become emerging centres for excellence in Engineering and Management education in a matter of 15 years. His commitment and determination to make Engineering and Management education available to the rural students around Puttur town reflects in the phenomenal growth of student strength in the last 15 years. His dedication to quality infrastructure and education reflects in the accreditation of three courses (SIETK) by National Board of Accreditations (NBA), New Delhi and achieved NAAC “A” Grade.")
		txt.insert(END, "\n"+"  A strong believer of collaboration and cooperation, Dr. Ashok Raju has played a key role in associating with VIT University and Jawahar Knowledge Center, IEG, Government of A.P. for Training and Placements of the students of his institutions. A recipient of “Educationist of the Year Award – 2008” from the WES, New Delhi, Dr. Ashok Raju aims at preparing the student community to meet Global industry needs and played a vital role in signing an MOU with University of Massachusetts Lowell, USA that enables exchange of students and faculty between the two institutions, joint projects, research, etc. He has played a pivotal role in bringing the chapters of “A.P.State Skill Development Corporation” and “Startup Incubation Center” to the institutions which benefit the students immensely. With his immeasurable achievements and untiring efforts to make a difference in the lives of the students, Dr. Ashok Raju has emerged as an iconic personality among thousands of young engineers as well as education circles in the state of Andhra Pradesh and the neighboring states."+"\n")
		txt.insert(END, "\n" + "")

	elif (user=="marks" or user=="my sem marks"):
		txt.insert(END, "\n")
		if choice=="1":
			txt.insert(END,"\n"+"you are logged in parents account close the application and login with student account")
		elif choice=="2":
			if(roll[0]+roll[1]=="19" ):
				txt.insert(END, "\n")
				txt.insert(END, "\n" + "Sietk -> Iam having the following semester marks of r19,r20,r22")
				txt.insert(END, "\n" + " Final Year")
				txt.insert(END, "\n" + " A. r19 I Btech Ist Semester   	")
				txt.insert(END, "\n" + " B. r19 I Btech 2nd Semester  ")
				txt.insert(END, "\n" + " C. r19 II Btech Ist Semester  			")
				txt.insert(END, "\n" + " D. r19 II Btech 2nd Semester")
				txt.insert(END, "\n" + " E. r19 III Btech Ist Semester")
				txt.insert(END, "\n" + " F. r19 III Btech 2nd Semester ")
				txt.insert(END, "\n" + " G.r19 IV Btech Ist Semester")
				txt.insert(END, "\n" + " H.r19 IV Btech 2nd Semester")
				txt.insert(END, "\n" + "Enter Your choice")
			txt.insert(END, "\n" + "")
		elif choice=="2" and roll[0]+roll[1]=="20" :
			txt.insert(END, "\n")
			txt.insert(END, "\n" + "Sietk -> Iam having the following semester marks  of third year r20")
			txt.insert(END, "\n" + "A1. r20 I Btech Ist Semester ")
			txt.insert(END, "\n" + "B1. r20 I Btech 2nd Semester  ")
			txt.insert(END, "\n" + "C1. r20 I Btech Ist Semester ")
		elif choice=="2" and roll[0]+roll[1]=="21" :
			txt.insert(END, "\n")
			txt.insert(END, "\n" + "Sietk -> Iam having the following semester marks of second Year r20")
			txt.insert(END, "\n" + "A1. r20 I Btech Ist Semester ")
			txt.insert(END, "\n" + "B1. r20 I Btech 2nd Semester  ")
			txt.insert(END, "\n" + "C1. r20 II Btech Ist Semester ")
		elif choice=="2" and roll[0]+roll[1]=="22" :
			txt.insert(END, "\n")
			txt.insert(END, "\n" + "Sietk -> Iam having the following semester marks of second Year r20")
			txt.insert(END, "\n" + "A1. r20 I Btech Ist Semester ")
			txt.insert(END, "\n" + "B1. r20 I Btech 2nd Semester  ")
			txt.insert(END, "\n" + "C1. r20 II Btech Ist Semester ")

	elif(user=='a2'):
		d=StudentMark("	http://siddharthgroup.ac.in/aut1btech1r20may2022.php?dbn=aut1btech1r20may2022")
		txt.insert(END, "\n" + "Name: "+d[1])
		txt.insert(END, "\n" + "Marks: "+d[0])
	elif(user=='b2'):
		d=StudentMark("	http://siddharthgroup.ac.in/aut1btech2r20nov2022.php?dbn=aut1btech2r20nov2022")
		txt.insert(END, "\n" + "Name: "+d[1])
		txt.insert(END, "\n" + "Marks: "+d[0])
	elif(user=='a1'):
		d=StudentMark("http://siddharthgroup.ac.in/aut1btech1r20july2021.php?dbn=aut1btech1r20july2021")
		txt.insert(END, "\n" + "Name: "+d[1])
		txt.insert(END, "\n" + "Marks: "+d[0])
	elif(user=='b1'):
		d=StudentMark("http://siddharthgroup.ac.in/aut1btech2r20nov2021.php?dbn=aut1btech2r20nov2021")
		txt.insert(END, "\n" + "Name: "+d[1])
		txt.insert(END, "\n" + "Marks: "+d[0])
	elif(user=='c1'):
		d=StudentMark("http://siddharthgroup.ac.in/aut2btech1r20may2022.php?dbn=aut2btech1r20may2022")
		txt.insert(END, "\n" + "Name: "+d[1])
		txt.insert(END, "\n" + "Marks: "+d[0])
	elif(user=='a'):
		txt.insert(END, "\n" + "Sietk -> your marks is loaded")
		d=StudentMark("http://siddharthgroup.ac.in/autr18dec2019.php?dbn=aut1btech1semr19regjan20")
		txt.insert(END, "\n" + "Name: "+d[1])
		txt.insert(END, "\n" + "Marks: "+d[0])

		txt.insert(END, "\n" + "")
	elif(user=='b'):
		txt.insert(END, "\n" + "Sietk -> your marks is loaded")
		d=StudentMark("http://siddharthgroup.ac.in/autr18oct2020.php?dbn=aut1btech2semr19regoct20")
		txt.insert(END, "\n" + "Name: "+d[1])
		txt.insert(END, "\n" + "Marks: "+d[0])
		txt.insert(END, "\n" + "")
	elif(user=='c'):
		txt.insert(END, "\n" + "Sietk -> your marks is loaded")
		d=StudentMark("http://siddharthgroup.ac.in/aut2btech1r19regfeb2021.php?dbn=aut2btech1r19feb2021")
		txt.insert(END, "\n" + "Name: "+d[1])
		txt.insert(END, "\n" + "Marks: "+d[0])

		txt.insert(END, "\n" + "")
	elif(user=='d'):
		txt.insert(END, "\n" + "Sietk -> your marks is loaded")
		d=StudentMark("http://siddharthgroup.ac.in/aut2btech2r19july2021.php?dbn=aut2btech2r19july2021")
		txt.insert(END, "\n" + "Name: "+d[1])
		txt.insert(END, "\n" + "Marks: "+d[0])
		txt.insert(END, "\n" + "")
	elif(user=='e'):
		txt.insert(END, "\n" + "Sietk -> your marks is loaded")
		d=[StudentMark("http://siddharthgroup.ac.in/aut3btech1r19dec2021.php?dbn=aut3btech1r19dec2021")]
		txt.insert(END, "\n" + "Name: "+d[1])
		txt.insert(END, "\n" + "Marks: "+d[0])

		txt.insert(END, "\n" + "")
	elif(user=='f'):
		txt.insert(END, "\n" + "Sietk -> your marks is loaded")
		d=StudentMark("http://siddharthgroup.ac.in/aut3btech2r19sep2022.php?dbn=aut3btech2r19sep2022")
		txt.insert(END, "\n" + "Name: "+d[1])
		txt.insert(END, "\n" + "Marks: "+d[0])
		txt.insert(END, "\n" + "")
	elif(user=='g'):
		txt.insert(END, "\n" + "Sietk -> your marks is loaded")
		d=StudentMark("http://siddharthgroup.ac.in/aut4btech1r19nov2022.php?dbn=aut4btech1r19nov2022")
		txt.insert(END, "\n" + "Name: "+d[1])
		txt.insert(END, "\n" + "Marks: "+d[0])
		txt.insert(END, "\n" + "")
	elif(user=='h'):
		txt.insert(END, "\n" + "your marks is not updated.......")
		# d=StudentMark("http://siddharthgroup.ac.in/autr18dec2019.php?dbn=aut1btech1semr19regjan20")
		# txt.insert(END, "\n" + d)	
		txt.insert(END, "\n" + "")
	elif(user=='placements'or user=='about placements'):
		txt.insert(END, "\n")
		txt.insert(END, "\n" + "Sietk -> Placements and Training Center(PAT) plays a vital role in networking graduating students with industry & many Technical Institution.")
		txt.insert(END, "\n" + "It prepares students for the process of recruitment; simultaneously, it creates awareness among companies about talent at ")
		txt.insert(END, "\n" + "S I E T K, and extends support to them to facilitate recruiting. The PAT is headed by a full time Training & Placement Officer. ")
		txt.insert(END, "\n" + "A team of faculty members assist in coordinating the work of the PAT Center . The college has been consistently topping the list of campus")
		txt.insert(END,  "placement of engineers among private engineering colleges extends information, advice, guidance and placement support to students.Career advisers engage them in discussions and students are encourage to attend talks, information fairs and recruitment events.")
		txt.insert(END, "\n"+" for more details please visit http://www.sietk.org/placements.php")
		txt.insert(END, "\n" + "")
	elif(user=='facilities of the college'or user=='feautres of the college'):
		txt.insert(END, "\n")
		txt.insert(END, "\n" + "SIETK has following facilities ")
		txt.insert(END, "\n" + "	Library")
		txt.insert(END, "\n" + "	Transport")
		txt.insert(END, "\n" + "	Canteen")
		txt.insert(END, "\n" + "	Sports")
		txt.insert(END, "\n" + "	ED Cell")
		txt.insert(END, "\n"+"	Anti ragging")
		txt.insert(END, "\n" + "")

	elif (user == "goodbye" or user == "see you later" or user == "see yaa" or user == "bye"):
		quit()
	elif (user == "library" ):
		txt.insert(END, "\n")
		txt.insert(END, "\n" + "Sietk -> we have two types of library""\n""1.CENTRAL LIBRARY""\n""2.DIGITAL LIBRARY")
		txt.insert(END, "\n" +"1.CENTRAL LIBRARY")
		txt.insert(END, "\n" +"The Digital Library well equipped with 30 Multimedia systems to access e-Journals, e-Books of International standards through DELNET, J-GATE, Taylor & Francis, EBSCO and N-List. Students can access to many of the knowledge networks regarding GRE,""\n""TOEFL, GMAT,IELTS and can practice test.""\n""The Library functions from 8.00 a.m. to 8.00 p.m. the library’s extended working hours make it easy for students to fit library research time into their demanding academic schedules.")
		txt.insert(END, "\n" +"2.DIGITAL LIBRARY")
		txt.insert(END, "\n" +"The Digital Library well equipped with 30 Multimedia systems to access e-Journals, e-Books of International standards through DELNET, J-GATE, Taylor & Francis, EBSCO and N-List. Students can access to many of the knowledge networks regarding GRE, ""\n""TOEFL, GMAT, IELTS and can practice test.The Library functions from 8.00 a.m. to 8.00 p.m. the library’s extended working hours make it easy for students to fit library research time into their demanding academic schedules.")
		txt.insert(END, "\n" + "")
	elif (user == "transport"):
		txt.insert(END, "\n")
		txt.insert(END, "\n" + "Sietk ->SIETK Transport")
		txt.insert(END, "\n" + ">>College buses ply across many routes from Tirupathi, Chittoor, Sri Kalahasthri and other Places.")
		txt.insert(END, "\n" + ">>Buses will start from a fixed place on a fixed time and reach the College campus.""\n""The starting place and the time will be announced by a separate notice.")
		txt.insert(END, "\n" + ">>All the buses are new to ensure comfortable and safe travel")
		txt.insert(END, "\n" + ">>The buses will stop only at the fixed stopping on the way and not in other places.""\n""Students are advised to come to the stopping well in advance.")
		txt.insert(END, "\n" + "Role & Responsiblities of Transport Committee")
		txt.insert(END, "\n" + ">>Taking care about transport facility for the students and faculty")
		txt.insert(END, "\n" + ">>Collecting the strength and seating capacity for the transport facility in the campus.")
		txt.insert(END, "\n" + ">>Collecting and maintaining transport fee and fine etc.,")
		txt.insert(END, "\n" + ">>Issuing bus pass ID cards to the students and faculty in various routes.")
		txt.insert(END, "\n" + ">> Identifying the transport facility needed in different routes")
		txt.insert(END, "\n" + ">>Maintaining the facility to run smoothly serving interests of the students and faculty.")
		txt.insert(END, "\n" + "")
	elif (user == "canteen" ):
		txt.insert(END, "\n")
		txt.insert(END, "\n" + "Sietk ->SIETK CANTEEN")
		txt.insert(END, "\n" + ">>Eating a variety of healthy foods is the key to a well-balanced diet and good nutrition. It keeps our bodies working well and helps prevent diseases such as diabetes, cancer and cardiovascular disease. On the other hand, youth would like to have a variety of modern food items to satisfy their love for food.")
		txt.insert(END, "\n" + ">>SIETK has the facility of spacious, clean and hygienic canteens and cafeterias that caters to the taste of all students and staff. In mess, South Indian vegetarian and non-vegetarian food are hygienically prepared by trained chefs. The Menu is designed taking into consideration the nutritional and calorific requirements of the student. High emphasis is placed on Quality and Quantity. Separate dining facilities are provided for men and women. We have an exquisite cafeteria for the sake of our Students to provide them a quality and hygienic with a variety of delicious food items at affordable rates. The Cafeteria is open from 8.00 A.M. to 6.00 P.M. on all days and it offers snacks during lunch / break time. In addition to hygienic food, the cafeteria provides stationary items and notebooks.")
		txt.insert(END, "\n" + ">>Wastage of food is measured and displayed both inside and outside of mess to make students realise the value of food. Also a calorie calculation chart is prepared by Bio-Tech students for each day menu and displayed at the entrance of mess")
		txt.insert(END, "\n" + "")
	elif (user == "sports" ):
		txt.insert(END, "\n")
		txt.insert(END, "\n" + "Sietk ->Sports Facilities Available To Develop The Fitness and Concentration Level of The Students")
		txt.insert(END, "\n" +">>we 3 Badminton Courts,3 Volley Ball Courts,1 Throwball court,2 Kabaddi Courts,2 Basketball Courts,Long jump,Hand Ball,Shot-Put,Cricket	,Chess and Carrom Boards")
		txt.insert(END, "\n" + "")
	elif (user == "ed cell" ):
		txt.insert(END, "\n")

		txt.insert(END, "\n" + "Sietk -> Entrepreneurship Development Cell (EDC) was started in the year 2011 in Siddharth Institute of Engineering & Technology with an aim to create awareness among the students regarding entrepreneurship, to develop entrepreneurial qualities and to motivate students to identify career prospects as Entrepreneur. In the recent years the promotion of entrepreneurship is considered as a possible source of job creation, empowerment and economic dynamism. Siddharth Institute of Engineering & Technology makes all possible efforts to provide training and other essential support to the students having innovative ideas to transform into new products and services for the betterment of the society. The Entrepreneurship Development Cell also assists all the aspirants with mentoring, planning and execution of their start up idea into a real business. This cell aims to foster the entrepreneurship culture among the students and incarnate the power of innovation.")
		txt.insert(END, "\n" + "Sietk -> for more details please visit:http://www.sietk.org/ed_cell.php")
		txt.insert(END, "\n" + "")
	elif (user == "anti ragging" ):
		txt.insert(END, "\n")
		txt.insert(END, "\n" + "Sietk ->Ragging” means the doing of any act which causes, or is likely to cause any physical, psychological or physiological harm of apprehension or shame or embarrassment to a student and includes")
		txt.insert(END,"\n"+"Ragging is not allowed in the college premesis")
		txt.insert(END,"\n"+"-->punishments for Ragging")
		txt.insert(END,"\n"+">>Suspension from attending classes")
		txt.insert(END,"\n"+">>Cancelling the scholorships")
		txt.insert(END,"\n"+">>Debarring from  appearing in the exam")
		txt.insert(END,"\n"+">>Debarring from representing the instution activity like youthfestival, annual day ,etc..")
		txt.insert(END,"\n"+">>cancellation of admission")
		txt.insert(END, "\n" + "")
	elif (user == "auditorium" ):
		txt.insert(END, "\n")
		txt.insert(END,"\n"+"Sietk-->The college provides state of art world class Auditorium to the students. Many work shops, PPT's, one day seminars including National Symposium has been conducted. It can occupy around 4000 students.")
		txt.insert(END, "\n" + "")
	elif (user == "about vice chairman" ):
		txt.insert(END, "\n")
		txt.insert(END,"\n"+"Sietk-->Dr. K. Indira Veni is an educationist, philanthropist and a business person.")
		txt.insert(END,"\n"+"As the Secretary of Jaya Educational Society, Vice-Chairperson of the Siddharth Group of Institutions and Chairman of Siddharth International Incubation Center, she has been spearheading innovative approaches in Engineering and Management education and is playing a pivotal role in the running of the institutions. She has also been the Proprietor of Indasri fuel and service center, Srikalahasti and a Partner in Elite Tours & Travels, Tirupati.")
		txt.insert(END, "\n" + "For more detials please visit:http://www.sietk.org/about_vice_chairman.php")
		txt.insert(END, "\n" + "")
	elif (user == "about principal" ):
		txt.insert(END, "\n")

		txt.insert(END,"\n"+"Sietk-->An accomplished educationist with a career spanning almost two decades, Dr. K. Chandrasekhar Reddy has been the Principal of this institute since July, 2011. He has received his B.Tech., in Civil Engineering from S.V. University and M.Tech., in Water Resources Engineering from N.I.E., Mysore. He has received his Ph.D., from S.V. University.")
		txt.insert(END,"\n"+"Dr. Chandrasekhar Reddy is a versatile professional. He has extensive experience as a Civil Engineer, teacher and as an administrator. He has taught undergraduate and post graduate students at S.V.U. College of Engineering, Tirupati and N.B.K.R. Institute of Science and Technology, Vidyanagar. He has published numerous technical papers in National/ International journals and has taken part in several National/ International conferences / workshops.")
		txt.insert(END, "\n" + "For more detials please visit:http://www.sietk.org/about_principal.php")
		txt.insert(END, "\n" + "")
	elif (user == "about vice principal" ):
		txt.insert(END, "\n")
		txt.insert(END,"\n"+"Sietk-->Dr P.G.Gopinath, currently working as Vice-Principal and Professor in Electronics and Communication Engineering in SIETK. He obtained his B.E. degree in Electronics and Communication Engineering from LVEC, Kanchipuram and M.E. degree in VLSI Design from Vel Multitech SRSEC, Chennai and Ph.D. degree from JNTUA, Ananthapuramu in 2019. His research interests are Nano Electronics, Nano Technology, VLSI, MEMS, Antennas, Wireless Communications and Signal Processing. ")
		txt.insert(END,"\n"+"He is a well-trained professional in NBA, NAAC, NIRF, and Autonomous accreditation processes. His major responsibilities include academic and administrative leadership, nurturing innovations and inspiring faculty and students to engage in cutting edge research and innovations of vital value to industry and society.")
		txt.insert(END, "\n" + "For more detials please visit:http://www.sietk.org/about_vp.php")
		txt.insert(END, "\n" + "")
	elif (user == "about civil" ):
		txt.insert(END, "\n")
		txt.insert(END,"\n"+"Sietk-->The Department of Civil Engineering has a wide array of most modern laboratory equipment that can adequately cater to the varied demands of B.Tech, M.Tech students along with different consultancy and research requirements. The department has state of the art infrastructure facilities. It consists of class rooms with LCD projectors and a dedicated departmental library with a decent collection of books in addition to the College Central Library. ")
		txt.insert(END,"\n"+"The HOD of Civil department is Dr. G. Prabhakaran")
		txt.insert(END, "\n" + "For more detials please visit:http://www.sietk.org/civil_dept.php")
		txt.insert(END, "\n" + "")
	elif (user == "about eee" ):
		txt.insert(END, "\n")
		txt.insert(END,"\n"+"Sietk-->The department of ELECTRICAL AND ELECTRONICS ENGINEERING (EEE) has been playing a pioneering role in producing scientists and technologists of good caliber. EEE department is to create talented and socially responsible engineers to make a better India and, in turn, a better world. ")
		txt.insert(END,"\n"+"N. Ramesh Raju is the HOD of EEE Department")
		txt.insert(END, "\n" + "For more detials please visit:http://www.sietk.org/eee_dept.php")
		txt.insert(END, "\n" + "")
	elif (user == "about mechanical" ):
		txt.insert(END, "\n")

		txt.insert(END,"\n"+"Sietk-->The department of MECHANICAL ENGINEERING is one of the vibrant departments of SIETK, which offers B.Tech Mechanical Engineering and M.Tech Program in CAD&M and Thermal Engineering. The department was established in 2001 with 60 student Intake and now running with 120 Intake. The PG courses CAD&M and Thermal Engineering has started in the year 2010 and 2012 respectively. The department is headed by Dr.S.SUNIL KUMAR REDDY who has more than 23 years of teaching experience.The Department is rich in term of faculty members who has vast teaching, Industrial and Research experience with an average teaching experience of 6 years. The Department has 6members with Ph.D and 8 pursuing their research in various prestigious Universities. ")
		txt.insert(END,"\n"+"The HOD of mechanical department is Dr.S.Sunil Kumar Reddy")
		txt.insert(END, "\n" + "For more detials please visit:http://www.sietk.org/mech_dept.php")
		txt.insert(END, "\n" + "")
	elif (user == "about ece" ):
		txt.insert(END, "\n")
		txt.insert(END,"\n"+"Sietk-->The department of Electronics and Communication Engineering (ECE) was established during the inception of the institute in 2001 with an annual intake of 60 students and subsequently increased to 300. The department also offers M.Tech program in three specializations of VLSI design, DECS and Embedded Systems with an intake of 18 students in each specialization. Since its inception, the department has grown into manifold in several aspects.")
		txt.insert(END,"\n"+"The HOD of ECE department is Dr.Ratna Kamala Petla ")
		txt.insert(END, "\n" + "For more detials please visit:http://www.sietk.org/ece_dept.php")
		txt.insert(END, "\n" + "")
	elif (user == "about cse" ):
		txt.insert(END, "\n")
		txt.insert(END,"\n"+"Sietk-->The Department of Computer Science and Engineering (CSE) was established in the year 2001 with a vision to provide a place for Innovation, Scientific Discovery and New Technology, to evolve as a Centre of Excellence in Research and Learning, Integrating Computer and Information Sciences with Natural Sciences and Basic Engineering.")
		txt.insert(END,"\n"+"Dr.B. Geethavani is the HOD of CSE department ")
		txt.insert(END, "\n" + "For more detials please visit:http://www.sietk.org/ece_dept.php")
		txt.insert(END, "\n" + "")
	elif (user == "about csit" ):
		txt.insert(END, "\n")
		txt.insert(END,"\n"+"Sietk-->The B.Tech. in CSIT is a broad and flexible degree program with the curriculum explicitly planned to reflect the complexity and coverage of computer science and information technology. It is the study of various aspects of computer to meet the requirements of the various industries and society. The course contains eminent procedures for processing, the application of statistical and mathematical methods to decision-making, and the simulation of higher-order thinking through computer programs.  It includes study of the basic computer sciences and its application, as well as the detailed study of the various aspects of its working. Proficient members from Academia and Industry provide inputs in introducing specialized courses in the curriculum to suit industry needs. The four-year course that lead to a degree in B.Tech (CSIT), adopt a University-mandated semester system of 8 semesters.")
		txt.insert(END,"\n"+"B. RAJA KUMAR is the HOD of CSIT department ")
		txt.insert(END, "\n" + "For more detials please visit:http://www.sietk.org/csit_dept.php")
		txt.insert(END, "\n" + "")
	elif (user == "about agriculture" ):
		txt.insert(END, "\n")
		txt.insert(END,"\n"+"Sietk-->The Department of Agricultural Engineering was established in the year 2017. The department emphasizes towards imparting quality education, rigorous teaching-learning. Here the students are exposed to wide range of topic within the field. Agricultural engineering covers various topics such as Soil & Water conservation, Irrigation and Drainage, Farm Machinery and Power, Post-harvest Processing, Farm Buildings & Storage etc. This course incorporates new technologies in the field of Agricultural Engineering.")
		txt.insert(END,"\n"+"Dr.Bogala Madhu is the HOD of agriculture department ")
		txt.insert(END, "\n" + "For more detials please visit:http://www.sietk.org/age_dept.php")
		txt.insert(END, "\n" + "")
	elif (user == "about bs&h" ):
		txt.insert(END, "\n")
		txt.insert(END,"\n"+"Sietk--> Department of Basic Sciences and Humanities is established with a view to brush up students in human skills like communication skills and improving English Language. This Department comprises English, Physics, Mathematics and Chemistry. The Faculty: under the dynamic and experienced HoD, this department has a Professor and an Associate Professor and nine more Assistant Professors with rich and varied experience. According to JNTU norms, the department has a sophisticated and modern English Language lab with the software of a reputed software company.")
		txt.insert(END,"\n"+"Prof. Harikrishna is the HOD of bs&h department ")
		txt.insert(END, "\n" + "For more detials please visit:http://www.sietk.org/bsh_dept.php")
		txt.insert(END, "\n" + "")
	elif (user == "about mba" ):
		txt.insert(END, "\n")
		txt.insert(END,"\n"+"Sietk--> The department of Master of Business Administration (MBA) in Siddharth Institute of Engineering & Technology, Puttur has emerged as a nodal center of knowledge in the field of Management and its specialized areas like Finance Management, Marketing Management, Human Resource Management and Information Systems. It was started with the aim of providing an uplift cognition about the business environment and economic growth at National stage and International stage as well. The Department has been well established with hygiene classrooms along with the E-establishment and being dedicated to sounded learning process for the students. Students are being undergone with full fledged training programs and focused on 360 degree career development activities. Continuity programs like Management Skill Developmental Activities and Management efficiency through Case study approach are followed by the department.")
		txt.insert(END,"\n"+"Dr. M. Vani is the HOD of mba department ")
		txt.insert(END, "\n" + "For more detials please visit:http://www.sietk.org/mba_dept.php")
		txt.insert(END, "\n" + "")
	elif (user == "about mca" ):
		txt.insert(END, "\n")
		txt.insert(END,"\n"+"Sietk--> The Department of MCA established in the year 2006 with the intake of 60 students, with the approval of AICTE and affiliated to the JNTUA, Ananthapuramu. Till now 12 batches of students have post graduated. The Department is Headed by Mr. J. S. Ananda Kumar, who has vast teaching experience and the department is formidable with both experienced and young committed faculty. Majority of the faculty members are actively involved in research and development activities. The faculty has attended many training programs conducted by various organizations. The college management encourages the faculty members to attend workshops, conferences, seminars to upgrade the knowledge.")
		txt.insert(END,"\n"+"Mr. J. S. Ananda Kumar is the incharge  of mca department ")
		txt.insert(END, "\n" + "For more detials please visit:http://www.sietk.org/mca_dept.php")
		txt.insert(END, "\n" + "")
	elif(user=="campus life" ):
		txt.insert(END, "\n" + "")
		txt.insert(END,"\n"+"Sietk--> SIETK WEC ""\n"" Campus View Infrastructure""\n"" Association ""\n""Grievance""\n"" Alumni ")
	elif(user=="women empowerment " or user=="women empowerment cell"):
		txt.insert(END,"\n")
		txt.insert(END,"\n"+"The formal inauguration of the Women's Cell was held on 23rd January 2010. Prior to this, publicity material was developed for the Cell in the form of bi-lingual posters announcing the constitution of the Cell, its purpose, mode of approaching the members and confidentiality of the complaint. Another flier with the slogan: Women at Work: Protest Not Fear was prepared for SIETK - Electronics and Communications Engineering Page 46 the benefit of all members. ")
		txt.insert(END, "\n" + "For more detials please visit:https://sietkwec.blogspot.com/")
	elif(user=="association" or user=="about association"):
		txt.insert(END,"\n")
		txt.insert(END,"The Association Activities are conducting every year to facilitate Innovative skills, Imaginative skills, Communication Skills, Presentation Skills, Leadership qualities, Technical Skills and verbal skills for translating the knowledge into skills which become survive in the competitive world.")
	elif(user=="grievance "):
		txt.insert(END,"\n")
		txt.insert(END,"\n"+"very organization must evolve a system for redressal of public grievances arising from its work. Grievance redressal mechanism is formed as an integral part of the machinery of the organization. No organization can claim to be accountable, responsible and user-friendly unless it has established an efficient and effective grievance redressal system. In fact, it is acting as gauge to measure its efficiency and effectiveness as it provides important feedback on the working of the organization. It helps the organization to deliver quality services to the public and other stakeholders in a hassle free manner and in eliminating the cause of grievances.")
		txt.insert(END, "\n" + "For more detials please visit:http://www.sietk.org/grievance.php")
	elif(user=="alumni"):
		txt.insert(END,"\n")
		txt.insert(END,"\n"+"Siddharth Institutions are committed to impart futuristic, relevant and empowering education & training leading to various professional degrees and aim at transforming the novice students into global industry-ready professionals and ethical global citizens.")
		txt.insert(END,"\n"+"For more detials please visit :http://alumni.siddharthgroup.ac.in/")
	elif(user=="contactno"):
		txt.insert(END,"\n")
		txt.insert(END,"\n"+"sietk---> Ph no: 08577-264999, Fax : 08577-264888 yahoo email:sietk_ptr@yahoo.com Email: sietk.puttur@gmail.com sietkverif@gmail.com (Student Verification)")
	elif(user=="college photos" or user=="photos"):
		txt.insert(END,"\n")	
		txt.insert(END,"\n"+"P1 auditorm")
		txt.insert(END,"\n"+"P2 college")
		txt.insert(END,"\n"+"p3 gd room")
		txt.insert(END,"\n"+"p4 ground")
		txt.insert(END,"\n"+"p5 lab")
		txt.insert(END,"\n"+"p6 seminar Halls")
		txt.insert(END,"\n"+"p7 library")
	elif(user=="p1" ):
		txt.insert(END,"\n")
		l=r"D:\Final year Project\finalized project\Code\Images\clg\audi.png"
		Display_img(l,"p1")
		 
	elif(user=="p2" ):
		txt.insert(END,"\n")
		l=r"D:\Final year Project\finalized project\Code\Images\clg\college.jpg"
		Display_img(l,"p2")
		 
	elif(user=="p3" ):
		txt.insert(END,"\n")
		l=r"D:\Final year Project\finalized project\Code\Images\clg\gd-room.png"
		Display_img(l,"p3")
		 
	elif(user=="p4" ):
		txt.insert(END,"\n")
		l=r"D:\Final year Project\finalized project\Code\Images\clg\ground.jpg"
		Display_img(l,"p4")
		 
	elif(user=="p5" ):
		txt.insert(END,"\n")
		l=r"D:\Final year Project\finalized project\Code\Images\clg\lab.png"
		Display_img(l,"p5")
		 
	elif(user=="p6" ):
		txt.insert(END,"\n")
		l=r"D:\Final year Project\finalized project\Code\Images\clg\library.png"
		Display_img(l,"p6")
		 
	elif(user=="p7" ):
		txt.insert(END,"\n")
		l=r"D:\Final year Project\finalized project\Code\Images\clg\seminar-hall.png"
		Display_img(l,"p7")
		 
	elif(user=="close_img" ):
		close()
	else:
		txt.insert(END, "\n")
		txt.insert(END, "\n" + "SIETK -> Sorry! I didn't understand that")
		txt.insert(END, "\n" + "")


	e.delete(0, END)
	# Create text widget
img1 = ImageTk.PhotoImage(Image.open(r"D:\Final year Project\finalized project\Code\Images\p1.png"))
lable1 =  Label(image = img1,width=1500,height=198).grid(row=0,column=0,columnspan=2)

txt = Text(root,bg=BG_COLOR,fg=TEXT_COLOR, font=FONT, width=130)
txt.grid(row=1, column=0,columnspan=15)
e = Entry(root, bg="red", fg=TEXT_COLOR,justify='center', font=FONT, width=100)
e.grid(row=2, column=0)

send = Button(root, text="Send   ", font=FONT_BOLD, bg=BG_GRAY,command=send,width=12).grid(row=2, column=1,columnspan=2)
exit_button = Button(root, text="Exit  ", font=FONT_BOLD, bg=BG_GRAY,command=root.destroy,width=12).grid(row=3, column=1)
root.mainloop()
