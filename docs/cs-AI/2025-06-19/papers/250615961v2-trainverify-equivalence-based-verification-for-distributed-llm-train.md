---
layout: default
title: "TrainVerify: Equivalence-Based Verification for Distributed LLM Training"
---

# TrainVerify: Equivalence-Based Verification for Distributed LLM Training

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15961" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15961v2</a>
  <a href="https://arxiv.org/pdf/2506.15961.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15961v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15961v2', 'TrainVerify: Equivalence-Based Verification for Distributed LLM Training')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yunchi Lu, Youshan Miao, Cheng Tan, Peng Huang, Yi Zhu, Xian Zhang, Fan Yang

**分类**: cs.DC, cs.AI, cs.LG

**发布日期**: 2025-06-19 (更新: 2025-06-24)

---

## 💡 一句话要点

**提出TrainVerify以解决分布式大语言模型训练的验证问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `分布式训练` `模型验证` `深度学习` `形状简化` `并行算法` `计算效率`

## 📋 核心要点

1. 现有的分布式大语言模型训练方法缺乏有效的验证机制，容易导致无声错误，造成资源浪费。
2. TrainVerify通过引入形状简化技术和阶段性并行验证算法，提供了一种可验证的分布式训练方案。
3. TrainVerify成功验证了Llama3和DeepSeek-V3的训练计划，展示了其在处理超大规模模型时的有效性。

## 📝 摘要（中文）

在大规模训练大语言模型（LLMs）时，通常需要在数千个设备上并行执行，这导致巨大的计算成本。然而，这些昂贵的分布式训练往往缺乏验证，容易出现无声错误，可能浪费数百万小时的GPU计算资源。为此，本文提出了TrainVerify，一个用于可验证的分布式LLM训练的系统。TrainVerify通过将深度学习模型的逻辑规范作为真值，正式验证分布式并行执行计划是否在数学上等价。由于LLMs的规模庞大，直接验证非常困难，因此TrainVerify引入了形状简化技术和阶段性并行验证算法，显著降低了复杂性，同时保持了形式上的正确性。TrainVerify能够扩展到前沿的LLMs，包括成功验证Llama3（405B）和DeepSeek-V3（671B）的训练计划。

## 🔬 方法详解

**问题定义**：本文旨在解决分布式大语言模型训练中缺乏有效验证的问题。现有方法在面对数十亿变量和复杂计算图时，难以进行直接验证，导致潜在的错误未被发现。

**核心思路**：TrainVerify的核心思路是通过将模型的逻辑规范作为真值，利用数学等价性进行验证。通过形状简化和阶段性验证，降低了验证的复杂性，同时确保了结果的正确性。

**技术框架**：TrainVerify的整体架构包括输入模型的逻辑规范、执行分布式训练计划、应用形状简化技术、执行阶段性并行验证等主要模块。每个阶段都旨在逐步验证训练计划的正确性。

**关键创新**：TrainVerify的主要创新在于引入了形状简化技术和阶段性并行验证算法，这与传统的直接验证方法相比，显著降低了计算复杂性并提高了验证效率。

**关键设计**：在设计中，TrainVerify采用了特定的参数设置和损失函数，以确保在不同阶段的验证过程中，能够有效捕捉到潜在的错误，并保持模型的形式正确性。

## 📊 实验亮点

TrainVerify在验证Llama3（405B）和DeepSeek-V3（671B）训练计划时，成功展示了其高效性和准确性。通过引入形状简化和阶段性验证，显著降低了验证复杂性，提升了验证效率，确保了训练过程的正确性。

## 🎯 应用场景

TrainVerify的研究成果具有广泛的应用潜力，尤其是在大规模深度学习模型的训练和验证领域。其可验证的特性可以帮助研究人员和工程师在开发和部署大语言模型时，确保模型的正确性和可靠性，从而节省计算资源和时间，提升整体效率。

## 📄 摘要（原文）

> Training large language models (LLMs) at scale requires parallel execution across thousands of devices, incurring enormous computational costs. Yet, these costly distributed trainings are rarely verified, leaving them prone to silent errors and potentially wasting millions of GPU hours. We introduce TrainVerify, a system for verifiable distributed training of LLMs. Given a deep learning model's logical specification as the ground truth, TrainVerify formally verifies that a distributed parallel execution plan is mathematically equivalent to it. Direct verification is notoriously difficult due to the sheer scale of LLMs which often involves billions of variables and highly intricate computation graphs. Therefore, TrainVerify introduces shape-reduction techniques and a stage-wise parallel verification algorithm that significantly reduces complexity while preserving formal correctness. TrainVerify scales to frontier LLMs, including the successful verification of the Llama3 (405B) and DeepSeek-V3 (671B) training plans.

