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

**关键词**: `4D人-物交互生成` `零样本学习` `先验蒸馏` `神经辐射场` `运动合成` `扩散模型` `视频生成` `交互建模`

## 📋 核心要点

1. 现有零样本4D HOI生成方法主要依赖图像扩散模型，交互线索蒸馏不足，限制了跨场景适用性。
2. AnchorHOI提出基于锚点的先验蒸馏策略，通过构建交互感知锚点（如锚点NeRF和关键点）指导生成过程。
3. 实验表明，该方法在多样性和泛化性上优于先前方法，有效提升了4D HOI生成质量。

## 📝 摘要（中文）

尽管基于监督方法的文本驱动4D人-物交互生成取得了显著进展，但由于大规模4D HOI数据集的稀缺性，其可扩展性仍然受限。为了克服这一限制，最近的方法尝试使用预训练的图像扩散模型进行零样本4D HOI生成。然而，在生成过程中交互线索的蒸馏非常有限，限制了它们在不同场景中的适用性。本文提出了AnchorHOI，这是一个新颖的框架，通过结合视频扩散模型超越图像扩散模型，充分利用混合先验，推进了4D HOI生成。然而，直接使用此类先验优化高维4D HOI仍然具有挑战性，特别是在人体姿态和组合运动方面。为了解决这一挑战，AnchorHOI引入了一种基于锚点的先验蒸馏策略，该策略构建交互感知的锚点，然后利用它们在一个可处理的两步过程中指导生成。具体来说，为4D HOI生成设计了两个定制的锚点：用于表达性交互组合的锚点神经辐射场，以及用于逼真运动合成的锚点关键点。大量实验表明，AnchorHOI在多样性和泛化性方面优于先前的方法。

## 🔬 方法详解

AnchorHOI是一个零样本4D人-物交互生成框架，整体基于混合先验（结合图像和视频扩散模型）进行生成。关键技术创新在于引入锚点先验蒸馏策略：首先构建两个交互感知锚点——锚点NeRF用于建模交互组合，锚点关键点用于合成运动；然后通过两步过程（先优化锚点，再指导生成）实现可处理的高维4D HOI优化。与现有方法的主要区别在于，它超越了仅依赖图像扩散模型的局限，通过锚点机制更充分地蒸馏交互线索，解决了直接优化4D HOI的挑战。

## 📊 实验亮点

实验结果显示，AnchorHOI在零样本4D HOI生成任务中，相比先前方法在多样性和泛化性方面表现更优，通过锚点先验蒸馏有效提升了交互质量和运动真实性，验证了框架的有效性。

## 🎯 应用场景

该研究在虚拟现实、游戏开发、机器人交互仿真和影视特效制作等领域具有潜在应用价值，能够生成多样且逼真的4D人-物交互序列，降低对大规模标注数据的依赖，提升内容创作的效率和灵活性。

## 📄 摘要（原文）

> Despite significant progress in text-driven 4D human-object interaction (HOI) generation with supervised methods, the scalability remains limited by the scarcity of large-scale 4D HOI datasets. To overcome this, recent approaches attempt zero-shot 4D HOI generation with pre-trained image diffusion models. However, interaction cues are minimally distilled during the generation process, restricting their applicability across diverse scenarios. In this paper, we propose AnchorHOI, a novel framework that thoroughly exploits hybrid priors by incorporating video diffusion models beyond image diffusion models, advancing 4D HOI generation. Nevertheless, directly optimizing high-dimensional 4D HOI with such priors remains challenging, particularly for human pose and compositional motion. To address this challenge, AnchorHOI introduces an anchor-based prior distillation strategy, which constructs interaction-aware anchors and then leverages them to guide generation in a tractable two-step process. Specifically, two tailored anchors are designed for 4D HOI generation: anchor Neural Radiance Fields (NeRFs) for expressive interaction composition, and anchor keypoints for realistic motion synthesis. Extensive experiments demonstrate that AnchorHOI outperforms previous methods with superior diversity and generalization.

