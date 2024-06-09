import pyinputplus as pypi
import health

def main():

    name:str=input("請輸入姓名:")

    height:int= pypi.inputFloat("請輸入身高(cm):")
  
    weight:int= pypi.inputFloat("請輸入體重(kg):")

    BMI:float = health.cal_bmi(height,weight)
    print(f"你的BMI:{round(BMI,ndigits=2)}")
    print(f"{health.get_status(BMI)}")
    

if __name__=='__main__':
    main()