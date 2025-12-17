---
layout: default
title: Raspi$^2$USBL: An open-source Raspberry Pi-Based Passive Inverted Ultra-Short Baseline Positioning System for Underwater Robotics
---

# Raspi$^2$USBL: An open-source Raspberry Pi-Based Passive Inverted Ultra-Short Baseline Positioning System for Underwater Robotics

**arXiv**: [2511.06998v1](https://arxiv.org/abs/2511.06998) | [PDF](https://arxiv.org/pdf/2511.06998.pdf)

**作者**: Jin Huang, Yingqiang Wang, Ying Chen

---

## 💡 一句话要点

**提出基于树莓派的开源被动倒置超短基线定位系统，以低成本解决水下机器人精确定位问题**

**关键词**: `水下机器人定位` `超短基线系统` `声学导航` `开源硬件` `实时信号处理` `低成本定位`

## 📋 核心要点

1. 核心问题：全球导航卫星系统信号无法穿透海面，水下机器人精确定位困难
2. 方法要点：采用被动声学接收器和主动信标，结合C++软件框架实现高精度时钟同步和实时信号处理
3. 实验或效果：在消声池、淡水湖和开放海域测试，斜距精度优于0.1%，方位精度在0.1°内，稳定距离达1.3公里

## 📄 摘要（原文）

> Precise underwater positioning remains a fundamental challenge for underwater
> robotics since global navigation satellite system (GNSS) signals cannot
> penetrate the sea surface. This paper presents Raspi$^2$USBL, an open-source,
> Raspberry Pi-based passive inverted ultra-short baseline (piUSBL) positioning
> system designed to provide a low-cost and accessible solution for underwater
> robotic research. The system comprises a passive acoustic receiver and an
> active beacon. The receiver adopts a modular hardware architecture that
> integrates a hydrophone array, a multichannel preamplifier, an oven-controlled
> crystal oscillator (OCXO), a Raspberry Pi 5, and an MCC-series data acquisition
> (DAQ) board. Apart from the Pi 5, OCXO, and MCC board, the beacon comprises an
> impedance-matching network, a power amplifier, and a transmitting transducer.
> An open-source C++ software framework provides high-precision clock
> synchronization and triggering for one-way travel-time (OWTT) messaging, while
> performing real-time signal processing, including matched filtering, array
> beamforming, and adaptive gain control, to estimate the time of flight (TOF)
> and direction of arrival (DOA) of received signals. The Raspi$^2$USBL system
> was experimentally validated in an anechoic tank, freshwater lake, and open-sea
> trials. Results demonstrate a slant-range accuracy better than 0.1%, a bearing
> accuracy within 0.1$^\circ$, and stable performance over operational distances
> up to 1.3 km. These findings confirm that low-cost, reproducible hardware can
> deliver research-grade underwater positioning accuracy. By releasing both the
> hardware and software as open-source, Raspi$^2$USBL provides a unified
> reference platform that lowers the entry barrier for underwater robotics
> laboratories, fosters reproducibility, and promotes collaborative innovation in
> underwater acoustic navigation and swarm robotics.

