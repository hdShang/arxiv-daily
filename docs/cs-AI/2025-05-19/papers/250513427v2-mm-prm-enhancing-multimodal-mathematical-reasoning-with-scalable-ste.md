---
layout: default
title: MM-PRM: Enhancing Multimodal Mathematical Reasoning with Scalable Step-Level Supervision
---

# MM-PRM: Enhancing Multimodal Mathematical Reasoning with Scalable Step-Level Supervision

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13427" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13427v2</a>
  <a href="https://arxiv.org/pdf/2505.13427.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13427v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13427v2', 'MM-PRM: Enhancing Multimodal Mathematical Reasoning with Scalable Step-Level Supervision')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lingxiao Du, Fanqing Meng, Zongkai Liu, Zhixiang Zhou, Ping Luo, Qiaosheng Zhang, Wenqi Shao

**分类**: cs.AI, cs.CV

**发布日期**: 2025-05-19 (更新: 2025-06-05)

**🔗 代码/项目**: [GITHUB](https://github.com/ModalMinds/MM-PRM)

---

## 💡 一句话要点

**提出MM-PRM以解决多模态数学推理中的步骤监督不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态推理` `数学问题求解` `过程奖励模型` `自动化监督` `蒙特卡洛树搜索` `逻辑一致性` `教育技术`

## 📋 核心要点

1. 现有的多模态大型语言模型在复杂的多步骤推理中表现不佳，常常导致逻辑不一致的结果。
2. 本文提出MM-PRM，通过构建过程奖励模型和MM-K12数据集，提供细粒度的步骤级监督来提升推理能力。
3. 实验结果表明，MM-PRM在多个基准测试中显著提高了推理的准确性和逻辑一致性。

## 📝 摘要（中文）

尽管多模态大型语言模型（MLLMs）在视觉-语言理解方面取得了显著进展，但在复杂的多步骤推理中仍然存在困难，常常产生逻辑不一致或部分正确的解决方案。关键的限制在于缺乏对中间推理步骤的细粒度监督。为此，本文提出了MM-PRM，一个在完全自动化、可扩展框架内训练的过程奖励模型。我们首先构建了MM-Policy，一个在多样化数学推理数据上训练的强多模态模型。然后，我们构建了MM-K12，一个包含10,000个可验证答案的多模态数学问题的精选数据集，作为种子数据。通过基于蒙特卡洛树搜索（MCTS）的管道，我们生成了超过70万个步骤级注释，无需人工标注。最终的PRM用于在最佳推理设置中对候选推理路径进行评分，并在领域内（MM-K12测试集）和领域外（OlympiadBench、MathVista等）基准测试中取得了显著提升。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态数学推理中缺乏细粒度监督的问题，现有方法在处理复杂推理时常常产生不一致的结果。

**核心思路**：MM-PRM通过引入过程奖励模型（PRM）来提供对推理步骤的监督，利用自动化生成的步骤级注释来提升推理的准确性和逻辑性。

**技术框架**：整体架构包括MM-Policy模型的构建、MM-K12数据集的创建，以及基于蒙特卡洛树搜索的注释生成管道，最终通过PRM对推理路径进行评分。

**关键创新**：最重要的创新在于通过自动化生成步骤级注释，解决了传统方法依赖人工标注的瓶颈，显著提升了模型的推理能力。

**关键设计**：在模型训练中，采用了软标签、小学习率和路径多样性等设计，优化了PRM的性能，确保了推理过程的逻辑一致性。

## 📊 实验亮点

实验结果显示，MM-PRM在MM-K12测试集上取得了显著提升，相较于基线模型，推理准确率提高了XX%。在领域外基准测试（如OlympiadBench和MathVista）中也表现出色，验证了模型的广泛适用性和有效性。

## 🎯 应用场景

该研究的潜在应用领域包括教育技术、智能辅导系统和自动化数学问题求解等。通过提升多模态推理系统的逻辑鲁棒性，MM-PRM能够在实际应用中提供更准确的解答，帮助学生和教育工作者更有效地解决数学问题，未来可能对教育领域产生深远影响。

## 📄 摘要（原文）

> While Multimodal Large Language Models (MLLMs) have achieved impressive progress in vision-language understanding, they still struggle with complex multi-step reasoning, often producing logically inconsistent or partially correct solutions. A key limitation lies in the lack of fine-grained supervision over intermediate reasoning steps. To address this, we propose MM-PRM, a process reward model trained within a fully automated, scalable framework. We first build MM-Policy, a strong multimodal model trained on diverse mathematical reasoning data. Then, we construct MM-K12, a curated dataset of 10,000 multimodal math problems with verifiable answers, which serves as seed data. Leveraging a Monte Carlo Tree Search (MCTS)-based pipeline, we generate over 700k step-level annotations without human labeling. The resulting PRM is used to score candidate reasoning paths in the Best-of-N inference setup and achieves significant improvements across both in-domain (MM-K12 test set) and out-of-domain (OlympiadBench, MathVista, etc.) benchmarks. Further analysis confirms the effectiveness of soft labels, smaller learning rates, and path diversity in optimizing PRM performance. MM-PRM demonstrates that process supervision is a powerful tool for enhancing the logical robustness of multimodal reasoning systems. We release all our codes and data at https://github.com/ModalMinds/MM-PRM.

