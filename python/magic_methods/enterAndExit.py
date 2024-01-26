class MySecretConnection:
    def __init__(self, url):
        self.url = url
        print("start")

    def __enter__(self):
        print('entering', self.url)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('leaving', self.url)
    
    def demo(self):
        print("ello")


with MySecretConnection('https://finxter.com') as finxter:
    # Called finxter.__enter__()
    print('hello')
    pass
    # Called finxter.__exit__()