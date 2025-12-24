---
layout: default
title: QoQ-Med: Building Multimodal Clinical Foundation Models with Domain-Aware GRPO Training
---

# QoQ-Med: Building Multimodal Clinical Foundation Models with Domain-Aware GRPO Training

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00711" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00711v2</a>
  <a href="https://arxiv.org/pdf/2506.00711.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00711v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00711v2', 'QoQ-Med: Building Multimodal Clinical Foundation Models with Domain-Aware GRPO Training')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wei Dai, Peilin Chen, Chanakya Ekbote, Paul Pu Liang

**分类**: cs.LG, cs.AI, cs.CV

**发布日期**: 2025-05-31 (更新: 2025-10-22)

**备注**: Accepted as Oral at NeurIPS 2025. Revision after camera ready

**🔗 代码/项目**: [GITHUB](https://github.com/DDVD233/QoQ_Med)

---

## 💡 一句话要点

**提出QoQ-Med以解决多模态临床决策中的数据不平衡问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `临床决策` `强化学习` `医学图像` `时间序列分析` `模型训练` `数据不平衡` `领域感知`

## 📋 核心要点

1. 现有的多模态语言模型在临床决策中主要集中于视觉数据，无法有效处理异构数据，导致泛化能力不足。
2. 本文提出QoQ-Med模型，结合医学图像、时间序列信号和文本报告，通过领域感知相对策略优化（DRPO）进行训练。
3. 实验结果表明，QoQ-Med在所有视觉领域的宏F1得分平均提升43%，并在密集分割任务中表现优异，IoU显著高于现有模型。

## 📝 摘要（中文）

临床决策通常需要对异构数据进行推理，但现有的多模态语言模型（MLLMs）主要集中于视觉数据，无法在不同临床专业之间有效泛化。为此，本文提出了QoQ-Med-7B/32B，这是首个开放的通用临床基础模型，能够同时对医学图像、时间序列信号和文本报告进行推理。QoQ-Med采用了一种新颖的强化学习目标——领域感知相对策略优化（DRPO），该方法根据领域稀缺性和模态难度分层缩放归一化奖励，从而缓解了由于临床数据分布偏斜造成的性能不平衡。经过261万对指令调优样本的训练，DRPO训练在所有视觉领域的宏F1得分上平均提升了43%。此外，QoQ-Med在密集分割数据上训练后，能够突出与诊断相关的显著区域，其IoU比开放模型高出10倍，同时达到OpenAI o4-mini的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多模态语言模型在临床决策中无法有效处理异构数据的问题，尤其是由于数据分布不均导致的性能不平衡。

**核心思路**：提出QoQ-Med模型，通过领域感知相对策略优化（DRPO）来训练模型，使其能够在不同模态和领域之间进行有效推理，提升模型的泛化能力。

**技术框架**：QoQ-Med的整体架构包括三个主要模块：医学图像处理模块、时间序列信号处理模块和文本报告处理模块。每个模块通过DRPO进行训练，确保模型能够综合考虑不同类型的数据。

**关键创新**：DRPO是本文的核心创新，它通过根据领域稀缺性和模态难度动态调整奖励，解决了传统方法在处理不平衡数据时的不足。

**关键设计**：在训练过程中，QoQ-Med使用261万对指令调优样本，采用特定的损失函数和网络结构设计，以确保模型在多模态数据上的高效学习和推理能力。具体的参数设置和网络结构细节在论文中有详细描述。

## 📊 实验亮点

实验结果显示，QoQ-Med在所有视觉领域的宏F1得分平均提升了43%，相较于其他无评论训练方法如GRPO。此外，模型在密集分割任务中的IoU比开放模型高出10倍，性能达到OpenAI o4-mini的水平，展示了其卓越的推理能力。

## 🎯 应用场景

QoQ-Med模型的潜在应用领域包括医疗影像分析、临床决策支持系统和智能健康管理等。其多模态推理能力将为医生提供更全面的诊断信息，提升临床决策的准确性和效率。未来，该模型有望推动个性化医疗和精准医疗的发展。

## 📄 摘要（原文）

> Clinical decision-making routinely demands reasoning over heterogeneous data, yet existing multimodal language models (MLLMs) remain largely vision-centric and fail to generalize across clinical specialties. To bridge this gap, we introduce QoQ-Med-7B/32B, the first open generalist clinical foundation model that jointly reasons across medical images, time-series signals, and text reports. QoQ-Med is trained with Domain-aware Relative Policy Optimization (DRPO), a novel reinforcement-learning objective that hierarchically scales normalized rewards according to domain rarity and modality difficulty, mitigating performance imbalance caused by skewed clinical data distributions. Trained on 2.61 million instruction tuning pairs spanning 9 clinical domains, we show that DRPO training boosts diagnostic performance by 43% in macro-F1 on average across all visual domains as compared to other critic-free training methods like GRPO. Furthermore, with QoQ-Med trained on intensive segmentation data, it is able to highlight salient regions related to the diagnosis, with an IoU 10x higher than open models while reaching the performance of OpenAI o4-mini. To foster reproducibility and downstream research, we release (i) the full model weights, (ii) the modular training pipeline, and (iii) all intermediate reasoning traces at https://github.com/DDVD233/QoQ_Med.

