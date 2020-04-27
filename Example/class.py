class Flight:
    def __init__(self,name,id):
        self.name = name
        self.id  = id
def main():
    c = Flight("Reetika",234)
    c.name = "Ravali"
    print(c.name)
    print(c.id)
    
if __name__ == "__main__":
    main()