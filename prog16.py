print("Enter the marks of five subjects::")

subject_1 = float (input ())
subject_2 = float (input ())
subject_3 = float (input ())
subject_4 = float (input ())
subject_5 = float (input ())

total, average, percentage,  = None, None, None

total = subject_1 + subject_2 + subject_3 + subject_4 + subject_5
average = total / 5.0
percentage = (total / 500.0) * 100

if percentage >= 70:
    cls = "Distiction"
elif percentage >= 60 and percentage < 75:
    cls = "First class"
elif percentage >= 50 and percentage < 60:
    cls = "Second calss"
elif percentage >= 35 and percentage < 50:
    cls = "Pass class"
else:
    cls = "Fail"

# It will produce the final output
print ("\nThe Total marks is:   \t", total, "/ 500.00")
print ("\nThe Average marks is: \t", average)
print ("\nThe Percentage is:    \t", percentage, "%")
print ("\nThe cls is:         \t", cls)