---
layout: default
title: "Aurora: Towards Universal Generative Multimodal Time Series Forecasting"
---

# Aurora: Towards Universal Generative Multimodal Time Series Forecasting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22295" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22295v2</a>
  <a href="https://arxiv.org/pdf/2509.22295.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22295v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22295v2', 'Aurora: Towards Universal Generative Multimodal Time Series Forecasting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xingjian Wu, Jianxin Jin, Wanghui Qiu, Peng Chen, Yang Shu, Bin Yang, Chenjuan Guo

**分类**: cs.LG

**发布日期**: 2025-09-26 (更新: 2025-10-20)

---

## 💡 一句话要点

**Aurora：面向通用生成式多模态时间序列预测的基座模型**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态时间序列预测` `跨领域泛化` `基础模型` `Flow Matching` `自注意力机制`

## 📋 核心要点

1. 现有时间序列预测方法难以有效利用文本等模态中的领域知识，限制了跨领域泛化能力。
2. Aurora通过预训练的多模态时间序列基础模型，自适应提取并利用文本和图像中的领域知识。
3. 实验表明，Aurora在多个基准测试中，单模态和多模态场景下均取得了领先的性能。

## 📝 摘要（中文）

跨领域泛化在时间序列预测中至关重要，因为相似的历史信息可能由于领域特定特征而导致不同的未来趋势。目前的研究主要集中在构建单模态时间序列基础模型和端到端多模态监督模型。前者缺乏对文本等模态中领域特定知识的显式利用，从而阻碍了性能。后者则针对端到端场景定制，不支持跨领域场景的零样本推理。本文提出了Aurora，一个多模态时间序列基础模型，它支持多模态输入和零样本推理。Aurora在跨领域多模态时间序列语料库上进行预训练，能够自适应地提取和关注相应文本或图像模态中包含的关键领域知识，从而具有强大的跨领域泛化能力。通过tokenization、编码和蒸馏，Aurora可以提取多模态领域知识作为指导，然后利用模态引导的多头自注意力将其注入到时间表示的建模中。在解码阶段，多模态表示用于生成未来token的条件和原型，从而促成了一种用于生成概率预测的新型原型引导的Flow Matching。在公认的基准测试（包括TimeMMD、TSFM-Bench和ProbTS）上进行的综合实验表明，Aurora在单模态和多模态场景中均具有一致的state-of-the-art性能。

## 🔬 方法详解

**问题定义**：论文旨在解决跨领域时间序列预测中，现有方法无法有效利用多模态信息（如文本、图像）中蕴含的领域知识，导致泛化能力不足的问题。现有方法要么侧重于单模态时间序列建模，忽略了其他模态的信息；要么是端到端的多模态模型，缺乏跨领域零样本推理能力。

**核心思路**：论文的核心思路是构建一个多模态时间序列基础模型Aurora，通过预训练的方式学习跨领域的多模态知识，并利用这些知识指导时间序列的预测。Aurora能够自适应地从文本和图像等模态中提取领域知识，并将其注入到时间序列的建模过程中，从而提高跨领域泛化能力。

**技术框架**：Aurora的整体框架包括三个主要阶段：1) 多模态知识提取：通过tokenization、编码和蒸馏等技术，从文本和图像等模态中提取领域知识。2) 时间序列建模：利用模态引导的多头自注意力机制，将提取的领域知识注入到时间序列的表示中。3) 概率预测：使用原型引导的Flow Matching方法，基于多模态表示生成未来token的条件和原型，进行概率预测。

**关键创新**：Aurora的关键创新在于：1) 提出了一个多模态时间序列基础模型，能够同时处理时间序列、文本和图像等多种模态的输入。2) 设计了一种模态引导的多头自注意力机制，能够有效地将领域知识注入到时间序列的建模中。3) 提出了一种原型引导的Flow Matching方法，用于生成概率预测，提高了预测的准确性和可靠性。

**关键设计**：Aurora的关键设计包括：1) 使用Transformer架构作为基础模型，进行多模态信息的编码和融合。2) 设计了专门的损失函数，用于指导多模态知识的提取和时间序列的建模。3) 采用了蒸馏技术，将领域知识从大型预训练模型迁移到Aurora模型中。

## 📊 实验亮点

Aurora在TimeMMD、TSFM-Bench和ProbTS等多个基准测试中取得了state-of-the-art的性能。具体来说，在跨领域时间序列预测任务中，Aurora相比于现有方法，在预测精度和泛化能力方面均有显著提升。实验结果表明，Aurora能够有效地利用多模态信息，提高时间序列预测的准确性和可靠性。

## 🎯 应用场景

Aurora具有广泛的应用前景，例如：供应链管理、金融风险预测、智能交通、能源消耗预测等。通过利用多模态信息，Aurora可以提高预测的准确性和可靠性，为决策提供更有效的支持。未来，Aurora可以进一步扩展到更多的领域和应用场景，例如：医疗健康、环境监测等。

## 📄 摘要（原文）

> Cross-domain generalization is very important in Time Series Forecasting because similar historical information may lead to distinct future trends due to the domain-specific characteristics. Recent works focus on building unimodal time series foundation models and end-to-end multimodal supervised models. Since domain-specific knowledge is often contained in modalities like texts, the former lacks the explicit utilization of them, thus hindering the performance. The latter is tailored for end-to-end scenarios and does not support zero-shot inference for cross-domain scenarios. In this work, we introduce Aurora, a Multimodal Time Series Foundation Model, which supports multimodal inputs and zero-shot inference. Pretrained on Corss-domain Multimodal Time Series Corpus, Aurora can adaptively extract and focus on key domain knowledge contained in corrsponding text or image modalities, thus possessing strong Cross-domain generalization capability. Through tokenization, encoding, and distillation, Aurora can extract multimodal domain knowledge as guidance and then utilizes a Modality-Guided Multi-head Self-Attention to inject them into the modeling of temporal representations. In the decoding phase, the multimodal representations are used to generate the conditions and prototypes of future tokens, contributing to a novel Prototype-Guided Flow Matching for generative probabilistic forecasting. Comprehensive experiments on well-recognized benchmarks, including TimeMMD, TSFM-Bench and ProbTS, demonstrate the consistent state-of-the-art performance of Aurora on both unimodal and multimodal scenarios.

