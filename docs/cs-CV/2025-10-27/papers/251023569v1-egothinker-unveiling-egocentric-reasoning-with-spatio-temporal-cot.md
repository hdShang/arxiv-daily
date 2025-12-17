---
layout: default
title: EgoThinker: Unveiling Egocentric Reasoning with Spatio-Temporal CoT
---

# EgoThinker: Unveiling Egocentric Reasoning with Spatio-Temporal CoT

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.23569" target="_blank" class="toolbar-btn">arXiv: 2510.23569v1</a>
    <a href="https://arxiv.org/pdf/2510.23569.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.23569v1" 
            onclick="toggleFavorite(this, '2510.23569v1', 'EgoThinker: Unveiling Egocentric Reasoning with Spatio-Temporal CoT')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Baoqi Pei, Yifei Huang, Jilan Xu, Yuping He, Guo Chen, Fei Wu, Yu Qiao, Jiangmiao Pang

**分类**: cs.CV

**发布日期**: 2025-10-27

**备注**: Accepted at NeurIPS 2025

**🔗 代码/项目**: [GITHUB](https://github.com/InternRobotics/EgoThinker)

---

## 💡 一句话要点

**EgoThinker：利用时空CoT揭示以自我为中心的推理能力**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `以自我为中心视频理解` `多模态大语言模型` `思维链推理` `时空定位` `强化学习`

## 📋 核心要点

1. 现有MLLM在以自我为中心的视频推理中，缺乏对隐藏意图和细粒度交互的理解，限制了其应用。
2. EgoThinker通过时空CoT监督和两阶段学习，赋予MLLM强大的以自我为中心的推理能力。
3. EgoThinker在多个基准测试中超越现有方法，并在细粒度时空定位任务中取得显著提升。

## 📝 摘要（中文）

以自我为中心的视频推理关注的是相机背后不可见的智能体，该智能体动态地塑造环境，需要推断隐藏的意图并识别细粒度的交互。这一核心挑战限制了当前的多模态大型语言模型（MLLM），这些模型擅长可见事件的推理，但缺乏具身的第一人称理解。为了弥合这一差距，我们引入了EgoThinker，这是一个新颖的框架，通过时空思维链（CoT）监督和两阶段学习课程，赋予MLLM强大的以自我为中心的推理能力。首先，我们引入了EgoRe-5M，这是一个大规模的以自我为中心的QA数据集，由1300万个不同的以自我为中心的视频片段构建而成。该数据集包含多分钟的片段，并带有详细的CoT理由和密集的hand-object grounding。其次，我们在EgoRe-5M上采用SFT来灌输推理技能，然后进行强化微调RFT，以进一步增强时空定位。实验结果表明，EgoThinker在多个以自我为中心的基准测试中优于现有方法，同时在细粒度的时空定位任务中取得了显著的改进。完整的代码和数据已在https://github.com/InternRobotics/EgoThinker上发布。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态大语言模型（MLLM）在以自我为中心的视频理解中推理能力不足的问题。现有的MLLM虽然在可见事件推理方面表现出色，但缺乏对第一人称视角下隐藏意图和细粒度交互的理解，无法有效处理以自我为中心的视频推理任务。

**核心思路**：论文的核心思路是通过引入时空思维链（CoT）监督和两阶段学习课程，来增强MLLM的以自我为中心推理能力。CoT监督旨在提供更详细的推理过程，帮助模型理解视频中的因果关系和意图。两阶段学习课程则分别侧重于推理技能的灌输和时空定位的增强。这样设计的目的是让模型不仅能“看到”发生了什么，还能“理解”为什么会发生，以及在哪里发生。

**技术框架**：EgoThinker框架主要包含两个阶段：1) 基于EgoRe-5M数据集的监督微调（SFT），用于学习推理能力；2) 强化微调（RFT），用于增强时空定位能力。EgoRe-5M数据集包含大量的以自我为中心的视频片段，并带有详细的CoT理由和hand-object grounding。SFT阶段利用这些数据来训练模型生成CoT推理过程，RFT阶段则进一步优化模型的时空定位能力。

**关键创新**：该论文的关键创新在于提出了EgoThinker框架，该框架通过引入时空CoT监督和两阶段学习课程，显著提升了MLLM在以自我为中心的视频推理方面的能力。与现有方法相比，EgoThinker更注重对视频中隐藏意图和细粒度交互的理解，从而实现了更准确的推理和定位。此外，EgoRe-5M数据集的构建也为以自我为中心的视频推理研究提供了宝贵的数据资源。

**关键设计**：EgoRe-5M数据集包含13M个视频片段，每个片段都标注了详细的CoT理由和hand-object grounding信息。在SFT阶段，模型被训练生成与视频内容相关的CoT推理过程。在RFT阶段，使用了特定的奖励函数来鼓励模型更准确地进行时空定位。具体的网络结构和参数设置在论文中应该有详细描述，但摘要中未提及。

## 📊 实验亮点

EgoThinker在多个以自我为中心的基准测试中超越了现有方法，并在细粒度的时空定位任务中取得了显著的改进。具体性能数据和对比基线需要在论文中查找，摘要中只提到“substantial improvements”，表明提升幅度较大。EgoRe-5M数据集的发布也为后续研究提供了重要资源。

## 🎯 应用场景

EgoThinker具有广泛的应用前景，例如在智能助手、人机交互、机器人导航、虚拟现实和增强现实等领域。通过理解以自我为中心的视角，EgoThinker可以帮助智能体更好地理解人类的意图和行为，从而实现更自然、更有效的交互。此外，该技术还可以用于分析和理解人类活动，例如在医疗保健、安全监控和运动分析等领域。

## 📄 摘要（原文）

> Egocentric video reasoning centers on an unobservable agent behind the camera who dynamically shapes the environment, requiring inference of hidden intentions and recognition of fine-grained interactions. This core challenge limits current multimodal large language models MLLMs, which excel at visible event reasoning but lack embodied, first-person understanding. To bridge this gap, we introduce EgoThinker, a novel framework that endows MLLMs with robust egocentric reasoning capabilities through spatio-temporal chain-of-thought supervision and a two-stage learning curriculum. First, we introduce EgoRe-5M, a large-scale egocentric QA dataset constructed from 13M diverse egocentric video clips. This dataset features multi-minute segments annotated with detailed CoT rationales and dense hand-object grounding. Second, we employ SFT on EgoRe-5M to instill reasoning skills, followed by reinforcement fine-tuning RFT to further enhance spatio-temporal localization. Experimental results show that EgoThinker outperforms existing methods across multiple egocentric benchmarks, while achieving substantial improvements in fine-grained spatio-temporal localization tasks. Full code and data are released at https://github.com/InternRobotics/EgoThinker.

