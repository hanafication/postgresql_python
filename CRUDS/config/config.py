from configparser import ConfigParser

def config(filename = '/Users/Rahadian/Documents/Python Scripts/Python in Pycharm/postgreSQL_python/config/database.ini', section = 'postgresql'):
    #create parser
    parser = ConfigParser()
    #read config file
    parser.read(filename)

    #get section
    db = dict()     #collect the iteration

    # checking if database.ini has certain section
    if parser.has_section(section):
        config_params = parser.items(section)
        #iteration to extract section into db dictionary
        for param in config_params:
            key = param[0]
            value = param[1]
            db[key] = value
        #print success if parsing completed
        print('Section {0} found in {1} file and parsing completed!'.format(section, filename))
    else:
        raise Exception('Section {0} not found in {1} file'.format(section, filename))

    return db







