
from .tracer.client import EPsolarTracerClient
from .tracer.registers import registers,coils

# configure the client logging
import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)



class epsolar_tracer():
    def __init__(self):
        self.client = EPsolarTracerClient()
        self.client.connect()

    def __del__(self):
        self.client.close()

    def getDeviceInfo(self):
        value = self.client.read_device_info()
        return value

    def getDeviceStatus(self):
        value = self.client.read_input("Charging equipment status")
        res = dict()
        if int(value.value)<<0 & 1:
            res['mode']='Running'
        else:
            res['mode']='Standby'

        if int(value.value)<<1 & 1:
            res['state']='Err'
        else:
            res['state']='Ok'

        if int(value.value)<<2 & 1:
            if int(value.value)<<3 & 1:
                res['charging']='Equalization'
            else:
                res['charging']='Float'
        else:
            if int(value.value)<<3 & 1:
                res['charging']='Not Charging'
            else:
                res['charging']='Boost'


        return res

    def getCurrentInputPower(self):
        value = self.client.read_input("Charging equipment input power")
        return value

    def getCurrentInputVoltage(self):
        value = self.client.read_input("Charging equipment input voltage")
        return value

    def getCurrentInputCurrent(self):
        value = self.client.read_input("Charging equipment input current")
        return value

    def getGeneratedEnergyToday(self):
        value = self.client.read_input("Generated energy today")
        return value

    def getGeneratedEnergyTotal(self):
        value = self.client.read_input("Total generated energy")
        return value



    def printInfo(self):
        response = self.client.read_device_info()

        print("Manufacturer:", repr(response.information[0]))
        print("Model:", repr(response.information[1]))
        print("Version:", repr(response.information[2]))

        response = self.client.read_input("Charging equipment rated input voltage")
        print(str(response))

        for reg in registers:
            #print
            #print reg
            value = self.client.read_input(reg.name)
            print(value)
            #if value.value is not None:
            #    print client.write_output(reg.name,value.value)

        for reg in coils:
            #print
            #print reg
            value = self.client.read_input(reg.name)
            print(value)
            #print client.write_output(reg.name,value.value)
