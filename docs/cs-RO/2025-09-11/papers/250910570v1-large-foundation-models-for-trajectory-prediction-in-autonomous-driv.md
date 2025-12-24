---
layout: default
title: "Large Foundation Models for Trajectory Prediction in Autonomous Driving: A Comprehensive Survey"
---

# Large Foundation Models for Trajectory Prediction in Autonomous Driving: A Comprehensive Survey

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10570" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10570v1</a>
  <a href="https://arxiv.org/pdf/2509.10570.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10570v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10570v1', 'Large Foundation Models for Trajectory Prediction in Autonomous Driving: A Comprehensive Survey')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wei Dai, Shengen Wu, Wei Wu, Zhenhao Wang, Sisuo Lyu, Haicheng Liao, Limin Yu, Weiping Ding, Runwei Guan, Yutao Yue

**分类**: cs.RO, cs.AI

**发布日期**: 2025-09-11

**备注**: 22 pages, 6 figures

---

## 💡 一句话要点

**综述性论文：利用大型预训练模型解决自动驾驶轨迹预测问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `轨迹预测` `自动驾驶` `大型预训练模型` `大型语言模型` `多模态学习` `上下文推理` `行为预测`

## 📋 核心要点

1. 传统轨迹预测方法依赖大量标注数据，缺乏可解释性，且在复杂长尾场景中泛化能力不足。
2. 利用大型预训练模型（LFMs），特别是LLMs和MLLMs，融合语言和场景语义，实现可解释的上下文推理。
3. 综述涵盖轨迹-语言映射、多模态融合、约束推理等方法，并讨论了挑战和未来方向，如低延迟推理。

## 📝 摘要（中文）

轨迹预测是自动驾驶的关键功能，它能够预测车辆和行人等交通参与者的未来运动轨迹，这对于驾驶安全至关重要。传统的深度学习方法虽然提高了准确性，但仍受到固有局限性的阻碍，包括缺乏可解释性、严重依赖大规模标注数据以及在长尾场景中泛化能力较弱。大型预训练模型（LFMs）的兴起正在改变轨迹预测的研究范式。本综述系统地回顾了LFMs，特别是大型语言模型（LLMs）和多模态大型语言模型（MLLMs）在轨迹预测方面的最新进展。通过整合语言和场景语义，LFMs促进了可解释的上下文推理，显著提高了复杂环境中预测的安全性和泛化能力。文章重点介绍了三种核心方法：轨迹-语言映射、多模态融合和基于约束的推理。涵盖了车辆和行人的预测任务、评估指标和数据集分析。讨论了计算延迟、数据稀缺和真实世界鲁棒性等关键挑战，以及包括低延迟推理、因果关系建模和运动基础模型在内的未来研究方向。

## 🔬 方法详解

**问题定义**：论文旨在解决自动驾驶场景下轨迹预测的难题。现有方法，如传统的深度学习模型，通常需要大量标注数据进行训练，并且在面对复杂和罕见场景时泛化能力较弱。此外，这些模型的可解释性也较差，难以理解其预测背后的逻辑。

**核心思路**：论文的核心思路是利用大型预训练模型（LFMs），特别是大型语言模型（LLMs）和多模态大型语言模型（MLLMs），来提升轨迹预测的性能和可解释性。通过将轨迹信息与语言描述或场景语义信息相结合，LFMs能够进行更有效的上下文推理，从而提高预测的准确性和鲁棒性。

**技术框架**：该综述文章主要围绕三种核心方法展开：1) 轨迹-语言映射：将轨迹数据映射到自然语言空间，利用LLMs进行推理和预测。2) 多模态融合：融合视觉、激光雷达等多种传感器数据，以及语言描述，利用MLLMs进行更全面的场景理解和轨迹预测。3) 基于约束的推理：在预测过程中引入物理约束、交通规则等约束条件，提高预测的合理性和安全性。

**关键创新**：该综述的关键创新在于系统性地总结了LFMs在轨迹预测领域的应用，并指出了该领域未来的发展方向。与传统方法相比，LFMs能够利用其强大的语言理解和生成能力，实现更可解释、更鲁棒的轨迹预测。

**关键设计**：论文中涉及的关键设计包括：如何将轨迹数据编码为语言描述（例如，使用token序列表示轨迹点），如何设计多模态融合模块（例如，使用注意力机制融合不同模态的信息），以及如何将约束条件融入到预测模型中（例如，使用损失函数惩罚违反约束的预测结果）。具体的参数设置、损失函数和网络结构因不同的方法而异，需要在具体论文中进行详细分析。

## 📊 实验亮点

该综述总结了当前基于大型预训练模型的轨迹预测方法，并分析了各种方法的优缺点。虽然没有提供具体的实验数据，但强调了LFMs在提高预测准确性、可解释性和鲁棒性方面的潜力。未来的研究方向包括降低计算延迟、提高数据利用率和增强模型在真实世界中的鲁棒性。

## 🎯 应用场景

该研究成果可广泛应用于自动驾驶系统，提升车辆在复杂交通环境中的安全性和可靠性。通过更准确的轨迹预测，自动驾驶车辆能够更好地理解周围环境，做出更合理的决策，从而减少交通事故的发生。此外，该研究还可以应用于机器人导航、智能交通管理等领域。

## 📄 摘要（原文）

> Trajectory prediction serves as a critical functionality in autonomous driving, enabling the anticipation of future motion paths for traffic participants such as vehicles and pedestrians, which is essential for driving safety. Although conventional deep learning methods have improved accuracy, they remain hindered by inherent limitations, including lack of interpretability, heavy reliance on large-scale annotated data, and weak generalization in long-tail scenarios. The rise of Large Foundation Models (LFMs) is transforming the research paradigm of trajectory prediction. This survey offers a systematic review of recent advances in LFMs, particularly Large Language Models (LLMs) and Multimodal Large Language Models (MLLMs) for trajectory prediction. By integrating linguistic and scene semantics, LFMs facilitate interpretable contextual reasoning, significantly enhancing prediction safety and generalization in complex environments. The article highlights three core methodologies: trajectory-language mapping, multimodal fusion, and constraint-based reasoning. It covers prediction tasks for both vehicles and pedestrians, evaluation metrics, and dataset analyses. Key challenges such as computational latency, data scarcity, and real-world robustness are discussed, along with future research directions including low-latency inference, causality-aware modeling, and motion foundation models.

