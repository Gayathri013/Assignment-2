from abc import ABC,abstractmethod
from services import get_records_by_name,get_records_by_type,check_validity

class Vehicle(ABC):

    def __init__(self,**kwargs):
        """
        As soon as object is created this function is called automatically
        Assignes the values to the attributes defined
        """
        self.owner = kwargs["owner"]
        self.vehical_name = kwargs["v_name"]
        self.vehical_make = kwargs["v_make"]
        self.age = kwargs["age"]
        self.kilometers_driven = kwargs["kilometers_driven"]
        self._1st_hand = kwargs["_1st_hand"]
        self._2nd_hand = kwargs["_2nd_hand"]
        self.register_number = kwargs["r_number"]
        self.owner_occupation = kwargs["owner_occupation"]
        

    @abstractmethod
    def get_vehicle_name(self):
        """
        Gets all the records of users who has specific vehicle name

        Params:-
        name : Name of the vechile given by user

        Returns:-
        list_of_records : returns list of records from database according to user requirement 

        """
        pass

    @abstractmethod
    def get_vehicle_type(self,name):
        """
        Gets all the records of users who has specific vehicle type

        Params:-
        self : takes vehical type from object associated to it

        Returns:-
        list_of_records : returns list of records from database according to user requirement 

        """
        pass



class Hatchbacks(Vehicle):

    def __init__(self,v_type,**kwargs):
        self.vehical_type = v_type
        super().__init__(**kwargs)
        flag = check_validity(v_type,**kwargs)
        if(flag):
            print("Data is added to database")
        
        else:
            print("Data is already present in database")
    __init__.__doc__ = Vehicle.__init__.__doc__

    def get_vehicle_name(self,name):
        records_of_given_name = get_records_by_name(name)
        if len(records_of_given_name) == 0:
            print("No records with given vehicle name")

        else:
            for record in records_of_given_name:
                print(record)
    get_vehicle_name.__doc__ = Vehicle.get_vehicle_name.__doc__

    def get_vehicle_type(self):
        records_of_given_type = get_records_by_type(self.vehical_type)
        if len(records_of_given_type) == 0:
            print("No records with given vehicle type")

        else:
            for record in records_of_given_type:
                print(record)
    get_vehicle_type.__doc__= Vehicle.get_vehicle_type.__doc__


class Sedans(Vehicle):

    def __init__(self,v_type,**kwargs):
        self.vehical_type = v_type
        super().__init__(**kwargs)
        flag = check_validity(v_type,**kwargs)
        if (flag):
            print("Data is added to database")
        
        else:
            print("Data is already present in database")
    __init__.__doc__ = Vehicle.__init__.__doc__

    def get_vehicle_name(self,name):
        records_of_given_name = get_records_by_name(name)
        if len(records_of_given_name) == 0:
            print("No records with given name")

        else:
            for record in records_of_given_name:
                print(record)
    get_vehicle_name.__doc__ = Vehicle.get_vehicle_name.__doc__

    def get_vehicle_type(self):
        records_of_given_type = get_records_by_type(self.vehical_type)
        if len(records_of_given_type) == 0:
            print("No records with given name")

        else:
            for record in records_of_given_type:
                print(record)
    get_vehicle_type.__doc__= Vehicle.get_vehicle_type.__doc__


class Crossovers(Vehicle):

    def __init__(self,v_type,**kwargs):
        self.vehical_type = v_type
        super().__init__(**kwargs)
        flag = check_validity(v_type,**kwargs)
        if (flag):
            print("Data is added to database")
        
        else:
            print("Data is already present in database")
    __init__.__doc__ = Vehicle.__init__.__doc__

    def get_vehicle_name(self,name):
        records_of_given_name = get_records_by_name(name)
        if len(records_of_given_name) == 0:
            print("No records with given name")

        else:
            for record in records_of_given_name:
                print(record)
    get_vehicle_name.__doc__= Vehicle.get_vehicle_name.__doc__


    def get_vehicle_type(self):
        records_of_given_type = get_records_by_type(self.vehical_type)
        if len(records_of_given_type) == 0:
            print("No records with given name")

        else:
            for record in records_of_given_type:
                print(record)
    get_vehicle_type.__doc__= Vehicle.get_vehicle_type.__doc__


class SUVs(Vehicle):

    def __init__(self,v_type,**kwargs):
        self.vehical_type = v_type
        super().__init__(**kwargs)
        flag = check_validity(v_type,**kwargs)
        if (flag):
            print("Data is added to database")
        
        else:
            print("Data is already present in database")
    __init__.__doc__ = Vehicle.__init__.__doc__


    def get_vehicle_name(self,name):
        records_of_given_name = get_records_by_name(name)
        if len(records_of_given_name) == 0:
            print("No records with given name")

        else:
            for record in records_of_given_name:
                print(record)
    get_vehicle_name.__doc__= Vehicle.get_vehicle_name.__doc__

    def get_vehicle_type(self):
        records_of_given_type = get_records_by_type(self.vehical_type)
        if len(records_of_given_type) == 0:
            print("No records with given name")

        else:
            for record in records_of_given_type:
                print(record)
    get_vehicle_type.__doc__= Vehicle.get_vehicle_type.__doc__


class Premium_SUVs(Vehicle):

    def __init__(self,v_type,**kwargs):
        self.vehical_type = v_type
        super().__init__(**kwargs)
        flag = check_validity(v_type,**kwargs)
        if (flag):
            print("Data is added to database")
        
        else:
            print("Data is already present in database")
    __init__.__doc__ = Vehicle.__init__.__doc__

    def get_vehicle_name(self,name):
        records_of_given_name = get_records_by_name(name)
        if len(records_of_given_name) == 0:
            print("No records with given name")

        else:
            for record in records_of_given_name:
                print(record)
    get_vehicle_name.__doc__= Vehicle.get_vehicle_name.__doc__

    def get_vehicle_type(self):
        records_of_given_type = get_records_by_type(self.vehical_type)
        if len(records_of_given_type) == 0:
            print("No records with given name")

        else:
            for record in records_of_given_type:
                print(record)
    get_vehicle_type.__doc__= Vehicle.get_vehicle_type.__doc__


class Limousine(Vehicle):

    def __init__(self,v_type,**kwargs):
        self.vehical_type = v_type
        super().__init__(**kwargs)
        flag = check_validity(v_type,**kwargs)
        if (flag):
            print("Data is added to database")
        
        else:
            print("Data is already present in database")
        
    __init__.__doc__ = Vehicle.__init__.__doc__

    def get_vehicle_name(self,name):
        records_of_given_name = get_records_by_name(name)
        if len(records_of_given_name) == 0:
            print("No records with given name")

        else:
            for record in records_of_given_name:
                print(record)
    get_vehicle_name.__doc__= Vehicle.get_vehicle_name.__doc__

    def get_vehicle_type(self):
        records_of_given_type = get_records_by_type(self.vehical_type)
        if len(records_of_given_type) == 0:
            print("No records with given name")

        else:
            for record in records_of_given_type:
                print(record)
    get_vehicle_type.__doc__= Vehicle.get_vehicle_type.__doc__



if __name__=="__main__":
    hatchbacks_1 = Hatchbacks(owner = "Rama",v_name = "Honda Fit" , v_make = "Honda",
                    v_type="Hatchbacks",age = 2.0 , kilometers_driven = 180,
                    _1st_hand = 0 , _2nd_hand = 1 , r_number = "AP26DQ5421",
                    owner_occupation = {"student":"STUDENT"} )
    
    
    hatchbacks_2 = Hatchbacks(owner = "Krishna",v_name = "Ford Focus" , v_make = "Ford",
                    v_type="Hatchbacks",age = 1.0 , kilometers_driven = 56,
                    _1st_hand = 0 , _2nd_hand = 1 , r_number = "TS98WQ1234",
                    owner_occupation = {"farmer":"FARMER"} )
    
    hatchbacks_3 = Hatchbacks(owner = "Siri",v_name = "Ford Focus" , v_make = "Ford",
                    v_type="Hatchbacks",age = 0.5 , kilometers_driven = 60,
                    _1st_hand = 1 , _2nd_hand = 0 , r_number = "KA98EQ9531",
                    owner_occupation = {"professor":"PROFESSOR"} )
    
    hatchbacks_4 = Hatchbacks(owner = "Krithi",v_name = "Ford Fiesta" , v_make = "Ford",
                    v_type="Hatchbacks",age = 2.0 , kilometers_driven = 305,
                    _1st_hand = 0 , _2nd_hand = 1 , r_number = "TS18SP7531",
                    owner_occupation = {"business":"BUSINESS"} )
    
    hatchbacks_5 = Hatchbacks(owner = "Yash",v_name = "Honda Fit" , v_make = "Honda",
                    v_type="Hatchbacks",age = 4.0 , kilometers_driven = 500,
                    _1st_hand = 1 , _2nd_hand = 0 , r_number = "DL43CP6532",
                    owner_occupation = {"driver":"DRIVER"} )
    
    sedans_1 = Sedans(owner = "Fransis",v_name = "Honda Amaze" , v_make = "Honda",
                    v_type="Sedans",age = 2.0 , kilometers_driven = 187,
                    _1st_hand = 1 , _2nd_hand = 0 , r_number = "AP65YS5434",
                    owner_occupation = {"artist":"ARTIST"} )
    

    sedans_2 = Sedans(owner = "Hardin",v_name = "Tata Tigor" , v_make = "Tata Motors",
                    v_type="Sedans",age = 2.5 , kilometers_driven = 542,
                    _1st_hand = 0 , _2nd_hand = 1 , r_number = "HR36WT6432",
                    owner_occupation = {"poet":"POET"} )
    
    sedans_3 = Sedans(owner = "Hrithik",v_name = "Hyundai Aura" , v_make = "Hyundai",
                    v_type="Sedans",age = 3.0 , kilometers_driven = 800,
                    _1st_hand = 0 , _2nd_hand = 1 , r_number = "AP98FE1276",
                    owner_occupation = {"manager":"MANAGER"} )
    
    sedans_4 = Sedans(owner = "Jasmin",v_name = "Tata Tigor" , v_make = "Tata Motors",
                    v_type="Sedans",age = 1.5 , kilometers_driven = 300,
                    _1st_hand = 1 , _2nd_hand = 0 , r_number = "KA65US4322",
                    owner_occupation = {"director":"DIRECTOR"} )
    
    sedans_5 = Sedans(owner = "Arha",v_name = "Hyundai Aura" , v_make = "Hyundai",
                    v_type="Sedans",age = 2.0 , kilometers_driven = 400,
                    _1st_hand = 0 , _2nd_hand = 1 , r_number = "AP74GT1346",
                    owner_occupation = {"mechanic":"MECHANIC"} )
    
    crossovers_1 = Crossovers(owner = "Preetham",v_name = "Honda CRV" , v_make = "Honda",
                    v_type="Crossovers",age = 0.5 , kilometers_driven = 100,
                    _1st_hand = 1 , _2nd_hand = 0 , r_number = "AP54EV7423",
                    owner_occupation = {"dancer":"DANCER"} )
    
    crossovers_2 = Crossovers(owner = "Armana",v_name = "Toyota RAV4" , v_make = "Toyota",
                    v_type="Crossovers",age = 1.0 , kilometers_driven = 600,
                    _1st_hand = 1 , _2nd_hand = 0 , r_number = "TS75RV5316",
                    owner_occupation = {"politician":"POLITICIAN"} )
    
    crossovers_3 = Crossovers(owner = "Anjali",v_name = "Toyota RAV4" , v_make = "Ford",
                    v_type="Crossovers",age = 1.5 , kilometers_driven = 423,
                    _1st_hand = 1 , _2nd_hand = 0 , r_number = "KA52UE8326",
                    owner_occupation = {"professor":"PROFESSOR"} )
    
    crossovers_4 = Crossovers(owner = "Aman",v_name = "Kia sportage" , v_make = "Kia",
                    v_type="Crossovers",age = 4.0 , kilometers_driven = 1305,
                    _1st_hand = 0 , _2nd_hand = 1 , r_number = "TS54JY9158",
                    owner_occupation = {"worker":"WORKER"} )
    
    crossovers_5 = Crossovers(owner = "Banu",v_name = "Honda CRV" , v_make = "Honda",
                    v_type="Crossovers",age = 1.0 , kilometers_driven = 700,
                    _1st_hand = 1 , _2nd_hand = 0 , r_number = "DL35EG9763",
                    owner_occupation = {"driver":"DRIVER"} )
    
    suv_1 = SUVs(owner = "kiran",v_name = "Mahindra Thar" , v_make = "Mahindra",
                    v_type="SUVs",age = 0.5 , kilometers_driven = 235,
                    _1st_hand = 1 , _2nd_hand = 0 , r_number = "AP86GQ1693",
                    owner_occupation = {"manager":"MANAGER"} )
    

    suv_2 = SUVs(owner = "David",v_name = "Chevrolet Suburban" , v_make = "Chevrolet",
                    v_type="SUVs",age = 1.5 , kilometers_driven = 831,
                    _1st_hand = 0 , _2nd_hand = 1 , r_number = "HR73YA1246",
                    owner_occupation = {"principle":"PRINCIPLE"} )
    
    suv_3 = SUVs(owner = "Yathra",v_name = "Chevrolet Suburban" , v_make = "Chevrolet",
                    v_type="SUVs",age = 3.5 , kilometers_driven = 800,
                    _1st_hand = 0 , _2nd_hand = 1 , r_number = "MH74OE4621",
                    owner_occupation = {"security":"SECURITY"} )
    
    suv_4 = SUVs(owner = "James",v_name = "Mahindra Thar" , v_make = "Mahindra",
                    v_type="SUVs",age = 2.5 , kilometers_driven = 622,
                    _1st_hand = 1 , _2nd_hand = 0 , r_number = "AS22UY3449",
                    owner_occupation = {"reporter":"REPORTER"} )
    
    suv_5 = SUVs(owner = "Tarak",v_name = "Mahindra Thar" , v_make = "Mahindra",
                    v_type="SUVs",age = 2.0 , kilometers_driven = 400,
                    _1st_hand = 0 , _2nd_hand = 1 , r_number = "TS64BG1259",
                    owner_occupation = {"mechanic":"MECHANIC"} )
    
    preminum_suv_1 = Premium_SUVs(owner = "Jaswanth",v_name = "Audi Q7" , v_make = "Audi",
                    v_type="Preminum_SUVs",age = 2.5 , kilometers_driven = 1000,
                    _1st_hand = 1 , _2nd_hand = 0 , r_number = "AP94KQ1579",
                    owner_occupation = {"student":"STUDENT"} )
    
    preminum_suv_2 = Premium_SUVs(owner = "Kris",v_name = "Jaguar F-Pace" , v_make = "Jaguar",
                    v_type="Preminum_SUVs",age = 5.0 , kilometers_driven = 2000,
                    _1st_hand = 0 , _2nd_hand = 1 , r_number = "MH53RV2475",
                    owner_occupation = {"business":"BUSINESS"} )
    
    preminum_suv_3 = Premium_SUVs(owner = "Calra",v_name = "Audi Q7" , v_make = "Audi",
                    v_type="Preminum_SUVs",age = 1.5 , kilometers_driven = 400,
                    _1st_hand = 1 , _2nd_hand = 0 , r_number = "KA54EQ9221",
                    owner_occupation = {"actor":"ACTOR"} )
    
    preminum_suv_4 = Premium_SUVs(owner = "chaitu",v_name = "Audi Q5" , v_make = "Audi",
                    v_type="Preminum_SUVs",age = 1.4 , kilometers_driven = 405,
                    _1st_hand = 0 , _2nd_hand = 1 , r_number = "TS65GK1964",
                    owner_occupation = {"dancer":"DANCER"} )
    
    preminum_suv_5 = Premium_SUVs(owner = "shanthi",v_name = "Jaguar F-Pace" , v_make = "Jaguar",
                    v_type="Preminum_SUVs",age = 1.0 , kilometers_driven = 600,
                    _1st_hand = 1 , _2nd_hand = 0 , r_number = "DL53HB8431",
                    owner_occupation = {"cameraman":"CAMERAMAN"} )
    
    limousine_1 = Limousine(owner = "Satya",v_name = "Chrysler 300" , v_make = "Stellantis",
                    v_type="Limousine",age = 1.0 , kilometers_driven = 400,
                    _1st_hand = 0 , _2nd_hand = 1 , r_number = "AS54KZ8521",
                    owner_occupation = {"actor":"ACTOR"} )
    

    limousine_2 = Limousine(owner = "Katumala",v_name = "Cadillac XTS" , v_make = "Cadillac",
                    v_type="Limousine",age = 2.5 , kilometers_driven = 1343,
                    _1st_hand = 0 , _2nd_hand = 1 , r_number = "MH53LX7632",
                    owner_occupation = {"worker":"WORKER"} )
    
    limousine_3 = Limousine(owner = "Raghava",v_name = "Chrysler 300" , v_make = "Stellantis",
                    v_type="Limousine",age = 1.0 , kilometers_driven = 2000,
                    _1st_hand = 1 , _2nd_hand = 0 , r_number = "AP03JN6420",
                    owner_occupation = {"dancer":"DANCER"} )
    
    limousine_4 = Limousine(owner = "sangeetha",v_name = "Lincoln Town Car" , v_make = "Ford",
                    v_type="Limousine",age = 0.5 , kilometers_driven = 50,
                    _1st_hand = 0 , _2nd_hand = 1 , r_number = "KA43MT8620",
                    owner_occupation = {"reporter":"REPORTER"} )
    
    limousine_5 = Limousine(owner = "Jannu",v_name = "Cadillac XTS" , v_make = "Cadillac",
                    v_type="Limousine",age = 1.0 , kilometers_driven = 700,
                    _1st_hand = 1 , _2nd_hand = 0 , r_number = "TS65VT5328",
                    owner_occupation = {"director":"DIRECTOR"})
    
    
    hatchbacks_1.get_vehicle_type()
    limousine_1.get_vehicle_name("Cadillac XTS")
    
    
    

   

