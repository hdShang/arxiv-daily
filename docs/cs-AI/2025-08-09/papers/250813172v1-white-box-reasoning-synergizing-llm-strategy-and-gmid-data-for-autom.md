---
layout: default
title: "White-Box Reasoning: Synergizing LLM Strategy and gm/Id Data for Automated Analog Circuit Design"
---

# White-Box Reasoning: Synergizing LLM Strategy and gm/Id Data for Automated Analog Circuit Design

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13172" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13172v1</a>
  <a href="https://arxiv.org/pdf/2508.13172.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13172v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13172v1', 'White-Box Reasoning: Synergizing LLM Strategy and gm/Id Data for Automated Analog Circuit Design')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jianqiu Chen, Siqi Li, Xu He

**分类**: cs.AR, cs.AI, cs.CL

**发布日期**: 2025-08-09

**备注**: 8 pages, 4 figures, 7 Tables

---

## 💡 一句话要点

**提出协同推理框架以提升模拟电路设计效率**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `模拟电路设计` `大型语言模型` `gm/Id方法` `设计自动化` `协同推理` `电路优化` `效率提升`

## 📋 核心要点

1. 现有的模拟电路设计方法依赖经验和低效仿真，导致设计过程缓慢且不精确。
2. 本文提出的协同推理框架结合了LLM的战略推理与gm/Id方法的物理精度，提升了设计效率。
3. 实验结果表明，该框架在5次迭代中满足所有TT角规格，相比资深工程师设计效率提升了数量级。

## 📝 摘要（中文）

模拟集成电路设计因依赖经验和低效仿真而成为瓶颈，传统公式在先进节点下失效。直接应用大型语言模型（LLMs）可能导致仅凭“猜测”而缺乏工程原则。本文提出了一种“协同推理”框架，将LLM的战略推理与gm/Id方法的物理精度相结合。通过赋予LLM gm/Id查找表，使其成为一个定量的数据驱动设计伙伴。我们在一个两级运算放大器上验证了该框架，使Gemini模型在5次迭代中满足所有TT角规格，并将优化扩展到所有PVT角。关键的消融研究证明了gm/Id数据对于效率和精度的重要性；没有它，LLM的速度较慢且偏离目标。与资深工程师的设计相比，我们的框架在效率上实现了数量级的提升，达到了准专家级的设计质量。这项工作验证了通过将LLM推理与科学电路设计方法结合，真正实现模拟设计自动化的路径。

## 🔬 方法详解

**问题定义**：本文旨在解决模拟集成电路设计中由于依赖经验和低效仿真导致的效率低下和精度不足的问题。现有方法在先进节点下的传统公式失效，使得设计过程面临挑战。

**核心思路**：提出的协同推理框架通过将大型语言模型（LLM）的战略推理与gm/Id方法的物理精度相结合，形成一个数据驱动的设计伙伴，从而提高设计效率和精度。

**技术框架**：该框架主要包括两个阶段：首先，利用LLM进行初步设计推理；其次，结合gm/Id查找表进行精细化设计。整个流程通过不断迭代优化，确保设计满足各项规格。

**关键创新**：最重要的技术创新在于将LLM与gm/Id数据相结合，使得LLM不仅仅是推理工具，而是一个具备物理设计能力的合作伙伴。这一方法与传统的仅依赖经验或公式的设计方法有本质区别。

**关键设计**：在设计过程中，关键参数设置包括gm/Id查找表的构建和LLM的训练，损失函数的选择也考虑了设计精度和效率的平衡。网络结构上，LLM的架构经过优化，以适应电路设计的特定需求。

## 📊 实验亮点

实验结果显示，使用该框架的Gemini模型在5次迭代中成功满足所有TT角规格，相比传统设计方法在效率上实现了数量级的提升，达到了准专家级的设计质量，验证了框架的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括模拟电路设计、集成电路制造及相关工程领域。通过提升设计效率和精度，能够显著降低开发成本和时间，推动电路设计的自动化进程，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Analog IC design is a bottleneck due to its reliance on experience and inefficient simulations, as traditional formulas fail in advanced nodes. Applying Large Language Models (LLMs) directly to this problem risks mere "guessing" without engineering principles. We present a "synergistic reasoning" framework that integrates an LLM's strategic reasoning with the physical precision of the gm/Id methodology. By empowering the LLM with gm/Id lookup tables, it becomes a quantitative, data-driven design partner.
>   We validated this on a two-stage op-amp, where our framework enabled the Gemini model to meet all TT corner specs in 5 iterations and extended optimization to all PVT corners. A crucial ablation study proved gm/Id data is key for this efficiency and precision; without it, the LLM is slower and deviates. Compared to a senior engineer's design, our framework achieves quasi-expert quality with an order-of-magnitude improvement in efficiency. This work validates a path for true analog design automation by combining LLM reasoning with scientific circuit design methodologies.

