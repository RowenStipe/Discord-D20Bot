""" Discord D20Bot  
    Copyright (C) 2016  RowenStipe

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import random

class sdmsg:
    def __init__(self, dice2r, modval, pmsg):
        self.d2r = dice2r
        self.mod = modval
        self.pmsg = pmsg

    def __iter__(self):
        return iter(self.d2r)
        
class rolld_d:
    def __init__(self, rolled, rollednum):
        self.rd = rolled
        self.rn = rollednum

    def __iter__(self):
        return iter(self.rn)


class calctotal:
    def __init__(self, calct):
        self.ct = calct

    def __iter__(self):
        return self


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def sortmsg(message : list):
    #Split dice into list
    dice2roll = message[0].split('+')
    modvl = [] #Create blank list
    prm = ''
    #Figure out if Mod is given and sort from player message
    if len(message) > 1:
        if is_number(message[1]) == True:
            modvl.extend(message[1])
            prm = ' '.join(message[2:])
        else:
            if "+" in message[1]:
                modvl.extend(message[1].split('+'))
                prm = ' '.join(message[2:])
            else:
                prm = ' '.join(message[1:])
            

    #Sort out numbers from dice list
    i = 0
    while (i < len(dice2roll)):
        if is_number(dice2roll[i]) == True:
            modvl.append(dice2roll[i])
            print('{0} | Added to modval list'.format(dice2roll[i]))
            del dice2roll[i]
        i = i + 1
    
    rsdm = sdmsg(dice2roll, modvl, prm)

    return rsdm


def dice( rdl : list):
    print('Rolling ...')
    rollt = 0
    maxn = 0
    
    di = 0

    results = []
    rnumbers = []

    while (di < len(rdl)):
        try:
            rollt, maxn = map(int, rdl[di].split('d')) # Decide what and how many times to roll

        except ValueError:
            pass
        dicer = [rdl[di]]
        try:
            valueerror = []
            if rollt > 255:
                valueerror.append('Too many Dice')
                raise ValueError('Too many dice')
            if maxn > 10000:
                valueerror.append('Too high of dice')
                raise ValueError('To high of dice')
        except ValueError:
            dicer.append(valueerror)
        else:
            try:
                i = 0
                while (i < rollt):
                    rng = random.randint(1, maxn)
                    dicer.append(rng)
                    rnumbers.append(rng)
                    i = i + 1
            except ValueError:
                pass
        finally:
            results.append(dicer)
            print(results)
            di = di + 1

    rrd = rolld_d(results, rnumbers)

    print('Rolled')

    return rrd


def calc(lotc: list, lomc: list):
    lotc = list(map(int, lotc))
    lomc = list(map(int, lomc))
    print('List of rolled numbers: {0}'.format(lotc))
    print('List of mod numbers: {0}' .format(lomc))
    rdt = sum(lotc)
    tmg = sum(lomc)

    total_rolled = calctotal(rdt + tmg)

    return total_rolled
