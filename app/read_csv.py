import csv


def read_csv(path):
    with open(path, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        header = next(reader)
        #print(header)
        data = []

        for d in reader:
            interar = list(zip(header, d))
            # print(f"**********" * 5)
            # print(d)
            country_dict = {key: value for key, value in interar}
            data.append(country_dict)
        return data



if __name__ == '__main__':
    data = read_csv("./data.csv")
    print(data[2])