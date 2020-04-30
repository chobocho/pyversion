import unittest
import sys
sys.path.append("..\\src")
from pyversion import *

class PyversionInfoTest(unittest.TestCase):
    def setUp(self):
        print("\n== setUp ==")
        self.makeTestVersionJson()
        self.versionInfo = VersionInfo()
        
    def makeTestVersionJson(self):
        print("_saveVersionInfo")
        jsonData = {}
        jsonData['filename'] = "version.py"
        jsonData['separator'] = '_'   
        jsonData['header'] = "SW_VERSION=V0.1105"
        jsonData['date'] = "TD"
        jsonData['month_release_count'] = 2
      
        f = open("version.json" ,'w', encoding="UTF-8")
        f.write(json.dumps(jsonData))
        f.close()
        
    def testUpdateVersionInfo(self):
        self.versionInfo.updateVersionInfo()
        f = open("version.py", 'r', encoding="UTF-8")
        version = f.read()
        f.close()
        self.assertEqual(version, "SW_VERSION=V0.1105_TE1")
        
    def testLoadVersionInfo(self):
        print("Run testLoadVersionInfo")
        self.versionInfo._readVersionInfo()
        versionInfo = self.versionInfo.getVersionInfo()
        self.assertEqual(versionInfo['filename'], "version.py")
        
    def testLoadNotExistFile(self):
        print("Run testLoadNotExistFile")
        self.versionInfo.updateVersionInfo("empty")
        versionInfo = self.versionInfo.getVersionInfo()
        self.assertEqual(versionInfo['filename'], "version.py")
        
    def testMakeNewVersion(self):
        print("Run testMakeNewVersion")
        self.versionInfo._readVersionInfo()
        self.assertEqual(self.versionInfo._makeNewVersion(), "SW_VERSION=V0.1105_TE1")
        
if __name__ == '__main__':
    unittest.main()