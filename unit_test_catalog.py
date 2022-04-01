import CSVCatalog
import json

# Example test, you will have to update the connection info
# Implementation Provided
def create_table_test():
    cat = CSVCatalog.CSVCatalog(
        dbhost="localhost",
        dbport=3306,
        dbuser="root",
        dbpw="222222",
        db="CSVCatalog")
    cat.create_table("test_table", "file_path_test.woo")
    t = cat.get_table("test_table")
    print("Table = ", t)

#create_table_test()

def drop_table_test():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog(
        dbhost="localhost",
        dbport=3306,
        dbuser="root",
        dbpw="222222",
        db="CSVCatalog")
    cat.drop_table("test_table")
    t = cat.get_table("test_table")
    if t.file_name is not None:
        print("Table = ", t)
    else:
        print("No table with name \'test_table\'")

#drop_table_test()

def add_column_test():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog(
        dbhost="localhost",
        dbport=3306,
        dbuser="root",
        dbpw="222222",
        db="CSVCatalog")
    cat.create_table("test_table", "file_path_test.woo")
    t = cat.get_table("test_table")
    t.add_column_definition(CSVCatalog.ColumnDefinition("test_column"))
    col = t.get_column("test_column")
    print("Column = ", col)

#add_column_test()

# Implementation Provided
# Fails because no name is given
def column_name_failure_test():
    cat = CSVCatalog.CSVCatalog()
    col = CSVCatalog.ColumnDefinition(None, "text", False)
    t = cat.get_table("test_table")
    t.add_column_definition(col)

#column_name_failure_test()

# Implementation Provided
# Fails because "canary" is not a permitted type
def column_type_failure_test():
    cat = CSVCatalog.CSVCatalog(
        dbhost="localhost",
        dbport=3306,
        dbuser="root",
        dbpw="222222",
        db="CSVCatalog")
    col = CSVCatalog.ColumnDefinition("bird", "canary", False)
    t = cat.get_table("test_table")
    t.add_column_definition(col)

#column_type_failure_test()

# Implementation Provided
# Will fail because "happy" is not a boolean
def column_not_null_failure_test():
    cat = CSVCatalog.CSVCatalog(
        dbhost="localhost",
        dbport=3306,
        dbuser="root",
        dbpw="222222",
        db="CSVCatalog")
    col = CSVCatalog.ColumnDefinition("name", "text", "happy")
    t = cat.get_table("test_table")
    t.add_column_definition(col)

#column_not_null_failure_test()


def add_index_test():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog(
        dbhost="localhost",
        dbport=3306,
        dbuser="root",
        dbpw="222222",
        db="CSVCatalog")
    t = cat.get_table("test_table")
    t.define_index(index_name="test_index", columns=['test_column'])
    idx = t.get_index("test_index")
    print("Index = ", idx)

#add_index_test()


def col_drop_test():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog(
        dbhost="localhost",
        dbport=3306,
        dbuser="root",
        dbpw="222222",
        db="CSVCatalog")
    t = cat.get_table("test_table")
    t.add_column_definition(CSVCatalog.ColumnDefinition("test_column2"))
    t.drop_column_definition("test_column2")
    col = t.get_column("test_columns2")
    print("Column = ", col)

#col_drop_test()

def index_drop_test():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog(
        dbhost="localhost",
        dbport=3306,
        dbuser="root",
        dbpw="222222",
        db="CSVCatalog")
    t = cat.get_table("test_table")
    t.add_column_definition(CSVCatalog.ColumnDefinition("test_column2"))
    t.define_index(index_name="test_index2", columns=['test_column2'])
    t.drop_index("test_index2")
    idx = t.get_index("test_index2")
    print("Index = ", idx)

#index_drop_test()

# Implementation provided
def describe_table_test():
    cat = CSVCatalog.CSVCatalog()
    t = cat.get_table("test_table")
    desc = t.describe_table()
    print("DESCRIBE People = \n", json.dumps(desc, indent = 2))

#describe_table_test()

"""
# reset
cat = CSVCatalog.CSVCatalog(
    dbhost="localhost",
    dbport=3306,
    dbuser="root",
    dbpw="222222",
    db="CSVCatalog")
cat.drop_table("test_table")
"""