from time import sleep
import user_request

CURRENT_ELEVATOR_POSITION=0
request_list=[user_request.userReq1,user_request.userReq2]

class Elevator():

    def call_Elevator(self,floor,direction,destination_floor):
                 global CURRENT_ELEVATOR_POSITION
                 if direction==1:
                    print("Called Elevator at floor %i for going up.. " %floor)
                    print("Elevator is currently at floor : %i" % CURRENT_ELEVATOR_POSITION)
                    self.move_elevator(floor,direction,destination_floor)
                    #self.select_floor(direction,destination_floor)

                 else:
                    print("Called Elevator at floor %i for going down.. " %floor)
                    print("Elevator is currently at floor : %i" %CURRENT_ELEVATOR_POSITION)
                    self.move_elevator(floor,direction,destination_floor)

    def move_elevator(self,floor,direction,destination_floor):
        global CURRENT_ELEVATOR_POSITION
        print("Current elevator position => %i" % CURRENT_ELEVATOR_POSITION)
        current_floor=CURRENT_ELEVATOR_POSITION

        while(current_floor != floor):
            if(floor > current_floor):
                current_floor += 1
                print("Elevator is at floor %i ..." % current_floor)
                sleep(2)
            else:
                current_floor -= 1
                print("Elevator is at floor %i ..." % current_floor)
                sleep(2)
        CURRENT_ELEVATOR_POSITION = current_floor
        print("Elevator has arrived at floor : %i" % CURRENT_ELEVATOR_POSITION)

        print("Passenger has selected destination floor as : %i" % destination_floor)
        while (current_floor != destination_floor):
            current_floor += direction
            print("Elevator is at floor %i ..." % current_floor)
            sleep(2)
        CURRENT_ELEVATOR_POSITION = current_floor
        print("Passenger has alighted at floor : %i" % CURRENT_ELEVATOR_POSITION)

    def process_request(self,req):
        for i in range(len(req)):
            self.start_floor=req[i].start_floor
            self.direction = req[i].direction
            self.destination_floor = req[i].destination_floor
            # self.req2[0]=req[1]
            self.call_Elevator(self.start_floor,self.direction,self.destination_floor)

elv = Elevator()
elv.process_request(request_list)
# print(request_list[0].start_floor)
# elv.call_Elevator(request_list)
# elv.process_request(request_list)
# elv.call_Elevator(4,-1,1)
#elv.call_Elevator(3,1,8)
# elv.call_Elevator(3,1,10)
# elv.call_Elevator(7,-1,0)
#elv.select_Floor(7)