from database_acess import add_to_db,get_records

def check_validity(v_type,**kwargs):
    """
    Takes all attributes of object and checks if values assigned are in
    correct format or not . If all the attributes are in correct format then calls 
    add_to_db function that is imported else raises exceptions

    Params :-
    v_type , **kwargs : used to accessing all the object attributes uniqly

    Returns :-
    flag_for_add : boolen value to check whether values are added to database or not


    """

    if (kwargs["_1st_hand"] not in (1,0)) or (kwargs["_2nd_hand"] not in (1,0)):
        raise Exception("Enter Valid Values for 1st Hand and 2nd Hand")

    if (kwargs["_1st_hand"] == kwargs["_2nd_hand"]) :
        raise Exception("Enter Valid Values for 1st Hand and 2nd Hand")
    
    if not isinstance(kwargs["owner"],str):
        raise Exception("Enter Valid Owner details")
    
    if not isinstance(kwargs["v_name"],str):
        raise Exception("Enter Valid vehicle name details")
    
    if not isinstance(kwargs["v_make"],str):
        raise Exception("Enter Valid vehicle maker details")
    
    if not isinstance(v_type,str):
        raise Exception("Enter Valid vehicle type details")
    
    if not isinstance(kwargs["age"],float):
        raise Exception("Enter Valid vehicle age ")
    
    if not isinstance(kwargs["kilometers_driven"],int):
        raise Exception("Enter Valid vehicle kilometers driven")
    
    if not (8 < len(kwargs["r_number"]) < 11):
        raise Exception("Give valid register number")
    
    for i,j in kwargs["owner_occupation"].items():
        if not i.islower():
            raise Exception("Give key value in lower case for owner occupation")
        if not j.isupper():
            raise Exception("Give value in upper case for owner occupation")

    flag_for_add = add_to_db(v_type,**kwargs)
    return flag_for_add

    


def get_records_by_name(name):
    """
    This function is used to get all the records based on name of vehicle

    Params:-
    name : name of the vehicle

    Returns:-
    li_of_records : list of required records
    """
    li_of_records = get_records(name,1)
    return li_of_records

def get_records_by_type(type):
    """
    This function is used to get all the records based on type of vehicle if type is valid

    Params:-
    type : type of the vehicle

    Returns:-
    li_of_records : list of required records
    """
    if type in ("Hatchbacks","Sedans","Crossovers","SUVs","Premium_SUVs","Limousine"):
        li_of_records = get_records(type,3)
        return li_of_records
    else:
        raise Exception("Enter a valid type of vehicle")




