import xmltodict
from lxml import objectify
from collections import OrderedDict
class plane:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color


def readXML(filename):
    fileptr = open(filename, "r")
    return xmltodict.parse(fileptr.read())

def convertXMLToObject(filename):
    fileptr = open(filename, "r")
    return objectify.fromstring(fileptr.read())

def get_objectify(filename):
    return objectify.parse(filename)

if __name__ == "__main__":
    filename = "data.xml"
    xmlDict = readXML(filename)
    data=get_objectify(filename)
    root = data.getroot()
    objPlane=plane(root.find('make'), root.find('model'), root.find('year'), root.find('color'))
    planeList=[]
    planeList.append((objPlane))
    for plane in planeList:
        print(plane.make, plane.model, plane.year, plane.color)

    for key, value in xmlDict.items():
        print(value['make'], value['model'], value['year'], value['color'])


    







