from micropython import const
from enum import IntEnum


class Register(IntEnum):
    FIFO          = const(0x00)
    OPMODE          = const(0x01)
    DATAMODUL      = const(0x02)
    BITRATEMSB      = const(0x03)
    BITRATELSB      = const(0x04)
    FDEVMSB          = const(0x05)
    FDEVLSB          = const(0x06)
    FRFMSB          = const(0x07)
    FRFMID          = const(0x08)
    FRFLSB          = const(0x09)
    OSC1          = const(0x0A)
    AFCCTRL          = const(0x0B)
    LOWBAT          = const(0x0C)
    LISTEN1          = const(0x0D)
    LISTEN2          = const(0x0E)
    LISTEN3          = const(0x0F)
    VERSION          = const(0x10)
    PALEVEL          = const(0x11)
    PARAMP          = const(0x12)
    OCP              = const(0x13)
    AGCREF          = const(0x14)
    AGCTHRESH1      = const(0x15)
    AGCTHRESH2      = const(0x16)
    AGCTHRESH3      = const(0x17)
    LNA              = const(0x18)
    RXBW          = const(0x19)
    AFCBW          = const(0x1A)
    OOKPEAK          = const(0x1B)
    OOKAVG          = const(0x1C)
    OOKFIX          = const(0x1D)
    AFCFEI          = const(0x1E)
    AFCMSB          = const(0x1F)
    AFCLSB          = const(0x20)
    FEIMSB          = const(0x21)
    FEILSB          = const(0x22)
    RSSICONFIG      = const(0x23)
    RSSIVALUE      = const(0x24)
    DIOMAPPING1      = const(0x25)
    DIOMAPPING2      = const(0x26)
    IRQFLAGS1      = const(0x27)
    IRQFLAGS2      = const(0x28)
    RSSITHRESH      = const(0x29)
    RXTIMEOUT1      = const(0x2A)
    RXTIMEOUT2      = const(0x2B)
    PREAMBLEMSB      = const(0x2C)
    PREAMBLELSB      = const(0x2D)
    SYNCCONFIG      = const(0x2E)
    SYNCVALUE1      = const(0x2F)
    SYNCVALUE2      = const(0x30)
    SYNCVALUE3      = const(0x31)
    SYNCVALUE4      = const(0x32)
    SYNCVALUE5      = const(0x33)
    SYNCVALUE6      = const(0x34)
    SYNCVALUE7      = const(0x35)
    SYNCVALUE8      = const(0x36)
    PACKETCONFIG1  = const(0x37)
    PAYLOADLENGTH  = const(0x38)
    NODEADRS      = const(0x39)
    BROADCASTADRS  = const(0x3A)
    AUTOMODES      = const(0x3B)
    FIFOTHRESH      = const(0x3C)
    PACKETCONFIG2  = const(0x3D)
    AESKEY1          = const(0x3E)
    AESKEY2          = const(0x3F)
    AESKEY3          = const(0x40)
    AESKEY4          = const(0x41)
    AESKEY5          = const(0x42)
    AESKEY6          = const(0x43)
    AESKEY7          = const(0x44)
    AESKEY8          = const(0x45)
    AESKEY9          = const(0x46)
    AESKEY10      = const(0x47)
    AESKEY11      = const(0x48)
    AESKEY12      = const(0x49)
    AESKEY13      = const(0x4A)
    AESKEY14      = const(0x4B)
    AESKEY15      = const(0x4C)
    AESKEY16      = const(0x4D)
    TEMP1          = const(0x4E)
    TEMP2          = const(0x4F)
    TESTPA1          = const(0x5A) # only present on RFM69HW/SX1231H)
    TESTPA2          = const(0x5C) # only present on RFM69HW/SX1231H)
    TESTDAGC      = const(0x6F)
    TESTAFC       = const(0x71)


class RF(IntEnum):
    OPMODE_SEQUENCER_OFF                     = const(0x80)
    OPMODE_SEQUENCER_ON                      = const(0x00) # Default

    OPMODE_LISTEN_ON                         = const(0x40)
    OPMODE_LISTEN_OFF                        = const(0x00) # Default

    OPMODE_LISTENABORT                       = const(0x20)

    OPMODE_SLEEP                             = const(0x00)
    OPMODE_STANDBY                           = const(0x04) # Default
    OPMODE_SYNTHESIZER                       = const(0x08)
    OPMODE_TRANSMITTER                       = const(0x0C)
    OPMODE_RECEIVER                          = const(0x10)

    # Reg Data Modul)
    DATAMODUL_DATAMODE_PACKET                = const(0x00) # Default
    DATAMODUL_DATAMODE_CONTINUOUS            = const(0x40)
    DATAMODUL_DATAMODE_CONTINUOUSNOBSYNC     = const(0x60)

    DATAMODUL_MODULATIONTYPE_FSK             = const(0x00) # Default
    DATAMODUL_MODULATIONTYPE_OOK             = const(0x08)

    DATAMODUL_MODULATIONSHAPING_00           = const(0x00) # Default
    DATAMODUL_MODULATIONSHAPING_01           = const(0x01)
    DATAMODUL_MODULATIONSHAPING_10           = const(0x02)
    DATAMODUL_MODULATIONSHAPING_11           = const(0x03)

    # RegBitRate (bits/sec) example bitrates)
    BITRATEMSB_1200                          = const(0x68)
    BITRATELSB_1200                          = const(0x2B)
    BITRATEMSB_2400                          = const(0x34)
    BITRATELSB_2400                          = const(0x15)
    BITRATEMSB_4800                          = const(0x1A) # Default
    BITRATELSB_4800                          = const(0x0B) # Default
    BITRATEMSB_9600                          = const(0x0D)
    BITRATELSB_9600                          = const(0x05)
    BITRATEMSB_19200                         = const(0x06)
    BITRATELSB_19200                         = const(0x83)
    BITRATEMSB_38400                         = const(0x03)
    BITRATELSB_38400                         = const(0x41)
    BITRATEMSB_38323                         = const(0x03)
    BITRATELSB_38323                         = const(0x43)
    BITRATEMSB_34482                         = const(0x03)
    BITRATELSB_34482                         = const(0xA0)
    BITRATEMSB_76800                         = const(0x01)
    BITRATELSB_76800                         = const(0xA1)
    BITRATEMSB_153600                        = const(0x00)
    BITRATELSB_153600                        = const(0xD0)
    BITRATEMSB_57600                         = const(0x02)
    BITRATELSB_57600                         = const(0x2C)
    BITRATEMSB_115200                        = const(0x01)
    BITRATELSB_115200                        = const(0x16)
    BITRATEMSB_12500                         = const(0x0A)
    BITRATELSB_12500                         = const(0x00)
    BITRATEMSB_25000                         = const(0x05)
    BITRATELSB_25000                         = const(0x00)
    BITRATEMSB_50000                         = const(0x02)
    BITRATELSB_50000                         = const(0x80)
    BITRATEMSB_100000                        = const(0x01)
    BITRATELSB_100000                        = const(0x40)
    BITRATEMSB_150000                        = const(0x00)
    BITRATELSB_150000                        = const(0xD5)
    BITRATEMSB_200000                        = const(0x00)
    BITRATELSB_200000                        = const(0xA0)
    BITRATEMSB_250000                        = const(0x00)
    BITRATELSB_250000                        = const(0x80)
    BITRATEMSB_300000                        = const(0x00)
    BITRATELSB_300000                        = const(0x6B)
    BITRATEMSB_32768                         = const(0x03)
    BITRATELSB_32768                         = const(0xD1)
    # custom bitrates)
    BITRATEMSB_55555                         = const(0x02)
    BITRATELSB_55555                         = const(0x40)
    BITRATEMSB_200KBPS                       = const(0x00)
    BITRATELSB_200KBPS                       = const(0xa0)

    # RegFdev - frequency deviation (Hz))
    FDEVMSB_2000                             = const(0x00)
    FDEVLSB_2000                             = const(0x21)
    FDEVMSB_5000                             = const(0x00) # Default
    FDEVLSB_5000                             = const(0x52) # Default
    FDEVMSB_7500                             = const(0x00)
    FDEVLSB_7500                             = const(0x7B)
    FDEVMSB_10000                            = const(0x00)
    FDEVLSB_10000                            = const(0xA4)
    FDEVMSB_15000                            = const(0x00)
    FDEVLSB_15000                            = const(0xF6)
    FDEVMSB_20000                            = const(0x01)
    FDEVLSB_20000                            = const(0x48)
    FDEVMSB_25000                            = const(0x01)
    FDEVLSB_25000                            = const(0x9A)
    FDEVMSB_30000                            = const(0x01)
    FDEVLSB_30000                            = const(0xEC)
    FDEVMSB_35000                            = const(0x02)
    FDEVLSB_35000                            = const(0x3D)
    FDEVMSB_40000                            = const(0x02)
    FDEVLSB_40000                            = const(0x8F)
    FDEVMSB_45000                            = const(0x02)
    FDEVLSB_45000                            = const(0xE1)
    FDEVMSB_50000                            = const(0x03)
    FDEVLSB_50000                            = const(0x33)
    FDEVMSB_55000                            = const(0x03)
    FDEVLSB_55000                            = const(0x85)
    FDEVMSB_60000                            = const(0x03)
    FDEVLSB_60000                            = const(0xD7)
    FDEVMSB_65000                            = const(0x04)
    FDEVLSB_65000                            = const(0x29)
    FDEVMSB_70000                            = const(0x04)
    FDEVLSB_70000                            = const(0x7B)
    FDEVMSB_75000                            = const(0x04)
    FDEVLSB_75000                            = const(0xCD)
    FDEVMSB_80000                            = const(0x05)
    FDEVLSB_80000                            = const(0x1F)
    FDEVMSB_85000                            = const(0x05)
    FDEVLSB_85000                            = const(0x71)
    FDEVMSB_90000                            = const(0x05)
    FDEVLSB_90000                            = const(0xC3)
    FDEVMSB_95000                            = const(0x06)
    FDEVLSB_95000                            = const(0x14)
    FDEVMSB_100000                           = const(0x06)
    FDEVLSB_100000                           = const(0x66)
    FDEVMSB_110000                           = const(0x07)
    FDEVLSB_110000                           = const(0x0A)
    FDEVMSB_120000                           = const(0x07)
    FDEVLSB_120000                           = const(0xAE)
    FDEVMSB_130000                           = const(0x08)
    FDEVLSB_130000                           = const(0x52)
    FDEVMSB_140000                           = const(0x08)
    FDEVLSB_140000                           = const(0xF6)
    FDEVMSB_150000                           = const(0x09)
    FDEVLSB_150000                           = const(0x9A)
    FDEVMSB_160000                           = const(0x0A)
    FDEVLSB_160000                           = const(0x3D)
    FDEVMSB_170000                           = const(0x0A)
    FDEVLSB_170000                           = const(0xE1)
    FDEVMSB_180000                           = const(0x0B)
    FDEVLSB_180000                           = const(0x85)
    FDEVMSB_190000                           = const(0x0C)
    FDEVLSB_190000                           = const(0x29)
    FDEVMSB_200000                           = const(0x0C)
    FDEVLSB_200000                           = const(0xCD)
    FDEVMSB_210000                           = const(0x0D)
    FDEVLSB_210000                           = const(0x71)
    FDEVMSB_220000                           = const(0x0E)
    FDEVLSB_220000                           = const(0x14)
    FDEVMSB_230000                           = const(0x0E)
    FDEVLSB_230000                           = const(0xB8)
    FDEVMSB_240000                           = const(0x0F)
    FDEVLSB_240000                           = const(0x5C)
    FDEVMSB_250000                           = const(0x10)
    FDEVLSB_250000                           = const(0x00)
    FDEVMSB_260000                           = const(0x10)
    FDEVLSB_260000                           = const(0xA4)
    FDEVMSB_270000                           = const(0x11)
    FDEVLSB_270000                           = const(0x48)
    FDEVMSB_280000                           = const(0x11)
    FDEVLSB_280000                           = const(0xEC)
    FDEVMSB_290000                           = const(0x12)
    FDEVLSB_290000                           = const(0x8F)
    FDEVMSB_300000                           = const(0x13)
    FDEVLSB_300000                           = const(0x33)

    # Reg Frf (MHz) - carrier frequency)
    # 315 Mhz band)
    FRFMSB_314                               = const(0x4E)
    FRFMID_314                               = const(0x80)
    FRFLSB_314                               = const(0x00)
    FRFMSB_315                               = const(0x4E)
    FRFMID_315                               = const(0xC0)
    FRFLSB_315                               = const(0x00)
    FRFMSB_316                               = const(0x4F)
    FRFMID_316                               = const(0x00)
    FRFLSB_316                               = const(0x00)
    # 433 mhz band)
    FRFMSB_433                               = const(0x6C)
    FRFMID_433                               = const(0x40)
    FRFLSB_433                               = const(0x00)
    FRFMSB_434                               = const(0x6C)
    FRFMID_434                               = const(0x80)
    FRFLSB_434                               = const(0x00)
    FRFMSB_435                               = const(0x6C)
    FRFMID_435                               = const(0xC0)
    FRFLSB_435                               = const(0x00)
    # 868 Mhz band)
    FRFMSB_863                               = const(0xD7)
    FRFMID_863                               = const(0xC0)
    FRFLSB_863                               = const(0x00)
    FRFMSB_864                               = const(0xD8)
    FRFMID_864                               = const(0x00)
    FRFLSB_864                               = const(0x00)
    FRFMSB_865                               = const(0xD8)
    FRFMID_865                               = const(0x40)
    FRFLSB_865                               = const(0x00)
    FRFMSB_866                               = const(0xD8)
    FRFMID_866                               = const(0x80)
    FRFLSB_866                               = const(0x00)
    FRFMSB_867                               = const(0xD8)
    FRFMID_867                               = const(0xC0)
    FRFLSB_867                               = const(0x00)
    FRFMSB_868                               = const(0xD9)
    FRFMID_868                               = const(0x00)
    FRFLSB_868                               = const(0x00)
    FRFMSB_869                               = const(0xD9)
    FRFMID_869                               = const(0x40)
    FRFLSB_869                               = const(0x00)
    FRFMSB_870                               = const(0xD9)
    FRFMID_870                               = const(0x80)
    FRFLSB_870                               = const(0x00)
    # 915 Mhz band)
    FRFMSB_902                               = const(0xE1)
    FRFMID_902                               = const(0x80)
    FRFLSB_902                               = const(0x00)
    FRFMSB_903                               = const(0xE1)
    FRFMID_903                               = const(0xC0)
    FRFLSB_903                               = const(0x00)
    FRFMSB_904                               = const(0xE2)
    FRFMID_904                               = const(0x00)
    FRFLSB_904                               = const(0x00)
    FRFMSB_905                               = const(0xE2)
    FRFMID_905                               = const(0x40)
    FRFLSB_905                               = const(0x00)
    FRFMSB_906                               = const(0xE2)
    FRFMID_906                               = const(0x80)
    FRFLSB_906                               = const(0x00)
    FRFMSB_907                               = const(0xE2)
    FRFMID_907                               = const(0xC0)
    FRFLSB_907                               = const(0x00)
    FRFMSB_908                               = const(0xE3)
    FRFMID_908                               = const(0x00)
    FRFLSB_908                               = const(0x00)
    FRFMSB_909                               = const(0xE3)
    FRFMID_909                               = const(0x40)
    FRFLSB_909                               = const(0x00)
    FRFMSB_910                               = const(0xE3)
    FRFMID_910                               = const(0x80)
    FRFLSB_910                               = const(0x00)
    FRFMSB_911                               = const(0xE3)
    FRFMID_911                               = const(0xC0)
    FRFLSB_911                               = const(0x00)
    FRFMSB_912                               = const(0xE4)
    FRFMID_912                               = const(0x00)
    FRFLSB_912                               = const(0x00)
    FRFMSB_913                               = const(0xE4)
    FRFMID_913                               = const(0x40)
    FRFLSB_913                               = const(0x00)
    FRFMSB_914                               = const(0xE4)
    FRFMID_914                               = const(0x80)
    FRFLSB_914                               = const(0x00)
    FRFMSB_915                               = const(0xE4) # Default
    FRFMID_915                               = const(0xC0) # Default
    FRFLSB_915                               = const(0x00) # Default
    FRFMSB_916                               = const(0xE5)
    FRFMID_916                               = const(0x00)
    FRFLSB_916                               = const(0x00)
    FRFMSB_917                               = const(0xE5)
    FRFMID_917                               = const(0x40)
    FRFLSB_917                               = const(0x00)
    FRFMSB_918                               = const(0xE5)
    FRFMID_918                               = const(0x80)
    FRFLSB_918                               = const(0x00)
    FRFMSB_919                               = const(0xE5)
    FRFMID_919                               = const(0xC0)
    FRFLSB_919                               = const(0x00)
    FRFMSB_920                               = const(0xE6)
    FRFMID_920                               = const(0x00)
    FRFLSB_920                               = const(0x00)
    FRFMSB_921                               = const(0xE6)
    FRFMID_921                               = const(0x40)
    FRFLSB_921                               = const(0x00)
    FRFMSB_922                               = const(0xE6)
    FRFMID_922                               = const(0x80)
    FRFLSB_922                               = const(0x00)
    FRFMSB_923                               = const(0xE6)
    FRFMID_923                               = const(0xC0)
    FRFLSB_923                               = const(0x00)
    FRFMSB_924                               = const(0xE7)
    FRFMID_924                               = const(0x00)
    FRFLSB_924                               = const(0x00)
    FRFMSB_925                               = const(0xE7)
    FRFMID_925                               = const(0x40)
    FRFLSB_925                               = const(0x00)
    FRFMSB_926                               = const(0xE7)
    FRFMID_926                               = const(0x80)
    FRFLSB_926                               = const(0x00)
    FRFMSB_927                               = const(0xE7)
    FRFMID_927                               = const(0xC0)
    FRFLSB_927                               = const(0x00)
    FRFMSB_928                               = const(0xE8)
    FRFMID_928                               = const(0x00)
    FRFLSB_928                               = const(0x00)

    # Reg Osc 1)
    OSC1_RCCAL_START                         = const(0x80)
    OSC1_RCCAL_DONE                          = const(0x40)

    AFCLOWBETA_ON                            = const(0x20)
    AFCLOWBETA_OFF                           = const(0x00) # Default

    # Reg Low Bat)
    LOWBAT_MONITOR                           = const(0x10)
    LOWBAT_ON                                = const(0x08)
    LOWBAT_OFF                               = const(0x00) # Default

    LOWBAT_TRIM_1695                         = const(0x00)
    LOWBAT_TRIM_1764                         = const(0x01)
    LOWBAT_TRIM_1835                         = const(0x02) # Default
    LOWBAT_TRIM_1905                         = const(0x03)
    LOWBAT_TRIM_1976                         = const(0x04)
    LOWBAT_TRIM_2045                         = const(0x05)
    LOWBAT_TRIM_2116                         = const(0x06)
    LOWBAT_TRIM_2185                         = const(0x07)

    # Reg Listen 1)
    LISTEN1_RESOL_64                         = const(0x50)
    LISTEN1_RESOL_4100                       = const(0xA0) # Default
    LISTEN1_RESOL_262000                     = const(0xF0)

    LISTEN1_CRITERIA_RSSI                    = const(0x00) # Default
    LISTEN1_CRITERIA_RSSIANDSYNC             = const(0x08)

    LISTEN1_END_00                           = const(0x00)
    LISTEN1_END_01                           = const(0x02) # Default
    LISTEN1_END_10                           = const(0x04)

    # Reg Listen 2)
    LISTEN2_COEFIDLE_VALUE                   = const(0xF5) # Default

    # Reg Listen 3)
    LISTEN3_COEFRX_VALUE                     = const(0x20) # Default

    # Reg PaLevel)
    PALEVEL_PA0_ON                           = const(0x80) # Default
    PALEVEL_PA0_OFF                          = const(0x00)
    PALEVEL_PA1_ON                           = const(0x40)
    PALEVEL_PA1_OFF                          = const(0x00) # Default
    PALEVEL_PA2_ON                           = const(0x20)
    PALEVEL_PA2_OFF                          = const(0x00) # Default

    PALEVEL_OUTPUTPOWER_00000                = const(0x00)
    PALEVEL_OUTPUTPOWER_00001                = const(0x01)
    PALEVEL_OUTPUTPOWER_00010                = const(0x02)
    PALEVEL_OUTPUTPOWER_00011                = const(0x03)
    PALEVEL_OUTPUTPOWER_00100                = const(0x04)
    PALEVEL_OUTPUTPOWER_00101                = const(0x05)
    PALEVEL_OUTPUTPOWER_00110                = const(0x06)
    PALEVEL_OUTPUTPOWER_00111                = const(0x07)
    PALEVEL_OUTPUTPOWER_01000                = const(0x08)
    PALEVEL_OUTPUTPOWER_01001                = const(0x09)
    PALEVEL_OUTPUTPOWER_01010                = const(0x0A)
    PALEVEL_OUTPUTPOWER_01011                = const(0x0B)
    PALEVEL_OUTPUTPOWER_01100                = const(0x0C)
    PALEVEL_OUTPUTPOWER_01101                = const(0x0D)
    PALEVEL_OUTPUTPOWER_01110                = const(0x0E)
    PALEVEL_OUTPUTPOWER_01111                = const(0x0F)
    PALEVEL_OUTPUTPOWER_10000                = const(0x10)
    PALEVEL_OUTPUTPOWER_10001                = const(0x11)
    PALEVEL_OUTPUTPOWER_10010                = const(0x12)
    PALEVEL_OUTPUTPOWER_10011                = const(0x13)
    PALEVEL_OUTPUTPOWER_10100                = const(0x14)
    PALEVEL_OUTPUTPOWER_10101                = const(0x15)
    PALEVEL_OUTPUTPOWER_10110                = const(0x16)
    PALEVEL_OUTPUTPOWER_10111                = const(0x17)
    PALEVEL_OUTPUTPOWER_11000                = const(0x18)
    PALEVEL_OUTPUTPOWER_11001                = const(0x19)
    PALEVEL_OUTPUTPOWER_11010                = const(0x1A)
    PALEVEL_OUTPUTPOWER_11011                = const(0x1B)
    PALEVEL_OUTPUTPOWER_11100                = const(0x1C)
    PALEVEL_OUTPUTPOWER_11101                = const(0x1D)
    PALEVEL_OUTPUTPOWER_11110                = const(0x1E)
    PALEVEL_OUTPUTPOWER_11111                = const(0x1F) # Default

    # Reg PaRamp)
    PARAMP_3400                              = const(0x00)
    PARAMP_2000                              = const(0x01)
    PARAMP_1000                              = const(0x02)
    PARAMP_500                               = const(0x03)
    PARAMP_250                               = const(0x04)
    PARAMP_125                               = const(0x05)
    PARAMP_100                               = const(0x06)
    PARAMP_62                                = const(0x07)
    PARAMP_50                                = const(0x08)
    PARAMP_40                                = const(0x09) # Default
    PARAMP_31                                = const(0x0A)
    PARAMP_25                                = const(0x0B)
    PARAMP_20                                = const(0x0C)
    PARAMP_15                                = const(0x0D)
    PARAMP_12                                = const(0x0E)
    PARAMP_10                                = const(0x0F)

    # Reg Ocp)
    OCP_OFF                                  = const(0x0F)
    OCP_ON                                   = const(0x1A) # Default

    OCP_TRIM_45                              = const(0x00)
    OCP_TRIM_50                              = const(0x01)
    OCP_TRIM_55                              = const(0x02)
    OCP_TRIM_60                              = const(0x03)
    OCP_TRIM_65                              = const(0x04)
    OCP_TRIM_70                              = const(0x05)
    OCP_TRIM_75                              = const(0x06)
    OCP_TRIM_80                              = const(0x07)
    OCP_TRIM_85                              = const(0x08)
    OCP_TRIM_90                              = const(0x09)
    OCP_TRIM_95                              = const(0x0A)
    OCP_TRIM_100                             = const(0x0B) # Default
    OCP_TRIM_105                             = const(0x0C)
    OCP_TRIM_110                             = const(0x0D)
    OCP_TRIM_115                             = const(0x0E)
    OCP_TRIM_120                             = const(0x0F)

    # Reg Agc Ref)
    AGCREF_AUTO_ON                           = const(0x40) # Default
    AGCREF_AUTO_OFF                          = const(0x00)

    AGCREF_LEVEL_MINUS80                     = const(0x00) # Default
    AGCREF_LEVEL_MINUS81                     = const(0x01)
    AGCREF_LEVEL_MINUS82                     = const(0x02)
    AGCREF_LEVEL_MINUS83                     = const(0x03)
    AGCREF_LEVEL_MINUS84                     = const(0x04)
    AGCREF_LEVEL_MINUS85                     = const(0x05)
    AGCREF_LEVEL_MINUS86                     = const(0x06)
    AGCREF_LEVEL_MINUS87                     = const(0x07)
    AGCREF_LEVEL_MINUS88                     = const(0x08)
    AGCREF_LEVEL_MINUS89                     = const(0x09)
    AGCREF_LEVEL_MINUS90                     = const(0x0A)
    AGCREF_LEVEL_MINUS91                     = const(0x0B)
    AGCREF_LEVEL_MINUS92                     = const(0x0C)
    AGCREF_LEVEL_MINUS93                     = const(0x0D)
    AGCREF_LEVEL_MINUS94                     = const(0x0E)
    AGCREF_LEVEL_MINUS95                     = const(0x0F)
    AGCREF_LEVEL_MINUS96                     = const(0x10)
    AGCREF_LEVEL_MINUS97                     = const(0x11)
    AGCREF_LEVEL_MINUS98                     = const(0x12)
    AGCREF_LEVEL_MINUS99                     = const(0x13)
    AGCREF_LEVEL_MINUS100                    = const(0x14)
    AGCREF_LEVEL_MINUS101                    = const(0x15)
    AGCREF_LEVEL_MINUS102                    = const(0x16)
    AGCREF_LEVEL_MINUS103                    = const(0x17)
    AGCREF_LEVEL_MINUS104                    = const(0x18)
    AGCREF_LEVEL_MINUS105                    = const(0x19)
    AGCREF_LEVEL_MINUS106                    = const(0x1A)
    AGCREF_LEVEL_MINUS107                    = const(0x1B)
    AGCREF_LEVEL_MINUS108                    = const(0x1C)
    AGCREF_LEVEL_MINUS109                    = const(0x1D)
    AGCREF_LEVEL_MINUS110                    = const(0x1E)
    AGCREF_LEVEL_MINUS111                    = const(0x1F)
    AGCREF_LEVEL_MINUS112                    = const(0x20)
    AGCREF_LEVEL_MINUS113                    = const(0x21)
    AGCREF_LEVEL_MINUS114                    = const(0x22)
    AGCREF_LEVEL_MINUS115                    = const(0x23)
    AGCREF_LEVEL_MINUS116                    = const(0x24)
    AGCREF_LEVEL_MINUS117                    = const(0x25)
    AGCREF_LEVEL_MINUS118                    = const(0x26)
    AGCREF_LEVEL_MINUS119                    = const(0x27)
    AGCREF_LEVEL_MINUS120                    = const(0x28)
    AGCREF_LEVEL_MINUS121                    = const(0x29)
    AGCREF_LEVEL_MINUS122                    = const(0x2A)
    AGCREF_LEVEL_MINUS123                    = const(0x2B)
    AGCREF_LEVEL_MINUS124                    = const(0x2C)
    AGCREF_LEVEL_MINUS125                    = const(0x2D)
    AGCREF_LEVEL_MINUS126                    = const(0x2E)
    AGCREF_LEVEL_MINUS127                    = const(0x2F)
    AGCREF_LEVEL_MINUS128                    = const(0x30)
    AGCREF_LEVEL_MINUS129                    = const(0x31)
    AGCREF_LEVEL_MINUS130                    = const(0x32)
    AGCREF_LEVEL_MINUS131                    = const(0x33)
    AGCREF_LEVEL_MINUS132                    = const(0x34)
    AGCREF_LEVEL_MINUS133                    = const(0x35)
    AGCREF_LEVEL_MINUS134                    = const(0x36)
    AGCREF_LEVEL_MINUS135                    = const(0x37)
    AGCREF_LEVEL_MINUS136                    = const(0x38)
    AGCREF_LEVEL_MINUS137                    = const(0x39)
    AGCREF_LEVEL_MINUS138                    = const(0x3A)
    AGCREF_LEVEL_MINUS139                    = const(0x3B)
    AGCREF_LEVEL_MINUS140                    = const(0x3C)
    AGCREF_LEVEL_MINUS141                    = const(0x3D)
    AGCREF_LEVEL_MINUS142                    = const(0x3E)
    AGCREF_LEVEL_MINUS143                    = const(0x3F)

    # Reg Agc Thresh 1)
    AGCTHRESH1_SNRMARGIN_000                 = const(0x00)
    AGCTHRESH1_SNRMARGIN_001                 = const(0x20)
    AGCTHRESH1_SNRMARGIN_010                 = const(0x40)
    AGCTHRESH1_SNRMARGIN_011                 = const(0x60)
    AGCTHRESH1_SNRMARGIN_100                 = const(0x80)
    AGCTHRESH1_SNRMARGIN_101                 = const(0xA0) # Default
    AGCTHRESH1_SNRMARGIN_110                 = const(0xC0)
    AGCTHRESH1_SNRMARGIN_111                 = const(0xE0)

    AGCTHRESH1_STEP1_0                       = const(0x00)
    AGCTHRESH1_STEP1_1                       = const(0x01)
    AGCTHRESH1_STEP1_2                       = const(0x02)
    AGCTHRESH1_STEP1_3                       = const(0x03)
    AGCTHRESH1_STEP1_4                       = const(0x04)
    AGCTHRESH1_STEP1_5                       = const(0x05)
    AGCTHRESH1_STEP1_6                       = const(0x06)
    AGCTHRESH1_STEP1_7                       = const(0x07)
    AGCTHRESH1_STEP1_8                       = const(0x08)
    AGCTHRESH1_STEP1_9                       = const(0x09)
    AGCTHRESH1_STEP1_10                      = const(0x0A)
    AGCTHRESH1_STEP1_11                      = const(0x0B)
    AGCTHRESH1_STEP1_12                      = const(0x0C)
    AGCTHRESH1_STEP1_13                      = const(0x0D)
    AGCTHRESH1_STEP1_14                      = const(0x0E)
    AGCTHRESH1_STEP1_15                      = const(0x0F)
    AGCTHRESH1_STEP1_16                      = const(0x10) # Default
    AGCTHRESH1_STEP1_17                      = const(0x11)
    AGCTHRESH1_STEP1_18                      = const(0x12)
    AGCTHRESH1_STEP1_19                      = const(0x13)
    AGCTHRESH1_STEP1_20                      = const(0x14)
    AGCTHRESH1_STEP1_21                      = const(0x15)
    AGCTHRESH1_STEP1_22                      = const(0x16)
    AGCTHRESH1_STEP1_23                      = const(0x17)
    AGCTHRESH1_STEP1_24                      = const(0x18)
    AGCTHRESH1_STEP1_25                      = const(0x19)
    AGCTHRESH1_STEP1_26                      = const(0x1A)
    AGCTHRESH1_STEP1_27                      = const(0x1B)
    AGCTHRESH1_STEP1_28                      = const(0x1C)
    AGCTHRESH1_STEP1_29                      = const(0x1D)
    AGCTHRESH1_STEP1_30                      = const(0x1E)
    AGCTHRESH1_STEP1_31                      = const(0x1F)

    # Reg Agc Thresh 2)
    AGCTHRESH2_STEP2_0                       = const(0x00)
    AGCTHRESH2_STEP2_1                       = const(0x10)
    AGCTHRESH2_STEP2_2                       = const(0x20)
    AGCTHRESH2_STEP2_3                       = const(0x30) # XXX wrong -- Default
    AGCTHRESH2_STEP2_4                       = const(0x40)
    AGCTHRESH2_STEP2_5                       = const(0x50)
    AGCTHRESH2_STEP2_6                       = const(0x60)
    AGCTHRESH2_STEP2_7                       = const(0x70) # Default
    AGCTHRESH2_STEP2_8                       = const(0x80)
    AGCTHRESH2_STEP2_9                       = const(0x90)
    AGCTHRESH2_STEP2_10                      = const(0xA0)
    AGCTHRESH2_STEP2_11                      = const(0xB0)
    AGCTHRESH2_STEP2_12                      = const(0xC0)
    AGCTHRESH2_STEP2_13                      = const(0xD0)
    AGCTHRESH2_STEP2_14                      = const(0xE0)
    AGCTHRESH2_STEP2_15                      = const(0xF0)

    AGCTHRESH2_STEP3_0                       = const(0x00)
    AGCTHRESH2_STEP3_1                       = const(0x01)
    AGCTHRESH2_STEP3_2                       = const(0x02)
    AGCTHRESH2_STEP3_3                       = const(0x03)
    AGCTHRESH2_STEP3_4                       = const(0x04)
    AGCTHRESH2_STEP3_5                       = const(0x05)
    AGCTHRESH2_STEP3_6                       = const(0x06)
    AGCTHRESH2_STEP3_7                       = const(0x07)
    AGCTHRESH2_STEP3_8                       = const(0x08)
    AGCTHRESH2_STEP3_9                       = const(0x09)
    AGCTHRESH2_STEP3_10                      = const(0x0A)
    AGCTHRESH2_STEP3_11                      = const(0x0B) # Default
    AGCTHRESH2_STEP3_12                      = const(0x0C)
    AGCTHRESH2_STEP3_13                      = const(0x0D)
    AGCTHRESH2_STEP3_14                      = const(0x0E)
    AGCTHRESH2_STEP3_15                      = const(0x0F)

    # Reg Agc Thresh 3)
    AGCTHRESH3_STEP4_0                       = const(0x00)
    AGCTHRESH3_STEP4_1                       = const(0x10)
    AGCTHRESH3_STEP4_2                       = const(0x20)
    AGCTHRESH3_STEP4_3                       = const(0x30)
    AGCTHRESH3_STEP4_4                       = const(0x40)
    AGCTHRESH3_STEP4_5                       = const(0x50)
    AGCTHRESH3_STEP4_6                       = const(0x60)
    AGCTHRESH3_STEP4_7                       = const(0x70)
    AGCTHRESH3_STEP4_8                       = const(0x80)
    AGCTHRESH3_STEP4_9                       = const(0x90) # Default
    AGCTHRESH3_STEP4_10                      = const(0xA0)
    AGCTHRESH3_STEP4_11                      = const(0xB0)
    AGCTHRESH3_STEP4_12                      = const(0xC0)
    AGCTHRESH3_STEP4_13                      = const(0xD0)
    AGCTHRESH3_STEP4_14                      = const(0xE0)
    AGCTHRESH3_STEP4_15                      = const(0xF0)

    AGCTHRESH3_STEP5_0                       = const(0x00)
    AGCTHRESH3_STEP5_1                       = const(0x01)
    AGCTHRESH3_STEP5_2                       = const(0x02)
    AGCTHRESH3_STEP5_3                       = const(0x03)
    AGCTHRESH3_STEP5_4                       = const(0x04)
    AGCTHRESH3_STEP5_5                       = const(0x05)
    AGCTHRESH3_STEP5_6                       = const(0x06)
    AGCTHRESH3_STEP5_7                       = const(0x07)
    AGCTHRES33_STEP5_8                       = const(0x08)
    AGCTHRESH3_STEP5_9                       = const(0x09)
    AGCTHRESH3_STEP5_10                      = const(0x0A)
    AGCTHRESH3_STEP5_11                      = const(0x0B) # Default
    AGCTHRESH3_STEP5_12                      = const(0x0C)
    AGCTHRESH3_STEP5_13                      = const(0x0D)
    AGCTHRESH3_STEP5_14                      = const(0x0E)
    AGCTHRESH3_STEP5_15                      = const(0x0F)

    # Reg Lna)
    LNA_ZIN_50                               = const(0x00)
    LNA_ZIN_200                              = const(0x80) # Default

    LNA_LOWPOWER_OFF                         = const(0x00) # Default
    LNA_LOWPOWER_ON                          = const(0x40)

    LNA_CURRENTGAIN                          = const(0x08)

    LNA_GAINSELECT_AUTO                      = const(0x00) # Default
    LNA_GAINSELECT_MAX                       = const(0x01)
    LNA_GAINSELECT_MAXMINUS6                 = const(0x02)
    LNA_GAINSELECT_MAXMINUS12                = const(0x03)
    LNA_GAINSELECT_MAXMINUS24                = const(0x04)
    LNA_GAINSELECT_MAXMINUS36                = const(0x05)
    LNA_GAINSELECT_MAXMINUS48                = const(0x06)

    # Reg Rx Bw)
    RXBW_DCCFREQ_000                         = const(0x00)
    RXBW_DCCFREQ_001                         = const(0x20)
    RXBW_DCCFREQ_010                         = const(0x40) # Default
    RXBW_DCCFREQ_011                         = const(0x60)
    RXBW_DCCFREQ_100                         = const(0x80)
    RXBW_DCCFREQ_101                         = const(0xA0)
    RXBW_DCCFREQ_110                         = const(0xC0)
    RXBW_DCCFREQ_111                         = const(0xE0)

    RXBW_MANT_16                             = const(0x00)
    RXBW_MANT_20                             = const(0x08)
    RXBW_MANT_24                             = const(0x10) # Default

    RXBW_EXP_0                               = const(0x00)
    RXBW_EXP_1                               = const(0x01)
    RXBW_EXP_2                               = const(0x02)
    RXBW_EXP_3                               = const(0x03)
    RXBW_EXP_4                               = const(0x04)
    RXBW_EXP_5                               = const(0x05) # Default
    RXBW_EXP_6                               = const(0x06)
    RXBW_EXP_7                               = const(0x07)

    # Reg Afc Bw)
    AFCBW_DCCFREQAFC_000                     = const(0x00)
    AFCBW_DCCFREQAFC_001                     = const(0x20)
    AFCBW_DCCFREQAFC_010                     = const(0x40)
    AFCBW_DCCFREQAFC_011                     = const(0x60)
    AFCBW_DCCFREQAFC_100                     = const(0x80) # Default
    AFCBW_DCCFREQAFC_101                     = const(0xA0)
    AFCBW_DCCFREQAFC_110                     = const(0xC0)
    AFCBW_DCCFREQAFC_111                     = const(0xE0)

    AFCBW_MANTAFC_16                         = const(0x00)
    AFCBW_MANTAFC_20                         = const(0x08) # Default
    AFCBW_MANTAFC_24                         = const(0x10)

    AFCBW_EXPAFC_0                           = const(0x00)
    AFCBW_EXPAFC_1                           = const(0x01)
    AFCBW_EXPAFC_2                           = const(0x02)
    AFCBW_EXPAFC_3                           = const(0x03) # Default
    AFCBW_EXPAFC_4                           = const(0x04)
    AFCBW_EXPAFC_5                           = const(0x05)
    AFCBW_EXPAFC_6                           = const(0x06)
    AFCBW_EXPAFC_7                           = const(0x07)

    AFCFEI_AFCAUTO_ON                        = const(0x04)
    AFCFEI_AFCAUTO_OFF                       = const(0x00)

    AFCFEI_FEI_DONE                          = const(0x40)
    AFCFEI_FEI_START                         = const(0x20)
    AFCFEI_AFC_DONE                          = const(0x10)
    AFCFEI_AFCAUTOCLEAR_ON                   = const(0x08)
    AFCFEI_AFCAUTOCLEAR_OFF                  = const(0x00)

    # Reg Ook Peak)
    OOKPEAK_THRESHTYPE_FIXED                 = const(0x00)
    OOKPEAK_THRESHTYPE_PEAK                  = const(0x40) # Default
    OOKPEAK_THRESHTYPE_AVERAGE               = const(0x80)

    OOKPEAK_PEAKTHRESHSTEP_000               = const(0x00) # Default
    OOKPEAK_PEAKTHRESHSTEP_001               = const(0x08)
    OOKPEAK_PEAKTHRESHSTEP_010               = const(0x10)
    OOKPEAK_PEAKTHRESHSTEP_011               = const(0x18)
    OOKPEAK_PEAKTHRESHSTEP_100               = const(0x20)
    OOKPEAK_PEAKTHRESHSTEP_101               = const(0x28)
    OOKPEAK_PEAKTHRESHSTEP_110               = const(0x30)
    OOKPEAK_PEAKTHRESHSTEP_111               = const(0x38)

    OOKPEAK_PEAKTHRESHDEC_000                = const(0x00) # Default
    OOKPEAK_PEAKTHRESHDEC_001                = const(0x01)
    OOKPEAK_PEAKTHRESHDEC_010                = const(0x02)
    OOKPEAK_PEAKTHRESHDEC_011                = const(0x03)
    OOKPEAK_PEAKTHRESHDEC_100                = const(0x04)
    OOKPEAK_PEAKTHRESHDEC_101                = const(0x05)
    OOKPEAK_PEAKTHRESHDEC_110                = const(0x06)
    OOKPEAK_PEAKTHRESHDEC_111                = const(0x07)

    # Reg Ook Avg)
    OOKAVG_AVERAGETHRESHFILT_00              = const(0x00)
    OOKAVG_AVERAGETHRESHFILT_01              = const(0x40)
    OOKAVG_AVERAGETHRESHFILT_10              = const(0x80) # Default
    OOKAVG_AVERAGETHRESHFILT_11              = const(0xC0)

    # Reg Ook Fix)
    OOKFIX_FIXEDTHRESH_VALUE                 = const(0x06) # Default

    # Reg Afc Fei)
    AFCFEI_FEI_DONE                          = const(0x40)
    AFCFEI_FEI_START                         = const(0x20)
    AFCFEI_AFC_DONE                          = const(0x10)
    AFCFEI_AFCAUTOCLEAR_ON                   = const(0x08)
    AFCFEI_AFCAUTOCLEAR_OFF                  = const(0x00) # Default

    AFCFEI_AFCAUTO_ON                        = const(0x04)
    AFCFEI_AFCAUTO_OFF                       = const(0x00) # Default

    AFCFEI_AFC_CLEAR                         = const(0x02)
    AFCFEI_AFC_START                         = const(0x01)

    # Reg Rssi Config)
    RSSI_FASTRX_ON                           = const(0x08)
    RSSI_FASTRX_OFF                          = const(0x00) # Default
    RSSI_DONE                                = const(0x02)
    RSSI_START                               = const(0x01)

    # Reg Dio Mapping 1)
    DIOMAPPING1_DIO0_00                      = const(0x00) # Default
    DIOMAPPING1_DIO0_01                      = const(0x40)
    DIOMAPPING1_DIO0_10                      = const(0x80)
    DIOMAPPING1_DIO0_11                      = const(0xC0)

    DIOMAPPING1_DIO1_00                      = const(0x00) # Default
    DIOMAPPING1_DIO1_01                      = const(0x10)
    DIOMAPPING1_DIO1_10                      = const(0x20)
    DIOMAPPING1_DIO1_11                      = const(0x30)

    DIOMAPPING1_DIO2_00                      = const(0x00) # Default
    DIOMAPPING1_DIO2_01                      = const(0x04)
    DIOMAPPING1_DIO2_10                      = const(0x08)
    DIOMAPPING1_DIO2_11                      = const(0x0C)

    DIOMAPPING1_DIO3_00                      = const(0x00) # Default
    DIOMAPPING1_DIO3_01                      = const(0x01)
    DIOMAPPING1_DIO3_10                      = const(0x02)
    DIOMAPPING1_DIO3_11                      = const(0x03)

    # Reg Dio Mapping 2)
    DIOMAPPING2_DIO4_00                      = const(0x00) # Default
    DIOMAPPING2_DIO4_01                      = const(0x40)
    DIOMAPPING2_DIO4_10                      = const(0x80)
    DIOMAPPING2_DIO4_11                      = const(0xC0)

    DIOMAPPING2_DIO5_00                      = const(0x00) # Default
    DIOMAPPING2_DIO5_01                      = const(0x10)
    DIOMAPPING2_DIO5_10                      = const(0x20)
    DIOMAPPING2_DIO5_11                      = const(0x30)

    DIOMAPPING2_CLKOUT_32                    = const(0x00)
    DIOMAPPING2_CLKOUT_16                    = const(0x01)
    DIOMAPPING2_CLKOUT_8                     = const(0x02)
    DIOMAPPING2_CLKOUT_4                     = const(0x03)
    DIOMAPPING2_CLKOUT_2                     = const(0x04)
    DIOMAPPING2_CLKOUT_1                     = const(0x05)
    DIOMAPPING2_CLKOUT_RC                    = const(0x06)
    DIOMAPPING2_CLKOUT_OFF                   = const(0x07) # Default

    # Reg Irq Flags 1)
    IRQFLAGS1_MODEREADY                      = const(0x80)
    IRQFLAGS1_RXREADY                        = const(0x40)
    IRQFLAGS1_TXREADY                        = const(0x20)
    IRQFLAGS1_PLLLOCK                        = const(0x10)
    IRQFLAGS1_RSSI                           = const(0x08)
    IRQFLAGS1_TIMEOUT                        = const(0x04)
    IRQFLAGS1_AUTOMODE                       = const(0x02)
    IRQFLAGS1_SYNCADDRESSMATCH               = const(0x01)

    # Reg Irq Flags 2)
    IRQFLAGS2_FIFOFULL                       = const(0x80)
    IRQFLAGS2_FIFONOTEMPTY                   = const(0x40)
    IRQFLAGS2_FIFOLEVEL                      = const(0x20)
    IRQFLAGS2_FIFOOVERRUN                    = const(0x10)
    IRQFLAGS2_PACKETSENT                     = const(0x08)
    IRQFLAGS2_PAYLOADREADY                   = const(0x04)
    IRQFLAGS2_CRCOK                          = const(0x02)
    IRQFLAGS2_LOWBAT                         = const(0x01)

    # Reg Rssi Thresh)
    RSSITHRESH_VALUE                         = const(0xE4) # Default

    # Reg Rx Timeout 1)
    RXTIMEOUT1_RXSTART_VALUE                 = const(0x00) # Default

    # Reg Rx Timeout 2)
    RXTIMEOUT2_RSSITHRESH_VALUE              = const(0x00) # Default

    # Reg Preamble)
    PREAMBLESIZE_MSB_VALUE                   = const(0x00) # Default
    PREAMBLESIZE_LSB_VALUE                   = const(0x03) # Default

    # Reg Sync Config)
    SYNC_ON                                  = const(0x80) # Default
    SYNC_OFF                                 = const(0x00)

    SYNC_FIFOFILL_AUTO                       = const(0x00) # Default -- when sync interrupt occurs
    SYNC_FIFOFILL_MANUAL                     = const(0x40)

    SYNC_SIZE_1                              = const(0x00)
    SYNC_SIZE_2                              = const(0x08)
    SYNC_SIZE_3                              = const(0x10)
    SYNC_SIZE_4                              = const(0x18) # Default
    SYNC_SIZE_5                              = const(0x20)
    SYNC_SIZE_6                              = const(0x28)
    SYNC_SIZE_7                              = const(0x30)
    SYNC_SIZE_8                              = const(0x38)

    SYNC_TOL_0                               = const(0x00) # Default
    SYNC_TOL_1                               = const(0x01)
    SYNC_TOL_2                               = const(0x02)
    SYNC_TOL_3                               = const(0x03)
    SYNC_TOL_4                               = const(0x04)
    SYNC_TOL_5                               = const(0x05)
    SYNC_TOL_6                               = const(0x06)
    SYNC_TOL_7                               = const(0x07)

    # Reg Sync Value 1-8)
    SYNC_BYTE1_VALUE                         = const(0x00) # Default
    SYNC_BYTE2_VALUE                         = const(0x00) # Default
    SYNC_BYTE3_VALUE                         = const(0x00) # Default
    SYNC_BYTE4_VALUE                         = const(0x00) # Default
    SYNC_BYTE5_VALUE                         = const(0x00) # Default
    SYNC_BYTE6_VALUE                         = const(0x00) # Default
    SYNC_BYTE7_VALUE                         = const(0x00) # Default
    SYNC_BYTE8_VALUE                         = const(0x00) # Default

    # Reg Packet Config 1)
    PACKET1_FORMAT_FIXED                     = const(0x00) # Default
    PACKET1_FORMAT_VARIABLE                  = const(0x80)

    PACKET1_DCFREE_OFF                       = const(0x00) # Default
    PACKET1_DCFREE_MANCHESTER                = const(0x20)
    PACKET1_DCFREE_WHITENING                 = const(0x40)

    PACKET1_CRC_ON                           = const(0x10) # Default
    PACKET1_CRC_OFF                          = const(0x00)

    PACKET1_CRCAUTOCLEAR_ON                  = const(0x00) # Default
    PACKET1_CRCAUTOCLEAR_OFF                 = const(0x08)

    PACKET1_ADRSFILTERING_OFF                = const(0x00) # Default
    PACKET1_ADRSFILTERING_NODE               = const(0x02)
    PACKET1_ADRSFILTERING_NODEBROADCAST      = const(0x04)

    # Reg Payload Length)
    PAYLOADLENGTH_VALUE                      = const(0x40) # Default

    # Reg Broadcast Adrs)
    BROADCASTADDRESS_VALUE                   = const(0x00)

    # Reg Auto Modes)
    AUTOMODES_ENTER_OFF                      = const(0x00) # Default
    AUTOMODES_ENTER_FIFONOTEMPTY             = const(0x20)
    AUTOMODES_ENTER_FIFOLEVEL                = const(0x40)
    AUTOMODES_ENTER_CRCOK                    = const(0x60)
    AUTOMODES_ENTER_PAYLOADREADY             = const(0x80)
    AUTOMODES_ENTER_SYNCADRSMATCH            = const(0xA0)
    AUTOMODES_ENTER_PACKETSENT               = const(0xC0)
    AUTOMODES_ENTER_FIFOEMPTY                = const(0xE0)

    AUTOMODES_EXIT_OFF                       = const(0x00) # Default
    AUTOMODES_EXIT_FIFOEMPTY                 = const(0x04)
    AUTOMODES_EXIT_FIFOLEVEL                 = const(0x08)
    AUTOMODES_EXIT_CRCOK                     = const(0x0C)
    AUTOMODES_EXIT_PAYLOADREADY              = const(0x10)
    AUTOMODES_EXIT_SYNCADRSMATCH             = const(0x14)
    AUTOMODES_EXIT_PACKETSENT                = const(0x18)
    AUTOMODES_EXIT_RXTIMEOUT                 = const(0x1C)

    AUTOMODES_INTERMEDIATE_SLEEP             = const(0x00) # Default
    AUTOMODES_INTERMEDIATE_STANDBY           = const(0x01)
    AUTOMODES_INTERMEDIATE_RECEIVER          = const(0x02)
    AUTOMODES_INTERMEDIATE_TRANSMITTER       = const(0x03)

    #Reg Fifo Thresh)
    FIFOTHRESH_TXSTART_FIFOTHRESH            = const(0x00)
    FIFOTHRESH_TXSTART_FIFONOTEMPTY          = const(0x80) # Default

    FIFOTHRESH_VALUE                         = const(0x0F) # Default

    # Reg Packet Config 2)
    PACKET2_RXRESTARTDELAY_1BIT              = const(0x00) # Default
    PACKET2_RXRESTARTDELAY_2BITS             = const(0x10)
    PACKET2_RXRESTARTDELAY_4BITS             = const(0x20)
    PACKET2_RXRESTARTDELAY_8BITS             = const(0x30)
    PACKET2_RXRESTARTDELAY_16BITS            = const(0x40)
    PACKET2_RXRESTARTDELAY_32BITS            = const(0x50)
    PACKET2_RXRESTARTDELAY_64BITS            = const(0x60)
    PACKET2_RXRESTARTDELAY_128BITS           = const(0x70)
    PACKET2_RXRESTARTDELAY_256BITS           = const(0x80)
    PACKET2_RXRESTARTDELAY_512BITS           = const(0x90)
    PACKET2_RXRESTARTDELAY_1024BITS          = const(0xA0)
    PACKET2_RXRESTARTDELAY_2048BITS          = const(0xB0)
    PACKET2_RXRESTARTDELAY_NONE              = const(0xC0)
    PACKET2_RXRESTART                        = const(0x04)

    PACKET2_AUTORXRESTART_ON                 = const(0x02) # Default
    PACKET2_AUTORXRESTART_OFF                = const(0x00)

    PACKET2_AES_ON                           = const(0x01)
    PACKET2_AES_OFF                          = const(0x00) # Default

    # Reg Aes Key 1-16)
    AESKEY1_VALUE                            = const(0x00) # Default
    AESKEY2_VALUE                            = const(0x00) # Default
    AESKEY3_VALUE                            = const(0x00) # Default
    AESKEY4_VALUE                            = const(0x00) # Default
    AESKEY5_VALUE                            = const(0x00) # Default
    AESKEY6_VALUE                            = const(0x00) # Default
    AESKEY7_VALUE                            = const(0x00) # Default
    AESKEY8_VALUE                            = const(0x00) # Default
    AESKEY9_VALUE                            = const(0x00) # Default
    AESKEY10_VALUE                           = const(0x00) # Default
    AESKEY11_VALUE                           = const(0x00) # Default
    AESKEY12_VALUE                           = const(0x00) # Default
    AESKEY13_VALUE                           = const(0x00) # Default
    AESKEY14_VALUE                           = const(0x00) # Default
    AESKEY15_VALUE                           = const(0x00) # Default
    AESKEY16_VALUE                           = const(0x00) # Default

    # Reg Temp 1)
    TEMP1_MEAS_START                         = const(0x08)
    TEMP1_MEAS_RUNNING                       = const(0x04)
    TEMP1_ADCLOWPOWER_ON                     = const(0x01) # Default
    TEMP1_ADCLOWPOWER_OFF                    = const(0x00)

    # Reg Test Dagc                             = const(0x6F : demodulator config and IO mode config
    DAGC_NORMAL                              = const(0x00) # Reset value
    DAGC_IMPROVED_LOWBETA1                   = const(0x20) #
    DAGC_IMPROVED_LOWBETA0                   = const(0x30) # Recommended default
