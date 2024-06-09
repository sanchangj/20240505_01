def cal_bmi(height:int,weight:int) -> float:
    
    return weight/(height/100)**2

def get_status(BMI:float) -> str:
    if BMI < 18.5:    
        return "你的體重過輕"
    elif BMI < 24:
        return "你的體重正常"
    elif BMI < 27:
        return "你的體重過重"
    elif BMI < 30:
        return "你的體重輕度肥胖"
    elif BMI < 35:
        return "你的體重中度肥胖"
    else:
        return "你的體重種度肥胖" 