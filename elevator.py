from time import sleep

CURRENT_ELEVATOR_POSITION=0

class Elevator(object):

    def call_Elevator(self,floor,direction,destination_floor):
                 global CURRENT_ELEVATOR_POSITION
                 if direction==1:
                    print("Called Elevator at floor %i for going up.. " %floor)
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


elv = Elevator()
elv.call_Elevator(6,1,9)
elv.call_Elevator(4,-1,1)
#elv.call_Elevator(3,1,8)
# elv.call_Elevator(3,1,10)
# elv.call_Elevator(7,-1,0)
#elv.select_Floor(7)