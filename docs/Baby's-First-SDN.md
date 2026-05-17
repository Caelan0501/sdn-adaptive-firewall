# Mininet
Mininet creates
- Hosts (h1, h2, ...): isolated linux namespaces
- Switches (s1, s2, ...): Open vSwitch instances
- Links: Virtual Ethernet cables


`sh ovs-ofctl show s1`
`sh ovs-ofctl dump-flows s1`: Shows all flows in a switch

Manual Flow Rules
1) Identify ports with `sh ovs-ofctl show s1`
2) Install Forwarding rules with `sh ovs-ofctl add-flow s1 -O OpenFlow13 "in_port=1,actions=output:2"` and `sh ovs-ofctl add-flow s1 -O OpenFlow13 "in_port=2,actions=output:1"`
3) Verify flow table with `sh ovs-ofctl dump-flows s1`
