########################################################
##                Test des fonctions verifier*        ##
########################################################	
class MyTest(unittest.TestCase):
	def testVerifActivite(self):
		bd = BD()
		bd.connexion()
		print("Test VerifActivite - False")
		self.assertEqual(bd.verifierActivite("2901"), False)
		print("Test VerifActivite - True")
		self.assertEqual(bd.verifierActivite("1"), True)
	def testVerifEquipement(self):
		bd = BD()
		bd.connexion()
		print("Test VerifEquipement- False")
		self.assertEqual(bd.verifierEquipement("723820001"), False)
		print("Test VerifEquipement- True")
		self.assertEqual(bd.verifierEquipement("1"), True)
	def testVerifEquipementBis(self):
		bd = BD()
		bd.connexion()
		print("Test VerifEquipementBis- False")
		self.assertEqual(bd.verifierEquipementBis("69849", "2901"), False)
		print("Test VerifEquipementBis- True")
		self.assertEqual(bd.verifierEquipementBis("1", "1"), True)

unittest.main()