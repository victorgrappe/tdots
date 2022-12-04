
from tdots.tdot import Tdot
from tdots.tdots import Tdots

dts = Tdots()

print(dts.all)

dts.create(Tdot(key="a", label="Alphonse"))
dts.create(Tdot(key="b", label="Bertrand"))
dts.create(Tdot(key="c", label="Charles"))
print(dts.all)

a = dts.read(key="a")
print(a)

dts.update(Tdot(key="a", label="Alexandre"))
print(dts.all)

dts.delete(key="a")
print(dts.all)


