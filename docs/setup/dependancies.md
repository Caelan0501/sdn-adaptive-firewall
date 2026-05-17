# Core Dependencies

## Java
sudo apt install openjdk-21-jdk

Version: `java -version`
```
openjdk version "21.0.10" 2026-01-20
OpenJDK Runtime Environment (build 21.0.10+7-Ubuntu-124.04)
OpenJDK 64-Bit Server VM (build 21.0.10+7-Ubuntu-124.04, mixed mode, sharing)
```
Purpose:
Required for OpenDaylight Titanium-SR2 runtime and development.

## Maven
sudo apt install maven

Version: `mvn -version`

```
Apache Maven 3.8.7
Maven home: /usr/share/maven
Java version: 21.0.10, vendor: Ubuntu, runtime: /usr/lib/jvm/java-21-openjdk-amd64
Default locale: en_US, platform encoding: UTF-8
OS name: "linux", version: "6.17.0-29-generic", arch: "amd64", family: "unix"
```
Purpose:
Java dependency management and OpenDaylight module builds.

## Mininet
`sudo apt install mininet`

Version: `mn --version`

`2.3.0`

Purpose:
Network topology emulation for SDN experimentation.

## Open vSwitch
`sudo apt install openvswitch-switch`

Version: `ovs-vsctl --version`
```
ovs-vsctl (Open vSwitch) 3.3.4
DB Schema 8.5.1
```
Purpose:
Virtual OpenFlow-capable switching layer.

## Wireshark
`sudo apt install wireshark`

Purpose:
OpenFlow packet inspection and traffic analysis.