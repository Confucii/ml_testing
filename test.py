import dvc.api

path = "data/test.txt"
repo = "/home/confucii/EOSDX/Repos/ml_testing"

data_url = dvc.api.get_url(path=path, repo=repo)

print(data_url)
