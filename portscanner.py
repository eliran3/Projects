#!/usr/bin/python3

import socket, timeit, multiprocessing, re, sys
from colorama import Fore

class _Open_Port:
    def __init__(self, _port: int, _service):
        self._port = _port
        self._service = _service
    
    def __eq__(self, other):
        return self._port == other._port and self._service == other._service

    def show(self):
        _p = len(str(self._port))
        if _p == 1:
            print(Fore.LIGHTGREEN_EX + f'{self._port}           open         {self._service}')
        elif _p == 2:
            print(Fore.LIGHTGREEN_EX + f'{self._port}          open         {self._service}')
        elif _p == 3:
            print(Fore.LIGHTGREEN_EX + f'{self._port}         open         {self._service}')
        elif _p == 4:
            print(Fore.LIGHTGREEN_EX + f'{self._port}        open         {self._service}')
        elif _p == 5:
            print(Fore.LIGHTGREEN_EX + f'{self._port}       open         {self._service}')
        elif _p == 6:
            print(Fore.LIGHTGREEN_EX + f'{self._port}      open         {self._service}')

def scan(_target, _port: int, _queue):
    _service = ''
    
    try:
        _sock = socket.socket()
        _sock.settimeout(0.75)
        _sock.connect((_target, _port))
        
        if _port <= 1024:
            try:
                _service = socket.getservbyport(_port)
            except:
                pass
        
        _queue.put(_Open_Port(_port, _service))
    except:
        pass

    _sock.close()

def check_ip(_ip):
        try:
            return socket.gethostbyaddr(_ip)[0]
        except:
            return socket.gethostbyname(_ip)

def scan_loop(_target, _start_p: int, _end_p: int, _queue):
    while (_start_p <= _end_p):
        scan(_target, _start_p, _queue)
        _start_p += 1

def multiprocessing_scan(_target, _ports_amount: int, _start_p: int, _end_p: int, _queue, _jumps: int=150):
    if _ports_amount < 700:
        _jumps = 2
    
    _start = _start_p
    _end = _start_p + _jumps
    _processes = []
    _processes_amount = int(_ports_amount / _jumps)
    _remaining_ports = 0
    
    if _ports_amount % _jumps != 0:
        _remaining_ports = _ports_amount % _jumps
    
    for _ in range(_processes_amount):
        _process = multiprocessing.Process(target=scan_loop, args=(_target, _start, _end, _queue))
        multiprocessing.Pool
        if __name__ == '__main__':
            _process.start()
            _processes.append(_process)
        
        _start += _jumps; _end += _jumps
    
    for _process in _processes:
        _process.join()
    
    if _remaining_ports != 0:
        _start =  _end_p - _remaining_ports
        scan_loop(_target, _start, _end_p, _queue)
    else:
        _start = _start_p
        _end = _start_p + _jumps
        scan_loop(_target, _start, _end, _queue)
    
    _outputs = arrange_outputs(_queue)
    
    for _o in _outputs:
        _o.show()
    
    print(Fore.MAGENTA + f'[=] Scan Ended! [{_target}]')

def regular_scan_loop(_target, _ports, _queue):
    for _p in _ports:
        _p = int(_p)
        scan(_target, _p, _queue)

    _outputs = arrange_outputs(_queue)
    
    for _o in _outputs:
        _o.show()
    
    print(Fore.MAGENTA + f'[=] Scan Ended! [{_target}]')

def arrange_outputs(_queue):
    _outputs = []
    
    while _queue.empty() is False:
        _outputs.append(_queue.get())

    def IsExists(_outputs, _o):
        counter = 0
        for _o1 in _outputs:
            if _o == _o1:
                counter += 1
        
        return counter
    
    for _o in _outputs:
        if IsExists(_outputs, _o) > 1:
            counter = IsExists(_outputs, _o)
            for i in range(0, counter - 1):
                _outputs.remove(_o)

    for i in range(len(_outputs)):
        for k in range(0, len(_outputs) - i - 1):
            if _outputs[k]._port > _outputs[k+1]._port:
                _temp = _outputs[k]
                _outputs[k] = _outputs[k+1]
                _outputs[k+1] = _temp
    
    return _outputs

print(Fore.CYAN + 'Copyright of @Eliran_Nissani, 2021')
print(Fore.LIGHTCYAN_EX + '----------------------------------')

_ip_pattern = r'({0-255}(\.{0-255})(\.{0-255})(\.{0-255}))|(www\.[a-zA-Z0-9-]\.(\w\.|\w\.w\.|\w\.w\.\w\.)?)'
_ip_pattern_obj = re.compile(_ip_pattern)

_start_addr_section = 0
_start_port_section = 0
for i in range(len(sys.argv)):
    if str(sys.argv[i]) == '-t':
        _start_addr_section = i
    elif str(sys.argv[i]) == '-p':
        _start_port_section = i
    
if _start_addr_section < _start_port_section:
    _ipaddr = sys.argv[_start_addr_section + 1:_start_port_section]
else:
    _ipaddr = sys.argv[_start_addr_section + 1:]

if re.fullmatch(_ip_pattern_obj, str(_ipaddr)) is not None:
    raise ValueError()

_targets = []

for _ip in _ipaddr:
    _targets.append(str(_ip.replace(',', '')))

for _target in _targets:
    _target = _target.replace(' ', '')
    _target = check_ip(_target)

    if _start_addr_section < _start_port_section:
        _stri_ports = sys.argv[_start_port_section + 1:]
    else:
        _stri_ports = sys.argv[_start_port_section + 1:_start_addr_section]

    _ports_amount = 0; _start_p = 0; _end_p = 0
    _queue = multiprocessing.Queue()

    print(Fore.MAGENTA + f'[=] Scanning... [{_target}]')
    print(Fore.LIGHTBLACK_EX + 'PORT        STATE        SERVICE')
    print(Fore.LIGHTBLACK_EX + '--------------------------------')

    if re.search(re.compile('(,)'), str(_stri_ports)) is not None:
        _ports = []

        for _p in _stri_ports:
            _ports.append(str(_p.replace(',', '')))
        
        print(Fore.GREEN + f'[=] Scan for {_target} took {timeit.timeit(lambda: regular_scan_loop(_target, _ports, _queue), number=1):.2f} seconds')
        print(Fore.CYAN + '------------------------------------------------')
    elif re.search(re.compile('(-)'), str(_stri_ports)) is not None:
        _stri_ports = str(_stri_ports)
        _stri_ports = _stri_ports.lstrip("'[")
        _stri_ports = _stri_ports.rstrip("']")
        _stri_ports = _stri_ports.split('-')
        _ports_amount = int(_stri_ports[1]) - int(_stri_ports[0])
        _start_p = int(_stri_ports[0])
        _end_p = int(_stri_ports[1])

        print(Fore.GREEN + f'[=] Scan for {_target} took {timeit.timeit(lambda: multiprocessing_scan(_target, _ports_amount, _start_p, _end_p, _queue), number=1):.2f} seconds')
        print(Fore.CYAN + '------------------------------------------------')
    else:
        raise ValueError
