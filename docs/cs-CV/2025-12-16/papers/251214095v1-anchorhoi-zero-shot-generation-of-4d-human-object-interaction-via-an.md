---
layout: default
title: AnchorHOI: Zero-shot Generation of 4D Human-Object Interaction via Anchor-based Prior Distillation
---

# AnchorHOI: Zero-shot Generation of 4D Human-Object Interaction via Anchor-based Prior Distillation

**arXiv**: [2512.14095v1](https://arxiv.org/abs/2512.14095) | [PDF](https://arxiv.org/pdf/2512.14095.pdf)

**作者**: Sisi Dai, Kai Xu

**分类**: cs.CV

**发布日期**: 2025-12-16

**备注**: AAAI 2026

---

## 💡 一句话要点

**提出AnchorHOI框架，通过基于锚点的先验蒸馏策略解决零样本4D人-物交互生成中的交互线索不足问题。**

🎯 **匹配领域**: **动作生成** **视觉里程计** **强化学习**

**关键词**: `4D人-物交互生成` `零样本学习` `先验蒸馏` `神经辐射场` `视频扩散模型` `运动合成` `交互感知锚点` `多模态生成`

## 📋 核心要点

1. 现有零样本4D HOI生成方法主要依赖图像扩散模型，交互线索蒸馏不足，限制了跨场景适用性。
2. 提出基于锚点的先验蒸馏策略，通过构建交互感知锚点（如锚点NeRF和关键点）指导生成过程。
3. 实验显示AnchorHOI在多样性和泛化性上优于先前方法，有效提升了4D HOI生成质量。

## 📝 摘要（中文）

尽管基于监督方法的文本驱动4D人-物交互生成取得了显著进展，但由于大规模4D HOI数据集的稀缺性，其可扩展性仍然受限。为了克服这一限制，最近的方法尝试使用预训练的图像扩散模型进行零样本4D HOI生成。然而，在生成过程中交互线索的蒸馏非常有限，限制了它们在不同场景中的适用性。在本文中，我们提出了AnchorHOI，这是一个新颖的框架，通过结合视频扩散模型超越图像扩散模型，充分利用混合先验，推进了4D HOI生成。然而，直接使用此类先验优化高维4D HOI仍然具有挑战性，特别是在人体姿态和组合运动方面。为了解决这一挑战，AnchorHOI引入了一种基于锚点的先验蒸馏策略，该策略构建交互感知的锚点，然后利用它们在一个可处理的两步过程中指导生成。具体来说，为4D HOI生成设计了两个定制的锚点：用于表达性交互组合的锚点神经辐射场，以及用于逼真运动合成的锚点关键点。大量实验表明，AnchorHOI在多样性和泛化性方面优于先前的方法。

## 🔬 方法详解

AnchorHOI是一个零样本4D人-物交互生成框架，整体采用基于锚点的先验蒸馏策略。关键技术创新包括：结合视频扩散模型以利用混合先验，设计锚点NeRF用于交互组合和锚点关键点用于运动合成，通过两步过程（先构建锚点再指导生成）优化高维4D HOI。与现有方法的主要区别在于，它超越了仅依赖图像扩散模型的局限，通过锚点机制更有效地蒸馏交互线索，解决了人体姿态和组合运动的优化挑战。

## 📊 实验亮点

AnchorHOI在零样本4D HOI生成任务中表现出色，实验结果表明其在多样性和泛化性方面显著优于先前方法，有效解决了交互线索不足的问题，提升了生成质量。

## 🎯 应用场景

该研究可应用于虚拟现实、游戏开发、机器人交互仿真和影视特效等领域，通过生成逼真的4D人-物交互序列，降低数据采集成本，提升场景构建的灵活性和多样性。

## 📄 摘要（原文）

> Despite significant progress in text-driven 4D human-object interaction (HOI) generation with supervised methods, the scalability remains limited by the scarcity of large-scale 4D HOI datasets. To overcome this, recent approaches attempt zero-shot 4D HOI generation with pre-trained image diffusion models. However, interaction cues are minimally distilled during the generation process, restricting their applicability across diverse scenarios. In this paper, we propose AnchorHOI, a novel framework that thoroughly exploits hybrid priors by incorporating video diffusion models beyond image diffusion models, advancing 4D HOI generation. Nevertheless, directly optimizing high-dimensional 4D HOI with such priors remains challenging, particularly for human pose and compositional motion. To address this challenge, AnchorHOI introduces an anchor-based prior distillation strategy, which constructs interaction-aware anchors and then leverages them to guide generation in a tractable two-step process. Specifically, two tailored anchors are designed for 4D HOI generation: anchor Neural Radiance Fields (NeRFs) for expressive interaction composition, and anchor keypoints for realistic motion synthesis. Extensive experiments demonstrate that AnchorHOI outperforms previous methods with superior diversity and generalization.

