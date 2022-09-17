sal=int(input("Enter a Amount:="));

tendigit=sal//10;

sal=sal%10;

fivedigit=sal//5;
sal=sal%5;

print("Number of 10:=",tendigit);
print("Number of 5:=",fivedigit);
print("Number of 1:= ",sal);
