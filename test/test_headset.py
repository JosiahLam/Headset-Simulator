# test_Headset
#
# Author: Josiah Lam
# Email: j23lam@uwaterloo.ca
# Student ID: 21026577
#
# these are the unit tests for Headset class

from headset.headset import Headset
import unittest
 
# Create Headset instance
templete_headset = Headset("Apple", "AirPod Pro MAX", 999.0, 10000)
wireless_templete_headset = Headset("BOSE", "A30", 2999.0, 10000, True)

class TestHeadset(unittest.TestCase):

#self.assertEqual(templete_headset.


#Constructor


    def test_contructor_typical1(self):
        """
        Input: "Apple" "AirPod Pro MAX" with a price of $2499.0, 5000 battery life hour
        Expected output: instance of a APPLE with all variables above 
        """

        # Create Headset instance
        wire_APPLE = Headset("Apple", "AirPod Pro MAX", 2499.0, 5000)

        # Check post conditions
        self.assertEqual(wire_APPLE.getName(), "Apple AirPod Pro MAX")
        self.assertEqual(wire_APPLE.getPrice(), 2499.0)
        self.assertEqual(wire_APPLE.getBattery_life_hour(), 5000)
        self.assertEqual(wire_APPLE.getWireless(), False)

    
    def test_contructor_typical2(self):
        """
        Input: "SONY" "XM5" with a price of $300.0, 6000 battery life hour
        Expected output: instance of a SONY with all variables above 
        """

        # Create Headset instance 
        wire_SONY = Headset("SONY", "XM5", 300.0, 6000)

        # Check post conditions
        self.assertEqual(wire_SONY.getName(), "SONY XM5")
        self.assertEqual(wire_SONY.getPrice(), 300.0)
        self.assertEqual(wire_SONY.getBattery_life_hour(), 6000)
        self.assertEqual(wire_SONY.getWireless(), False)


    def test_contructor2_typical1(self):
        """
        Input: "Crusher" "ANC" with a price of $72514.0, 10000 battery life hour and wireless
        Expected output: instance of a Crusher with all variables above 
        """

        # Create Headset instance 
        wireless_Crusher = Headset("Crusher", "ANC", 72514.0, 10000, True)

        # Check post conditions
        self.assertEqual(wireless_Crusher.getName(), "Crusher ANC")
        self.assertEqual(wireless_Crusher.getPrice(), 72514.0)
        self.assertEqual(wireless_Crusher.getBattery_life_hour(), 10000)
        self.assertEqual(wireless_Crusher.getWireless(), True)


    def test_contructor2_typical2(self):
        """
        Input: "BOSE" "A30" with a price of $2999.0, 6000 battery life hour and wireless
        Expected output: instance of a BOSE with all variables above 
        """

        # Create Headset instance 
        wireless_BOSE = Headset("BOSE", "A30", 2999.0, 10000, True)

        # Check post conditions
        self.assertEqual(wireless_BOSE.getName(), "BOSE A30")
        self.assertEqual(wireless_BOSE.getPrice(), 2999.0)
        self.assertEqual(wireless_BOSE.getBattery_life_hour(), 10000)
        self.assertEqual(wireless_BOSE.getWireless(), True)


    def test_constructor_unusual1(self):
        """
        Input: "Apple" + "Pro" with a price of $3499.0, 1,000,000,000 battery life hour and
        Expected output: instance of a Apple with all variables above 
        """

        # Create Headset instance 
        negative_batterylifehour_headset = Headset("Apple", "Pro", 3499.0, 1000000000)

        # Check post conditions
        self.assertEqual(negative_batterylifehour_headset.getName(), "Apple Pro")
        self.assertEqual(negative_batterylifehour_headset.getPrice(), 3499.0)
        self.assertEqual(negative_batterylifehour_headset.getBattery_life_hour(), 1000000000)


    def test_constructor_unusual2(self):
        """
        Input: empty string with a 0.0 dollar price, 6000 battery life hour and
        Expected output: instance of a Apple with all variables above 
        """

        # Create Headset instance 
        zero_dollar_price_headset = Headset("_______________", "---", 0.0, 6000)

        # Check post conditions
        self.assertEqual(zero_dollar_price_headset.getName(), "_______________" + " " + "---")
        self.assertEqual(zero_dollar_price_headset.getPrice(), 0.0)
        self.assertEqual(zero_dollar_price_headset.getBattery_life_hour(), 6000)
    

    def test_constructor_error1(self):
        """
        Input: Invalid product price (negative)
        Expected output: An error should occur when trying to create the Headset
        """
        # Attempt to create Headset with negative product price
        with self.assertRaises(ValueError):
            #create headset instance
            negative_price_headset = Headset("Apple", "Pro", -3000.0, 6000)


    def test_constructor_error2(self):
        """
        Input: Invalid brand & model name (type)
        Expected output: An error should occur when trying to create the Headset
        """
        # Attempt to create Headset with list type brand & model name
        with self.assertRaises(TypeError):
            #create headset instance
            invalid_type_brand_model = Headset(["A","P","P","L","E"], ["Air","Pod","Pro"], "3000", 6000)
            
            


#Accessor Basic Functions


    def test_getName(self):
        """
        Input: "Apple" "AirPod Pro MAX" with a price of $999, 10000 battery life hour
        Expected output: instance of a APPLE with all variables above 
        """        
        # Check post conditions
        self.assertEqual(templete_headset.getName(), "Apple AirPod Pro MAX")
        
        
    def test_getPrice(self):
        """
        Input: "Apple" "AirPod Pro MAX" with a price of $999.0, 10000 battery life hour
        Expected output: instance of a APPLE with all variables above 
        """
        # Check post conditions
        self.assertEqual(templete_headset.getPrice(), 999.0)        
        
        
    def test_getBattery_life_hour(self):
        """
        Input: "Apple" "AirPod Pro MAX" with a price of $999, 10000 battery life hour
        Expected output: 
        """
        # Check post conditions
        self.assertEqual(templete_headset.getBattery_life_hour(), 10000)
    
    
    def test_getWireless1(self):
        """
        Input: "Apple" "AirPod Pro MAX" with a price of $999, 10000 battery life hour
        Expected output: False 
        """
        # Check post conditions
        self.assertEqual(templete_headset.getWireless(), False)
        
    def test_getWireless2(self):
        """
        Input: "BOSE" "A30" with a price of $2999, 6000 battery life hour and wireless
        Expected output: True
        """
        # Check post conditions
        self.assertEqual(wireless_templete_headset.getWireless(), True)
 
        
# Accessor: Sound Control Options


    def test_getSoundControl(self):
        """
        Input: "Apple" "AirPod Pro MAX" with a price of $999, 10000 battery life hour
        Expected output: "off"
        """
        #turn of sound control 
        templete_headset.sound_control_off()
        #check sound control off function
        self.assertEqual(templete_headset.getSoundControl(), 'off')

        
    def test_getNoiseCancelling(self):
        """
        Input: "Apple" "AirPod Pro MAX" with a price of $9999, 251825 battery life hour
        Expected output: False
        """
        #turn off sound control
        templete_headset.sound_control_off()
        #check getNoiseCancelling function
        self.assertEqual(templete_headset.getNoiseCancelling(), False)
        
    def test_getAmbientSound(self):
        """
        Input: "Apple" "AirPod Pro MAX" with a price of $999, 10000 battery life hour
        Expected output: False
        """
        #turn off ambient sound
        templete_headset.ambient_sound_off()
        #check getAmbientSound function 
        self.assertEqual(templete_headset.getAmbientSound(), False)
        
        
#Accessor methods: Power, Charge, Battery level


    def test_getPowerStatus(self):
        """
        Input: "Apple" "AirPod Pro MAX" with a price of $999, 10000 battery life hour
        Expected output: False 
        """
        # Check post conditions
        self.assertEqual(templete_headset.getPowerStatus(), False)
            
        
    def test_getBatteryLevel(self):
        """
        Input: "Apple" "AirPod Pro MAX" with a price of $999, 10000 battery life hour
        Expected output: 100  
        """
         # Check post conditions
        self.assertEqual(templete_headset.getBatteryLevel(), 100)
        
    def test_getVolumn(self):
        """
        Input: "Apple" "AirPod Pro MAX" with a price of $999, 10000 battery life hour
        Expected output: 50 
        """
         # Check post conditions
        self.assertEqual(templete_headset.getVolumn(), 50)
        
    def test_getPlaying(self):
        """
        Input: "Apple" "AirPod Pro MAX" with a price of $999, 10000 battery life hour
        Expected output: False 
        """
        #check the status, if headset is playing music
        self.assertEqual(templete_headset.getPlaying(), False)
        
    def test_getLibrary(self):
        """
        Input: "Apple" "AirPod Pro MAX" with a price of $999, 10000 battery life hour
        Expected output: {} empty dictionary
        """
         # Check post conditions
        self.assertEqual(templete_headset.getLibrary(), {})
        
        
    def test_getQueue(self):
        """
        Input: "Apple" "AirPod Pro MAX" with a price of $999, 10000 battery life hour
        Expected output: [] empty list
        """
         # Check post conditions
        self.assertEqual(templete_headset.getQueue(), [])
        

#Mutator methods: test_set_name()


    def test_set_name_typical1(self):
        """
        Input: "SONY", "XM5"
        Expected output: True
        """
        #Check post conditions
        self.assertEqual(templete_headset.set_name("SONY", "XM5"), True)
        self.assertEqual(templete_headset.getName(), "SONY XM5")
        
    def test_set_name_typical2(self):
        """
        Input: "BOSE", "A30"
        Expected output: True
        """
        #Check post conditions
        self.assertEqual(templete_headset.set_name("BOSE", "A30"), True)
        self.assertEqual(templete_headset.getName(), "BOSE A30")

    def test_set_name_unusual1(self):
        """
        Input: " ", " "
        Expected output: True
        """
        self.assertEqual(templete_headset.set_name(" ", " "), True)
        self.assertEqual(templete_headset.getName(), "   ")

        
    def test_set_name_unusual2(self):
        """
        Input: "APple", "PROOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
        Expected output: True
        """
        self.assertEqual(templete_headset.set_name("APple", "PROOOOOOOOOOOOOOOOOOOOOOOOOOOOO"), True)
        self.assertEqual(templete_headset.getName(), "APple PROOOOOOOOOOOOOOOOOOOOOOOOOOOOO")

        
    def test_set_name_error1(self):
        """
        Input: {123,123,123}, [234,234]
        Expected output: Type Error
        """
        with self.assertRaises(TypeError):
            templete_headset.set_name({123,123,123}, [234,234])
        
    def test_set_name_error2(self):
        """
        Input: 369, 963.369
        Expected output: True
        """
        with self.assertRaises(TypeError):
            templete_headset.set_name(369, 963.369)
        
        
#Mutator methods: test_set_price()


    def test_set_price_typical1(self):
        """
        Input: 1000
        Expected output: True
        """
         # Check post conditions
        self.assertEqual(templete_headset.set_price(1000.0), True)
        self.assertEqual(templete_headset.getPrice(), 1000.0)

        
    def test_set_price_typical2(self):
        """
        Input: 3000
        Expected output: True
        """
         # Check post conditions
        self.assertEqual(templete_headset.set_price(3000.0), True)
        self.assertEqual(templete_headset.getPrice(), 3000.0)

    
    def test_set_price_unusual1(self):
        """
        Input: 123456789
        Expected output: True
        """
         # Check post conditions
        self.assertEqual(templete_headset.set_price(123456789.0), True)
        self.assertEqual(templete_headset.getPrice(), 123456789.0)

        
    def test_set_price_unusual2(self):
        """
        Input: 0
        Expected output: True
        """
         # Check post conditions
        self.assertEqual(templete_headset.set_price(0.0), True)
        self.assertEqual(templete_headset.getPrice(), 0.0)
        
    def test_set_price_error1(self):
        """
        Input: -1000 
        Expected output: ValueError
        """
        with self.assertRaises(ValueError):
            templete_headset.set_price(-1000.0)
        
    def test_set_price_error2(self):
        """
        Input: "1000"
        Expected output: TypeError
        """
        with self.assertRaises(TypeError):
            templete_headset.set_price("1000.0")
        

#Mutator methods: test_set_battery_life_hour()


    def test_set_battery_life_hour_typical1(self):
        """
        Input: 1000
        Expected output: True
        """
         # Check post conditions
        self.assertEqual(templete_headset.set_battery_life_hour(1000), True)
        self.assertEqual(templete_headset.getBattery_life_hour(), 1000)

        
        
    def test_set_battery_life_hour_typical2(self):
        """
        Input: 90000
        Expected output: True
        """
         # Check post conditions
        self.assertEqual(templete_headset.set_battery_life_hour(90000), True)
        self.assertEqual(templete_headset.getBattery_life_hour(), 90000)

        
    
    def test_set_battery_life_hour_unusual1(self):
        """
        Input: 2340056700890
        Expected output: True
        """
         # Check post conditions
        self.assertEqual(templete_headset.set_battery_life_hour(2340056700890), True)
        self.assertEqual(templete_headset.getBattery_life_hour(), 2340056700890)

        
    def test_set_battery_life_hour_unusual2(self):
        """
        Input: 0
        Expected output: True
        """
         # Check post conditions
        self.assertEqual(templete_headset.set_battery_life_hour(0), True)
        self.assertEqual(templete_headset.getBattery_life_hour(), 0)

        
    def test_set_battery_life_hour_error1(self):
        """
        Input: -10000
        Expected output: ValueError
        """
         # Check post conditions
        with self.assertRaises(ValueError):
            templete_headset.set_battery_life_hour(-1000)

        
    def test_set_battery_life_hour_error2(self):
        """
        Input: "1000"
        Expected output: TypeError
        """
         # Check post conditions
        with self.assertRaises(TypeError):
            templete_headset.set_battery_life_hour("1000")  
        
        
#Mutator methods: test_set_volumn()     


    def test_set_volumn_typical1(self):
        """
        Input: 10
        Expected output: True
        """
         # Check post conditions
        self.assertEqual(templete_headset.set_volumn(10), True)
        self.assertEqual(templete_headset.getVolumn(), 10)

        
    def test_set_volumn_typical2(self):
        """
        Input: 90
        Expected output: True
        """
         # Check post conditions
        self.assertEqual(templete_headset.set_volumn(90), True)
        self.assertEqual(templete_headset.getVolumn(), 90)

        
    def test_set_volumn_unusual1(self):
        """
        Input: 200
        Expected output: False
        """
         # Check post conditions
        self.assertEqual(templete_headset.set_volumn(200), False)
        self.assertEqual(templete_headset.getVolumn(), 90)

    
    def test_set_volumn_unusual2(self):
        """
        Input: -10
        Expected output: False
        """
         # Check post conditions
        self.assertEqual(templete_headset.set_volumn(-10), False)
        self.assertEqual(templete_headset.getVolumn(), 90)

        
    def test_set_volum_error1(self):
        """
        Input: " " 
        Expected output: TypeError
        """
         # Check post conditions
        with self.assertRaises(TypeError):
            templete_headset.set_volumn(" ")
        
    def test_set_volum_error1(self):
        """
        Input: [10,20,30]
        Expected output: True
        """
         # Check post conditions
        with self.assertRaises(TypeError):
            templete_headset.set_volumn([10,20,30])
        
        
#Mutator methods: test_set_library()


    def test_set_library_typical1(self):
        """
        Input: {"One Direction" : ["History","Perfect","One Thing", "Story of my life"] , "Taylor Swift": ["I Knew You Were Trouble.", "Blank Space", "Anti-Hero", "Love Story"]}

        Expected output: True
        """
         # Check post conditions
        self.assertEqual(templete_headset.set_library({"One Direction" : ["History","Perfect","One Thing", "Story of my life"] , "Taylor Swift": ["I Knew You Were Trouble.", "Blank Space", "Anti-Hero", "Love Story"]}), True)
        # self.assertEqual(templete_headset.getLibrary(), {"One Direction" : ["History","Perfect","One Thing", "Story of my life"] , "Taylor Swift": ["I Knew You Were Trouble.", "Blank Space", "Anti-Hero", "Love Story"]})

    def test_set_library_typical2(self):
        """
        Input: {"Travis Scott" : ["5% TINT","K-POP","SICKO MODE", "TELEKINESIS"] , "Dua Lipa": ["Leviatating"]}
        Expected output: True
        """
         # Check post conditions
        self.assertEqual(templete_headset.set_library({"Travis Scott" : ["5% TINT","K-POP","SICKO MODE", "TELEKINESIS"] , "Dua Lipa": ["Leviatating"]}), True)
        # self.assertEqual(templete_headset.getLibrary(),{"Travis Scott" : ["5% TINT","K-POP","SICKO MODE", "TELEKINESIS"] , "Dua Lipa": ["Leviatating"]}) 

    def test_set_library_unusual1(self):
        """
        Input: {" ": ["I Knew You Were Trouble.", "Blank Space", "Anti-Hero", "Love Story"]}
        Expected output: True
        """
         # Check post conditions
        self.assertEqual(templete_headset.set_library({" ": ["I Knew You Were Trouble.", "Blank Space", "Anti-Hero", "Love Story"]}), True)
        # self.assertEqual(templete_headset.getLibrary(), {" ": ["I Knew You Were Trouble.", "Blank Space", "Anti-Hero", "Love Story"]})
        
    def test_set_library_unusual2(self):
        """
        Input: {"Taylor Swift": []}

        Expected output: True
        """
         # Check post conditions
        self.assertEqual(templete_headset.set_library({"Taylor Swift": []}), True)
        # self.assertEqual(templete_headset.getLibrary(),{"Taylor Swift": []})
        
    def test_set_library_error1(self):
        """
        Input: ["I Knew You Were Trouble.", "Blank Space", "Anti-Hero", "Love Story"]
        Expected output: TyperError
        """
         # Check post conditions
        with self.assertRaises(TypeError):
            templete_headset.set_library(["I Knew You Were Trouble.", "Blank Space", "Anti-Hero", "Love Story"])
        
    def test_set_library_error2(self):
        """
        Input: "I Knew You Were Trouble."
        Expected output: TyperError
        """
         # Check post conditions
        with self.assertRaises(TypeError):
            templete_headset.set_library("I Knew You Were Trouble.")
        
        
#Mutator methods: test_remove_library()


    def test_remove_library_typical1(self):
        """
        Input: {"LE SSERAFIM" : ["Impurities","No-return","Blue Flame", "UNFORGIVEN"] , "Taylor Swift": ["I Knew You Were Trouble.", "Blank Space", "Anti-Hero", "Love Story"]}


        Expected output: True
        """
        #create a headset instance
        test_remove = Headset("Samsung", "XX", 4900.0 , 6000)
        #clear all before next test
        test_remove.remove_all_library()
        #import artist name and songs into library 
        test_remove.set_library({"LE SSERAFIM" : ["Impurities","No-return","Blue Flame", "UNFORGIVEN"] , "Taylor Swift": ["I Knew You Were Trouble.", "Blank Space", "Anti-Hero", "Love Story"]})
        #remove artist and song from library
        self.assertEqual(test_remove.remove_library({"LE SSERAFIM" : ["Impurities","No-return","Blue Flame"] , "Taylor Swift": ["I Knew You Were Trouble.", "Blank Space", "Anti-Hero", "Love Story"]}), True)
        
        #check library (to be cont.)
        # self.assertEqual(templete_headset.getLibrary(),{"One Direction" : ["Story of my life"]})

    def test_remove_library_typical2(self):
        """
        Input: {"NewJeans" : ["ETA","Cool with you","OMG", "HypeBoy"] , "Dua Lipa": ["Leviatating"]
        Expected output: True
        """
        #create a headset instance
        test_remove2 = Headset("Samsung", "XX", 4900.0 , 6000)
        #clear all before next test
        test_remove2.remove_all_library()
        #import artist name and songs into library
        test_remove2.set_library({"NewJeans" : ["ETA","Cool with you","OMG", "HypeBoy"] , "Dua Lipa": ["Leviatating"]})
        #remove artist and song from library
        self.assertEqual(test_remove2.remove_library({"NewJeans" : ["Cool with you","HypeBoy"] , "Dua Lipa": ["Leviatating"]}), True)
        
        #check library (to be cont.)
        # self.assertEqual(templete_headset.getLibrary(), {"NewJeans" : ["ETA", "OMG"]})
                
    def test_remove_library_typical3(self):
        """
        Input: {"Travis Scott" : ["5% TINT","K-POP","SICKO MODE", "TELEKINESIS"]}
        Expected output: True (Artist: Travis Scott should be remove from the library)
        """
        #clear all before next test
        templete_headset.remove_all_library()
        #import artist name and songs into library
        templete_headset.set_library({"Travis Scott" : ["5% TINT","K-POP","SICKO MODE", "TELEKINESIS"] , "Dua Lipa": ["Leviatating"]})
        #remove artist and song from library
        self.assertEqual(templete_headset.remove_library({"Travis Scott" : ["5% TINT","K-POP","SICKO MODE", "TELEKINESIS"]}), True)
        
        
        #check library (to be cont.)
        # self.assertEqual(templete_headset.getLibrary(),{"Dua Lipa": ["Leviatating"]})
        

    def test_remove_library_unusual1(self):
        """
        Input: {" ": ["I Knew You Were Trouble.", "Blank Space", "Anti-Hero", "Love Story"]}
        Expected output: True 
        """
        #clear all before next test
        templete_headset.remove_all_library()
        #import artist name and songs into library
        templete_headset.set_library({"Taylor Swift": ["I Knew You Were Trouble.", "Blank Space"]})
        #remove artist and song from library
        self.assertEqual(templete_headset.remove_library({" ": ["I Knew You Were Trouble.", "Blank Space", "Anti-Hero", "Love Story"]}), False)
        
        #check library (to be cont.)
        # self.assertEqual(templete_headset.getLibrary(),{"Taylor Swift": ["I Knew You Were Trouble.", "Blank Space"]})
        
    def test_remove_library_unusual2(self):
        """
        Input: {"Taylor Swift": []}
        Expected output: False
        """
        #clear all before next test
        templete_headset.remove_all_library(), True
        #import artist name and songs into library
        templete_headset.set_library({"Taylor Swift": ["I Knew You Were Trouble.", "Blank Space"]})
        #remove artist and song from library 
        self.assertEqual(templete_headset.remove_library({"Taylor Swift": []}), False)
        
        
        #check library (to be cont.)
        # self.assertEqual(templete_headset.getLibrary(),{"Taylor Swift": ["I Knew You Were Trouble.", "Blank Space"]})
    

    def test_remove_library_error1(self):
        """
        Input: ["I Knew You Were Trouble.", "Blank Space", "Anti-Hero", "Love Story"]
        Expected output: TyperError
        """
        #clear all before next test
        templete_headset.remove_all_library()
        #import artist name and songs into library
        templete_headset.set_library({"Taylor Swift": ["I Knew You Were Trouble.", "Blank Space"]})
        #remove artist and song from library
        with self.assertRaises(TypeError):
            templete_headset.remove_library(["I Knew You Were Trouble.", "Blank Space", "Anti-Hero", "Love Story"])
        
    def test_remove_library_error2(self):
        """
        Input: "I Knew You Were Trouble."
        Expected output: TyperError
        """
        #clear all before next test
        templete_headset.remove_all_library()
        #import artist name and songs into library
        templete_headset.set_library({"Taylor Swift": ["I Knew You Were Trouble.", "Blank Space"]})
        #remove artist and song from library
        with self.assertRaises(TypeError):
            templete_headset.remove_library("I Knew You Were Trouble.")
        
        
#Mutator methods: test_all_remove_library()


    def test_remove_all_library(self):
        """
        Input:
        Expected output: True
        """
        #clear all before next test
        templete_headset.remove_all_library(), True
        #import artist name and songs into library
        templete_headset.set_library({"Taylor Swift": ["I Knew You Were Trouble.", "Blank Space"]})
        #remove artist and song from library
        self.assertEqual(templete_headset.remove_all_library(), True)
        #check library
        self.assertEqual(templete_headset.getLibrary(), {})


#Mutator methods: features test_...

        
    def test_power_on(self):
        """
        Input: 
        Expected output: True
        """
        self.assertEqual(templete_headset.power_on(), True)
        self.assertEqual(templete_headset.getPowerStatus(), True)
        
    def test_power_off(self):
        """
        Input: 
        Expected output: True
        """
        self.assertEqual(templete_headset.power_off(), True)
        self.assertEqual(templete_headset.getPowerStatus(), False)

        
    def test_play(self):
        """
        Input: 
        Expected output: True
        """
        #turn on headset
        self.assertAlmostEqual(templete_headset.power_on(), True)
        #check play function
        self.assertEqual(templete_headset.play(), True)
        
    def test_pause(self):
        """
        Input: 
        Expected output: True
        """
        #turn headset on
        self.assertEqual(templete_headset.power_on(), True)
        #import artist name and songs into library 
        self.assertEqual(templete_headset.set_library({"One Direction" : ["History","Perfect","One Thing", "Story of my life"] , "Taylor Swift": ["I Knew You Were Trouble.", "Blank Space", "Anti-Hero", "Love Story"]}), True)
        #set songs from library to queue
        self.assertEqual(templete_headset.set_queue(),True)
        #play music
        self.assertEqual(templete_headset.play(), True)
        #test pause function
        self.assertEqual(templete_headset.pause(), True)
        #check play is off
        self.assertEqual(templete_headset.getPlaying(), False)
        
    def test_skip(self):
        """
        Input: 
        Expected output: True
        """
        #turn on headset
        self.assertEqual(templete_headset.power_on(), True)
        #import artist name and songs into library 
        self.assertEqual(templete_headset.set_library({"One Direction" : ["History","Perfect","One Thing", "Story of my life"] , "Taylor Swift": ["I Knew You Were Trouble.", "Blank Space", "Anti-Hero", "Love Story"]}), True)
        #set songs from library to queue
        self.assertEqual(templete_headset.set_queue(),True)
        #play music
        self.assertEqual(templete_headset.play(), True)
        #check current song
        self.assertEqual(templete_headset.getCurrent_song(), "History")
        #test skip function
        self.assertEqual(templete_headset.skip(), True)
        #check result (skipped song)
        self.assertEqual(templete_headset.getCurrent_song(), "Perfect")

        
    def test_previous(self):
        """
        Input: 
        Expected output: True
        """        #turn on headset
        self.assertEqual(templete_headset.power_on(), True)
        #import artist name and songs into library 
        self.assertEqual(templete_headset.set_library({"One Direction" : ["History","Perfect","One Thing", "Story of my life"] , "Taylor Swift": ["I Knew You Were Trouble.", "Blank Space", "Anti-Hero", "Love Story"]}), True)
        #set songs from library to queue
        self.assertEqual(templete_headset.set_queue(),True)
        #play music
        self.assertEqual(templete_headset.play(), True)
        #check current song
        self.assertEqual(templete_headset.getCurrent_song(), "History")
        #test previous function
        self.assertEqual(templete_headset.previous(), True)
        #check result (skipped song)
        self.assertEqual(templete_headset.getCurrent_song(), "Love Story")

        
#Mutator methods: Sound Control


    def test_noise_cancelling_on(self):
        """
        Input: 
        Expected output: True
        """
        #test noise cancelling on function
        self.assertEqual(templete_headset.noise_cancelling_on(), True)
        #check sound control varable 
        self.assertEqual(templete_headset.getSoundControl(), "noise_cancelling")

        

    def test_noise_cancelling_off(self):
        """
        Input: 
        Expected output: True
        """
        #test noise cancelling off function
        self.assertEqual(templete_headset.noise_cancelling_off(), True)
        #check sound control varable 
        self.assertEqual(templete_headset.getSoundControl(), "off")


        
    def test_ambient_sound_on(self):
        """
        Input: 
        Expected output: True
        """
        #test ambient sound on function
        self.assertEqual(templete_headset.ambient_sound_on(), True)
        #check sound control varable 
        self.assertEqual(templete_headset.getSoundControl(), "ambient_sound")
 
        
    def test_ambient_sound_off(self):
        """
        Input: 
        Expected output: True
        """
        #test ambient sound off function
        self.assertEqual(templete_headset.ambient_sound_off(), True)
        #check sound control varable 
        self.assertEqual(templete_headset.getSoundControl(), "off")

        
    def test_sound_control_off(self):
        """
        Input: 
        Expected output: True
        """
        #test ambient sound off function
        self.assertEqual(templete_headset.sound_control_off(), True)
        #check sound control varable 
        self.assertEqual(templete_headset.getSoundControl(), "off")

        
        
#Mutator methods: calculation


    def test_optimizer_typical1(self):
        """
        Input: 4769
        Expected output: Returns a number representing the result of Fourier Transform theorem
        """
        self.assertEqual(templete_headset.optimizer(4769), -137567336876)
        
    def test_optimizer_typical2(self):
        """
        Input: 3112
        Expected output: Returns a number representing the result of Fourier Transform theorem
        """
        self.assertEqual(templete_headset.optimizer(3112), -519548)
        
    def test_optimizer_unusual1(self):
        """
        Input: 21
        Expected output: Returns a number representing the result of Fourier Transform theorem
        """
        self.assertEqual(templete_headset.optimizer(21), 1361142)
        
    def test_optimizer_unusual2(self):
        """
        Input: 19000
        Expected output: Returns a number representing the result of Fourier Transform theorem
        """
        self.assertEqual(templete_headset.optimizer(19000), 152099645312)
        
    def test_optimizer_error1(self):
        """
        Input: -400
        Expected output: ValueError
        """
        with self.assertRaises(ValueError):
            templete_headset.optimizer(-400)
    
    def test_optimizer_error2(self):
        """
        Input: "400"
        Expected output: TypeError
        """
        with self.assertRaises(TypeError):
            templete_headset.optimizer("400")
