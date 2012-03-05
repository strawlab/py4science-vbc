import requests

def get_from_strawlab(name, save=True):
    data = requests.get("http://straw-static.imp.ac.at/py4science-vbc/%s" % name)
    if save:
        name = name.split("/")[-1]
        with open(name, "w") as f:
            f.write(data.content)
        return name
    else:
        return data.content

if __name__ == "__main__":
    print get_from_strawlab("week1/README", False)
