def incomodam (n):
    if n<=0 or type(n) != int:
        return ("")
    return "incomodam " + incomodam(n-1)
        
def elefantes (n, num = 0):
    if n <= 0:
        return ("")
    if n == 1:
        return ("Um elefante incomoda muita gente\n")
    if num == 0:
        return (elefantes(n-1,num+1) + (str(n)+" elefantes "+incomodam(n)+"muito mais\n"))
    else:
        return (elefantes(n-1,num+1) + (str(n)+" elefantes "+incomodam(n)+"muito mais\n") + (str(n)+" elefantes "+incomodam(1)+"muita gente\n"))
            






