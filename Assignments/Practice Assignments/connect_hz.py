#!/ms/dist/python/PROJ/core/2.7.1/bin/python

import sys,ms.version
ms.version.addpkg('python_modules','1.3',meta='horizon')
import Horizon,q

hz = Horizon.HzConnection()
conn = hz.connect('pdbc:hrz://prod/?useIndex=y&moduleLoad=horizon:funcDSUtils:prod')

#query = "`vd xdesc getDSData `ids`sd`ed`cnames!(`UA.N;.z.d-10;.z.d-1;`id`vd`tp`tp_thic`ocp_dailyprc`cp_thic)"
query = "getDSData`cnames`sd`ed`where!(`id`vd`short_sell_volume;2013.01.27;2013.01.28;enlist (in;`e;enlist `KS`KQ))"
#query = "`vd xdesc .dsg2.getData `dname`tname`ids`cnames`sd`ed !(`ds2;`ds_price;`MS.N;`id`vd`rawtp`rawvs;`date$.z.Z-30;`date$.z.Z)"

res=hz.executeQuery(query)
print res

hz.disconnect()
