import unittest
import sys
import traceback
import collections
import re
import random
this = sys.modules[__name__]

import cours_python_utils as cpy_utils
## test_with_expected
## check_fonction_in_code

class TestExercice1( unittest.TestCase ):
    def test_code(self):
        nb_lignes = In[-1].count( "\n" ) + 1
        if nb_lignes > 10:
            print( "WARNING: Mais pourquoi donc tant de lignes de code ? {0}".format( nb_lignes ) )

    def test_fonction(self):
        if not 'x' in globals():
            self.fail("Vous n'avez pas défini de variable x")
        self.assertEqual( x, 0, 'x doit être égal à 0, x est égal à {0}'.format( x ) )
        self.assertIsInstance( x, int )

class TestExercice2( unittest.TestCase ):
    def test_code(self):
        nb_lignes = In[-1].count( "\n" ) + 1
        if nb_lignes > 10:
            print( "WARNING: Mais pourquoi donc tant de lignes de code ? {0}".format( nb_lignes ) )

    def test_fonction(self):
        if not 'Y' in globals():
            self.fail("Vous n'avez pas défini de variable x")
        self.assertEqual( Y, 1, 'Y doit être égal à 1, Y est égal à {0}'.format( Y ) )
        self.assertIsInstance( Y, int )

def tester_exo( n, globals_dict ):
    for k, v in globals_dict.items():
        setattr( this, k, v )
    launch_test_case( eval( "TestExercice{0}".format(n) ) )

def launch_test_case( test_case ):
  suite = unittest.TestLoader().loadTestsFromTestCase( test_case )
  unittest.TextTestRunner(verbosity=2).run(suite)

