import unittest
import urllib.request

class TestWebsite(unittest.TestCase):
    
    def test_website_load(self):
        print("Loading website...")
        try:
            with urllib.request.urlopen("https://atg.world") as response:
                html = response.read()
                print("Website loaded. Verifying response code...")
                assert response.code == 200
                print("Response code verified.")
        except Exception as e:
            print("Error loading website: ", str(e))
            assert False
        
if __name__ == '__main__':
    unittest.main()
