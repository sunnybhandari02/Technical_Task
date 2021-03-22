class CountWords:
    def __init__(self,str=""):      # Parameterized Constructor
        self.str2 = str

    def solve(self):        # Function to count the frequency of each word in the string
        # print(self.str2)
        self.str2 = self.str2.split()
        str3 = []

        for i in self.str2:
            if i not in str3:
                str3.append(i)

        for i in range(0,len(str3)):
            print("Frequncy of", str3[i], ' is :',self.str2.count(str3[i]))

def main():
    str1 = input("Enter the string: ")
    obj = CountWords(str1)      # creating object of class CountWords
    obj.solve()

main()