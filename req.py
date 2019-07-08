import requests
import json

# Here we are writing a file.
def writingFile(fileName,fileData):
      file=open(fileName,"w")  
      file.write(fileData)
      file.close()

# Here we are reading a file.
def readingFile(fileName):
      file=open(fileName ,"r")
      data_file = file.read()
      loded_file = json.loads(data_file)
      return loded_file


#Api calling
def apiCalling(url):
    getData = requests.get(url)
    json_data = getData.json()
    json_string = json.dumps(json_data)

    fileName="courses.json"
    fileData=json_string
    writingFile(fileName,fileData)
    data=readingFile(fileName)
    return data

url = 'http://saral.navgurukul.org/api/courses'

#Function Calling
saralData=apiCalling(url)

#List of Saral courses
def courseList(saralData):
    for index in range(0,len(saralData['availableCourses'])):
        courseName= saralData["availableCourses"][index]["name"]
        print index+1 , ":",courseName 
courseList(saralData)

#select course by user with help of id which is front of courses.
user_input=int(raw_input("Enter courseId:"))
Particular_courseName=saralData["availableCourses"][user_input-1]["name"]
courseId= saralData["availableCourses"][user_input-1]["id"]

print "Course Name:", Particular_courseName,", Course Id:", courseId
