---
layout: default
title: Governance-Aware Hybrid Fine-Tuning for Multilingual Large Language Models
---

# Governance-Aware Hybrid Fine-Tuning for Multilingual Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17344" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17344v1</a>
  <a href="https://arxiv.org/pdf/2512.17344.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17344v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17344v1', 'Governance-Aware Hybrid Fine-Tuning for Multilingual Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haomin Qi, Chengbo Huang, Zihan Dai, Yunkai Gao

**分类**: cs.CL

**发布日期**: 2025-12-19

**备注**: 11 pages, 4 figures, 6 tables. arXiv admin note: substantial text overlap with arXiv:2507.18076

**期刊**: 2025 IEEE International Conference on Big Data

---

## 💡 一句话要点

**提出一种治理感知的混合微调框架，用于多语言大语言模型的低资源自适应。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多语言模型` `低资源学习` `参数高效微调` `数据治理` `正交变换`

## 📋 核心要点

1. 现有方法在低资源场景下微调多语言大语言模型时，难以兼顾准确性、校准性和跨语言公平性，且计算成本高昂。
2. 提出一种混合微调框架，结合梯度对齐的低秩更新和结构化正交变换，并引入酉约束，以稳定优化过程。
3. 实验表明，该方法在XNLI和FLORES数据集上优于现有PEFT基线，同时提高了概率校准和对拼写变体的鲁棒性。

## 📝 摘要（中文）

本文提出了一种治理感知的混合微调框架，用于多语言大语言模型的低资源自适应。该核心算法结合了梯度对齐的低秩更新与结构化正交变换，通过逐层混合并在选定的子层中引入酉约束来稳定深度优化。结合轻量级的、无标签的数据治理步骤，包括语言识别、近重复删除和质量过滤，该框架旨在在严格的计算预算下提高准确性、校准性和跨语言对等性。在XNLI和FLORES上的实验表明，混合方法在强大的PEFT基线上实现了持续的收益，同时保持了方向平衡并改善了概率校准。它对轻量级的拼写变体更具弹性，并且受益于简单的数据治理步骤。训练占用空间测量表明开销适中，并且具有良好的成本-质量边界。总之，这些结果表明，混合和酉PEFT在与实际数据治理相结合时，为资源高效的多语言自适应提供了一条稳定且易于访问的路径。

## 🔬 方法详解

**问题定义**：本文旨在解决多语言大语言模型在低资源场景下的微调问题。现有方法通常面临以下痛点：1) 准确性不足，尤其是在目标语言数据稀缺时；2) 模型校准性差，预测概率与实际置信度不符；3) 跨语言公平性难以保证，不同语言的表现差异较大；4) 微调成本高昂，难以在有限的计算资源下完成。

**核心思路**：本文的核心思路是结合梯度对齐的低秩更新和结构化正交变换，并引入酉约束，以实现高效且稳定的微调。梯度对齐的低秩更新可以减少需要训练的参数量，降低计算成本；结构化正交变换可以保持模型参数的正交性，避免梯度消失或爆炸；酉约束可以进一步稳定优化过程，提高模型的泛化能力。此外，还引入了数据治理步骤，包括语言识别、近重复删除和质量过滤，以提高训练数据的质量。

**技术框架**：该框架主要包含以下几个模块：1) 数据治理模块：对原始数据进行预处理，包括语言识别、近重复删除和质量过滤；2) 混合微调模块：结合梯度对齐的低秩更新和结构化正交变换，对模型进行微调；3) 酉约束模块：在选定的子层中引入酉约束，以稳定优化过程；4) 评估模块：评估模型在准确性、校准性和跨语言公平性等方面的表现。

**关键创新**：本文最重要的技术创新点在于提出了治理感知的混合微调方法，该方法结合了多种技术手段，以实现高效且稳定的微调。与现有方法相比，该方法不仅降低了计算成本，还提高了模型的准确性、校准性和跨语言公平性。此外，数据治理步骤的引入也提高了训练数据的质量，进一步提升了模型的性能。

**关键设计**：在混合微调模块中，采用了梯度对齐的低秩更新，具体来说，使用LoRA (Low-Rank Adaptation) 方法，只训练少量新增的低秩矩阵，而冻结预训练模型的参数。在结构化正交变换中，使用了 Householder 变换。在酉约束模块中，使用了 Cayley 变换来参数化酉矩阵。损失函数包括交叉熵损失和正则化项，用于约束模型参数。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17344v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17344v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17344v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该混合微调方法在XNLI和FLORES数据集上均优于现有的PEFT基线。例如，在XNLI数据集上，该方法在准确率方面取得了显著提升，同时保持了良好的校准性和跨语言公平性。此外，该方法对轻量级的拼写变体具有更强的鲁棒性，并且受益于简单的数据治理步骤。训练成本分析表明，该方法具有良好的成本-质量比。

## 🎯 应用场景

该研究成果可应用于多语言机器翻译、跨语言信息检索、多语言对话系统等领域。通过低成本地将大型语言模型适配到各种语言和场景，可以有效提升模型的性能和用户体验，尤其是在低资源语言场景下具有重要价值。未来，该方法有望进一步推广到更多自然语言处理任务中。

## 📄 摘要（原文）

> We present a governance-aware hybrid fine-tuning framework for multilingual, low-resource adaptation of large language models. The core algorithm combines gradient-aligned low-rank updates with structured orthogonal transformations through layer-wise mixing and introduces unitary constraints in selected sub-layers to stabilize deep optimization. In tandem with lightweight, label-free data governance steps, including language identification, near-duplicate removal, and quality filtering, the framework targets accuracy, calibration, and cross-language parity under tight compute budgets. Across XNLI and FLORES, the hybrid approach delivers consistent gains over strong PEFT baselines while maintaining directional balance and improving probability calibration, as shown in Tables II and III. It is more resilient to lightweight orthographic variants, as shown in Table IV, and benefits additively from simple governance steps, as shown in Table V. Training footprint measurements indicate modest overhead and a favorable cost-quality frontier, as shown in Table VI and Figure 2. Together, these results show that hybrid and unitary PEFT provide a stable and accessible path to resource-efficient multilingual adaptation when paired with practical data governance.

