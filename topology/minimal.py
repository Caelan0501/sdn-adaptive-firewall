from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import TCLink
from mininet.node import RemoteController

def minimal_topology():
    net = Mininet(controller=RemoteController, link=TCLink)

    print ("*** Creating Controller ***")
    c0 = net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6633)

    print ("*** Creating Host***")
    h1 = net.addHost('h1', ip='10.0.0.1/24')
    h2 = net.addHost('h2', ip='10.0.0.2/24')

    print ("*** Creating Switch***")
    s1 = net.addSwitch('s1', protocols='OpenFlow13')

    print ("*** Creating Link***")
    net.addLink(h1, s1)
    net.addLink(h2, s1)

    print ("*** Starting Network***")
    net.build()
    c0.start()
    s1.start([c0])

    print ("*** Running CLI***")
    CLI(net)

    print("*** Stopping Network***")
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    minimal_topology()