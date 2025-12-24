---
layout: default
title: "P/D-Device: Disaggregated Large Language Model between Cloud and Devices"
---

# P/D-Device: Disaggregated Large Language Model between Cloud and Devices

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09035" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09035v1</a>
  <a href="https://arxiv.org/pdf/2508.09035.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09035v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09035v1', 'P/D-Device: Disaggregated Large Language Model between Cloud and Devices')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yibo Jin, Yixu Xu, Yue Chen, Chengbin Wang, Tao Wang, Jiaqi Huang, Rongfei Zhang, Yiming Dong, Yuting Yan, Ke Cheng, Yingjie Zhu, Shulan Wang, Qianqian Tang, Shuaishuai Meng, Guanxin Cheng, Ze Wang, Shuyan Miao, Ketao Wang, Wen Liu, Yifan Yang, Tong Zhang, Anran Wang, Chengzhou Lu, Tiantian Dong, Yongsheng Zhang, Zhe Wang, Hefei Guo, Hongjie Liu, Wei Lu, Zhengyong Zhang

**分类**: cs.DC, cs.CL, cs.LG

**发布日期**: 2025-08-12

---

## 💡 一句话要点

**提出P/D-Device以解决云端与设备间资源瓶颈问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `云计算` `设备协作` `响应时间优化` `吞吐量提升`

## 📋 核心要点

1. 现有方法在解码阶段生成的令牌过多，导致云端资源占用过长，无法提高吞吐量。
2. 论文提出将大型语言模型分离到云端和设备之间，云端负责预填充，设备则快速响应用户请求。
3. 实验结果显示，首次令牌时间减少至少60%，最大输出令牌时间为数十毫秒，云端吞吐量提升至15倍。

## 📝 摘要（中文）

在工业实践中，分散的大型语言模型被广泛应用以提升性能。然而，在解码阶段生成的过多令牌占用资源，导致云端无法实现更高的吞吐量。同时，由于设备资源有限，随着提示长度的增加，首次令牌时间（TTFT）显著增加。为了解决这一资源瓶颈，本文提出将大型语言模型分离到云端和设备之间。具体而言，云端在预填充阶段为每个设备提供部分内容，设备在接收到第一个令牌后立即响应用户，从而降低TTFT。后续令牌通过速度控制器平滑呈现，直到设备赶上进度。实验结果表明，TTFT减少至少60%，最大TPOT约为数十毫秒，云端吞吐量提高至15倍。

## 🔬 方法详解

**问题定义**：本文旨在解决云端与设备间的资源瓶颈问题，现有方法在解码阶段生成过多令牌，导致云端吞吐量低且设备首次令牌时间显著增加。

**核心思路**：通过将大型语言模型分离到云端和设备之间，云端在预填充阶段为设备提供部分内容，设备在接收到第一个令牌后立即响应用户，从而降低TTFT。

**技术框架**：整体架构包括云端预填充和设备响应两个主要阶段。云端生成初始令牌后，设备快速响应用户请求，随后通过速度控制器平滑呈现后续令牌，直到设备赶上进度。

**关键创新**：最重要的技术创新在于将大型语言模型的处理分散到云端和设备之间，显著降低了设备的响应延迟，并提高了云端的资源利用率。

**关键设计**：在设计中，采用速度控制器来平滑后续令牌的呈现，同时利用云端生成的中间数据来优化设备的推理过程。

## 📊 实验亮点

实验结果显示，首次令牌时间（TTFT）减少至少60%，最大输出令牌时间（TPOT）约为数十毫秒，云端吞吐量提升至15倍，验证了P/D-Device方案的有效性和优越性。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、在线客服和实时翻译等场景。通过优化云端与设备间的协作，可以显著提升用户体验，降低响应延迟，满足对实时性要求较高的应用需求，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Serving disaggregated large language models has been widely adopted in industrial practice for enhanced performance. However, too many tokens generated in decoding phase, i.e., occupying the resources for a long time, essentially hamper the cloud from achieving a higher throughput. Meanwhile, due to limited on-device resources, the time to first token (TTFT), i.e., the latency of prefill phase, increases dramatically with the growth on prompt length. In order to concur with such a bottleneck on resources, i.e., long occupation in cloud and limited on-device computing capacity, we propose to separate large language model between cloud and devices. That is, the cloud helps a portion of the content for each device, only in its prefill phase. Specifically, after receiving the first token from the cloud, decoupling with its own prefill, the device responds to the user immediately for a lower TTFT. Then, the following tokens from cloud are presented via a speed controller for smoothed TPOT (the time per output token), until the device catches up with the progress. On-device prefill is then amortized using received tokens while the resource usage in cloud is controlled. Moreover, during cloud prefill, the prompt can be refined, using those intermediate data already generated, to further speed up on-device inference. We implement such a scheme P/D-Device, and confirm its superiority over other alternatives. We further propose an algorithm to decide the best settings. Real-trace experiments show that TTFT decreases at least 60%, maximum TPOT is about tens of milliseconds, and cloud throughput increases by up to 15x.

