# calculate the SPI of the given marks
#AMC,ADC,VLSI,IPDC,DE
#total credit is 25
#each subject has 5 credites
#range(10->85,9->75-85,8->65-75,7->55-65,6->45-55,back<45)

AMC_ce = 5 
ADC_ce =5
VLSI_ce =5
IPDC_ce =5
DE_ce =5

AMC_c=0
ADC_c=0
VLSI_c=0
IPDC_c=0
DE_c=0


AMC = int(input("Enter the marks of AMC:"))
ADC = int(input("Enter the marks of ADC:"))
VLSI = int(input("Enter the marks of VLSI:"))
IPDC = int(input("Enter the marks of IPDC:"))
DE = int(input("Enter the marks of DE:"))

#AMC

if (AMC in range(85,101)):
    AMC_c = 10
elif(AMC  in range(75,85)):
    AMC_c = 9 
elif(AMC  in range(65,75)):
    AMC_c = 8
elif(AMC  in range(55,65)):
    AMC_c = 7 
elif(AMC  in range(45,55)):
    AMC_c = 6   
else:
    AMC_c = 0 
#ADC    
    
if (ADC in range(85,101)):
    ADC_c = 10
elif(ADC  in range(75,85)):
    ADC_c = 9 
elif(ADC  in range(65,75)):
    ADC_c = 8
elif(ADC  in range(55,65)):
    ADC_c =7 
elif(ADC  in range(45,55)):
    ADC_c = 6     

#VLSI

if (VLSI in range(85,101)):
    VLSI_c = 10
elif(VLSI  in range(75,85)):
    VLSI_c = 9 
elif(VLSI  in range(65,75)):
    VLSI_c = 8
elif(VLSI  in range(55,65)):
    VLSI_c = 7 
elif(VLSI  in range(45,55)):
    VLSI_c = 6  
    
#IPDC

if (IPDC in range(85,101)):
    IPDC_c = 10
elif(IPDC  in range(75,85)):
    IPDC_c = 9 
elif(IPDC  in range(65,75)):
    IPDC_c = 8
elif(IPDC  in range(55,65)):
    IPDC_c = 7 
elif(IPDC  in range(45,55)):
    IPDC_c = 6  
    
#DE

if (DE in range(85,101)):
    DE_c = 10
elif(DE  in range(75,85)):
    DE_c = 9 
elif(DE  in range(65,75)):
    DE_c = 8
elif(DE  in range(55,65)):
    DE_c = 7 
elif(DE  in range(45,55)):
    DE_c = 6                 
                      
    
AMC_G = AMC_ce * AMC_c
if AMC_G == 0:
    print("you have backlong in AMC")
ADC_G = ADC_ce * ADC_c
VLSI_G = VLSI_ce * VLSI_c
IPDC_G = IPDC_ce * IPDC_c
DE_G = DE_ce * DE_ce


# print(AMC_G)
# print(ADC_G)
# print(VLSI_G)
# print(IPDC_G)
# print(DE_G)

SUM = AMC_G + ADC_G + VLSI_G + IPDC_G + DE_G

SPI = SUM /25

print(SPI)