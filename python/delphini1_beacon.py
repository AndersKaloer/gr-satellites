#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2016 Daniel Estevez <daniel@destevez.net>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#

import struct
from datetime import datetime

class beacon_1_0(object):
    def __init__(self, payload):
        if payload[0] != 0 or len(payload) != 88:
            raise ValueError("Malformed beacon of type 1 0")
        
        data = payload[1:-4]
        print(len(data))
        eps, com, obc = struct.unpack("49s14s20s", data)

        self.eps_timestamp, \
        self.eps_vboost_0, \
        self.eps_vboost_1, \
        self.eps_vboost_2, \
        self.eps_vbatt, \
        self.eps_curout_0, \
        self.eps_curout_1, \
        self.eps_curout_2, \
        self.eps_curout_3, \
        self.eps_curout_4, \
        self.eps_curout_5, \
        self.eps_curout_6, \
        self.eps_curin_0, \
        self.eps_curin_1, \
        self.eps_curin_2, \
        self.eps_cursun, \
        self.eps_cursys, \
        self.eps_temp_0, \
        self.eps_temp_1, \
        self.eps_temp_2, \
        self.eps_temp_3, \
        self.eps_temp_4, \
        self.eps_temp_5, \
        self.eps_battmode \
        = struct.unpack('>I16H6hB', eps)

        self.eps_timestamp = datetime.utcfromtimestamp(self.eps_timestamp)
        self.eps_vboost_0 = self.eps_vboost_0 / 1000.0
        self.eps_vboost_1 = self.eps_vboost_1 / 1000.0
        self.eps_vboost_2 = self.eps_vboost_2 / 1000.0
        self.eps_vbatt = self.eps_vbatt / 1000.0
        

        self.com_timestamp, \
        self.com_temp_brd, \
        self.com_temp_pa, \
        self.com_last_rssi, \
        self.com_last_rferr, \
        self.com_bgnd_rssi \
        = struct.unpack('>I5h', com)

        self.com_timestamp = datetime.utcfromtimestamp(self.com_timestamp)
        self.com_temp_brd = self.com_temp_brd / 10.0
        self.com_temp_pa = self.com_temp_pa / 10.0

        self.obc_timestamp, \
        self.obc_cur_gssb1, \
        self.obc_cur_gssb2, \
        self.obc_cur_flash, \
        self.obc_cur_pwm, \
        self.obc_cur_gps, \
        self.obc_cur_wde, \
        self.obc_temp_a, \
        self.obc_temp_b \
        = struct.unpack('>I6H2h', obc)

        self.obc_timestamp = datetime.utcfromtimestamp(self.obc_timestamp)
        self.obc_temp_a = self.obc_temp_a / 10.0
        self.obc_temp_b = self.obc_temp_b / 10.0

    def __str__(self):
        return ("""Beacon type 1 0:
    EPS:
        Timestamp:\t\t\t{}
        Boost converter voltage:\t{}V, {}V, {}V
        Battery voltage:\t\t{}V
        Out current:\t\t\t{}mA, {}mA, {}mA, {}mA, {}mA, {}mA, {}mA
        In current:\t\t\t{}mA, {}mA, {}mA
        Sun current:\t\t\t{}mA
        System current:\t\t\t{}mA
        Temperature:\t\t\t{}ºC, {}ºC, {}ºC, {}ºC, {}ºC, {}ºC
        Battery mode:\t\t\t{}
    COM:
        Timestamp:\t\t{}
        Board temperature:\t{}ºC
        PA temperature:\t\t{}ºC
        Last RSSI:\t\t{}dB
        Last rferr:\t\t{}
        Background RSSI:\t{}dB
    OBC:
        Timestamp:\t{}
        GSSb1 current:\t{}mA
        GSSb2 current:\t{}mA
        Flash current:\t{}mA
        PWM current:\t{}mA
        GPS current:\t{}mA
        WDE current:\t{}mA
        Temperature A:\t{}ºC
        Temperature B:\t{}ºC""".format(
            self.eps_timestamp, \
            self.eps_vboost_0, \
            self.eps_vboost_1, \
            self.eps_vboost_2, \
            self.eps_vbatt, \
            self.eps_curout_0, \
            self.eps_curout_1, \
            self.eps_curout_2, \
            self.eps_curout_3, \
            self.eps_curout_4, \
            self.eps_curout_5, \
            self.eps_curout_6, \
            self.eps_curin_0, \
            self.eps_curin_1, \
            self.eps_curin_2, \
            self.eps_cursun, \
            self.eps_cursys, \
            self.eps_temp_0, \
            self.eps_temp_1, \
            self.eps_temp_2, \
            self.eps_temp_3, \
            self.eps_temp_4, \
            self.eps_temp_5, \
            self.eps_battmode, \
            self.com_timestamp, \
            self.com_temp_brd, \
            self.com_temp_pa, \
            self.com_last_rssi, \
            self.com_last_rferr, \
            self.com_bgnd_rssi, \
            self.obc_timestamp, \
            self.obc_cur_gssb1, \
            self.obc_cur_gssb2, \
            self.obc_cur_flash, \
            self.obc_cur_pwm, \
            self.obc_cur_gps, \
            self.obc_cur_wde, \
            self.obc_temp_a, \
            self.obc_temp_b))
        
