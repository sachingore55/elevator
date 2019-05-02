class User_Request:
    def request(self,start_floor,direction,destination_floor):
        self.start_floor=start_floor
        self.direction=direction
        self.destination_floor=destination_floor


userReq1=User_Request()
userReq2=User_Request()
userReq1.request(6,1,9)
userReq2.request(4,-1,1)
print("User1 Selected, Start Flor as {} , Direction as {} and Destination_floor as {}".format(userReq1.start_floor,userReq1.direction,userReq1.destination_floor))
print("User2 Selected, Start Flor as {} , Direction as {} and Destination_floor as {}".format(userReq2.start_floor,userReq2.direction,userReq2.destination_floor))