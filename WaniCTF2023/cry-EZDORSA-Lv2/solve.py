from Crypto.Util.number import bytes_to_long, getPrime, long_to_bytes
import gmpy2

n = 25465155563758206895066841861765043433123515683929678836771513150236561026403556218533356199716126886534636140138011492220383199259698843686404371838391552265338889731646514381163372557117810929108511770402714925176885202763093259342499269455170147345039944516036024012941454077732406677284099700251496952610206410882558915139338028865987662513205888226312662854651278789627761068396974718364971326708407660719074895819282719926846208152543027213930660768288888225218585766787196064375064791353928495547610416240104448796600658154887110324794829898687050358437213471256328628898047810990674288648843902560125175884381
e = 7
c = 25698620825203955726406636922651025698352297732240406264195352419509234001004314759538513429877629840120788601561708588875481322614217122171252931383755532418804613411060596533561164202974971066750469395973334342059753025595923003869173026000225212644208274792300263293810627008900461621613776905408937385021630685411263655118479604274100095236252655616342234938221521847275384288728127863512191256713582669212904042760962348375314008470370142418921777238693948675063438713550567626953125

c = c // pow(5, 100, n)
m = gmpy2.iroot(c, e)[0]
print(long_to_bytes(int(m)).decode())