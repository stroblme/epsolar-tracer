# EPSolar-Tracer Python 3 Library & Linux Drivers

*This project was forked from [here](https://github.com/kasbert/epsolar-tracer). I plan to do the following changes:*

- [x] Convert to Python 3
- [ ] Creating clean modules so you can use it as a component in another project
- [ ] Adding MQTT support to provide a standalone solution

## Hardware requirements

EPEVER Tracer A(N) and BN solar charge controllers tested with current version:

[Product link 2](https://solarv.de/product-category/laderegeler/mppt/)

You need RS-485 adapter for communication:

[Product link 3](https://solarv.de/product/epever-laderegeler-kabel/)

## Python module

By now, the modules are tested in *Python 3.6*.

The [modbus library](https://github.com/bashwork/pymodbus) is the only requirement.
```
pip install pymodbus
```

### Example usage
```
# python info.py
Manufacturer: 'EPsolar Tech co., Ltd'
Model: 'Tracer2215BN'
Version: 'V02.05+V07.12'
Charging equipment rated input voltage = 150.0V
Charging equipment rated input voltage = 150.0V
Charging equipment rated input current = 20.0A
...
```

## Linux driver for Exar USB UART

In [directory](xr_usb_serial_common-1a) there is a Linux driver for Exar based USB RS-485 adapter.
[Original source](https://www.exar.com/common/content/default.aspx?id=10296)

The driver has also been tested on aarch-64 platform, so you can use them on raspberry & co!

## Protocol

[Protocol](http://www.solar-elektro.cz/data/dokumenty/1733_modbus_protocol.pdf)
See for [windows capture](archive/epsolar.txt) for some extra commands.
