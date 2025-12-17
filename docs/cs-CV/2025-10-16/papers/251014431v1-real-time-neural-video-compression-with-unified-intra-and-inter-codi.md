---
layout: default
title: Real-Time Neural Video Compression with Unified Intra and Inter Coding
---

# Real-Time Neural Video Compression with Unified Intra and Inter Coding

**arXiv**: [2510.14431v1](https://arxiv.org/abs/2510.14431) | [PDF](https://arxiv.org/pdf/2510.14431.pdf)

**作者**: Hui Xiang, Yifan Bian, Li Li, Jingran Wu, Xianguo Zhang, Dong Liu

---

## 💡 一句话要点

**提出统一帧内帧间编码的神经视频压缩框架，以解决遮挡和误差传播问题。**

**关键词**: `神经视频压缩` `帧内帧间编码` `实时编码` `误差传播抑制` `遮挡处理`

## 📋 核心要点

1. 现有神经视频压缩存在遮挡处理低效和帧间误差传播问题。
2. 引入帧内编码工具，自适应处理帧内/帧间编码，无需手动刷新机制。
3. 实验显示BD-rate平均降低10.7%，保持实时性能，帧质量更稳定。

## 📄 摘要（原文）

> Neural video compression (NVC) technologies have advanced rapidly in recent
> years, yielding state-of-the-art schemes such as DCVC-RT that offer superior
> compression efficiency to H.266/VVC and real-time encoding/decoding
> capabilities. Nonetheless, existing NVC schemes have several limitations,
> including inefficiency in dealing with disocclusion and new content, interframe
> error propagation and accumulation, among others. To eliminate these
> limitations, we borrow the idea from classic video coding schemes, which allow
> intra coding within inter-coded frames. With the intra coding tool enabled,
> disocclusion and new content are properly handled, and interframe error
> propagation is naturally intercepted without the need for manual refresh
> mechanisms. We present an NVC framework with unified intra and inter coding,
> where every frame is processed by a single model that is trained to perform
> intra/inter coding adaptively. Moreover, we propose a simultaneous two-frame
> compression design to exploit interframe redundancy not only forwardly but also
> backwardly. Experimental results show that our scheme outperforms DCVC-RT by an
> average of 10.7\% BD-rate reduction, delivers more stable bitrate and quality
> per frame, and retains real-time encoding/decoding performances. Code and
> models will be released.

