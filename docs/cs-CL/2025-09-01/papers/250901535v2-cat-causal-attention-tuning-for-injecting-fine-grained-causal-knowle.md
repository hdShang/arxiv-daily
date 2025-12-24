---
layout: default
title: "CAT: Causal Attention Tuning For Injecting Fine-grained Causal Knowledge into Large Language Models"
---

# CAT: Causal Attention Tuning For Injecting Fine-grained Causal Knowledge into Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.01535" class="toolbar-btn" target="_blank">📄 arXiv: 2509.01535v2</a>
  <a href="https://arxiv.org/pdf/2509.01535.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.01535v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.01535v2', 'CAT: Causal Attention Tuning For Injecting Fine-grained Causal Knowledge into Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kairong Han, Wenshuo Zhao, Ziyu Zhao, JunJian Ye, Lujia Pan, Kun Kuang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-01 (更新: 2025-09-09)

**备注**: Accepted to EMNLP2025 Main conference

**🔗 代码/项目**: [GITHUB](https://github.com/Kairong-Han/CAT)

---

## 💡 一句话要点

**提出因果注意力调整（CAT）方法，将细粒度因果知识注入大型语言模型。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `因果推理` `大型语言模型` `注意力机制` `分布外泛化` `因果知识注入`

## 📋 核心要点

1. 大型语言模型在利用因果知识方面存在不足，容易捕获虚假相关性，导致泛化能力差，尤其是在分布外场景。
2. 提出因果注意力调整（CAT）方法，通过自动化流程生成token级别的因果信号，并使用Re-Attention机制引导模型关注因果结构。
3. 实验表明，CAT方法在Spurious Token Game基准和下游任务上均取得了显著提升，尤其是在分布外场景下，模型性能得到大幅改善。

## 📝 摘要（中文）

大型语言模型（LLMs）在各个领域取得了显著成功。然而，一个根本问题仍然存在：LLMs能否有效地利用因果知识进行预测和生成？通过实证研究，我们发现直接在大型数据集上训练的LLMs通常捕获虚假相关性，而不是真实的因果关系，导致次优的性能，尤其是在分布外（OOD）场景中。为了解决这个挑战，我们提出了一种新颖的方法，即因果注意力调整（CAT），将细粒度的因果知识注入到注意力机制中。我们提出了一个自动化的流程，利用人类先验知识自动生成token级别的因果信号，并引入了Re-Attention机制来指导训练，帮助模型关注因果结构，同时减轻注意力分数中的噪声和偏差。在我们提出的Spurious Token Game（STG）基准和多个下游任务上的实验结果表明，我们的方法有效地利用了因果知识进行预测，并在OOD场景中保持了鲁棒性。CAT在STG数据集上平均提高了5.76%，在下游任务上平均提高了1.56%。值得注意的是，Llama-3.1-8B模型在STG_M上的OOD性能从64.5%提高到90.5%，Qwen在STG_H数据集上的OOD性能从25.4%提高到55.9%。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLMs）在利用因果知识进行预测和生成时表现出的不足。现有LLMs容易学习到数据中的虚假相关性，而非真实的因果关系，导致模型在分布外（OOD）场景下的泛化能力较差。这种现象限制了LLMs在需要可靠因果推理的应用中的表现。

**核心思路**：论文的核心思路是将细粒度的因果知识注入到LLMs的注意力机制中，从而引导模型关注数据中真实的因果结构，减少对虚假相关性的依赖。通过这种方式，模型能够更好地理解数据背后的因果关系，提高在OOD场景下的鲁棒性和泛化能力。

**技术框架**：CAT方法包含一个自动化的流程，用于生成token级别的因果信号。该流程利用人类先验知识，例如领域专家提供的因果关系图，来自动标注训练数据中每个token的因果重要性。然后，引入Re-Attention机制，该机制根据token的因果信号调整注意力权重，从而引导模型更加关注因果相关的token。整个框架通过微调LLM来实现，目标是使模型在预测和生成过程中更加依赖因果知识。

**关键创新**：CAT方法的关键创新在于其能够以细粒度的方式将因果知识注入到LLMs的注意力机制中。与以往的方法相比，CAT不需要手动设计复杂的因果推理模块，而是通过自动化的流程和Re-Attention机制，使模型能够自适应地学习和利用因果知识。这种方法更加灵活和高效，能够适用于各种不同的领域和任务。

**关键设计**：CAT的关键设计包括：1) 自动化因果信号生成流程，该流程能够根据人类先验知识自动标注训练数据；2) Re-Attention机制，该机制根据token的因果信号调整注意力权重，具体实现方式未知；3) 微调策略，通过在特定任务上微调LLM，使模型能够更好地利用注入的因果知识。论文中没有明确说明具体的损失函数和网络结构细节，这部分信息未知。

## 📊 实验亮点

实验结果表明，CAT方法在Spurious Token Game（STG）基准和多个下游任务上均取得了显著提升。在STG数据集上，CAT平均提高了5.76%。更重要的是，在分布外（OOD）场景下，Llama-3.1-8B模型在STG_M上的OOD性能从64.5%提高到90.5%，Qwen在STG_H数据集上的OOD性能从25.4%提高到55.9%，表明CAT方法能够显著提高LLMs在OOD场景下的泛化能力。

## 🎯 应用场景

该研究成果可应用于各种需要可靠因果推理的领域，例如医疗诊断、金融风险评估、自动驾驶等。通过提高LLMs对因果关系的理解能力，可以使其在这些领域做出更准确、更可靠的决策，从而提升效率和安全性。此外，该方法还有助于提高LLMs在面对数据偏差和对抗攻击时的鲁棒性。

## 📄 摘要（原文）

> Large Language Models (LLMs) have achieved remarkable success across various domains. However, a fundamental question remains: Can LLMs effectively utilize causal knowledge for prediction and generation? Through empirical studies, we find that LLMs trained directly on large-scale data often capture spurious correlations rather than true causal relationships, leading to suboptimal performance, especially in out-of-distribution (OOD) scenarios. To address this challenge, we propose Causal Attention Tuning (CAT), a novel approach that injects fine-grained causal knowledge into the attention mechanism. We propose an automated pipeline that leverages human priors to automatically generate token-level causal signals and introduce the Re-Attention mechanism to guide training, helping the model focus on causal structures while mitigating noise and biases in attention scores. Experimental results on our proposed Spurious Token Game (STG) benchmark and multiple downstream tasks demonstrate that our approach effectively leverages causal knowledge for prediction and remains robust in OOD scenarios. The CAT achieves an average improvement of 5.76% on the STG dataset and 1.56% on downstream tasks. Notably, the OOD performance of the Llama-3.1-8B model on STG_M increased from 64.5% to 90.5%, and Qwen's OOD performance on the STG_H dataset improved from 25.4% to 55.9%. Implementation details can be found at https://github.com/Kairong-Han/CAT.

