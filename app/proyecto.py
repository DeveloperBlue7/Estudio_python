def poblacion(pais_dic):
    poblacion_dic = {
        "2022": pais_dic['2022 population'],
        "2020": pais_dic['2020 population'],
        "2015": pais_dic['2015 population'],
        "2010": pais_dic['2010 population'],
        "2000": pais_dic['2000 population'],
        "1990": pais_dic['1990 population'],
        "1980": pais_dic['1980 population'],
        "1070": pais_dic['2970 population'],
    }
    labels = poblacion_dic.keys()
    values = poblacion_dic.values()
    return labels, values