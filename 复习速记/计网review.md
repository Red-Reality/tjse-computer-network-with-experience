* definitions
* 算法
* 线索：OSI model，TCP/IP model（protocol stack）

## introduction

* 从覆盖范围来分类计算机网络
  * WAN，MAN，LAN，PAN（主要是WAN和LAN）
  * PPT下面的是他们用的方法
* 接入网络，核心网络
  * 接入：ADSL，FTTH，Wireless
  * 核心网络：IP（重点），Frame Relay and ATM 
* Packet Switching 和Circuit Switch
  * Packet:一个包一个包传
  * Circuit:必须长时间连接才能连上
  * 根据PPT上表格来理解特点
* Modem：硬件问题
  * 电子信号转化成模拟信号
  * 调制与借条：几种rate理解
    * 波特率：一秒钟传几个符号（symbol）
    * bit Rate：一秒传几个字节（波特率乘一个symbol几个字节）
  * AM，FM，PM的调制方式
* OSI：七层用来对每层的功能抽象（理论，实际实现很复杂）
* TCP/IP：现有协议的描述
  * 协议理解TCPIP，功能理解OSI
* 网络评价（一些指标）
  * 理解怎么计算这些指标与指标的含义

## 物理层

* 有三种方式承载01：频率快慢，幅度大小与相位差（AM，FM，PM），
* 传播方式
  * 定向传播：wire，fiber，coax cable
  * 非定向广播：air，vacuum
* FDMA（分频发送），TDMA（分时发送），WDMA（波分复用，就是频分复用一种形式，用不同的波传输），CDMA（码分复用）：想办法将时间，频率分配给不同的波段来实现同时发送不同信息

## 链路层

* 错误校验
  * 奇偶校验
  * CRC
  * 汉明码
  * 编码的海明距离，检错纠错能力
* 连接帧
* ARQ算法（连接纠错机制）
  * stop and wait
  * go back n（滑动窗口方法）
  * selective repeat protocol（需要buffer）

## Link Mac

* 指挥不同user谁什么时候接入信道
* MAC  protocols
  * collision: 2 nodes transmit same time
    * how detect
    * how recover
  * collision zone:交换机，网桥将它分为不同的zone，hub是不能的
* CSMA：前身aloha（能传就传，传不到就重传）
  * 侦听信道，忙碌就等，不忙就发
  * CSMA/CD：以太网：collsion detect 检测到collision在信道发生就立刻停止，避免collision对channel的占用
  * CSMA/CA：WIFI：collision avoid(collsion detect 很困难)，
  * 理解名字，怎么工作，主要区别，在哪里使用
* Addressing：
  * mac address
    * 格式
  * some special address

## Network layer

* 路由设置
  * protocol
  * algorithms
    * Dijkstra-OSFP 要有全局信息(widely use)
    * Bullman-ford - RIP
* 拥塞控制
  * queue
  * schedule(时间片轮转)
  * traffic shaping：拥塞丢弃
* IP addressing
  * 它是个interface，可以随意设置
  * subnet mask（192.168.1.2/24后面的24是子网掩码前面1的个数，即255.255.255.0）
    * CIDR
  * 要理解0.0.0.0，组播方式，广播方式的ip地址
* 网络层还有一些其他协议，ARP，RARP等
  * ARP：动态获得目标的IP和MAC地址

## transport layer

TCP\IP

* 稳定性
* 流量控制 rwnd
* 拥塞控制 cwnd

* 三次握手，四次挥手
* TCP的拥塞控制协议
  * Reno
  * dupAcks
* UDP和TCP的比较

## application layer

some protocols

what do they do,how do they do

用在哪个传输层

* DNS ,DHCP,URL ,HTTP ……

## Network Security

* 公钥私钥，KDC，CA
* 防火墙