# when a model is used inside another model 
# for example: if we are taking patient information like name, age, etc have clear type but 'address' type is not clear
# like, will address would be str?,will address would be int? so to solve this problem we use nested model

from pydantic import BaseModel

class Address(BaseModel):

    city:str
    state:str
    pincode:int

class Patient(BaseModel):

    name:str
    age:int
    gender:str
    address: Address

address_dict={'city':'olololo','state':'olololo','pincode':'898098'}    

address1=Address(**address_dict)

patient_dict={'name':'ella','age':28,'gender':'female','address': address1}

patient1=Patient(**patient_dict)

# temp=patient1.model_dump() # when i to export all

# temp=patient1.model_dump(include=['name'])  #when we just have to export any particular field
temp=patient1.model_dump(exclude=['name'])  #when we have to eclude any particular field

print(temp)
print(type(temp))

