# If KERNELRELEASE is defined, we've been invoked from the
# kernel build system and can use its language.

ifneq ($(KERNELRELEASE),)
	obj-m := keylogger.o

# Otherwise we were called directly from the command
# line; invoke the kernel build system.
else
	KERNELDIR ?= /lib/modules/$(shell uname -r)/build/
	PWD := $(shell pwd)

default:
	$(MAKE) -C $(KERNELDIR) M=$(PWD) modules

clean:	
	$(MAKE) -C $(KERNELDIR) M=$(PWD) clean

reset:
	$(MAKE) clean && clear && make

install:
	sudo rmmod -v keylogger; make && sudo insmod keylogger.ko

all:
	$(MAKE) reset && $(MAKE) install

endif
