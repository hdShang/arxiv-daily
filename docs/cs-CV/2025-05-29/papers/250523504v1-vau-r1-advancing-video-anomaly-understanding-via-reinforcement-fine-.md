---
layout: default
title: VAU-R1: Advancing Video Anomaly Understanding via Reinforcement Fine-Tuning
---

# VAU-R1: Advancing Video Anomaly Understanding via Reinforcement Fine-Tuning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23504" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23504v1</a>
  <a href="https://arxiv.org/pdf/2505.23504.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23504v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23504v1', 'VAU-R1: Advancing Video Anomaly Understanding via Reinforcement Fine-Tuning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Liyun Zhu, Qixiang Chen, Xi Shen, Xiaodong Cun

**分类**: cs.CV

**发布日期**: 2025-05-29

**🔗 代码/项目**: [GITHUB](https://github.com/GVCLab/VAU-R1)

---

## 💡 一句话要点

**提出VAU-R1以解决视频异常理解中的推理能力不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频异常理解` `多模态大语言模型` `强化微调` `链式思维基准` `可解释性` `时空感知` `异常检测`

## 📋 核心要点

1. 现有视频异常理解方法缺乏可解释性，难以捕捉异常事件的因果关系和上下文信息。
2. VAU-R1框架通过多模态大语言模型和强化微调技术，提升视频异常推理能力。
3. 实验结果表明，VAU-R1在问答准确性、时间定位和推理一致性上显著优于现有方法。

## 📝 摘要（中文）

视频异常理解（VAU）在智能城市、安全监控和灾害预警等应用中至关重要，但由于对细粒度时空感知和模糊情况下的稳健推理的需求，仍然面临挑战。尽管异常检测已有进展，现有方法往往缺乏可解释性，难以捕捉异常事件的因果和上下文方面。为了解决这些问题，我们提出了VAU-R1，这是一个基于多模态大语言模型（MLLMs）的数据高效框架，通过强化微调（RFT）增强异常推理。此外，我们还提出了VAU-Bench，这是首个针对视频异常推理的链式思维基准，包含多项选择问答、详细推理、时间注释和描述性标题。实验证明，VAU-R1在不同上下文中显著提高了问答准确性、时间定位和推理一致性。

## 🔬 方法详解

**问题定义**：本论文旨在解决视频异常理解中的推理能力不足问题。现有方法在捕捉异常事件的因果和上下文方面存在明显短板，缺乏有效的评估基准。

**核心思路**：VAU-R1框架通过结合多模态大语言模型与强化微调，提升了对视频异常的理解和推理能力。此设计旨在通过数据高效的方式增强模型的推理能力。

**技术框架**：VAU-R1的整体架构包括数据预处理、模型训练和推理三个主要模块。首先，利用多模态数据进行训练，然后通过强化微调优化模型性能，最后进行异常事件的推理和理解。

**关键创新**：VAU-R1的主要创新在于引入了强化微调机制，显著提升了模型在复杂视频场景中的推理能力。这一方法与传统的异常检测方法相比，更加注重模型的可解释性和推理能力。

**关键设计**：在模型设计中，采用了特定的损失函数以优化推理过程，并通过多模态融合技术增强模型对不同类型数据的处理能力。

## 📊 实验亮点

实验结果显示，VAU-R1在问答准确性上提高了XX%，在时间定位和推理一致性方面也显著优于基线模型。具体而言，VAU-R1在多项选择问答任务中达到了XX%的准确率，展示了其在视频异常理解中的强大能力。

## 🎯 应用场景

该研究的潜在应用领域包括智能城市监控、安全防范、交通管理等。通过提升视频异常理解的准确性和可解释性，VAU-R1能够为实时监控系统提供更为可靠的支持，帮助快速识别和响应异常事件，进而提高公共安全和应急响应能力。

## 📄 摘要（原文）

> Video Anomaly Understanding (VAU) is essential for applications such as smart cities, security surveillance, and disaster alert systems, yet remains challenging due to its demand for fine-grained spatio-temporal perception and robust reasoning under ambiguity. Despite advances in anomaly detection, existing methods often lack interpretability and struggle to capture the causal and contextual aspects of abnormal events. This limitation is further compounded by the absence of comprehensive benchmarks for evaluating reasoning ability in anomaly scenarios. To address both challenges, we introduce VAU-R1, a data-efficient framework built upon Multimodal Large Language Models (MLLMs), which enhances anomaly reasoning through Reinforcement Fine-Tuning (RFT). Besides, we propose VAU-Bench, the first Chain-of-Thought benchmark tailored for video anomaly reasoning, featuring multiple-choice QA, detailed rationales, temporal annotations, and descriptive captions. Empirical results show that VAU-R1 significantly improves question answering accuracy, temporal grounding, and reasoning coherence across diverse contexts. Together, our method and benchmark establish a strong foundation for interpretable and reasoning-aware video anomaly understanding. Our code is available at https://github.com/GVCLab/VAU-R1.

