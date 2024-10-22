import matplotlib.pyplot as plt


tp_hybrid   = [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,13.0,14.0,15.0,16.0,17.0,18.0,19.0]
tp_ixy      = [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,13.0,14.0,15.0,16.0]
tp_safeRust = [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,13.0,14.0,15.0,16.0,17.0,17.85]
tp_full     = [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,13.0,14.0,15.0,16.0,17.0,18.0,19.0,20.0]
    
hybrid_theseus              = [4166.0, 4231.0, 4333.0, 4560.0, 4982.5, 5156.0, 5235.0, 5354.0, 5420.5, 5648.0, 7312.0, 7834.0, 7597.0, 7587.0, 7034.0, 7114.0, 7308.0, 7616.0, 8490.0, 9145.0]
ixy_ubuntu                  = [4147.0, 4233.0, 4375.0, 4672.0, 5034.0, 5156.0, 5238.0, 5453.0, 5706.0, 6020.0, 6628.0, 8199.0, 7702.0, 8387.0, 9175.0, 10752.0, 11677.0]  
safeRust_ubuntu             = [4124.0, 4205.0, 4384.0, 4768.0, 5133.0, 5316.0, 5344.0, 5344.0, 5398.0, 5482.0, 7478.0, 7578.0, 7568.0, 7555.0, 6665.0, 6659.5, 6739.0, 6989.0, 7507.0]
hybrid_restricted_theseus   = [4003.0, 4112.0, 4336.0, 4570.0, 4806.0, 4957.0, 5095.0, 5155.0, 5239.0, 5328.0, 5469.0, 5661.0, 5673.0, 5750.0, 5798.0, 5901.0, 5958.0, 6080.0, 6659.0, 7059.0, 9136.0]
tinynf_ubuntu               = [3987.0, 4073.0, 4272.0, 4522.0, 4723.0, 4887.0, 5012.0, 5072.0, 5145.0, 5235.0, 5376.0, 5533.0, 5597.0, 5667.0, 5722.0, 5802.0, 5853.0, 5962.0, 6394.0, 6832.0, 11312.0]
dpdk_ubuntu                 = [4057.0, 4086.0, 4166.0, 4317.0, 4391.0, 4403.0, 4464.0, 4573.0, 4659.0, 4775.0, 4976.0, 5280.0, 5353.0, 5501.0, 5568.0, 5696.0, 5833.0, 6023.0, 6816.0, 7344.0, 13805.0]


yerrl_hybrid = [57.0, 103.0, 182.0, 339.0, 492.5, 571.0, 627.0, 707.0, 754.5, 854.0, 1873.35, 1306.0, 1680.35, 1722.4, 1459.0, 1450.0, 1545.0, 1692.0, 2035.2, 2102.0]
yerru_hybrid = [128.0, 530.0, 557.0, 690.7, 783.5, 886.1, 928.0, 1135.0, 1552.5, 1837.0, 2387.45, 2166.0, 2243.0, 2211.0, 2291.0, 2250.0, 2296.0, 2458.0, 2576.0, 2477.0]

yerrl_ixy = [32.0, 111.0, 224.0, 384.0, 436.0, 474.0, 470.0, 518.0, 576.0, 634.0, 852.0, 1776.0, 1005.0, 1091.0, 1184.0, 1699.0, 1088.0]
yerru_ixy = [157.0, 625.0, 575.55, 688.0, 748.8, 730.2, 893.0, 929.2, 1211.7, 1688.4, 2142.4, 2345.0, 2153.1, 2119.6, 2134.0, 1612.45, 2794.5]

yerrl_safeRust = [38.0, 115.0, 320.0, 439.0, 484.0, 480.0, 497.0, 461.0, 448.0, 470.0, 1962.0, 646.0, 919.95, 1184.0, 787.0, 672.0, 611.0, 662.0, 998.0]
yerru_safeRust = [147.0, 752.0, 723.0, 784.0, 770.0, 675.0, 684.0, 704.0, 842.4, 2128.0, 985.0, 959.4, 968.95, 1004.45, 1507.0, 1445.1, 1206.0, 1299.0, 1165.0]

yerrl_hybrid_restricted= [38.0, 131.0, 323.0, 378.0, 428.0, 410.0, 433.0, 403.0, 414.0, 413.0, 426.0, 451.0, 409.0, 413.0, 409.0, 404.0, 406.0, 429.0, 752.0, 707.0, 0] # 2231.5]
yerru_hybrid_restricted = [176.7, 665.0, 713.0, 662.0, 663.0, 608.0, 618.8, 630.0, 646.0, 659.0, 656.0, 1651.0, 1050.0, 1072.0, 809.85, 758.4, 695.0, 807.9, 864.0, 673.0, 0] # 1402.0]

yerrl_tinynf = [32.0, 114.0, 282.0, 362.0, 406.0, 401.0, 411.0, 397.0, 422.0, 423.0, 435.0, 435.0, 417.0, 406.0, 391.0, 400.0, 417.0, 429.0, 663.0, 732.65, 0] #4672.0#]
yerru_tinynf = [151.0, 634.0, 696.5, 675.0, 704.0, 678.0, 664.95, 713.1, 683.0, 727.0, 698.0, 665.55, 640.75, 762.0, 733.8, 732.25, 669.0, 915.0, 1053.9, 1213.9, 0] #16544.0#]

yerrl_dpdk23 = [35.0, 67.0, 137.0, 237.0, 253.0, 237.0, 234.0, 244.0, 266.0, 279.0, 324.0, 413.0, 364.0, 419.0, 445.0, 454.0, 444.0, 455.0, 899.3, 832.0, 0] # 6605.0]
yerru_dpdk23 = [222.0, 372.0, 394.0, 515.0, 486.0, 485.7, 480.0, 486.0, 528.95, 593.9, 650.0, 1709.0, 1367.0, 1276.0, 901.25, 746.0, 840.2, 965.1, 947.3, 1714.4, 0] # 2784.45]

# Create the plot
fig = plt.figure(figsize=(15, 10))

# Plot hybrid
plt.plot(tp_hybrid, [x/ 1000.0 for x in hybrid_theseus], label='hybrid_theseus', marker='^', markersize=12) #, color='green') #, yerr=[yerr_restricted_lower, yerr_restricted_upper])

# Plot ixy
plt.plot(tp_ixy, [x/ 1000.0 for x in ixy_ubuntu], label='ixy_ubuntu', marker='x', markersize=12) #, color='green') #, yerr=[yerr_restricted_lower, yerr_restricted_upper])

# Plot safe rust
plt.plot(tp_safeRust, [x/ 1000.0 for x in safeRust_ubuntu], label='safeRust_ubuntu', marker='s', markersize=12) #, color='red') #, yerr=[yerr_restricted_lower, yerr_restricted_upper])

# Plot hybrid data
plt.plot(tp_full, [x/ 1000.0 for x in hybrid_restricted_theseus], label='hybrid(restricted)_theseus', marker='D', markersize=12) #, color='orange') #, yerr=[yerr_restricted_lower, yerr_restricted_upper])

# Plot tinynf data
plt.plot(tp_full, [x/ 1000.0 for x in tinynf_ubuntu], label='tinynf_ubuntu', marker='o', markersize=12) #, color='blue') #, yerr=[yerr_tinynf_lower, yerr_tinynf_upper])

# Plot DPDK data
plt.plot(tp_full, [x/ 1000.0 for x in dpdk_ubuntu], label='DPDK-23.11.2_ubuntu', marker='*', markersize=12) #, color='purple') #, yerr=[yerr_dpdk23_lower, yerr_dpdk23_upper])


# plt.xlim(0, 20)
# plt.ylim(0, 14)

# Add labels and title
plt.xlabel('Background Traffic Throughput (Gbps)', fontsize=25, labelpad=20) 
plt.ylabel('Median Latency (us)', fontsize=25, labelpad=20)
# plt.title('Latency of ixgbe drivers')
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)
# Add legend
plt.legend(fontsize=22)

plt.rcParams['figure.dpi']=500
plt.rcParams['pdf.fonttype']=42
plt.rcParams['ps.fonttype']=42
# plt.rcParams['axes.labelsize']='x-large'
# plt.rcParams['axes.titlesize']='x-large'
# plt.rcParams['xticks.labelsize']='x-large'
# plt.rcParams['yticks.labelsize']='x-large'
# plt.rcParams['legend.fontsize']='x-large'


plt.show()

fig.savefig('latencies.eps', format='eps')