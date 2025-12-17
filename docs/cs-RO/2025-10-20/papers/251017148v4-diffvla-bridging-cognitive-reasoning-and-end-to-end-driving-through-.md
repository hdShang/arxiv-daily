---
layout: default
title: DiffVLA++: Bridging Cognitive Reasoning and End-to-End Driving through Metric-Guided Alignment
---

# DiffVLA++: Bridging Cognitive Reasoning and End-to-End Driving through Metric-Guided Alignment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.17148" class="toolbar-btn" target="_blank">📄 arXiv: 2510.17148v4</a>
  <a href="https://arxiv.org/pdf/2510.17148.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.17148v4" onclick="toggleFavorite(this, '2510.17148v4', 'DiffVLA++: Bridging Cognitive Reasoning and End-to-End Driving through Metric-Guided Alignment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yu Gao, Anqing Jiang, Yiru Wang, Wang Jijun, Hao Jiang, Zhigang Sun, Heng Yuwen, Wang Shuo, Hao Zhao, Sun Hao

**分类**: cs.RO, cs.CV

**发布日期**: 2025-10-20 (更新: 2025-11-04)

---

## 💡 一句话要点

**DiffVLA++：通过度量引导对齐桥接认知推理与端到端驾驶**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动驾驶` `端到端学习` `视觉语言动作模型` `认知推理` `轨迹规划`

## 📋 核心要点

1. 端到端驾驶模型缺乏世界知识，难以泛化到复杂场景，而VLA模型虽然具备推理能力，但3D推理不足导致动作不合理。
2. DiffVLA++通过度量引导对齐，融合VLA模型的认知推理和端到端模型的物理可行性，从而提升自动驾驶性能。
3. 实验表明，DiffVLA++在ICCV 2025自动驾驶大赛排行榜上取得了显著成果，EPDMS达到了49.12。

## 📝 摘要（中文）

传统的端到端(E2E)驾驶模型在生成物理上可行的轨迹方面很有效，但由于缺乏理解和推理周围环境的基本世界知识，通常无法推广到长尾场景。相比之下，视觉-语言-动作(VLA)模型利用世界知识来处理具有挑战性的案例，但其有限的3D推理能力可能导致物理上不可行的动作。本文介绍了一种增强的自动驾驶框架DiffVLA++，该框架通过度量引导对齐显式地桥接认知推理和E2E规划。首先，我们构建了一个VLA模块，直接生成语义上接地的驾驶轨迹。其次，我们设计了一个具有密集轨迹词汇表的E2E模块，以确保物理可行性。第三，也是最关键的是，我们引入了一个度量引导的轨迹评分器，用于引导和对齐VLA和E2E模块的输出，从而整合它们的互补优势。在ICCV 2025自动驾驶大赛排行榜上的实验表明，DiffVLA++实现了49.12的EPDMS。

## 🔬 方法详解

**问题定义**：现有端到端驾驶模型在处理长尾场景时泛化能力不足，因为它们缺乏对周围环境的理解和推理能力。而视觉-语言-动作（VLA）模型虽然具备一定的推理能力，但其3D推理能力有限，可能导致产生物理上不可行的驾驶行为。因此，如何将认知推理和物理可行性结合起来，是当前自动驾驶研究面临的一个重要挑战。

**核心思路**：DiffVLA++的核心思路是通过度量引导的对齐，将VLA模型的认知推理能力和端到端模型的物理可行性相结合。具体来说，该方法首先分别构建VLA模块和E2E模块，然后通过一个度量引导的轨迹评分器，对两个模块的输出进行对齐和融合，从而生成既符合语义逻辑又物理可行的驾驶轨迹。

**技术框架**：DiffVLA++框架主要包含三个模块：VLA模块、E2E模块和度量引导的轨迹评分器。VLA模块负责生成语义上合理的驾驶轨迹，E2E模块负责生成物理上可行的驾驶轨迹，而轨迹评分器则负责根据一定的度量标准，对两个模块的输出进行评分和对齐，最终生成融合了两者优势的驾驶轨迹。

**关键创新**：DiffVLA++的关键创新在于提出了度量引导的轨迹评分器，该评分器能够有效地对齐和融合VLA模块和E2E模块的输出。通过这种方式，DiffVLA++能够充分利用VLA模型的认知推理能力和E2E模型的物理可行性，从而生成更加合理和安全的驾驶轨迹。

**关键设计**：VLA模块直接生成语义接地的驾驶轨迹，E2E模块使用密集轨迹词汇表确保物理可行性。度量引导的轨迹评分器是关键，其具体度量标准和对齐策略（例如损失函数的设计、参数的权重分配等）是影响最终性能的重要因素，但论文摘要中未详细说明，具体实现未知。

## 📊 实验亮点

DiffVLA++在ICCV 2025自动驾驶大赛排行榜上取得了显著成果，EPDMS达到了49.12。这一结果表明，DiffVLA++能够有效地融合认知推理和物理可行性，从而提升自动驾驶系统的性能。具体的基线模型和提升幅度未知。

## 🎯 应用场景

DiffVLA++具有广泛的应用前景，可用于提升自动驾驶系统的安全性和可靠性，尤其是在复杂和不确定的交通环境中。该研究成果还可以应用于机器人导航、智能交通管理等领域，促进人工智能技术在交通领域的应用和发展。

## 📄 摘要（原文）

> Conventional end-to-end (E2E) driving models are effective at generating physically plausible trajectories, but often fail to generalize to long-tail scenarios due to the lack of essential world knowledge to understand and reason about surrounding environments. In contrast, Vision-Language-Action (VLA) models leverage world knowledge to handle challenging cases, but their limited 3D reasoning capability can lead to physically infeasible actions. In this work we introduce DiffVLA++, an enhanced autonomous driving framework that explicitly bridges cognitive reasoning and E2E planning through metric-guided alignment. First, we build a VLA module directly generating semantically grounded driving trajectories. Second, we design an E2E module with a dense trajectory vocabulary that ensures physical feasibility. Third, and most critically, we introduce a metric-guided trajectory scorer that guides and aligns the outputs of the VLA and E2E modules, thereby integrating their complementary strengths. The experiment on the ICCV 2025 Autonomous Grand Challenge leaderboard shows that DiffVLA++ achieves EPDMS of 49.12.

