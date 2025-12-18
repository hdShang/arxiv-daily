---
layout: default
title: Nemotron-Math: Efficient Long-Context Distillation of Mathematical Reasoning from Multi-Mode Supervision
---

# Nemotron-Math: Efficient Long-Context Distillation of Mathematical Reasoning from Multi-Mode Supervision

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15489" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15489v1</a>
  <a href="https://arxiv.org/pdf/2512.15489.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15489v1" onclick="toggleFavorite(this, '2512.15489v1', 'Nemotron-Math: Efficient Long-Context Distillation of Mathematical Reasoning from Multi-Mode Supervision')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wei Du, Shubham Toshniwal, Branislav Kisacanin, Sadegh Mahdavi, Ivan Moshkov, George Armstrong, Stephen Ge, Edgar Minasyan, Feng Chen, Igor Gitman

**分类**: cs.AI

**发布日期**: 2025-12-17

---

## 💡 一句话要点

**Nemotron-Math：通过多模式监督，高效地进行数学推理长文本蒸馏。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `数学推理` `长文本建模` `数据集构建` `多模式学习` `工具集成` `蒸馏训练` `分桶策略`

## 📋 核心要点

1. 现有数学推理数据集在推理风格多样性、长文本轨迹和有效工具集成方面存在局限性。
2. 利用gpt-oss-120b的多模式生成能力，构建大规模数学推理数据集Nemotron-Math，包含多种推理模式和工具集成。
3. 实验表明，Nemotron-Math在数学竞赛和泛化能力上均有提升，并通过分桶策略加速长文本训练。

## 📝 摘要（中文）

本文介绍了Nemotron-Math，一个大规模数学推理数据集，包含750万条解题轨迹，涵盖高、中、低三种推理模式，每种模式都提供是否集成Python工具推理（TIR）的版本。该数据集整合了8.5万道精选的AoPS问题和26.2万道来自StackExchange-Math社区的问题，结合了结构化的竞赛任务和多样化的真实数学查询。通过受控评估验证了数据集的质量。Nemotron-Math在匹配的AoPS问题上始终优于原始的OpenMathReasoning。整合StackExchange-Math显著提高了鲁棒性和泛化能力，尤其是在HLE-Math上，同时保持了数学竞赛基准上的准确性。为了支持高效的长文本训练，开发了一种顺序分桶策略，在不显著降低准确性的前提下，将128K上下文长度的微调加速2-3倍。Nemotron-Math实现了最先进的性能，包括在AIME 2024和2025上使用Python TIR达到100%的maj@16准确率。

## 🔬 方法详解

**问题定义**：现有数学推理数据集规模有限，缺乏多样化的推理风格、长文本解题过程以及与外部工具（如Python）的有效集成。这限制了模型学习复杂数学推理能力。

**核心思路**：利用大型语言模型（gpt-oss-120b）生成高质量的数学解题轨迹，构建一个大规模、多模式的数学推理数据集。通过整合来自不同来源（AoPS和StackExchange-Math）的问题，增加数据集的多样性和泛化能力。同时，引入Python工具集成，提升模型解决复杂问题的能力。

**技术框架**：Nemotron-Math数据集的构建包括以下几个阶段：问题收集与筛选、解题轨迹生成（使用gpt-oss-120b）、数据清洗与标注、以及数据集整合。为了支持长文本训练，论文提出了一种顺序分桶策略，将长文本序列分割成多个桶，并按照顺序进行训练，从而减少计算量并加速训练过程。

**关键创新**：该论文的关键创新在于：1) 构建了一个大规模、多模式的数学推理数据集Nemotron-Math，包含多种推理风格和工具集成；2) 提出了一种顺序分桶策略，用于加速长文本训练，该策略在不显著降低准确性的前提下，显著提高了训练效率；3) 整合了来自不同来源的问题，提高了模型的泛化能力。

**关键设计**：顺序分桶策略是关键设计之一。具体来说，将128K长度的上下文分割成多个桶，每个桶的长度可以根据计算资源进行调整。在训练过程中，模型按照桶的顺序进行训练，并在每个桶的末尾进行预测。损失函数采用标准的交叉熵损失函数。数据集包含高、中、低三种推理模式，以及是否集成Python工具推理（TIR）的版本，方便研究者进行对比实验。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15489v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15489v1/x2.png" alt="img_1" loading="lazy">
</figure>
</div>

## 📊 实验亮点

Nemotron-Math在AIME 2024和2025上使用Python TIR达到了100%的maj@16准确率，表明其在数学竞赛问题上的卓越性能。此外，该数据集在HLE-Math上的表现也显著提升，验证了其在复杂数学问题上的泛化能力。顺序分桶策略将128K上下文长度的微调加速了2-3倍，而没有显著降低准确性。

## 🎯 应用场景

该研究成果可应用于开发更强大的数学问题求解器，辅助数学教育，提升AI在科学计算领域的应用能力。高质量的数学推理数据集和高效的训练方法，有助于推动AI在逻辑推理、问题解决等方面的研究进展，并可能扩展到其他需要复杂推理的领域。

## 📄 摘要（原文）

> High-quality mathematical reasoning supervision requires diverse reasoning styles, long-form traces, and effective tool integration, capabilities that existing datasets provide only in limited form. Leveraging the multi-mode generation ability of gpt-oss-120b, we introduce Nemotron-Math, a large-scale mathematical reasoning dataset containing 7.5M solution traces across high, medium, and low reasoning modes, each available both with and without Python tool-integrated reasoning (TIR).
>   The dataset integrates 85K curated AoPS problems with 262K community-sourced StackExchange-Math problems, combining structured competition tasks with diverse real-world mathematical queries. We conduct controlled evaluations to assess the dataset quality.
>   Nemotron-Math consistently outperforms the original OpenMathReasoning on matched AoPS problems. Incorporating StackExchange-Math substantially improves robustness and generalization, especially on HLE-Math, while preserving accuracy on math competition benchmarks.
>   To support efficient long-context training, we develop a sequential bucketed strategy that accelerates 128K context-length fine-tuning by 2--3$\times$ without significant accuracy loss. Overall, Nemotron-Math enables state-of-the-art performance, including 100\% maj@16 accuracy on AIME 2024 and 2025 with Python TIR.

