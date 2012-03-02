import requests

def get_from_strawlab(name, save=True):
    data = requests.get("http://straw-static.imp.ac.at/py4science-vbc/%s" % name)
    if save:
        with open(name.split("/")[-1],"w") as f:
            f.write(data.content)
        return name.split("/")[-1]
    else:
        return data.content

if __name__ == "__main__":
    print get_from_strawlab("week1/README", True)
