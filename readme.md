# Download_VOT2019RGBD_Challenge

This script allows you to download [VOT Challenge](http://votchallenge.net/)
sequences, without requiring the VOT toolkit.

If you want to download another subclass challenge, you can see this [Repositories](<https://github.com/brobeson/dlvot>)

## Prerequisites 

- Setup python environment

```
pip install -r requirements.txt
```

## Download these sequences

- Setup your python environment
- Download the [description.json](http://data.votchallenge.net/vot2018/main/description.json) and put this document in your folder
- Edit dlvot.py on line 140 - 147
  - The default root download directory is **./Videos/vot/** , and you can change this directory on line 140
  - To avoid the network error, you can set the cycle index on line 142

```python
if __name__ == "__main__":
    ROOT_DIRECTORY = os.path.join(os.getcwd(), "Videos", "vot")
    print(ROOT_DIRECTORY)
    for i in range(100):
        print(i)
        try:
            _download_dataset()
        except:
            pass
```

- Run the dlvot.py

```
$ dlvot
```

On Windows:

```
python dlvot.py
```

For Windows user: It's necessary to run dlvot with elevated privileges
