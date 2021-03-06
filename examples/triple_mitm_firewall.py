
load_modules = {
    'hw_CANBusTriple':    {
        'port':'auto',
        'debug': 2,
        'speed':500,'bus':'CBT'}, # IO hardware module
    'hw_USBtin~2':  {'port':'auto', 'debug':2, 'speed':500, 'bus': 'TIN2'},
    'hw_USBtin':    {'port':'auto', 'debug':2, 'speed':500, 'bus': 'TIN1'},
    'mod_stat':    {},     'gen_ping' :    {'debug': 1} ,                                 # Mod stat
    'mod_firewall':    {'debug': 2}                            # Generator/Ping
}

actions = [
    {'hw_CANBusTriple':   {'action': 'read','bus':1}}, # Read from bus_1
    {'hw_CANBusTriple':   {'action': 'read','bus':2,'pipe':2}}, # Read from  bus_2

    {'mod_firewall':      {'black_list': [0x22]}}, # Block chosen frames by ID
    {'mod_stat':          {}},                            # read not blocked packets from both buses

    {'mod_firewall':      {'black_list': [0x22],'pipe':2}}, # Block chosen frames by ID
    {'mod_stat':          {'pipe':2}},                            # read not blocked packets from both buses



#    {'hw_CANBusTriple':   {'action': 'write','bus':1,'pipe':2}},            # Write packets back but in different buses (MITM)

#    {'hw_CANBusTriple':   {'action': 'write','bus':2}},            # Write packets back but in different buses (MITM)



     {'gen_ping':    {                              # Generate pings to PIPE 1
        'delay':0.06,
        'body': '112233', # ISO TP data
        'range': [0x10, 0x30],    # ID range (from 502999 to 543002)
        'mode': 'can', 'pipe':'fake1'} # Send packets in ISO-TP format
    },
    {'hw_USBtin~2':{'pipe':'fake1','action':'write'}},
    {'hw_USBtin':{'pipe':'fake2','action':'read'}},
    {'hw_USBtin':{'pipe':'fake1','action':'read'}}
    ]



