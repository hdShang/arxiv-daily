---
layout: default
title: ReasonPlan: Unified Scene Prediction and Decision Reasoning for Closed-loop Autonomous Driving
---

# ReasonPlan: Unified Scene Prediction and Decision Reasoning for Closed-loop Autonomous Driving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20024" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20024v2</a>
  <a href="https://arxiv.org/pdf/2505.20024.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20024v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20024v2', 'ReasonPlan: Unified Scene Prediction and Decision Reasoning for Closed-loop Autonomous Driving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xueyi Liu, Zuodong Zhong, Yuxin Guo, Yun-Fu Liu, Zhiguo Su, Qichao Zhang, Junli Wang, Yinfeng Gao, Yupeng Zheng, Qiao Lin, Huiyong Chen, Dongbin Zhao

**分类**: cs.CV, cs.AI, cs.RO

**发布日期**: 2025-05-26 (更新: 2025-09-22)

**备注**: 18 pages; 9 figures; https://github.com/Liuxueyi/ReasonPlan

**🔗 代码/项目**: [GITHUB](https://github.com/Liuxueyi/ReasonPlan)

---

## 💡 一句话要点

**提出ReasonPlan以解决闭环自主驾驶中的决策推理问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `闭环自主驾驶` `多模态大语言模型` `决策推理` `自监督学习` `监督学习` `视觉理解` `零-shot泛化` `智能交通系统`

## 📋 核心要点

1. 现有的多模态大语言模型在闭环自主驾驶中的应用尚未充分探索，且未能超越传统的E2E模仿学习方法。
2. 本文提出ReasonPlan，通过自监督的下一场景预测和监督的决策链推理，促进视觉表示与驾驶上下文的对齐。
3. 实验结果显示，ReasonPlan在Bench2Drive基准上比主流方法提高了19%的L2和16.1的驾驶评分，且在零-shot场景中表现优异。

## 📝 摘要（中文）

由于多模态大语言模型（MLLM）在视觉-语言推理和泛化能力方面的强大，近年来在端到端（E2E）自主驾驶领域引起了广泛关注。然而，它们在闭环系统中的应用仍然未得到充分探索，现有的基于MLLM的方法未能明显优于主流的E2E模仿学习方法。本文提出了ReasonPlan，一个新颖的MLLM微调框架，旨在通过自监督的下一场景预测任务和监督的决策链推理过程实现闭环驾驶的整体推理。该双重机制促使模型将视觉表示与可操作的驾驶上下文对齐，同时促进可解释和因果基础的决策制定。我们整理了一个以规划为导向的决策推理数据集PDR，包含21万个多样且高质量的样本。我们的算法在Bench2Drive基准测试中比主流E2E模仿学习方法提高了19%的L2和16.1的驾驶评分。此外，ReasonPlan在未见的DOS基准测试中表现出强大的零-shot泛化能力，突显了其在处理零-shot边界案例中的适应性。

## 🔬 方法详解

**问题定义**：本文旨在解决闭环自主驾驶中决策推理的不足，现有方法在处理复杂场景时缺乏有效的推理能力，导致决策不够准确和可靠。

**核心思路**：ReasonPlan的核心思路是通过结合自监督学习和监督学习，利用下一场景预测任务来增强模型的视觉理解，同时通过决策链推理过程来提升决策的可解释性和因果性。

**技术框架**：ReasonPlan的整体架构包括两个主要模块：自监督的下一场景预测模块和监督的决策链推理模块。前者负责生成对未来场景的预测，后者则基于这些预测进行决策制定。

**关键创新**：ReasonPlan的创新点在于其双重机制的设计，既考虑了视觉信息的理解，又强调了决策过程的可解释性。这与传统的E2E模仿学习方法不同，后者往往缺乏对决策过程的深入分析。

**关键设计**：在关键设计上，ReasonPlan采用了特定的损失函数来平衡自监督和监督学习的目标，同时在网络结构上引入了多层次的特征提取模块，以增强模型对复杂场景的适应能力。通过这些设计，模型能够更好地处理多样化的驾驶情境。

## 📊 实验亮点

ReasonPlan在Bench2Drive基准测试中相较于主流E2E模仿学习方法，L2损失减少了19%，驾驶评分提高了16.1分。此外，该方法在未见的DOS基准测试中展现出强大的零-shot泛化能力，显示出其在处理边界案例时的适应性。

## 🎯 应用场景

ReasonPlan的研究成果在自动驾驶领域具有广泛的应用潜力，尤其是在复杂和动态环境下的决策制定。其可解释性和因果推理能力使得模型能够在实际驾驶中做出更为安全和可靠的决策，未来可能推动智能交通系统的发展和普及。

## 📄 摘要（原文）

> Due to the powerful vision-language reasoning and generalization abilities, multimodal large language models (MLLMs) have garnered significant attention in the field of end-to-end (E2E) autonomous driving. However, their application to closed-loop systems remains underexplored, and current MLLM-based methods have not shown clear superiority to mainstream E2E imitation learning approaches. In this work, we propose ReasonPlan, a novel MLLM fine-tuning framework designed for closed-loop driving through holistic reasoning with a self-supervised Next Scene Prediction task and supervised Decision Chain-of-Thought process. This dual mechanism encourages the model to align visual representations with actionable driving context, while promoting interpretable and causally grounded decision making. We curate a planning-oriented decision reasoning dataset, namely PDR, comprising 210k diverse and high-quality samples. Our method outperforms the mainstream E2E imitation learning method by a large margin of 19% L2 and 16.1 driving score on Bench2Drive benchmark. Furthermore, ReasonPlan demonstrates strong zero-shot generalization on unseen DOS benchmark, highlighting its adaptability in handling zero-shot corner cases. Code and dataset will be found in https://github.com/Liuxueyi/ReasonPlan.

