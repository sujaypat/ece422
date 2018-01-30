#
#  Note: You must run ./setcookie before running make.
#

CC := gcc
CFLAGS := -m32 -static -U_FORTIFY_SOURCE -DCOOKIE=$(shell cat cookie)
LDFLAGS :=
LDLIBS :=

programs := 1.1.1 1.1.2 1.1.3 1.1.4 1.1.5 1.2.1 1.2.2 1.2.3 1.2.4 1.2.5 1.2.6 1.2.7 1.2.8 1.2.9 1.2.10 1.2.11

.PHONY: default clean install uninstall

default: $(programs) permissions

1.1.1: CFLAGS += -w
1.1.2: CFLAGS +=
1.1.3: CFLAGS +=
1.1.4: CFLAGS +=
1.1.5: CFLAGS +=
1.2.1: CFLAGS += -fno-stack-protector -z execstack
1.2.2: CFLAGS += -fno-stack-protector -z execstack
1.2.3: CFLAGS += -fno-stack-protector -z execstack 
1.2.4: CFLAGS += -fno-stack-protector -z execstack 
1.2.5: CFLAGS += -fno-stack-protector -z execstack
1.2.6: CFLAGS += -fno-stack-protector
1.2.7: CFLAGS += -fno-stack-protector -z execstack
1.2.8: CFLAGS += -fno-stack-protector -z execstack
1.2.9: CFLAGS += -fno-stack-protector
1.2.10: CFLAGS += -fno-stack-protector -z execstack
1.2.11: CFLAGS += -fno-stack-protector -z execstack -w

1.1.1: 1.1.1.c helper.c 1.1.1.S
1.1.2: 1.1.2.c helper.c 1.1.2.S
1.1.3: 1.1.3.c helper.c 1.1.3.S
1.1.4: 1.1.4.c helper.c 1.1.4.S
1.1.5: helper.c 1.1.5.S
1.2.1: 1.2.1.c helper.c
1.2.2: 1.2.2.c helper.c
1.2.3: 1.2.3.c helper.c
1.2.4: 1.2.4.c helper.c
1.2.5: 1.2.5.c helper.c
1.2.6: 1.2.6.c helper.c
1.2.7: 1.2.7.c helper.c
1.2.8: 1.2.8.c helper.c
1.2.9: 1.2.9.c helper.c
1.2.10: 1.2.10.c helper.c
1.2.11: 1.2.11.c helper.c

clean:
	rm -f $(programs)

permissions:
	sudo chown root:ubuntu 1.2.[123456789] 1.2.10 1.2.11 1.1.5
	sudo chmod 6777 1.2.[123456789] 1.2.10 1.2.11 1.1.5
	
