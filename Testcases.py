from lru import lru

class Testcases:
    
    def __init__(self):
        pass
    
    def test(self):
        gets = lru(5)
        gets.put("Reetika")
        assert gets.get("Reetika") == "HelloReetika","Testcase failed" 
        print("Testcase1 Passed")
        
        gets.put("Sandhya")
        assert gets.get("Sandhya") == "HelloSandhya","Failed" 
        print("Testcase2 Passed")
        
        gets.put("Karthik")
        assert gets.get("Karthik") == "HelloKarthik" ,"Failed" 
        print("Testcase3 Passed")
        gets.put("Koushik")
        gets.put("Priya")
        gets.put("Sravya")
              
        assert gets.get("Reetika") == None ,"Failed"
        print("All test cases passed")
        
        lists = gets.get_cache()
        for i in lists:
            print(i)
        
        
if __name__  == "__main__":
    a = Testcases()
    a.test()
