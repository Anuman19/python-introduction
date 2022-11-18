#!/usr/bin/python3
##############################################
#
# Name: Bankkonto_3.py
#
# Author: Peter Christen
#
# Version: 1.1
# 
# Date: 22.05.2020
#       05.05.2022 V1.1 Zeitanpassung
#
# Purpose: Kontoverwaltung
#          Daten ausgeben
#
##############################################

import datetime

#Klassen
class Konto:
  '''Klasse Konto zur Verwaltung von Bankkonten'''
  
  #Konstruktor Methode
  def __init__(self,ktnr):
      #Attribute
      self.kontonummer=ktnr

  #Weitere Methode
  def kontostand_erfassen(self,kontostand):
      '''Initialer Kontostand erfassen'''

      now = datetime.datetime.now()
      self.kontostand=kontostand
      self.aenderung_kontostand=now.strftime("%d.%m.%Y %H:%M:%S")
      
  def personalien_erfassen(self, fname, lname, location):
      
      self.fname = fname
      self.lname = lname
      self.location = location
      self.timestamp = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

  def daten_ausgeben(self):
      '''Kunden- und Kontodaten ausgeben'''

      print (50*"#")
      print ("# Kontoangaben       ")
      print (50*"#")
      print ("Kontonummer:", self.kontonummer)
      print ("Vorname:", self.fname)
      print ("Nachname:", self.lname)
      print ("Wohnort:", self.location)
      print ("Letzte Änderung:", self.timestamp)
      print (50*"#")
      print ("Kontostand:", "{:.2f}".format(self.kontostand))
      print ("per Stichtag:", self.aenderung_kontostand)
      print ()

#Objekt/Daten erfassen
konto1=Konto("12345-1")
konto1.kontostand_erfassen(200)
konto1.personalien_erfassen("Max", "Muster", "Biglen")

#Daten ausgeben
konto1.daten_ausgeben()

