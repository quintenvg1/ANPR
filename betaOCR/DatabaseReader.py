class _DatabaseReader():
    databasefile = "./DataBase.tsv"
    def __init__():
        pass
    def select(text):
        f = open("./DataBase.tsv", "r")
        for line in f:
            if text in line:
                print("found")
                f.close()
                return(line)
        f.close()
        return("not found")
    def advanced_search(text):
        pass
    #end_advanced_search
