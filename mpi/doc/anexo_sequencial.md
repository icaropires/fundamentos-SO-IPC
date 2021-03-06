# Relatório de execução da versão sequencial

## Computador 1:
### Informações:
	Sistema Operacional: Ubuntu 16.04
	Processador: Intel® Core™ i5-4210U CPU @ 1.70GHz × 4 
	Memória: 7,7 GB
	Estado do computador antes das execuções: Anexo 1

### Execução
#### Comando
``` sh
$ time ./bin:
```
### Saídas
#### Primeira:
```
Max: 500000000.000000
Min: 0.000000

real	0m10.770s
user	0m10.416s
sys	0m0.352s
```

#### Segunda:
```
Max: 500000000.000000
Min: 0.000000

real	0m10.642s
user	0m10.360s
sys	0m0.280s
```

#### Terceira:
```
Max: 500000000.000000
Min: 0.000000

real	0m10.752s
user	0m10.480s
sys	0m0.272s
```


## Computador 2:
### Informações:
	VM com 3 CPUs disponíveis.
	Sistema Operacional: Ubuntu
	Processador: Intel® Cor i7-7200U CPU @ 2.40GHz 4 
	Memória:5,120 GB
	Estado do computador antes das execuções: Anexo 2

### Execução

#### Comando
``` sh
$ time ./bin:
```
### Saídas

#### Primeira:
```
Max: 500000000.000000
Min: 0.000000

real	0m9.569s
user	0m8.597s
sys	0m0.940s
```

#### Segunda:
```
Max: 500000000.000000
Min: 0.000000

real	0m9.584s
user	0m8.557s
sys	0m0.988s
```

#### Terceira:
```
Max: 500000000.000000
Min: 0.000000

real	0m9.640s
user	0m8.701s
sys	0m0.908s
```


### Anexo 1
#### Comando
``` sh
$ top -b:
```
### Saída
```
	top - 19:56:16 up 17:41,  3 users,  load average: 0,04, 0,09, 0,15
	Tasks: 224 total,   1 running, 223 sleeping,   0 stopped,   0 zombie
	%Cpu(s):  8,2 us,  2,3 sy,  0,1 ni, 88,4 id,  0,9 wa,  0,0 hi,  0,1 si,  0,0 st
	KiB Mem :  8063556 total,  5019020 free,  1352508 used,  1692028 buff/cache
	KiB Swap: 12182520 total, 12177756 free,     4764 used.  6165368 avail Mem 

	  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
	14170 icaro     20   0 2527724  84480  17228 S  12,5  1,0   0:51.21 vim
	 2242 icaro     20   0  339368  10996   5180 S   6,2  0,1   0:29.08 ibus-daemon
		1 root      20   0  119896   6076   3980 S   0,0  0,1   0:01.85 systemd
		2 root      20   0       0      0      0 S   0,0  0,0   0:00.00 kthreadd
		3 root      20   0       0      0      0 S   0,0  0,0   0:00.25 ksoftirqd/0
		5 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 kworker/0:0H
		7 root      20   0       0      0      0 S   0,0  0,0   0:16.20 rcu_sched
		8 root      20   0       0      0      0 S   0,0  0,0   0:00.00 rcu_bh
		9 root      rt   0       0      0      0 S   0,0  0,0   0:00.04 migration/0
	   10 root      rt   0       0      0      0 S   0,0  0,0   0:00.04 watchdog/0
	   11 root      rt   0       0      0      0 S   0,0  0,0   0:00.04 watchdog/1
	   12 root      rt   0       0      0      0 S   0,0  0,0   0:00.03 migration/1
	   13 root      20   0       0      0      0 S   0,0  0,0   0:00.08 ksoftirqd/1
	   15 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 kworker/1:0H
	   16 root      rt   0       0      0      0 S   0,0  0,0   0:00.04 watchdog/2
	   17 root      rt   0       0      0      0 S   0,0  0,0   0:00.04 migration/2
	   18 root      20   0       0      0      0 S   0,0  0,0   0:00.11 ksoftirqd/2
	   20 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 kworker/2:0H
	   21 root      rt   0       0      0      0 S   0,0  0,0   0:00.04 watchdog/3
	   22 root      rt   0       0      0      0 S   0,0  0,0   0:00.04 migration/3
	   23 root      20   0       0      0      0 S   0,0  0,0   0:00.08 ksoftirqd/3
	   25 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 kworker/3:0H
	   26 root      20   0       0      0      0 S   0,0  0,0   0:00.00 kdevtmpfs
	   27 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 netns
	   28 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 perf
	   29 root      20   0       0      0      0 S   0,0  0,0   0:00.00 khungtaskd
	   30 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 writeback
	   31 root      25   5       0      0      0 S   0,0  0,0   0:00.00 ksmd
	   32 root      39  19       0      0      0 S   0,0  0,0   0:01.27 khugepaged
	   33 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 crypto
	   34 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 kintegrityd
	   35 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 bioset
	   36 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 kblockd
	   37 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 ata_sff
	   38 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 md
	   39 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 devfreq_wq
	   46 root      20   0       0      0      0 S   0,0  0,0   0:00.04 kswapd0
	   47 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 vmstat
	   48 root      20   0       0      0      0 S   0,0  0,0   0:00.00 fsnotify_mark
	   49 root      20   0       0      0      0 S   0,0  0,0   0:00.00 ecryptfs-kthrea
	   65 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 kthrotld
	   66 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 acpi_thermal_pm
	   69 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 bioset
	   70 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 bioset
	   71 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 bioset
	   72 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 bioset
	   73 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 bioset
	   74 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 bioset
	   75 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 bioset
	   76 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 bioset
	   80 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 ipv6_addrconf
	   93 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 deferwq
	   94 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 charger_manager
	  142 root      20   0       0      0      0 S   0,0  0,0   0:00.00 scsi_eh_0
	  143 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 scsi_tmf_0
	  144 root      20   0       0      0      0 S   0,0  0,0   0:00.00 scsi_eh_1
	  145 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 scsi_tmf_1
	  146 root      20   0       0      0      0 S   0,0  0,0   0:00.00 scsi_eh_2
	  147 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 scsi_tmf_2
	  148 root      20   0       0      0      0 S   0,0  0,0   0:00.00 scsi_eh_3
	  149 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 scsi_tmf_3
	  153 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 rtsx_pci_sdmmc_
	  158 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 bioset
	  159 root      20   0       0      0      0 S   0,0  0,0   0:00.00 scsi_eh_4
	  160 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 scsi_tmf_4
	  161 root      20   0       0      0      0 S   0,0  0,0   0:00.33 usb-storage
	  162 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 bioset
	  165 root       0 -20       0      0      0 S   0,0  0,0   0:00.05 kworker/2:1H
	  167 root       0 -20       0      0      0 S   0,0  0,0   0:00.02 kworker/3:1H
	  168 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 bioset
	  196 root       0 -20       0      0      0 S   0,0  0,0   0:00.10 kworker/1:1H
	  198 root      20   0       0      0      0 S   0,0  0,0   0:00.34 jbd2/sda7-8
	  199 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 ext4-rsv-conver
	  235 root      20   0       0      0      0 S   0,0  0,0   0:00.00 kauditd
	  249 root      20   0   35484   5616   5136 S   0,0  0,1   0:00.57 systemd-journal
	  275 root      20   0   45860   5188   3064 S   0,0  0,1   0:01.17 systemd-udevd
	  343 root     -51   0       0      0      0 S   0,0  0,0   0:50.02 irq/39-SYN1B7E:
	  387 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 kmemstick
	  496 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 cfg80211
	  527 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 kvm-irqfd-clean
	  614 root       0 -20       0      0      0 S   0,0  0,0   0:00.08 kworker/0:1H
	  850 systemd+  20   0  102384   2576   2356 S   0,0  0,0   0:00.02 systemd-timesyn
	  970 root      20   0   29012   3040   2760 S   0,0  0,0   0:00.01 cron
	  975 message+  20   0   44540   5464   3512 S   0,0  0,1   0:05.41 dbus-daemon
	 1005 avahi     20   0   44904   3516   3128 S   0,0  0,0   0:00.41 avahi-daemon
	 1012 root      20   0  276000   6396   5552 S   0,0  0,1   0:00.34 accounts-daemon
	 1017 root      20   0  166444   8668   7944 S   0,0  0,1   0:00.83 thermald
	 1019 root      20   0    4400   1276   1180 S   0,0  0,0   0:01.33 acpid
	 1022 root      20   0   32052   4556   4132 S   0,0  0,1   0:00.01 bluetoothd
	 1044 root      20   0   29880   1596   1376 S   0,0  0,0   0:00.00 cgmanager
	 1048 syslog    20   0  256396   3364   2736 S   0,0  0,0   0:00.13 rsyslogd
	 1051 root      20   0  597372  19440  13748 S   0,0  0,2   0:05.78 NetworkManager
	 1057 root      20   0   93984   8264   6376 S   0,0  0,1   0:00.02 cupsd
	 1072 root      20   0   20412   2696   2376 S   0,0  0,0   0:00.14 systemd-logind
	 1074 root      20   0  229584  23592  13600 S   0,0  0,3   0:00.05 snapd
	 1124 root      20   0  276680   6152   5324 S   0,0  0,1   0:00.04 lightdm
	 1126 avahi     20   0   44788    340     12 S   0,0  0,0   0:00.00 avahi-daemon
	 1127 root      20   0  274964   9184   7948 S   0,0  0,1   0:00.05 cups-browsed
	 1141 root      20   0  282192   8652   6184 S   0,0  0,1   0:00.33 polkitd
	 1262 colord    20   0  301420  11368   8492 S   0,0  0,1   0:00.17 colord
	 1340 lp        20   0   81244   5576   4808 S   0,0  0,1   0:00.00 dbus
	 1343 root      20   0   44028   6496   5848 S   0,0  0,1   0:00.57 wpa_supplicant
	 1436 root      20   0  363572  58944  44660 S   0,0  0,7   3:44.01 Xorg
	 1437 root      20   0  977484   3000   2412 S   0,0  0,0   0:00.75 nscd
	 1476 root      20   0   19472   2240   1976 S   0,0  0,0   0:00.62 irqbalance
	 1503 root      20   0  882136  23584  19776 S   0,0  0,3   0:02.59 core
	 1506 debian-+  20   0   77500  40768  14004 S   0,0  0,5   0:08.19 tor
	 1514 mysql     20   0 1252704 200540  14900 S   0,0  2,5   0:07.54 mysqld
	 1533 root      20   0    7708    680    608 S   0,0  0,0   0:00.00 agetty
	 1556 tomcat8   20   0 3145776 126980  16864 S   0,0  1,6   0:17.10 java
	 1561 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 iprt-VBoxWQueue
	 1565 root      20   0       0      0      0 S   0,0  0,0   0:00.00 iprt-VBoxTscThr
	 1740 root      20   0  232828   6880   6092 S   0,0  0,1   0:00.13 lightdm
	 1804 rtkit     21   1  175308   1524   1324 S   0,0  0,0   0:00.11 rtkit-daemon
	 1813 root      10 -10       0      0      0 S   0,0  0,0   0:00.00 krfcommd
	 1821 root      20   0  347460  10156   8440 S   0,0  0,1   0:00.46 upowerd
	 1885 icaro     20   0   37012   4424   3648 S   0,0  0,1   0:00.04 systemd
	 1887 icaro     20   0  145680   2028      0 S   0,0  0,0   0:00.00 (sd-pam)
	 1892 icaro     20   0  205852   7912   6500 S   0,0  0,1   0:00.31 gnome-keyring-d
	 1895 icaro     20   0  237272  14548  12720 S   0,0  0,2   0:00.01 kwalletd5
	 1896 icaro     20   0   38588   4600   3396 S   0,0  0,1   0:00.29 upstart
	 2006 nobody    20   0   44848   2072   1792 S   0,0  0,0   0:00.82 dnsmasq
	 2188 icaro     20   0   32864   2200   1864 S   0,0  0,0   0:00.09 upstart-udev-br
	 2197 icaro     20   0   36156   4540   2764 S   0,0  0,1   0:03.36 dbus-daemon
	 2209 icaro     20   0   86356   9116   8484 S   0,0  0,1   0:00.13 window-stack-br
	 2233 icaro     20   0   32876   1696   1284 S   0,0  0,0   0:00.60 upstart-dbus-br
	 2234 icaro     20   0   32800    308     12 S   0,0  0,0   0:00.68 upstart-dbus-br
	 2254 icaro     20   0   33056    356     12 S   0,0  0,0   0:00.02 upstart-file-br
	 2266 icaro     20   0  348268   6232   5448 S   0,0  0,1   0:00.06 gvfsd
	 2271 icaro     20   0  406864   6836   4308 S   0,0  0,1   0:00.00 gvfsd-fuse
	 2282 icaro     20   0  264288   6092   5544 S   0,0  0,1   0:00.00 ibus-dconf
	 2283 icaro     20   0  478872  31032  25540 S   0,0  0,4   0:07.79 ibus-ui-gtk3
	 2285 icaro     20   0  427720  21748  18500 S   0,0  0,3   0:00.18 ibus-x11
	 2295 icaro     20   0  338032   5816   5348 S   0,0  0,1   0:00.00 at-spi-bus-laun
	 2302 icaro     20   0   35000   3668   3256 S   0,0  0,0   0:00.18 dbus-daemon
	 2304 icaro     20   0  206868   6448   5812 S   0,0  0,1   0:01.10 at-spi2-registr
	 2307 icaro     20   0  166544    696    456 S   0,0  0,0   0:00.29 gpg-agent
	 2314 icaro     20   0  523200  26896  21676 S   0,0  0,3   0:05.00 bamfdaemon
	 2328 icaro     20   0  716260  43108  33548 S   0,0  0,5   0:01.19 hud-service
	 2329 icaro     20   0  188528   6256   5680 S   0,0  0,1   0:08.35 ibus-engine-sim
	 2331 icaro     20   0  981940  33376  26128 S   0,0  0,4   0:00.92 unity-settings-
	 2338 icaro     20   0  558668  15060  12852 S   0,0  0,2   0:00.32 gnome-session-b
	 2344 icaro     20   0  641336  35560  26652 S   0,0  0,4   0:05.51 unity-panel-ser
	 2359 icaro     20   0   22372   1108    944 S   0,0  0,0   0:00.86 syndaemon
	 2368 icaro      9 -11  584860  12272   8948 S   0,0  0,2   2:39.85 pulseaudio
	 2382 icaro     20   0  179060   5208   4216 S   0,0  0,1   0:00.24 dconf-service
	 2396 icaro     20   0  346696   7472   6188 S   0,0  0,1   0:00.06 indicator-messa
	 2397 icaro     20   0  407288   7632   4960 S   0,0  0,1   0:00.02 indicator-bluet
	 2401 icaro     20   0  570120  11840   6388 S   0,0  0,1   0:00.17 indicator-power
	 2404 icaro     20   0 1225380  16796  13704 S   0,0  0,2   0:00.22 indicator-datet
	 2408 icaro     20   0  706268  28360  21332 S   0,0  0,4   0:00.28 indicator-keybo
	 2410 icaro     20   0  805184  12816   8812 S   0,0  0,2   0:00.15 indicator-sound
	 2411 icaro     20   0  538968  21916  18300 S   0,0  0,3   0:00.17 indicator-print
	 2412 icaro     20   0  952916   8824   5708 S   0,0  0,1   0:00.14 indicator-sessi
	 2437 icaro     20   0  403152  12868  11388 S   0,0  0,2   0:00.77 indicator-appli
	 2466 icaro     20   0 1177392  27428  19544 S   0,0  0,3   0:00.06 evolution-sourc
	 2481 icaro     20   0  629220  31716  26936 S   0,0  0,4   0:00.37 polkit-gnome-au
	 2484 icaro     20   0  568416  14300   9748 S   0,0  0,2   0:01.31 core
	 2487 icaro     20   0  877308  35484  29304 S   0,0  0,4   0:05.15 nm-applet
	 2488 icaro     20   0 1508836  62052  41808 S   0,0  0,8   0:08.50 nautilus
	 2500 icaro     20   0  511324  21312  18056 S   0,0  0,3   0:00.23 unity-fallback-
	 2501 icaro     20   0 1364168 110264  28132 S   0,0  1,4   0:03.57 gnome-software
	 2505 icaro     20   0  510440  23008  19416 S   0,0  0,3   0:00.30 indicator-kdeco
	 2506 icaro     20   0 1540420 213128  70104 S   0,0  2,6   3:38.60 compiz
	 2522 icaro     20   0  350960   7564   6352 S   0,0  0,1   0:00.08 gvfs-udisks2-vo
	 2524 icaro     20   0  987700  61588  50212 S   0,0  0,8   0:04.66 kdeconnectd
	 2535 root      20   0  424692   8800   6172 S   0,0  0,1   0:01.77 udisksd
	 2550 icaro     20   0  259532   4540   4132 S   0,0  0,1   0:00.01 gvfs-mtp-volume
	 2556 icaro     20   0  257544   4252   3936 S   0,0  0,1   0:00.00 gvfs-goa-volume
	 2561 icaro     20   0  271856   6108   5356 S   0,0  0,1   0:00.01 gvfs-gphoto2-vo
	 2564 icaro     20   0  854836  59212  21280 S   0,0  0,7   0:00.12 evolution-calen
	 2569 icaro     20   0  403612  10952   7888 S   0,0  0,1   0:00.01 gvfs-afc-volume
	 2587 root      20   0  620416  33288   9828 S   0,0  0,4   0:00.70 fwupd
	 2595 icaro     20   0  348156   6284   5544 S   0,0  0,1   0:00.00 gvfsd-burn
	 2610 icaro     20   0  350580   8476   5684 S   0,0  0,1   0:00.02 gvfsd-trash
	 2627 icaro     20   0  187528   6808   4948 S   0,0  0,1   0:00.03 gvfsd-metadata
	 2633 icaro     20   0  552376  24580  21108 S   0,0  0,3   0:00.17 telepathy-indic
	 2639 icaro     20   0  427500  14916  11104 S   0,0  0,2   0:01.42 mission-control
	 2646 icaro     20   0  873320  53200  12852 S   0,0  0,7   0:00.23 evolution-calen
	 2656 icaro     20   0  682368  19884  15280 S   0,0  0,2   0:00.03 evolution-addre
	 2659 icaro     20   0 1054304  49800  13092 S   0,0  0,6   0:00.25 evolution-calen
	 2692 icaro     20   0  757864  21904  15400 S   0,0  0,3   0:00.20 evolution-addre
	 2734 icaro     20   0    4508    788    708 S   0,0  0,0   0:00.00 sh
	 2738 icaro     20   0  410432   7336   6036 S   0,0  0,1   0:00.23 zeitgeist-daemo
	 2745 icaro     20   0  317304  15036  12468 S   0,0  0,2   0:00.18 zeitgeist-fts
	 2747 icaro     20   0  445076  17004  14224 S   0,0  0,2   0:00.39 zeitgeist-datah
	 2875 icaro     20   0   53060   5184   4616 S   0,0  0,1   0:00.01 gconfd-2
	 2914 icaro     20   0  516576  25912  22084 S   0,0  0,3   0:00.39 update-notifier
	 4217 icaro     20   0  435484   7084   6256 S   0,0  0,1   0:00.19 deja-dup-monito
	 4692 icaro     20   0  490968  32072  27020 S   0,0  0,4   0:01.78 notify-osd
	 6650 icaro     20   0  426708   6756   6004 S   0,0  0,1   0:00.01 gvfsd-network
	 6673 icaro     20   0  361724   8528   5728 S   0,0  0,1   0:00.00 gvfsd-dnssd
	 8807 icaro     20   0  497024  27488  16188 S   0,0  0,3   0:00.55 unity-scope-loa
	10622 icaro     20   0  563108  19160  13184 S   0,0  0,2   0:00.32 unity-scope-hom
	10931 icaro     20   0  577704  23296  11196 S   0,0  0,3   0:00.07 gvfsd-http
	12846 root     -51   0       0      0      0 S   0,0  0,0   0:00.00 irq/47-mei_me
	12947 root      20   0   14212   3604   2756 S   0,0  0,0   0:00.00 dhclient
	13108 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 kworker/u17:0
	13109 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 hci0
	13110 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 hci0
	13113 root       0 -20       0      0      0 S   0,0  0,0   0:00.00 kworker/u17:2
	13440 icaro     20   0  802268  69268  42472 S   0,0  0,9   0:28.32 /usr/bin/x-term
	13451 icaro     20   0    6848    824    740 S   0,0  0,0   0:00.00 gnome-pty-helpe
	13452 icaro     20   0   21888  12776   3388 S   0,0  0,2   0:00.33 bash
	14173 icaro     20   0 2443796 166476  37444 S   0,0  2,1   0:04.96 python2
	14330 icaro     20   0   21888  12580   3192 S   0,0  0,2   0:00.36 bash
	14840 root      20   0       0      0      0 S   0,0  0,0   0:05.12 kworker/3:0
	15111 root      20   0       0      0      0 S   0,0  0,0   0:00.91 kworker/0:0
	15965 root      20   0       0      0      0 S   0,0  0,0   0:00.16 kworker/1:1
	15991 root      20   0       0      0      0 S   0,0  0,0   0:00.52 kworker/u16:1
	16264 root      20   0       0      0      0 S   0,0  0,0   0:00.54 kworker/u16:2
	16424 icaro     20   0   29116    340      0 S   0,0  0,0   0:00.00 xclip
	16557 root      20   0       0      0      0 S   0,0  0,0   0:00.66 kworker/2:2
	16573 root      20   0       0      0      0 S   0,0  0,0   0:00.00 kworker/3:1
	16605 root      20   0       0      0      0 S   0,0  0,0   0:00.00 kworker/0:1
	16606 root      20   0       0      0      0 S   0,0  0,0   0:00.21 kworker/u16:3
	16619 root      20   0       0      0      0 S   0,0  0,0   0:00.00 kworker/1:0
	16654 root      20   0       0      0      0 S   0,0  0,0   0:00.15 kworker/2:0
	16806 root      20   0       0      0      0 S   0,0  0,0   0:00.00 kworker/0:2
	16818 root      20   0       0      0      0 S   0,0  0,0   0:00.00 kworker/u16:0
	16843 root      20   0       0      0      0 S   0,0  0,0   0:00.00 kworker/1:2
	16852 root      20   0       0      0      0 S   0,0  0,0   0:00.00 kworker/2:1
	16855 root      20   0       0      0      0 S   0,0  0,0   0:00.00 kworker/3:2
	16865 icaro     20   0   33572   3412   2856 R   0,0  0,0   0:00.00 top
```

### Anexo 2
#### Comando
``` sh
$ top -b:
```
### Saída
```
top - 10:19:56 up 6 min,  1 user,  load average: 0.10, 0.06, 0.03
Tasks:  82 total,   1 running,  81 sleeping,   0 stopped,   0 zombie
Cpu(s):  0.2%us,  0.3%sy,  0.0%ni, 99.4%id,  0.1%wa,  0.0%hi,  0.0%si,  0.0%st
Mem:   5081940k total,   183712k used,  4898228k free,    17380k buffers
Swap:   786428k total,        0k used,   786428k free,    53652k cached

  PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND                                    
    1 root      20   0 24332 2224 1340 S    0  0.0   0:00.67 init                                       
    2 root      20   0     0    0    0 S    0  0.0   0:00.00 kthreadd                                   
    3 root      20   0     0    0    0 S    0  0.0   0:00.02 ksoftirqd/0                                
    6 root      RT   0     0    0    0 S    0  0.0   0:00.00 migration/0                                
    7 root      RT   0     0    0    0 S    0  0.0   0:00.00 watchdog/0                                 
    8 root      RT   0     0    0    0 S    0  0.0   0:00.00 migration/1                                
   10 root      20   0     0    0    0 S    0  0.0   0:00.01 ksoftirqd/1                                
   11 root      20   0     0    0    0 S    0  0.0   0:00.09 kworker/0:1                                
   12 root      RT   0     0    0    0 S    0  0.0   0:00.00 watchdog/1                                 
   13 root      RT   0     0    0    0 S    0  0.0   0:00.00 migration/2                                
   15 root      20   0     0    0    0 S    0  0.0   0:00.00 ksoftirqd/2                                
   16 root      RT   0     0    0    0 S    0  0.0   0:00.00 watchdog/2                                 
   17 root       0 -20     0    0    0 S    0  0.0   0:00.00 cpuset                                     
   18 root       0 -20     0    0    0 S    0  0.0   0:00.00 khelper                                    
   19 root      20   0     0    0    0 S    0  0.0   0:00.00 kdevtmpfs                                  
   20 root       0 -20     0    0    0 S    0  0.0   0:00.00 netns                                      
   22 root      20   0     0    0    0 S    0  0.0   0:00.00 sync_supers                                
   23 root      20   0     0    0    0 S    0  0.0   0:00.00 bdi-default                                
   24 root       0 -20     0    0    0 S    0  0.0   0:00.00 kintegrityd                                
   25 root       0 -20     0    0    0 S    0  0.0   0:00.00 kblockd                                    
   26 root       0 -20     0    0    0 S    0  0.0   0:00.00 ata_sff                                    
   27 root      20   0     0    0    0 S    0  0.0   0:00.00 khubd                                      
   28 root       0 -20     0    0    0 S    0  0.0   0:00.00 md                                         
   30 root      20   0     0    0    0 S    0  0.0   0:00.00 khungtaskd                                 
   31 root      20   0     0    0    0 S    0  0.0   0:00.00 kswapd0                                    
   32 root      25   5     0    0    0 S    0  0.0   0:00.00 ksmd                                       
   33 root      39  19     0    0    0 S    0  0.0   0:00.00 khugepaged                                 
   34 root      20   0     0    0    0 S    0  0.0   0:00.00 fsnotify_mark                              
   35 root      20   0     0    0    0 S    0  0.0   0:00.00 ecryptfs-kthrea                            
   36 root       0 -20     0    0    0 S    0  0.0   0:00.00 crypto                                     
   44 root       0 -20     0    0    0 S    0  0.0   0:00.00 kthrotld                                   
   45 root      20   0     0    0    0 S    0  0.0   0:00.00 kworker/u:2                                
   46 root      20   0     0    0    0 S    0  0.0   0:00.03 kworker/1:1                                
   47 root      20   0     0    0    0 S    0  0.0   0:00.00 scsi_eh_0                                  
   48 root      20   0     0    0    0 S    0  0.0   0:00.00 scsi_eh_1                                  
   49 root      20   0     0    0    0 S    0  0.0   0:00.00 scsi_eh_2                                  
   51 root      20   0     0    0    0 S    0  0.0   0:00.06 kworker/2:1                                
   52 root      20   0     0    0    0 S    0  0.0   0:00.00 kworker/u:4                                
   71 root       0 -20     0    0    0 S    0  0.0   0:00.00 devfreq_wq                                 
   72 root      20   0     0    0    0 S    0  0.0   0:00.08 kworker/2:2                                
  119 root      20   0     0    0    0 S    0  0.0   0:00.04 kworker/2:3                                
  163 root      20   0     0    0    0 S    0  0.0   0:00.44 kworker/0:2                                
  252 root       0 -20     0    0    0 S    0  0.0   0:00.00 kdmflush                                   
  264 root       0 -20     0    0    0 S    0  0.0   0:00.00 kdmflush                                   
  273 root      20   0     0    0    0 S    0  0.0   0:00.00 jbd2/dm-0-8                                
  274 root       0 -20     0    0    0 S    0  0.0   0:00.00 ext4-dio-unwrit                            
  365 root      20   0 17240  632  452 S    0  0.0   0:00.04 upstart-udev-br                            
  368 root      20   0 21616 1436  816 S    0  0.0   0:00.04 udevd                                      
  471 root      20   0 21460  852  380 S    0  0.0   0:00.01 udevd                                      
  472 root      20   0 21540  876  328 S    0  0.0   0:00.00 udevd                                      
  473 root       0 -20     0    0    0 S    0  0.0   0:00.00 iprt                                       
  486 root      20   0     0    0    0 S    0  0.0   0:00.00 kworker/1:2                                
  540 root       0 -20     0    0    0 S    0  0.0   0:00.00 kpsmoused                                  
  602 root      20   0 15196  388  196 S    0  0.0   0:00.00 upstart-socket-                            
  614 root      20   0 19204 1024  740 S    0  0.0   0:00.00 rpcbind                                    
  669 root       0 -20     0    0    0 S    0  0.0   0:00.00 rpciod                                     
  684 root       0 -20     0    0    0 S    0  0.0   0:00.00 nfsiod                                     
  696 messageb  20   0 23824  704  456 S    0  0.0   0:00.01 dbus-daemon                                
  700 syslog    20   0  243m 1468 1088 S    0  0.0   0:00.04 rsyslogd                                   
  701 root      20   0 25544  436  212 S    0  0.0   0:00.00 rpc.idmapd                                 
  706 statd     20   0 21508 1360  900 S    0  0.0   0:00.00 rpc.statd                                  
  747 root      20   0  7268  588  104 S    0  0.0   0:00.00 dhclient3                                  
  794 root      20   0 50052 2908 2304 S    0  0.1   0:00.00 sshd                                       
  867 root      20   0 16028  964  800 S    0  0.0   0:00.00 getty                                      
  875 root      20   0 16028  964  800 S    0  0.0   0:00.00 getty                                      
  882 root      20   0 16028  960  800 S    0  0.0   0:00.00 getty                                      
  886 root      20   0 16028  968  800 S    0  0.0   0:00.00 getty                                      
  889 root      20   0 16028  956  800 S    0  0.0   0:00.00 getty                                      
  891 root      20   0 19116  880  688 S    0  0.0   0:00.00 cron                                       
  892 daemon    20   0 16912  376  216 S    0  0.0   0:00.00 atd                                        
  894 root      20   0 15988  696  516 S    0  0.0   0:00.05 irqbalance                                 
  912 root      20   0     0    0    0 S    0  0.0   0:00.00 flush-8:0                                  
  913 root      20   0     0    0    0 S    0  0.0   0:00.02 flush-252:0                                
 1132 ntp       20   0 37792 2208 1576 S    0  0.0   0:00.06 ntpd                                       
 1181 root      20   0  209m  556  252 S    0  0.0   0:00.13 VBoxService                                
 1235 root      20   0  7268  600  104 S    0  0.0   0:00.00 dhclient                                   
 1237 root      20   0 16028  964  800 S    0  0.0   0:00.00 getty                                      
 1239 root      20   0 71376 3484 2700 S    0  0.1   0:00.03 sshd                                       
 1254 vagrant   20   0 71376 1964 1168 S    0  0.0   0:00.19 sshd                                       
 1255 vagrant   20   0 29444 8432 1720 S    0  0.2   0:00.29 bash                                       
 1427 root      20   0     0    0    0 S    0  0.0   0:00.00 kworker/2:0                                
 1528 vagrant   20   0 17356 1236  948 R    0  0.0   0:00.00 top                                        
 ```
