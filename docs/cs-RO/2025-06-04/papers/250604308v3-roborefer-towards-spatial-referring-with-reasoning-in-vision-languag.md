---
layout: default
title: "RoboRefer: Towards Spatial Referring with Reasoning in Vision-Language Models for Robotics"
---

# RoboRefer: Towards Spatial Referring with Reasoning in Vision-Language Models for Robotics

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04308" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04308v3</a>
  <a href="https://arxiv.org/pdf/2506.04308.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04308v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04308v3', 'RoboRefer: Towards Spatial Referring with Reasoning in Vision-Language Models for Robotics')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Enshen Zhou, Jingkun An, Cheng Chi, Yi Han, Shanyu Rong, Chi Zhang, Pengwei Wang, Zhongyuan Wang, Tiejun Huang, Lu Sheng, Shanghang Zhang

**分类**: cs.RO, cs.AI, cs.CV

**发布日期**: 2025-06-04 (更新: 2025-10-25)

**备注**: Accepted by NeurIPS 2025. Project page: https://zhoues.github.io/RoboRefer/

**🔗 代码/项目**: [PROJECT_PAGE](https://zhoues.github.io/RoboRefer)

---

## 💡 一句话要点

**提出RoboRefer以解决机器人空间指称与推理问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `空间指称` `视觉语言模型` `三维理解` `强化学习` `机器人技术` `多步推理` `深度学习`

## 📋 核心要点

1. 现有方法在理解复杂三维场景和动态推理指示位置方面存在不足，难以满足机器人交互需求。
2. 提出RoboRefer，通过集成深度编码器和强化微调，提升空间理解和多步推理能力。
3. 实验结果显示，RoboRefer在空间理解和推理任务上表现优异，超越了现有的多个基线模型。

## 📝 摘要（中文）

空间指称是具身机器人与三维物理世界互动的基本能力。然而，即使是强大的预训练视觉语言模型（VLM），现有方法仍无法准确理解复杂的三维场景并动态推理指示位置。为此，本文提出RoboRefer，一个具有三维感知能力的VLM，通过集成解耦的深度编码器实现精确的空间理解，并通过强化微调（RFT）推进多步空间推理。我们引入了RefSpatial，一个包含2000万个问答对的大规模数据集，涵盖31种空间关系，支持复杂的推理过程。实验表明，经过监督微调的RoboRefer在空间理解上达到了89.6%的成功率，经过强化微调的RoboRefer在RefSpatial-Bench上超越所有基线，平均准确率比Gemini-2.5-Pro高出17.4%。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人在复杂三维场景中进行空间指称和推理的能力不足问题。现有方法在理解和推理方面的局限性导致机器人无法有效执行任务。

**核心思路**：RoboRefer通过集成解耦的深度编码器实现精确的空间理解，并采用强化微调（RFT）来提升多步空间推理能力，旨在增强机器人对环境的理解和互动能力。

**技术框架**：RoboRefer的整体架构包括两个主要阶段：首先是通过监督微调（SFT）进行深度编码器的训练，以实现空间理解；其次是通过强化微调（RFT）进行多步推理的训练，使用针对空间指称任务的度量敏感过程奖励函数。

**关键创新**：RoboRefer的主要创新在于引入了RefSpatial数据集，包含2000万个问答对和31种空间关系，支持复杂的推理过程，显著提升了模型的推理能力和准确性。

**关键设计**：在模型设计中，采用了特定的损失函数和奖励机制，以优化空间指称任务的性能，同时确保模型能够处理多步推理的复杂性。

## 📊 实验亮点

实验结果表明，经过监督微调的RoboRefer在空间理解任务上取得了89.6%的成功率，而经过强化微调的RoboRefer在RefSpatial-Bench上超越所有基线，平均准确率比Gemini-2.5-Pro高出17.4%，显示出显著的性能提升。

## 🎯 应用场景

RoboRefer的研究成果具有广泛的应用潜力，特别是在服务机器人、自动驾驶和智能家居等领域。通过提升机器人对环境的理解能力，RoboRefer能够更好地执行复杂的动态任务，推动机器人技术的实际应用和发展。

## 📄 摘要（原文）

> Spatial referring is a fundamental capability of embodied robots to interact with the 3D physical world. However, even with the powerful pretrained vision language models (VLMs), recent approaches are still not qualified to accurately understand the complex 3D scenes and dynamically reason about the instruction-indicated locations for interaction. To this end, we propose RoboRefer, a 3D-aware VLM that can first achieve precise spatial understanding by integrating a disentangled but dedicated depth encoder via supervised fine-tuning (SFT). Moreover, RoboRefer advances generalized multi-step spatial reasoning via reinforcement fine-tuning (RFT), with metric-sensitive process reward functions tailored for spatial referring tasks. To support SFT and RFT training, we introduce RefSpatial, a large-scale dataset of 20M QA pairs (2x prior), covering 31 spatial relations (vs. 15 prior) and supporting complex reasoning processes (up to 5 steps). In addition, we introduce RefSpatial-Bench, a challenging benchmark filling the gap in evaluating spatial referring with multi-step reasoning. Experiments show that SFT-trained RoboRefer achieves state-of-the-art spatial understanding, with an average success rate of 89.6%. RFT-trained RoboRefer further outperforms all other baselines by a large margin, even surpassing Gemini-2.5-Pro by 17.4% in average accuracy on RefSpatial-Bench. Notably, RoboRefer can be integrated with various control policies to execute long-horizon, dynamic tasks across diverse robots (e,g., UR5, G1 humanoid) in cluttered real-world scenes. Please see the project page at https://zhoues.github.io/RoboRefer.

