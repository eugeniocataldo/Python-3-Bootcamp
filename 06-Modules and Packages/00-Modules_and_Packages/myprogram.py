# %%

from MyMainPackage.some_main_script import report_main
from MyMainPackage.SubPackage import mysubscript

report_main()

mysubscript.sub_report()

# %%

import MyMainPackage.some_main_script as this
# import MyMainPackage

this.report_main()


# %%
