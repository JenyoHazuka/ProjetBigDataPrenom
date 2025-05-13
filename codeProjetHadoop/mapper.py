#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import csv

def mapper():
	try:
		reader = csv.reader(sys.stdin, delimiter=';')
	
		header = None

    		try:
			header = reader.next()
		except StopIteration:
			return

    		if not header:
			return

    		try:
        		# Index des colonnes, detectes dynamiquement
        		idx_annee = header.index('annais')
        		idx_sexe = header.index('sexe')
        		idx_prenom = header.index('preusuel')
        		idx_nombre = header.index('nombre')
			idx_dpt = header.index('dept')
    		except ValueError:
        		return

    		for row in reader:
        		try:
            			annee = row[idx_annee].strip()
            			sexe = row[idx_sexe].strip()
            			prenom = row[idx_prenom].strip()
            			nombre_str = row[idx_nombre].strip()
	    			dept = row[idx_dpt].strip()

	    			try:
					nombre = int(nombre_str)
	    			except ValueError:
					continue

            			if annee != 'XXXX' and annee and sexe and prenom:
	                		key = "{}_{}_{}\t{}".format(annee, sexe, prenom, nombre)
					print >> sys.stdout, key

			except Exception:
        	    		continue

	except Exception:
		pass

if __name__ == "__main__":
    mapper()
