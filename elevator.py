from time import sleep

CURRENT_ELEVATOR_POSITION=1

class Elevator():

    def call_Elevator(self,floor,direction):
                 global CURRENT_ELEVATOR_POSITION
                 if direction==1:
                    print("Called Elevator at floor %i for going up.. " %floor)

                    for count in range (CURRENT_ELEVATOR_POSITION-1,floor+1):
                        current_floor = count
                        print("Elevator is moving up and is at floor %i ..." %count)
                        sleep(2)
                    CURRENT_ELEVATOR_POSITION = current_floor
                    print("Elevator is currently at floor : %i" %CURRENT_ELEVATOR_POSITION)


                 elif direction==-1:
                    print("Called Elevator at floor %i for going down.. " %floor)
                    print("Elevator is currently at floor : %i" %CURRENT_ELEVATOR_POSITION)

                    for count in range (CURRENT_ELEVATOR_POSITION-1,floor-1,-1):
                        current_floor = count
                        print("Elevator is moving down and is at floor %i ..." %count)
                        sleep(2)
                    CURRENT_ELEVATOR_POSITION = current_floor
                    print("Elevator is currently at floor : %i" %CURRENT_ELEVATOR_POSITION)


    def select_Floor(self,destination_floor):

        global CURRENT_ELEVATOR_POSITION
        print("Current elevator position => %i" % CURRENT_ELEVATOR_POSITION)
        print("Passenger has boarded the elevator and selected destination floor as %i" %destination_floor)

        if CURRENT_ELEVATOR_POSITION < destination_floor:
            for count in range (CURRENT_ELEVATOR_POSITION+1,destination_floor+1):
                current_floor = count
                print("Elevator is moving UP and is at floor %i ..." %count)
                sleep(2)
            CURRENT_ELEVATOR_POSITION = current_floor
            print("Person has alighted at floor %i" %CURRENT_ELEVATOR_POSITION)

        elif CURRENT_ELEVATOR_POSITION > destination_floor:
            for count in range (CURRENT_ELEVATOR_POSITION-1,destination_floor-1,-1):
                current_floor = count
                print("Elevator is moving DOWN and is at floor %i ..." %count)
                sleep(2)
            CURRENT_ELEVATOR_POSITION = current_floor
            print("Person has alighted at floor %i" %CURRENT_ELEVATOR_POSITION)


elv = Elevator()
elv.call_Elevator(5,1)
elv.select_Floor(9)
elv.call_Elevator(7,-1)
elv.select_Floor(3)
elv.call_Elevator(2,1)
elv.select_Floor(9)
#elv.call_Elevator(1,1)
#elv.select_Floor(7)