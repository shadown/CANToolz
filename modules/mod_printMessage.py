from libs.module import *


class mod_printMessage(CANModule):
    name = "Print CAN message"
    help = """
    
    This module do only printing CAN messages and Debug info.
    
    Init parameters:  None
    
    Module configuration: 
    
      white_list - list of ID that should be printed
      black_list - list of ID that should not be printed
      pipe       - integer, 1 or 2 - from which pipe to print, default 1
      
      Example: {'white_list':[133,111]}
    
    """
    _active = True
    id = 5
    version = 1.0

    # Effect (could be fuzz operation, sniff, filter or whatever)
    def do_effect(self, can_msg, args={}):
        if can_msg.CANData:
            if 'white_list' in args:
                if can_msg.CANFrame.frame_id in args['white_list']:
                    print("Read: " + self.do_read(can_msg))  # Print CAN Message
            elif 'black_list' in args:
                if can_msg.CANFrame.frame_id not in args['black_list']:
                    print("Read: " + self.do_read(can_msg))  # Print CAN Message
            else:
                print("Read: " + self.do_read(can_msg))  # Print CAN Message
        elif not can_msg.CANData and can_msg.debugData:
            self.dprint(1, "DEBUG: " + can_msg.debugText)
        return can_msg

    def do_read(self, can_msg):
        return "BUS = " + str(can_msg.bus) + " ID = " + str(can_msg.CANFrame.frame_id) + " Message: " + \
               str(can_msg.CANFrame.frame_raw_data).encode('hex') + " Len: " + str(can_msg.CANFrame.frame_length)
