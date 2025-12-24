---
layout: default
title: "OmniDrive-R1: Reinforcement-driven Interleaved Multi-modal Chain-of-Thought for Trustworthy Vision-Language Autonomous Driving"
---

# OmniDrive-R1: Reinforcement-driven Interleaved Multi-modal Chain-of-Thought for Trustworthy Vision-Language Autonomous Driving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14044" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14044v1</a>
  <a href="https://arxiv.org/pdf/2512.14044.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14044v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14044v1', 'OmniDrive-R1: Reinforcement-driven Interleaved Multi-modal Chain-of-Thought for Trustworthy Vision-Language Autonomous Driving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhenguo Zhang, Haohan Zhen, Yishen Wang, Le Xu, Tianchen Deng, Xuefeng Chen, Qu Chen, Bo Zhang, Wuxiong Huang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**OmniDrive-R1：强化学习驱动的交错多模态CoT，提升自动驾驶视觉语言模型的可靠性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动驾驶` `视觉语言模型` `强化学习` `思维链` `多模态融合` `目标幻觉` `视觉 grounding`

## 📋 核心要点

1. 现有视觉语言模型在自动驾驶中存在目标幻觉问题，主要原因是依赖于无根据的文本CoT推理，且感知和推理阶段解耦。
2. OmniDrive-R1通过交错多模态CoT机制统一感知和推理，并利用强化学习驱动的视觉 grounding 能力，聚焦关键区域。
3. 在DriveLMM-o1数据集上，OmniDrive-R1显著提升了推理得分和答案准确率，表明其在自动驾驶场景下的有效性。

## 📝 摘要（中文）

视觉语言模型(VLMs)在自动驾驶(AD)等安全关键领域的部署受到可靠性问题的严重阻碍，特别是目标幻觉。这种失败源于它们对无根据的、基于文本的思维链(CoT)推理的依赖。现有的多模态CoT方法试图缓解这个问题，但存在两个根本缺陷：(1)解耦的感知和推理阶段，阻碍了端到端的联合优化；(2)依赖于昂贵的、密集的定位标签。因此，我们引入了OmniDrive-R1，这是一个为自动驾驶设计的端到端VLM框架，它通过交错多模态思维链(iMCoT)机制统一了感知和推理。我们的核心创新是强化学习驱动的视觉 grounding 能力，使模型能够自主地将其注意力引导并“放大”到关键区域进行细粒度分析。这种能力由我们纯粹的两阶段强化学习训练流程和Clip-GRPO算法实现。至关重要的是，Clip-GRPO引入了一种无标注的、基于过程的 grounding 奖励。这种奖励不仅消除了对密集标签的需求，而且通过强制视觉焦点和文本推理之间的实时跨模态一致性，规避了外部工具调用的不稳定性。在DriveLMM-o1上的大量实验证明了我们模型的显著改进。与基线Qwen2.5VL-7B相比，OmniDrive-R1将整体推理得分从51.77%提高到80.35%，最终答案准确率从37.81%提高到73.62%。

## 🔬 方法详解

**问题定义**：论文旨在解决视觉语言模型在自动驾驶领域中，由于依赖于无根据的文本思维链（CoT）推理而导致的目标幻觉问题。现有方法通常采用解耦的感知和推理阶段，无法进行端到端联合优化，并且依赖于昂贵的密集标注数据，限制了其应用范围。

**核心思路**：论文的核心思路是通过交错多模态思维链（iMCoT）机制，将感知和推理过程进行统一，实现端到端的联合优化。同时，利用强化学习驱动的视觉 grounding 能力，使模型能够自主地关注图像中的关键区域，从而减少对密集标注数据的依赖，并提高推理的准确性。

**技术框架**：OmniDrive-R1 框架包含一个交错多模态思维链（iMCoT）模块和一个强化学习驱动的视觉 grounding 模块。iMCoT 模块负责将视觉信息和文本信息进行交错融合，进行多模态推理。视觉 grounding 模块通过强化学习算法，学习如何自主地选择图像中的关键区域进行细粒度分析。整个框架采用端到端的方式进行训练。

**关键创新**：论文的关键创新在于提出了强化学习驱动的视觉 grounding 能力，以及相应的 Clip-GRPO 算法。该算法引入了一种无标注的、基于过程的 grounding 奖励，鼓励模型关注与文本推理相关的视觉区域，从而减少了对密集标注数据的依赖，并提高了推理的准确性。此外，交错多模态思维链（iMCoT）机制也促进了感知和推理的联合优化。

**关键设计**：Clip-GRPO 算法的关键设计在于其奖励函数，该奖励函数基于视觉焦点和文本推理之间的跨模态一致性进行设计，无需人工标注。具体来说，该奖励函数鼓励模型选择与文本推理相关的视觉区域，并惩罚模型选择无关的区域。此外，论文还采用了两阶段强化学习训练流程，首先预训练视觉 grounding 模块，然后再进行端到端的联合训练。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14044v1/exam.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14044v1/overview.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14044v1/2_stage.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

OmniDrive-R1 在 DriveLMM-o1 数据集上取得了显著的性能提升。与基线模型 Qwen2.5VL-7B 相比，OmniDrive-R1 将整体推理得分从 51.77% 提高到 80.35%，最终答案准确率从 37.81% 提高到 73.62%。这些结果表明，该模型在自动驾驶场景下的视觉语言推理能力得到了显著提升。

## 🎯 应用场景

OmniDrive-R1 的研究成果可应用于自动驾驶、机器人导航、智能监控等领域。通过提高视觉语言模型在复杂环境下的感知和推理能力，可以提升自动驾驶系统的安全性、可靠性和智能化水平，并为其他需要视觉理解和决策的智能系统提供技术支持。

## 📄 摘要（原文）

> The deployment of Vision-Language Models (VLMs) in safety-critical domains like autonomous driving (AD) is critically hindered by reliability failures, most notably object hallucination. This failure stems from their reliance on ungrounded, text-based Chain-of-Thought (CoT) reasoning.While existing multi-modal CoT approaches attempt mitigation, they suffer from two fundamental flaws: (1) decoupled perception and reasoning stages that prevent end-to-end joint optimization, and (2) reliance on expensive, dense localization labels.Thus we introduce OmniDrive-R1, an end-to-end VLM framework designed for autonomous driving, which unifies perception and reasoning through an interleaved Multi-modal Chain-of-Thought (iMCoT) mechanism. Our core innovation is an Reinforcement-driven visual grounding capability, enabling the model to autonomously direct its attention and "zoom in" on critical regions for fine-grained analysis. This capability is enabled by our pure two-stage reinforcement learning training pipeline and Clip-GRPO algorithm. Crucially, Clip-GRPO introduces an annotation-free, process-based grounding reward. This reward not only eliminates the need for dense labels but also circumvents the instability of external tool calls by enforcing real-time cross-modal consistency between the visual focus and the textual reasoning. Extensive experiments on DriveLMM-o1 demonstrate our model's significant improvements. Compared to the baseline Qwen2.5VL-7B, OmniDrive-R1 improves the overall reasoning score from 51.77% to 80.35%, and the final answer accuracy from 37.81% to 73.62%.

