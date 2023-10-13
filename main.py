#encoding=utf8
import os
from wox import Wox, WoxAPI

class main(Wox):

    def query(self, q):
        results = []
        results.append({
            "Title": "Brigtness",
            "SubTitle": "Set monitor brightness to: " + q,
            "IcoPath": "Images/pic.ico",
            "JsonRPCAction": {
                "method": "doNothing",
                "parameters":  [q],
                "dontHideAfterAction": True
                }
            })

        return results

    def doNothing(self, q):
        os.popen("LOCATION TO\\ClickMonitorDDC_7_2.exe b " + q)



if __name__ == "__main__":
    main()

