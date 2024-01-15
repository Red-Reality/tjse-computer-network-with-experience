1:

*  a: Transport layer, as the transport layer is used to take care of the communication between two host processes and functions to provide reliable transmission services from end to end. This layer can provide services such as flow control, error control, quality of service, data transfer management, etc.
* b：Data Link Layer. The data link layer has a special sublayer: the media access sublayer is used to deal with this problem
* c：Data Link Layer. The unit of transmission at the data link layer is the frame, and its task is to assemble the IP datagrams coming from the network layer into frames
* d：Network layer. Deciding which port to send data from is implemented based on the ip protocol, so it is the network layer protocol that determines which port the data is sent from.

2：

* a: listed modulation are AM (digital signal is ASK), PM (PSK), FM (FSK); for digital signals, there are QPSK and 8PSK, as well as QAM (with quadrant recording signal)
* b: the listed communication microsofts are near-Earth satellites, geosynchronous satellites, and far-Earth satellites
* c: introduced twisted pair (network cable), coaxial cable, fiber optics, the
* d: Multiplexing methods are FDM, wavelength-division multiplexing, time-division multiplexing, and code-division multiple access, which improves the efficiency of the use of time and spectrum

3：

Not always, if the end-to-end communication is low load and there are multiple sessions transmitting on a pathway packet switching has less latency; however, when the end-to-end communication is high load, real-time transmission is required and the amount of signals to be transmitted is large and there are fewer or even only one session on the pathway (i.e., the entire pathway is only used by one end-to-end communication), the latency of circuit switching is even less (avoiding delays due to sending, receiving and parsing of packets)

4：

* a: When using circuit switching, the entire link allows only 6Mbps/0.5Mbps = 12 users to use it.
* b: It means to find the probability that more than 12 people will use the network; that is , find 1-P(0)-P(1)-... -P(12), using the binomial distribution. This can be obtained using the following procedure:

~~~python
import math
def binomial_pmf(n, k, p):
    combination = math.comb(n, k)
    pmf = combination * (p ** k) * ((1 - p) ** (n - k))
    return pmf
num = 0
for i in range(0,13):
    num = num +binomial_pmf(30,i,0.3)
print(1-num)
~~~

the output is 8.45%

* c: Accord to the following conclusion ：$$C=Wlog_2(1+\dfrac {S} {N})$$,we can get that $$6=30log_2(1+\dfrac {S} {N})$$,$$\dfrac {S} {N}$$ = $$\sqrt[5]2-1$$

5:

The queuing delay is depended on the transmit speed of the first and the second packet.

First, we need to consider how much later packet 3 arrives at R than packet 1 in an A-R transfer:

packets 1 arrive time： $$ d_{prop}+d_{trans} = 10ms+\dfrac {50kb} {10Mbps}  = 15ms$$ 

packets 3 arrive time： $$ d_{prop}+d_{trans} = 10ms+\dfrac {150kb} {10Mbps}  = 25ms$$ 

so when packet 1 start to transmit, it need 10 ms for packet  3 transmit to R.

with the same route, we can calculate that when packet 2 start to transmit, it need 5 ms for packet 3 transmit to R.

however, when packet 2 reach to R, packet 1 haven't finish transmitted yet. It consume packet 1 $$ \dfrac {50kb} {1Mbps} = 50ms$$ to start transmit. So we can get the following conclusion:

packet 1 start to transmit from R to B: $$ d_{delay1}=d_{propA}+d_{transA}+d_{transB} = 10ms+\dfrac {50kb} {10Mbps}+\dfrac {50kb} {1Mbps}  = 65ms$$ 

when packet 1 start to transmit, packet 2 has already in R, so packet 2 start to transmit:

$$d_{delay2}=d_{delay1}+d_{transB} = 65ms + \frac{50kb} {1Mbps} = 115ms$$

So packet3's queue time is $$d_{delay2}$$ -$$d_{3-arrive-time}$$= 90ms.

6:

<S,A> = $$ \dfrac {1} {8}$$ (1-1+3+1-1+3+1+1) = 1,

<S,B> = $$ \dfrac {1} {8}$$ (1-1-3-1-1-3+1-1)=-1,

<S,C> = $$ \dfrac {1} {8}$$(1+1+3+1-1-3-1-1)=0,

<S,D> = $$ \dfrac {1} {8}$$ (1+1+3-1-1+1+3+1)=1

so ABD is transmitted, A is 1, B is 0, D is 1;

7:

* the number of the correction capability of the horizontal-vertical for the 7×7 block is 1,because accord to case 2, with 2 bit error occur, we can only know the block has error occur but can not detected the error.
* the number of the detection capability of the horizontal-vertical for the 7×7 block is 3. Because accord to case 4, with 4 bit error occur, the checkbit won't change, that is, we can not check if the block is error. However, we can still detect case 3's error.

So we know that the Hamming distance is max{2m+1,n+1}=3+1=4.

8:

* a): 4 check bits needed. Consider the conclusion: $$ n+k \le 2^k-1$$,easy to see that minimum of k is 4.
* b): the check bit are $$p_1,p_2,p_3,p_4$$ ,so we first we calculate the position of check bits.
  * $$p_1$$ 's position is $$2^{1-1}=1$$.
  * $$p_2$$ 's position is $$2^{2-1}=2$$
  * $$p_3$$ 's position is $$2^{3-1}=4$$
  * $$p_4$$ 's position is $$2^{4-1}=8$$
* So the array is:[1,0,0,1,0,$$p_4$$,1,0,1,$$p_3$$,1,$$p_2$$,$$p_1$$,]
* Next, we will calculate 4 check bits. 
* $$p_1 = D_3\oplus D_5 \oplus D_7 \oplus D_9 \oplus D_{11} \oplus D_{13} = 0$$
*  $$p_2 = D_3 \oplus D_6\oplus D_{7} \oplus D_{10} \oplus D_{11} = 1$$
* $$p_3 = D_5 \oplus D_6 \oplus D_7 \oplus D_{12} \oplus D_{13} = 1$$
* $$p_4 = D_9\oplus D_{10} \oplus D_{11} \oplus D_{12} \oplus D_{13} = 0$$
* So the number is 100100101110 

9:

* a): The coding process is as below:
  * source string is 10010011101, the G(x) is 1001.So we calculate the mod 2 remainder r(x) = 110.(This result is calculated by pen and paper)
  * So the data we transmit is 10010011101 110,
  * T(x) = $$X^{13}+X^{10}+X^{7}+X^{6}+X^{5}+X^{3}+X^{2}+X^{1}$$
* b): yes. Now what we get is 011 10011101 110. So we check if the first 11 bits are correct. So we calcuate the mod 2 :
  * 01110011101 $$mod_2$$ 1001 =001
  * And $$ 001 \ne 110$$, So the data transmitted is not correct.