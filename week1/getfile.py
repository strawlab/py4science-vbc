import os.path
import requests

def get_from_strawlab(name):
    fname = name.split("/")[-1]
    if not os.path.exists(fname):
      data = requests.get("http://straw-static.imp.ac.at/py4science-vbc/%s" % name)
      with open(fname, "w") as f:
          f.write(data.content)
    return fname

if __name__ == "__main__":
    print open(get_from_strawlab("week1/README"),'r').read()
