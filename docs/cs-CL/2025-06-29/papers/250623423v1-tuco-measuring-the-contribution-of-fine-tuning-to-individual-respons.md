---
layout: default
title: "TuCo: Measuring the Contribution of Fine-Tuning to Individual Responses of LLMs"
---

# TuCo: Measuring the Contribution of Fine-Tuning to Individual Responses of LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23423" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23423v1</a>
  <a href="https://arxiv.org/pdf/2506.23423.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23423v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23423v1', 'TuCo: Measuring the Contribution of Fine-Tuning to Individual Responses of LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Felipe Nuti, Tim Franzmeyer, João Henriques

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-29

**备注**: ICML 2025

---

## 💡 一句话要点

**提出TuCo以量化微调对LLM个体响应的贡献**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `微调` `对抗攻击` `模型安全性` `定量分析`

## 📋 核心要点

1. 现有研究缺乏对微调对LLM个体输出影响的定量分析方法，主要集中在整体性能上。
2. 本文提出了一种新方法，通过跟踪模型中间状态来量化微调对个体响应的贡献，提供更细致的分析。
3. 实验结果表明，微调组件的调整能够显著影响模型行为，并且在对抗攻击中，TuCo的降低与攻击成功相关。

## 📝 摘要（中文）

以往的研究主要关注微调对大型语言模型（LLMs）整体性能的影响，但缺乏对个体输出影响的定量分析方法。本文提出了一种新方法，测量微调对LLM响应的贡献，假设可以访问原始预训练模型。该方法通过跟踪模型的中间隐藏状态，提供比简单比较预训练和微调模型最终输出更细致的见解。我们引入并理论分析了微调LLM的精确分解，发现通过调整微调组件的规模可以引导模型行为和性能。我们定义了调优贡献（TuCo），作为微调组件与预训练组件的比率，并观察到在三种主要对抗攻击中，TuCo的降低与攻击成功相关。这表明微调对模型输出的影响在攻击成功中起到了一定作用。总之，TuCo使得微调如何影响模型行为和安全性的定量研究成为可能。

## 🔬 方法详解

**问题定义**：本文旨在解决缺乏定量分析微调对LLM个体响应影响的问题。现有方法主要关注整体性能，无法深入理解微调对具体输出的贡献。

**核心思路**：论文提出通过跟踪模型的中间隐藏状态，精确分解微调LLM为预训练组件和微调组件，从而量化微调对个体响应的影响。

**技术框架**：整体架构包括预训练模型、微调过程及其对模型输出的影响分析。通过对比微调前后的中间状态，提取出微调对输出的具体贡献。

**关键创新**：最重要的创新在于引入了调优贡献（TuCo）的概念，能够量化微调与预训练的相对影响，这在现有研究中尚未实现。

**关键设计**：在模型的前向传播过程中，通过调整微调组件的规模，观察其对模型行为的影响，设计了相应的实验来验证这一理论。

## 📊 实验亮点

实验结果显示，微调组件的调整能够有效引导模型行为，且在三种对抗攻击中，成功攻击的情况下TuCo显著降低。这表明微调对模型输出的影响在对抗攻击中起到关键作用，提供了新的安全性分析视角。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对抗性机器学习和模型安全性分析。通过量化微调对模型输出的影响，研究人员可以更好地理解和优化LLM的行为，提升其在实际应用中的安全性和可靠性。

## 📄 摘要（原文）

> Past work has studied the effects of fine-tuning on large language models' (LLMs) overall performance on certain tasks. However, a quantitative and systematic method for analyzing its effect on individual outputs is still lacking. Here, we propose a new method for measuring the contribution that fine-tuning makes to individual LLM responses, assuming access to the original pre-trained model. Our method tracks the model's intermediate hidden states, providing a more fine-grained insight into the effects of fine-tuning than a simple comparison of final outputs from pre-trained and fine-tuned models. We introduce and theoretically analyze an exact decomposition of any fine-tuned LLM into a pre-training component and a fine-tuning component. Empirically, we find that model behavior and performance can be steered by up- or down-scaling the fine-tuning component during the forward pass. Motivated by this finding and our theoretical analysis, we define the Tuning Contribution (TuCo) as the ratio of the magnitudes of the fine-tuning component to the pre-training component. We observe that three prominent adversarial attacks on LLMs circumvent safety measures in a way that reduces TuCo, and that TuCo is consistently lower on prompts where these attacks succeed compared to those where they do not. This suggests that attenuating the effect of fine-tuning on model outputs plays a role in the success of such attacks. In summary, TuCo enables the quantitative study of how fine-tuning influences model behavior and safety, and vice versa.

