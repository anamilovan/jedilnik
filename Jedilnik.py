#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "Dobrodosli v dnevni jedilnik nase restavracije!"

dnevni_meni = {}

while True:
    jed = raw_input("Prosim vnesite jed ")
    cena = raw_input("Prosim vnesite ceno jedi ")
    dnevni_meni[jed] = cena

    print "Jed " + jed + " stane " + cena + " EUR"

    new = raw_input("Ali zelite vnesti novo jed? (da/ne) ")

    if new.lower() == "ne".lower() :
        break

jedilnik_file = open("jedilnik.txt", "w+")
jedilnik_file.write("Jedilnik: \n")
for jed in dnevni_meni:
    jedilnik_file.write("Jed %s stane %s EUR\n" % (jed, dnevni_meni[jed]))

print "Jedilnik: %s" % dnevni_meni

print "Konec jedilnika"