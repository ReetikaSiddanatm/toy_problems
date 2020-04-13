from lru import lru

class Testcases:
    
    def __init__(self):
        pass
    
    def test(self):
        gets = lru(5)
        gets.put("Reetika")
        assert gets.get("Reetika") == "Reetika","Testcase failed" 
        print("Testcase1 Passed")
        
        gets.put("Sandhya")
        assert gets.get("Sandhya") == "Sandhya","Failed" 
        print("Testcase2 Passed")
        
        
        gets.put("Karthik")
        assert gets.get("Karthik") == "Karthik" ,"Failed" 
        print("Testcase3 Passed")
        gets.put("Koushik")
        gets.put("Priyanka")
        gets.put("Sravya")
        
        assert gets.get("Reetika") ==None ,"Failed"
        print("All test cases passed")
        
        
if __name__  == "__main__":
    a = Testcases()
    a.test()
