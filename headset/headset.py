#Headset.py
#
# Author: Josiah Lam
# Email: j23lam@uwaterloo.ca
# Student ID: 21026577
#
# Source code for the Headset class

#--------------------------------- MY CODE --------------------------------
#import libraries
import numpy as np
from scipy.integrate import quad
import pandas as pd
import sys
import matplotlib.pyplot as plt


        
class Headset:
    '''
    Headset
    Author: Josiah Lam
    
    class representing a headset, its functions, model name, price, battery_life_hours and an optional parameter for wire or wireless headsets 
    '''
    def __init__(self, brand:str , model:str , price:float , battery_life_hours:int , wireless = False):
        '''
        Constructor
        brand: string representing the brand of the headset
        model: string representing the model of the headset
        price: float representing the price fo the headset
        battery_life_hours: interger representing the battery_life_hours of the headset
        wireless: boolean representing wire headset as (False) or wireless headset as (True)
        '''    
        #parameter
        
        
        #brand
        #TypeError checking for brand
        if type(brand) != str:
            raise TypeError("Please enter string for brand variable")
        
        #ValueError checking for brand
        elif brand == "":
            raise ValueError("Please enter a appropriate string for brand variable")
        
        #if condition passes, add variable
        else:
            self._brand = brand
        
        
        #model
        #TypeError checking for model
        if type(model) != str:
            raise TypeError("Please enter string for model variable")

        #ValueError checking for brand
        elif model == "":
            raise ValueError("Please enter a appropriate string for model variable")
        
        #if condition passes, add variable
        else:
            self._model = model
            
        #price
        #TypeError checking for price
        if type(price) != float:
            raise TypeError("Please enter float for price variable")
        
        #ValueError checking for price
        elif price < 0:
            raise ValueError("Please enter price greater than 0")
        
        #if condition passes, add variable
        else:        
            self._price = price
            
        #battery_life_hours
        #TypeError checking for battery_life_hours
        if type(battery_life_hours) != int:
            raise TypeError("Please enter float for battery_life_hours variable")
        
        #ValueError checking for batter_life_hours
        elif battery_life_hours < 0:
            raise ValueError("Please enter battery_life_hours greater than 0")
        
        #if condition passes, add variable
        else:
            self._battery_life_hours = battery_life_hours
            
        #wireless
        #TypeError checking for wireless
        if type(wireless) != bool:
            raise TypeError("Please enter a boolean for wireless")
        
        else: 
            self._wireless = wireless 


        #sound control parameter
        self._sound_control = ['noise_cancelling','ambient_sound','off'] #a list that stores sound control options
        self._noise_cancelling = False #default parameter shows noise cancelling is off(False) / on(True)
        self._ambient_sound = False #default parameter shows ambient is off(False) / on(True)

        #hardware  paramter
        self._power_status = False #default power status of the headset, off(False) / on(True)
        self._battery_level = 100 #default battery level status of the headset 
        self._volumn = 50 #the default volumn of the headset 
        self._playing = False #the default setting play or pause of the headset
        
        #music paramter
        self._queue = [] #stores the song
        self._library = {} #storing playlist #artist name(key) #list of strings
        self._current_song = ""
        self._current_song_index = 0
        self._current_sound_control = "off"
        
                
#==========================================================================
#Accessor methods: Basic

    def getName(self):
        '''
        getName()

        Accessor method for the name: in brand and the model of the headset
        '''
        return self._brand + " " + self._model
    
    def getPrice(self):
        '''
        getPrice()

        Accessor method for the price of the headset
        '''
        return self._price

    def getBattery_life_hour(self):
        '''
        get_battery_life_hour()

        Accessor method for the Batterylife of the headset
        '''
        return self._battery_life_hours

    def getWireless(self):
        '''
        getWireless()

        Accessor method for the Wire or Wireless headset
        '''
        return self._wireless

#--------------------------------------------------------------------------
#Accessor methods: Sound Control Options
    
    def getSoundControl(self):
        '''
        getSoundControl()

        Accessor method for the Sound Control option of the headset
        '''
        return self._current_sound_control

    def getNoiseCancelling(self):
        '''
        getNoiseCancelling()

        Accessor method for the NoiseCancelling status
        '''
        return self._noise_cancelling

    def getAmbientSound(self):
        '''
        getAmbientSound()

        Accessor method for the Ambient Sound status
        '''
        return self._ambient_sound

#--------------------------------------------------------------------------
#Accessor methods: Power, Charge, Battery level

    def getPowerStatus(self):
        '''
        getPowerStatus()

        Accessor method for the Power status of the headset
        '''
        return self._power_status 


    def getBatteryLevel(self):
        '''
        getBatteryLevel()

        Accessor method for the Battery level of the headset
        '''
        return self._battery_level
    
#--------------------------------------------------------------------------
#Accessor methods: feature

    def getVolumn(self):
        '''
        getVolumn()

        Accessor method for the volumn of the headset
        '''
        return self._volumn


    def getPlaying(self):
        '''
        getPlaying()

        Accessor method for the playing status of the headset
        '''
        return self._playing
        
    def getQueue(self):
        '''
        getQuese()

        Accessor method for the queus of playlist store in playlist
        '''
        return self._queue
    
    def getLibrary(self):
        '''
        getLibrary()

        Accessor method for library
        '''
        return self._library
    
#==========================================================================
#new parm

    def getCurrent_song(self):
        '''
        getCurrent_song()

        Accessor method for current song
        '''
        return self._current_song
    
    def _getLibrary_Values(self):
        '''
        _getLibrary_Values()
        
        Accessor method for Library Values which are the songs
        '''
        store = []
        for ele in list(self._library.values()):
            for elee in ele:
                store.append(elee)
        
        return store
    

#==========================================================================
#Mutator methods: Basic

    def set_name(self, brand:str, model:str):
        '''
        set_name()
        changes the name of the headset

        name the new name as a string
        
        return true if the name is changed, false otherwise 
        '''
        #TypeError checking
        if type(brand) != str and type(model) != str:
            raise TypeError("Please enter a str type for brand or model")
        
        elif  type(brand) == str and type(model) == str:
            #update parmeters
            self._brand = brand
            self._model = model
            return True

    def set_price(self, price:float):
        '''
        set_price()
        changes the price of the headset

        price the new price as a float
        
        return true if the price is changed, false otherwise 
        '''
        #ValueError checking
        #TypeError checking
        # try: 
        #     price = float(price)
            
        # except TypeError as err:
        #         raise {err}("Please enter a float type for price")
        
        if type(price) != float:
            raise TypeError("Please enter a float type for price")
        #ValueError checking
        elif price < 0: 
            raise ValueError("Please enter a price greater than zero")
        
        #update parmeter
        else:
            self._price = price
            return True

    def set_battery_life_hour(self, battery_life_hours:int):
        '''
        set_battery_life_hour()
        changes the Batterylife of the headset

        batterylife the new batterylife as a interger
        
        return true if the batterylife is changed, false otherwise 
        '''
        #TypeError checking
        if type(battery_life_hours) != int:
            raise TypeError("Please enter a integer type for battery_life_hours")

        elif battery_life_hours < 0:
            raise ValueError("Please enter a battery_life_hour greater than zero")
        # try:
        #     battery_life_hours = int(battery_life_hours)
            
        # except TypeError as err:
        #     raise{err}("Please enter a integer type for battery_life_hours")
        
        # #ValueError checking
        # # elif battery_life_hours <= 0:
        # except ValueError as err:
        #     raise {err}("Please enter a battery_life_hour greater than zero")
        
        else:
            #updates parmeter
            self._battery_life_hours = battery_life_hours
            return True

    def set_volumn(self, level:int):
        '''
        set_volumn()
        changes the volumn of the headset

        volumn the new volumn as a integer
        
        return true if the volumn is changed, false otherwise 
        '''
        #TypeError checking
        if type(level) != int:
            raise TypeError("Please enter a integer type for volumn level")
        
        #ValueError checking
        if level < 0 or level > 101:
            return False

        #update parmeter
        else:
            self._volumn = level
            return True

#==========================================================================
#Mutator methods:library

    def set_library(self, new_library:dict):
        '''
        set_library()
        updates the library of the headset
        
        library the new library as a dictionary
        
        key: Artist name in (str)
        value: Songs in (list) of (str)s
        
        return true if the library is updated, false otherwise 
        '''
        #Open list of new library items
        
        
        # try:
        #     new_library = dict(new_library)
        
        # except TypeError as err:
        #     raise {err}("Please Enter a dict type in 'new_library'")
        if type(new_library) != dict:
            raise TypeError("Please enter a dict type with key as (str) and value as (list of str)")
        for k, v in new_library.items():
            
            #if Artist(k) not in library, append Artist(k) and list of songs(v) to self._library
            if k not in self._library:
                self._library[k] = v
            
            #if Artist(k) already stored in library, append the new list of songs(v) to self._library
            elif k in self._library:
                for ele in new_library[k]:
                    self._library[k].append(ele)
        
        #returns True when operation completed
        return True

    def remove_all_library(self):
        '''
        remove_all_library()
        removes all song from the library of the headset

        remove all song from the library
        
        return true if the library is changed, false otherwise 
        '''
        #clears self._library dictionary
        self._library.clear()
        #returns True when operation completed
        return True

    def remove_library(self, remove_library:dict):
        '''
        remove_library()
        changes the library of the headset

        library the new library as a dictionary
        
        return true if the library is changed, false otherwise 
        '''
        if type(remove_library) != dict:
            raise(TypeError, "Please Enter a dict type in 'new_library'")
        
        elif type(remove_library) == dict:
            for k, v in remove_library.items():
                #if Artist(k) not in self._library, return False
                if k not in self._library.keys() or k == "" :
                    return False
                
                #if the list of song(v) or an empty list not in self._library, return False
                elif v == self._getLibrary_Values() or v == []:
                    return False

                #if Artist(k) in self._library, remove list of songs(v) from self._library
                elif k or v in self._library:
                    for ele in remove_library[k]:
                        self._library[k].remove(ele)
                        
                    #if there is no songs left under the Artist, remove Artist from self._library
                    if self._library[k] == []:
                        self._library.pop(k)
                                                
                                                
            #returns True when operation completed
            return True
        
#==========================================================================
#Mutator methods:queue

    def set_queue(self):
        '''
        set_queue()
        changes the queue of the headset

        queue the new que as a list
        
        imports all songs from playlist and insert into the queue
        
        return true if the queue is changed, false otherwise 
        '''
        #getting all song names from Library
        for ele in self._library.values():
            for elee in ele:
                if elee not in self._queue:
                    self._queue.append(elee)
                    
                elif elee in self._queue:
                    continue
                
        return True
    
    def remove_all_queue(self):
        '''
        remove_all_queue()
        removes all song from the queue of the headset

        remove all song from the queue
        
        return true if the queue is changed, false otherwise 
        '''
        #clears self._queue list
        self._queue.clear()
        #returns True when operation completed
        return True
    
    def remove_queue(self, remove_queue):
        '''
        remove_queue()
        changes the queue of the headset

        queue the new queue as a dictionary
        
        return true if the queue is changed, false otherwise 
        '''
        for ele in remove_queue:
            self._queue.remove(ele)

        return True

#==========================================================================
#Mutator methods:features 
        
    def power_on(self):
        ''' 
        Power_on()
        Turns on power of the headset

        return true if power is on, false otherwise
        '''
        self._power_status = True
        return True

    def power_off(self):
        ''' 
        Power_off()
        Pause queue
        Turns off power of the headset 

        return true if power is off, false otherwise
        '''
        #pause queue
        self._playing = False
        
        #Turn off noise cancelling
        self._noise_cancelling = False
        
        #Turn off ambient sound
        self._ambient_sound = False
        
        #set sound control to 'off'
        self._current_sound_control = self._sound_control[2]
        
        #Turn off headset
        self._power_status = False
        return True

    def play(self):
        '''
        _Play()
        Plays que

        return true if playing, false otherwise
        '''
        #check if headset is on        
        if self._power_status == True:
            
            #update queue song
            self.set_queue() #make sure there are songs in queue
            self._current_song = self._queue[self._current_song_index] #playing the first song in 
            
            #update playing to True
            self._playing = True
            
        else:
            return False
            
        return True

    def pause(self):
        '''
        _Pause()
        Pause que

        return true if paused, false otherwise
        '''
        #pause the queue
        self._playing = False
        return True

    def skip(self):
        '''
        skip()
        skip the queue

        retrun true if skipped, false otherwise
        '''
        #check if headset is turned on and playing
        if self._power_status == True and self._playing == True:
            #
            self._current_song = self._queue[self._current_song_index + 1]
            return True
        
        else: 
            return False

    def previous(self):
        ''' 
        previous()
        goes back to the previous song on the queue

        return true if goes back previous song on the queue
        '''
        #check if headset is turned on and playing
        if self._power_status == True and self._playing == True:
            
            #check if the queue is playing the first song
            if self._current_song_index != 0: 
                self._current_song = self._queue[self._current_song_index - 1]
                return True
               
            #play the song at the end of the queue if self._current_song_index is at 0  
            elif self._current_song_index == 0:
                self._current_song = self._queue[-1]
                return True
            
            else: 
                return False

        else: 
            return False


#==========================================================================
#Mutator methods: Sound Control

    def noise_cancelling_on(self):
        ''' 
        NoiseCancelling_on()
        Turns on Noise Cancelling of the headset

        return true if Noise Cancelling is on, false otherwise
        '''
        #set self._current_sond_control to "noice_cancelling"
        self._current_sound_control = self._sound_control[0]
        #update self._noise_cancelling
        self._noise_cancelling = True
        return True


    def noise_cancelling_off(self):
        ''' 
        NoiseCancelling_off()
        Turns off Noise Cancelling of the headset

        return true if Noise Cancelling is off, false otherwise
        '''
        #set self._current_sond_control to "off"
        self._current_sound_control = self._sound_control[2]
        #update self._noise_cancelling
        self._noise_cancelling = False
        return True

    
    def ambient_sound_on(self):
        ''' 
        ambientSound_on()
        Turns on Noise Cancelling of the headset

        return true if Noise Cancelling is on, false otherwise
        '''
        #set self._current_sond_control to "ambient_sound"
        self._current_sound_control = self._sound_control[2]
        #update self._ambient_sond
        self._ambient_sound = True
        return True


    def ambient_sound_off(self):
        ''' 
        ambientSound_off()
        Turns off Noise Cancelling of the headset

        return true if Noise Cancelling is off, false otherwise
        '''
        #set self._current_sond_control to "off"
        self._current_sound_control = self._sound_control[0]
        #update self._ambient_sond
        self._ambient_sound = False
        return True
    

    def sound_control_off(self):
        ''' 
        SoundControl_off(self)
        Turns off Noise Cancelling or Ambient Sound of the headset

        return true if Noise Cancelling or Ambient Sound is off, false otherwise
        '''
        #set self._current_sond_control to "off"
        self._current_sound_control = self._sound_control[2]
        return True
    

#==========================================================================
#Mutator methods: calculation 

    def optimizer(self, f):
        '''
        Optimizer()
        detects frequency outside the headset and optmize noise cancelling inside the headset

        f for frequency in Hz
        
        return true if Optimizer completed, false otherwise     
        '''
        if type(f) != int:
            raise TypeError("Please enter an integer for f")
        
        elif f < 20 or f > 20000 :
            raise ValueError("Please enter an integer between 20 to 20000 for f")
        
        else:
            # x(t) is the input function: x for singal represents a sound wave, the unit in pressure units such as pascals (Pa) or decibels (dB)
            # f is the frequency to calculate the Fourier Transform
            # t for time in seconds
            def x(t):
                return t if t >= 0 else 0
 
            # intergral formula with Fourier Transform
            def integrand(t):
                return x(t) * np.exp(-2j * np.pi * f * t)

            # using scipy quad to intergral from negative infinity to postive infinity
            result, _ = quad(integrand, -np.inf, np.inf)
            return int(result)
        
    
    def __sizeof__(self):
        return sys.getsizeof(self._brand) + sys.getsizeof(self._model) + sys.getsizeof(self._price) + sys.getsizeof(self._battery_life_hours) + sys.getsizeof(self._wireless) + sys.getsizeof(self._sound_control) + sys.getsizeof(self._noise_cancelling) + sys.getsizeof(self._ambient_sound) + sys.getsizeof(self._power_status) + sys.getsizeof(self._battery_level) + sys.getsizeof(self._volumn) + sys.getsizeof(self._playing) + sys.getsizeof(self._queue) + sys.getsizeof(self._library) + sys.getsizeof(self._current_song) + sys.getsizeof(self._current_song_index) + sys.getsizeof(self._current_sound_control)
    
    #strings
    #dictionary
    #list
    #int
    #float
        
#==========================================================================

if __name__ == "__main__":
    #set default variables
    brand_str = "Appleeeeeeeeeeeeeeeeeeeeeee" 
    model_str = "AirPod MAX"
    price_float = 3000.0
    battery_life_hour_int = 3000
    
    #create a class instance
    #test str
    str_mstore = []
    str_count = 0
    str_store_count = []
    for i in range(30):
        #create a class instance
        str_memory_headset = Headset(brand_str, model_str, price_float, battery_life_hour_int)
        #update count str
        str_count += len(brand_str)
        #append str_count to a list
        str_store_count.append(str_count)
        #append memory to list
        str_mstore.append((sys.getsizeof(str_memory_headset)))
        #add strings to the orginal 
        brand_str += brand_str
    

    #test float
    float_mstore = []
    float_count = 0
    float_store_count = []
    for i in range(30):
        #create a class instance
        float_memory_headset = Headset(brand_str, model_str, price_float, battery_life_hour_int)
        #update count float
        float_count += 10000.0
        #append float_count to a list
        float_store_count.append(float_count)
        #append memory to list
        float_mstore.append((sys.getsizeof(float_memory_headset)))
        #add floatation values to the orginal 
        price_float += 10000 #price_float


    #test int
    int_mstore = []
    int_count = 0
    int_store_count = []
    for i in range(30):
        #create a class instance
        int_memory_headset = Headset(brand_str, model_str, price_float, battery_life_hour_int)
        #update count int
        int_count += 10000
        #append int_count to a list
        int_store_count.append(int_count)
        #append memory to list
        int_mstore.append((sys.getsizeof(int_memory_headset)))
        #add interger values to the orginal 
        battery_life_hour_int += 10000 #battery_life_hour_int 

    #create a dictionary to store items
    data = {
    'Size of String': str_store_count,
    'String Memory': str_mstore,
    'Size of Float' : float_store_count,
    'Float Memory' : float_mstore,
    'Size of Interger': int_store_count,
    'Int Memory': int_mstore
    }

    # Create a DataFrame from the dictionary
    df = pd.DataFrame(data)
    print(df)
    
    
    # Create a plot for 'Size of String' vs. 'String Memory'
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Size of String'], df['String Memory'])
    plt.title('Size of String vs. String Memory')
    plt.xlabel('Size of String')
    plt.ylabel('String Memory')
    plt.grid(True)
    plt.show()

    # # Create a plot for 'Size of Float' vs. 'Float Memory'
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Size of Float'], df['Float Memory'])
    plt.title('Size of Float vs. Float Memory')
    plt.xlabel('Size of Float')
    plt.ylabel('Float Memory')
    plt.grid(True)
    plt.show()

    # # Create a plot for 'Size of Integer' vs. 'Int Memory'
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Size of Interger'], df['Int Memory'])
    plt.title('Size of Integer vs. Int Memory')
    plt.xlabel('Size of Integer')
    plt.ylabel('Int Memory')
    plt.grid(True)
    plt.show()

# graph axis
# y momoery
# x int or float or list or str or dict

