---
layout: default
title: "OpenCUA: Open Foundations for Computer-Use Agents"
---

# OpenCUA: Open Foundations for Computer-Use Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09123" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09123v3</a>
  <a href="https://arxiv.org/pdf/2508.09123.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09123v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09123v3', 'OpenCUA: Open Foundations for Computer-Use Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinyuan Wang, Bowen Wang, Dunjie Lu, Junlin Yang, Tianbao Xie, Junli Wang, Jiaqi Deng, Xiaole Guo, Yiheng Xu, Chen Henry Wu, Zhennan Shen, Zhuokai Li, Ryan Li, Xiaochuan Li, Junda Chen, Boyuan Zheng, Peihang Li, Fangyu Lei, Ruisheng Cao, Yeqiao Fu, Dongchan Shin, Martin Shin, Jiarui Hu, Yuyan Wang, Jixuan Chen, Yuxiao Ye, Danyang Zhang, Dikang Du, Hao Hu, Huarong Chen, Zaida Zhou, Haotian Yao, Ziwei Chen, Qizheng Gu, Yipu Wang, Heng Wang, Diyi Yang, Victor Zhong, Flood Sung, Y. Charles, Zhilin Yang, Tao Yu

**分类**: cs.AI, cs.CV

**发布日期**: 2025-08-12 (更新: 2025-10-04)

**备注**: Updata author list, modify first page format, correct typos

---

## 💡 一句话要点

**提出OpenCUA框架以推动计算机使用代理的研究与应用**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `计算机使用代理` `开源框架` `视觉语言模型` `数据集` `长链思维推理` `自动化任务` `人机交互`

## 📋 核心要点

1. 现有的计算机使用代理系统在透明性和可访问性方面存在不足，限制了研究者对其能力和风险的深入分析。
2. OpenCUA框架通过提供注释基础设施和大规模数据集，旨在提升CUA系统的研究和应用，促进其开放性和可扩展性。
3. 实验结果表明，OpenCUA-72B在多个基准测试中表现优异，特别是在OSWorld-Verified上达到了45.0%的成功率，显著提升了开源模型的性能。

## 📝 摘要（中文）

视觉语言模型在自动化多种计算机任务方面展现了卓越的能力，然而，现有的计算机使用代理（CUA）系统的关键细节仍然封闭。为了填补这一空白，本文提出了OpenCUA，一个全面的开源框架，旨在扩展CUA数据和基础模型。该框架包括一个注释基础设施、首个大规模计算机使用任务数据集AgentNet，以及一个可扩展的管道，将演示转化为状态-动作对。我们的端到端代理模型在CUA基准测试中表现出色，OpenCUA-72B在OSWorld-Verified上实现了45.0%的平均成功率，确立了开源模型的新状态。我们还发布了注释工具、数据集、代码和模型，以促进CUA研究的开放基础。

## 🔬 方法详解

**问题定义**：本文旨在解决现有计算机使用代理（CUA）系统的封闭性和缺乏透明性的问题，限制了研究者对其能力、局限性和风险的深入分析。

**核心思路**：OpenCUA框架通过构建一个全面的开源平台，提供注释基础设施和大规模数据集，旨在促进CUA的研究和应用，提升其开放性和可扩展性。

**技术框架**：OpenCUA框架由三个主要模块组成：注释基础设施用于捕捉人类计算机使用演示；AgentNet数据集涵盖了三个操作系统和200多个应用程序与网站；可扩展的管道将演示转化为状态-动作对，支持长链思维推理。

**关键创新**：OpenCUA的最大创新在于其开放性和可扩展性，尤其是AgentNet数据集的构建和长链思维推理的引入，使得模型在数据规模增加时仍能保持良好的性能。

**关键设计**：在模型设计中，采用了反映长链思维推理的状态-动作对生成机制，并通过优化参数设置和损失函数，确保模型在不同领域的良好泛化能力。实验表明，增加测试时的计算量显著提升了模型性能。

## 📊 实验亮点

OpenCUA-72B在OSWorld-Verified基准测试中实现了45.0%的平均成功率，设立了开源模型的新状态，显示出该框架在多领域的良好泛化能力和显著的性能提升，尤其是在数据规模扩大时。

## 🎯 应用场景

OpenCUA框架的潜在应用领域广泛，包括自动化办公、智能助手、教育技术等。通过提供开放的CUA研究基础，能够促进更高效的计算机交互和决策支持，推动人机协作的进一步发展。

## 📄 摘要（原文）

> Vision-language models have demonstrated impressive capabilities as computer-use agents (CUAs) capable of automating diverse computer tasks. As their commercial potential grows, critical details of the most capable CUA systems remain closed. As these agents will increasingly mediate digital interactions and execute consequential decisions on our behalf, the research community needs access to open CUA frameworks to study their capabilities, limitations, and risks. To bridge this gap, we propose OpenCUA, a comprehensive open-source framework for scaling CUA data and foundation models. Our framework consists of: (1) an annotation infrastructure that seamlessly captures human computer-use demonstrations; (2) AgentNet, the first large-scale computer-use task dataset spanning 3 operating systems and 200+ applications and websites; (3) a scalable pipeline that transforms demonstrations into state-action pairs with reflective long Chain-of-Thought reasoning that sustain robust performance gains as data scales. Our end-to-end agent models demonstrate strong performance across CUA benchmarks. In particular, OpenCUA-72B achieves an average success rate of 45.0% on OSWorld-Verified, establishing a new state-of-the-art (SOTA) among open-source models. Further analysis confirms that our approach generalizes well across domains and benefits significantly from increased test-time computation. We release our annotation tool, datasets, code, and models to build open foundations for further CUA research.

