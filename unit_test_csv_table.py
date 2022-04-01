import CSVTable
import CSVCatalog
import json
import csv
import time

#Must clear out all tables in CSV Catalog schema before using if there are any present
#Please change the path name to be whatever the path to the CSV files are
#First methods set up metadata!! Very important that all of these be run properly

# Only need to run these if you made the tables already in your CSV Catalog tests
# You will not need to include the output in your submission as executing this is not required
# Implementation is provided
def drop_tables_for_prep():
    cat = CSVCatalog.CSVCatalog()
    cat.drop_table("people")
    cat.drop_table("batting")
    cat.drop_table("appearances")

#drop_tables_for_prep()

# Implementation is provided
# You will need to update these with the correct path
def create_lahman_tables():
    cat = CSVCatalog.CSVCatalog()
    cat.create_table("people", "/Users/w695375415/Desktop/W4111_HW2_Programming/People.csv")
    cat.create_table("batting","/Users/w695375415/Desktop/W4111_HW2_Programming/Batting.csv")
    cat.create_table("appearances", "/Users/w695375415/Desktop/W4111_HW2_Programming/Appearances.csv")

#create_lahman_tables()

# Note: You can default all column types to text
def update_people_columns():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog()
    table = cat.get_table("people")

    try:
        f = "/Users/w695375415/Desktop/W4111_HW2_Programming/People.csv"
        with open(f, "r") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=",", quotechar='"')
            header = reader.fieldnames
            for col in header:
                table.add_column_definition(CSVCatalog.ColumnDefinition(col))

    except IOError as e:
        raise DataTableExceptions.DataTableException(
            code = DataTableExceptions.DataTableException.invalid_file,
            message="Could not read file = " + f)

#update_people_columns()

def update_appearances_columns():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog()
    table = cat.get_table("appearances")

    try:
        f = "/Users/w695375415/Desktop/W4111_HW2_Programming/Appearances.csv"
        with open(f, "r") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=",", quotechar='"')
            header = reader.fieldnames
            for col in header:
                table.add_column_definition(CSVCatalog.ColumnDefinition(col))

    except IOError as e:
        raise DataTableExceptions.DataTableException(
            code = DataTableExceptions.DataTableException.invalid_file,
            message="Could not read file = " + f)

#update_appearances_columns()

def update_batting_columns():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog()
    table = cat.get_table("batting")

    try:
        f = "/Users/w695375415/Desktop/W4111_HW2_Programming/Batting.csv"
        with open(f, "r") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=",", quotechar='"')
            header = reader.fieldnames
            for col in header:
                table.add_column_definition(CSVCatalog.ColumnDefinition(col))

    except IOError as e:
        raise DataTableExceptions.DataTableException(
            code = DataTableExceptions.DataTableException.invalid_file,
            message="Could not read file = " + f)

#update_batting_columns()

#Add primary key indexes for people, batting, and appearances in this test
def add_index_definitions():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog()

    people = cat.get_table("people")
    people.define_index("PK people", ["playerID"], "PRIMARY")

    batting = cat.get_table("batting")
    batting.define_index("PK batting", ["playerID", "stint", "yearID"], "PRIMARY")

    appearances = cat.get_table("appearances")
    appearances.define_index("PK appearances", ["yearID", "teamID", "playerID"], "PRIMARY")

#add_index_definitions()


def test_load_info():
    table = CSVTable.CSVTable("people")
    print(table.__description__.file_name)

#test_load_info()

def test_get_col_names():
    table = CSVTable.CSVTable("people")
    names = table.__get_column_names__()
    print(names)

#test_get_col_names()

def add_other_indexes():
    """
    We want to add indexes for common user stories
    People: nameLast, nameFirst
    Batting: teamID
    Appearances: None that are too important right now
    :return:
    """
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog()

    people = cat.get_table("people")
    people.define_index("last_first", ["nameLast", "nameFirst"], "INDEX")

    batting = cat.get_table("batting")
    batting.define_index("TeamID", ["teamID"], "INDEX")

#add_other_indexes()

def load_test():
    batting_table = CSVTable.CSVTable("batting")
    print(batting_table)

#load_test()

def dumb_join_test():
    batting_table = CSVTable.CSVTable("batting")
    appearances_table = CSVTable.CSVTable("appearances")
    t = time.time() # record time
    result = batting_table.dumb_join(appearances_table, ["playerID", "yearID"], {"playerID": "baxtemi01"},
                                     ["playerID", "yearID", "teamID", "AB", "H", "G_all", "G_batting"])
    print(f"dumb join runs in {(time.time() - t) / 60:.3f} minutes")
    print(result)


#dumb_join_test()


def get_access_path_test():
    batting_table = CSVTable.CSVTable("batting")
    template = {"teamID" : "TRO", "playerID" : "abercda01", "yearID" : "1871"}
    index_result, count = batting_table.__get_access_path__(template)
    print(index_result)
    print(count)

#get_access_path_test()

def sub_where_template_test():
    # ************************ TO DO ***************************
    people = CSVTable.CSVTable("people")
    where_template = {"playerID" : "aardsda01", "randomColumn" : "randomValue"}
    sub_template = people.__get_sub_where_template__(where_template)
    print(json.dumps(sub_template, indent = 2))

#sub_where_template_test()


def test_find_by_template_index():
    # ************************ TO DO ***************************
    people = CSVTable.CSVTable("people")
    result = people.__find_by_template_index__({"nameFirst" : "David", "nameLast" : "Aardsma"}, "last_first", ["playerID", "nameFirst", "nameLast"])
    for r in result:
        print(json.dumps(r, indent = 2))

#test_find_by_template_index()

def smart_join_test():
    # ************************ TO DO ***************************
    batting_table = CSVTable.CSVTable("batting")
    appearances_table = CSVTable.CSVTable("appearances")
    t = time.time()
    result = batting_table.__smart_join__(appearances_table, ["playerID", "yearID"], {"playerID": "baxtemi01"},
                                     ["playerID", "yearID", "teamID", "AB", "H", "G_all", "G_batting"])
    print(f"smart join runs in {(time.time() - t) / 60:.3f} minutes")
    print(result)

#smart_join_test()
