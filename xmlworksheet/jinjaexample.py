from jinja2 import Template
from jinja2 import FileSystemLoader, Environment

class city():
    def __init__(self,name,description,enabled,ip,netmask):
        self.name = name
        self.description = description
        self.enabled = enabled
        self.ip=ip
        self.netmask=netmask






if __name__=="__main__":
    filename = "data1.xml"
    data = {"name": "Amsterdam",
            "description": "Located in the locker room",
            "enabled": "false",
            "ip": "192.168.0.1",
            "netmask": "255.255.255.0"}

    templates = Environment(loader=FileSystemLoader('./'))
    content=templates.get_template(filename).render(data)
    dataTemplate=content.format(**data)
    with open('data2.xml','w') as outfile:
        outfile.write(dataTemplate)
    print(dataTemplate)