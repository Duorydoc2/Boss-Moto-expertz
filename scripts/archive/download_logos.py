import urllib.request
try:
    urllib.request.urlretrieve('https://logo.clearbit.com/tvsmotor.com', 'assets/brands/tvs.png')
    print("Downloaded tvs.png")
except Exception as e:
    print(f"Failed tvs: {e}")

try:
    urllib.request.urlretrieve('https://logo.clearbit.com/powersports.honda.com', 'assets/brands/honda.png')
    print("Downloaded honda.png")
except Exception as e:
    print(f"Failed honda: {e}")
