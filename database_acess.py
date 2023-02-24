import pandas as pd
import os

def isExists(file):
     """
     checks if the given file exists

     Params:-
     file : name of the file 

     Returns:-
     boolen value 

     """
     return os.path.exists(file)


def add_to_db(v_type,**kwargs):
    """
    Creates a data frame for all the values that need to be stored. Checks if the given 
    csv file exists or not. If csv file exists and if the given vechile number is not present
    in the database then appended the data . If csv file doesn't exists then creates and stores the
    data

    Params :-
    v_type , **kwargs : Data that need to store in database

    Returns :-
    Boolean value to know whether the records are saved in database or not
    """

    user_info  = pd.DataFrame({
        "Owner" : kwargs["owner"],
        "Vehical Name" : kwargs["v_name"],
        "Vehical Make" : kwargs["v_make"],
        "Vehical Type" : v_type,
        "Age" : kwargs["age"],
        "Kilometers Driven" : kwargs["kilometers_driven"],
        "1st Hand" : kwargs["_1st_hand"],
        "2nd Hand" : kwargs["_2nd_hand"],
        "Register Number" : kwargs["r_number"],
        "Owner Occupation" : kwargs["owner_occupation"]

    })
    
    if (isExists("database.csv")):
        with open("database.csv") as data:
            data2 = pd.read_csv(data)
            num = user_info.iloc[0,8]
            for row in range(len(data2)):
                num2 = data2.iloc[row,8]
                if str(num2) == str(num):
                    return 0
                
            user_info.to_csv("database.csv",mode="a",index=False,header=False)
            return 1


    else:
        user_info.to_csv("database.csv",index=False,header=True)
        return 1

    
    

def get_records(specific_value,column_number):
    """
    Get all the records based on the value and column number given

    Params:-
    specific_value : It can be vehicle name or vehicle type
    column_number : Column number in the database

    Returns:-
    required_records : returns all the records in a list
    """
    required_records = []
    with open("database.csv","r") as data:
        records = pd.read_csv(data)
        for i in range(len(records)):
            if str(records.iloc[i,column_number]) == specific_value:
                required_records.append(list(records.loc[i]))

    return required_records
                

    
            
