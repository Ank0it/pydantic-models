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

print(patient1)
print(patient1.name)
print(patient1.gender)
print(patient1.address.city)
print(patient1.address.pincode)

# Better organisation of related data(i.e address,insurance)
# Reusability : Use Vitals in multiple models (e.g Patient, MedicalRecord)
# Readability : Easier for developers and API consumer to understand
# Validation : Nested models are validated automatically - no extra work needed
