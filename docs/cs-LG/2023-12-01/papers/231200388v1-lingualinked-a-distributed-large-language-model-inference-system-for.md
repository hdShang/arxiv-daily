---
layout: default
title: "LinguaLinked: A Distributed Large Language Model Inference System for Mobile Devices"
---

# LinguaLinked: A Distributed Large Language Model Inference System for Mobile Devices

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2312.00388" class="toolbar-btn" target="_blank">📄 arXiv: 2312.00388v1</a>
  <a href="https://arxiv.org/pdf/2312.00388.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2312.00388v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2312.00388v1', 'LinguaLinked: A Distributed Large Language Model Inference System for Mobile Devices')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junchen Zhao, Yurun Song, Simeng Liu, Ian G. Harris, Sangeetha Abdu Jyothi

**分类**: cs.LG, cs.DC, cs.NI

**发布日期**: 2023-12-01

**备注**: 16 pages, 8 figures

---

## 💡 一句话要点

**提出LinguaLinked以解决移动设备上大语言模型推理的挑战**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `移动设备` `分布式推理` `数据隐私` `负载均衡` `模型优化` `性能提升`

## 📋 核心要点

1. 现有方法在移动设备上部署大语言模型面临内存需求过高和推理效率低下的挑战。
2. LinguaLinked通过去中心化的分布式推理和优化的模型分配、数据传输及负载均衡策略来解决这些问题。
3. 实验结果表明，LinguaLinked在单线程设置下推理性能提升1.11倍至1.61倍，多线程下提升1.73倍至2.65倍。

## 📝 摘要（中文）

在移动设备上本地部署大语言模型（LLMs）面临显著挑战，主要是由于其庞大的内存需求。本文介绍了LinguaLinked，一个用于移动设备的去中心化分布式LLM推理系统。LinguaLinked通过多个可信设备的协作执行推理任务，确保数据隐私。该系统采用三项关键策略：首先，优化的模型分配技术将LLMs进行分段，并利用线性优化将段与每个设备的能力对齐；其次，优化的数据传输机制确保模型段之间高效、结构化的数据流，同时保持原始模型结构的完整性；最后，LinguaLinked集成了一个运行时负载均衡器，主动监控并重新分配任务，以防止瓶颈，提高系统的整体效率和响应能力。通过对各种移动设备的广泛测试，LinguaLinked在保持一致的吞吐量和最小延迟的同时，促进了高效的LLM推理。

## 🔬 方法详解

**问题定义**：本论文旨在解决在移动设备上本地部署大语言模型时的内存需求和推理效率问题。现有方法往往无法满足移动设备的资源限制，导致推理性能不足。

**核心思路**：LinguaLinked的核心思路是通过去中心化的方式，将推理任务分散到多个可信设备上执行，从而降低单个设备的负担，并确保数据隐私。

**技术框架**：LinguaLinked的整体架构包括三个主要模块：优化的模型分配模块、数据传输机制和运行时负载均衡器。模型分配模块负责将LLMs进行分段并分配给设备，数据传输机制确保数据流的高效性，而负载均衡器则监控任务分配，动态调整以优化性能。

**关键创新**：LinguaLinked的关键创新在于其优化的模型分配和数据传输机制，这与现有方法的集中式推理模式形成鲜明对比，显著提高了移动设备的推理效率。

**关键设计**：在模型分配中，采用线性优化算法来匹配模型段与设备能力；数据传输机制则设计为高效且结构化，以保持模型完整性；负载均衡器通过实时监控任务状态，确保各设备负载均匀，避免性能瓶颈。

## 📊 实验亮点

LinguaLinked在多种移动设备上的实验结果显示，单线程推理性能提升1.11倍至1.61倍，多线程下提升1.73倍至2.65倍，运行时负载均衡实现了整体推理加速1.29倍至1.32倍，显著优于基线性能。

## 🎯 应用场景

LinguaLinked的研究成果具有广泛的应用潜力，尤其是在需要高效处理自然语言的移动应用场景中，如智能助手、实时翻译和个性化推荐系统。通过在移动设备上实现高效的LLM推理，LinguaLinked能够提升用户体验，并推动智能移动应用的发展。

## 📄 摘要（原文）

> Deploying Large Language Models (LLMs) locally on mobile devices presents a significant challenge due to their extensive memory requirements. In this paper, we introduce LinguaLinked, a system for decentralized, distributed LLM inference on mobile devices. LinguaLinked enables collaborative execution of the inference task across multiple trusted devices. LinguaLinked ensures data privacy by processing information locally. LinguaLinked uses three key strategies. First, an optimized model assignment technique segments LLMs and uses linear optimization to align segments with each device's capabilities. Second, an optimized data transmission mechanism ensures efficient and structured data flow between model segments while also maintaining the integrity of the original model structure. Finally, LinguaLinked incorporates a runtime load balancer that actively monitors and redistributes tasks among mobile devices to prevent bottlenecks, enhancing the system's overall efficiency and responsiveness. We demonstrate that LinguaLinked facilitates efficient LLM inference while maintaining consistent throughput and minimal latency through extensive testing across various mobile devices, from high-end to low-end Android devices. In our evaluations, compared to the baseline, LinguaLinked achieves an inference performance acceleration of $1.11\times$ to $1.61\times$ in single-threaded settings, $1.73\times$ to $2.65\times$ with multi-threading. Additionally, runtime load balancing yields an overall inference acceleration of $1.29\times$ to $1.32\times$.

