from numpy import *
arr1 = array([
                [1,2,3,7,8,5],
                [4,5,6,6,9,3]
            ])
arr2 = arr1.flatten()#aa ee 2d ne 1d ma convert kare che.
arr3 = arr2.reshape(3,4)#aa ee 2d ne 3d ma convert kare che.
print(arr2)
print(arr3)
#print(arr1)
#print(arr1.ndim)#ketala type nu array che ee(1d,2d,3d)
#print(arr1.shape)#ketali raw and ketali colum.
#print(arr1.size)#total size ketali che ee saw karase.(2*3=6)