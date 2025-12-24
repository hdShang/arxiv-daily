---
layout: default
title: "ABBA-Adapters: Efficient and Expressive Fine-Tuning of Foundation Models"
---

# ABBA-Adapters: Efficient and Expressive Fine-Tuning of Foundation Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14238" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14238v3</a>
  <a href="https://arxiv.org/pdf/2505.14238.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14238v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14238v3', 'ABBA-Adapters: Efficient and Expressive Fine-Tuning of Foundation Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Raghav Singhal, Kaustubh Ponkshe, Rohit Vartak, Praneeth Vepakomma

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-05-20 (更新: 2025-10-02)

**备注**: Raghav Singhal, Kaustubh Ponkshe, and Rohit Vartak contributed equally to this work

**🔗 代码/项目**: [GITHUB](https://github.com/CERT-Lab/abba)

---

## 💡 一句话要点

**提出ABBA以解决大语言模型高效适应新领域的问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `参数高效微调` `大语言模型` `Hadamard积` `低秩矩阵` `模型适应性` `算术推理` `常识推理`

## 📋 核心要点

1. 现有的参数高效微调方法在表达能力上受到限制，难以充分适应新领域。
2. ABBA通过将更新表示为两个独立可学习的低秩矩阵的Hadamard积，提供了更高的表达能力。
3. ABBA在多个模型上实现了算术和常识推理基准的最先进结果，超越了现有方法。

## 📝 摘要（中文）

大型语言模型在多种任务中表现出色，但如何高效地将其适应新领域仍然是一个关键挑战。参数高效微调（PEFT）方法通过引入轻量级可训练模块来解决这一问题，同时保持大部分预训练权重不变。现有方法如LoRA通过低秩分解建模更新，但其表达能力受到秩的限制。ABBA是一种新的PEFT架构，它将更新重新参数化为两个独立可学习的低秩矩阵的Hadamard积，从而完全解耦更新与预训练权重，使得两个组件可以自由优化。实验表明，ABBA在算术和常识推理基准上取得了最先进的结果，显著超越现有PEFT方法。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型在新领域适应时的高效微调问题。现有方法如LoRA和HiRA在表达能力上存在局限，难以充分利用预训练模型的潜力。

**核心思路**：ABBA提出了一种新的参数高效微调架构，通过将更新表示为两个独立可学习的低秩矩阵的Hadamard积，完全解耦更新与预训练权重，从而实现更高的表达能力。

**技术框架**：ABBA的整体架构包括两个独立的低秩矩阵，这两个矩阵通过Hadamard积与固定的预训练权重结合，形成最终的模型更新。该框架允许在保持参数预算不变的情况下，优化更新的自由度。

**关键创新**：ABBA的主要创新在于其完全解耦的更新机制，与现有方法相比，提供了更大的灵活性和表达能力，能够更好地适应不同的任务需求。

**关键设计**：ABBA的设计中，低秩矩阵的秩和学习策略是关键参数设置，损失函数则结合了模型的推理能力与更新的有效性，确保了模型在新领域的适应性。

## 📊 实验亮点

ABBA在算术和常识推理基准上取得了最先进的结果，显著超越了现有的PEFT方法。具体而言，ABBA在多个模型上实现了性能提升，验证了其在相同参数预算下的高表达能力。

## 🎯 应用场景

ABBA的研究成果在多个领域具有广泛的应用潜力，包括自然语言处理、对话系统和智能助手等。通过提高大语言模型的适应能力，ABBA可以帮助企业和研究机构更高效地部署和优化模型，提升智能应用的性能和用户体验。

## 📄 摘要（原文）

> Large Language Models have demonstrated strong performance across a wide range of tasks, but adapting them efficiently to new domains remains a key challenge. Parameter-Efficient Fine-Tuning (PEFT) methods address this by introducing lightweight, trainable modules while keeping most pre-trained weights fixed. The prevailing approach, LoRA, models updates using a low-rank decomposition, but its expressivity is inherently constrained by the rank. Recent methods like HiRA aim to increase expressivity by incorporating a Hadamard product with the frozen weights, but still rely on the structure of the pre-trained model. We introduce ABBA, a new PEFT architecture that reparameterizes the update as a Hadamard product of two independently learnable low-rank matrices. In contrast to prior work, ABBA fully decouples the update from the pre-trained weights, enabling both components to be optimized freely. This leads to significantly higher expressivity under the same parameter budget, a property we validate through matrix reconstruction experiments. Empirically, ABBA achieves state-of-the-art results on arithmetic and commonsense reasoning benchmarks, consistently outperforming existing PEFT methods by a significant margin across multiple models. Our code is publicly available at: https://github.com/CERT-Lab/abba.

