---
layout: default
title: SceneDesigner: Controllable Multi-Object Image Generation with 9-DoF Pose Manipulation
---

# SceneDesigner: Controllable Multi-Object Image Generation with 9-DoF Pose Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.16666" class="toolbar-btn" target="_blank">📄 arXiv: 2511.16666v1</a>
  <a href="https://arxiv.org/pdf/2511.16666.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.16666v1" onclick="toggleFavorite(this, '2511.16666v1', 'SceneDesigner: Controllable Multi-Object Image Generation with 9-DoF Pose Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhenyuan Qin, Xincheng Shuai, Henghui Ding

**分类**: cs.CV

**发布日期**: 2025-11-20

**备注**: NeurIPS 2025 (Spotlight), Project Page: https://henghuiding.com/SceneDesigner/

**🔗 代码/项目**: [GITHUB](https://github.com/FudanCVL/SceneDesigner)

---

## 💡 一句话要点

**SceneDesigner：提出基于CNOCS Map和强化学习的两阶段训练方法，实现多物体9自由度姿态精确控制的图像生成。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `可控图像生成` `9自由度姿态控制` `多物体场景` `CNOCS Map` `强化学习` `两阶段训练` `解耦对象采样` `ObjectPose9D数据集`

## 📋 核心要点

1. 现有方法在多物体9自由度姿态控制方面存在可控性不足和生成质量下降的问题，难以实现精确控制。
2. SceneDesigner利用CNOCS Map编码9自由度姿态信息，并采用分支网络结构，实现更高效和稳定的训练。
3. 通过ObjectPose9D数据集和基于强化学习的两阶段训练，以及解耦对象采样，显著提升了生成质量和可控性。

## 📝 摘要（中文）

可控图像生成近年来备受关注，它允许用户操纵视觉内容，例如身份和风格。然而，同时控制多个物体的9自由度姿态（位置、大小和方向）仍然是一个开放的挑战。尽管最近取得了一些进展，但现有方法通常存在可控性有限和质量下降的问题，无法实现全面的多物体9自由度姿态控制。为了解决这些限制，我们提出了SceneDesigner，一种用于精确和灵活的多物体9自由度姿态操纵的方法。SceneDesigner将一个分支网络集成到预训练的基础模型中，并利用一种新的表示方法，CNOCS Map，它从相机视角编码9自由度姿态信息。这种表示方法表现出很强的几何解释特性，从而实现更有效和稳定的训练。为了支持训练，我们构建了一个新的数据集ObjectPose9D，它聚合了来自不同来源的图像以及9自由度姿态注释。为了进一步解决数据不平衡问题，特别是低频姿态下的性能下降问题，我们引入了一种带有强化学习的两阶段训练策略，其中第二阶段使用基于奖励的目标在重新平衡的数据上微调模型。在推理时，我们提出了解耦对象采样，这是一种缓解复杂多对象场景中对象生成不足和概念混淆的技术。此外，通过集成用户特定的个性化权重，SceneDesigner可以为参考对象实现定制的姿态控制。大量的定性和定量实验表明，SceneDesigner在可控性和质量方面都显著优于现有方法。

## 🔬 方法详解

**问题定义**：现有方法在多物体场景下，难以同时控制物体的9自由度姿态（位置、大小、方向），存在可控性差、生成质量低的问题。尤其是在复杂场景和低频姿态下，性能会显著下降。这些方法难以满足用户对场景进行精细化编辑的需求。

**核心思路**：论文的核心思路是利用一种新的姿态表示方法CNOCS Map，它能够有效地编码物体的9自由度姿态信息，并具有良好的几何解释性，从而提高训练的稳定性和效率。此外，通过两阶段训练策略和解耦对象采样，解决数据不平衡和概念混淆的问题。

**技术框架**：SceneDesigner的整体框架包括以下几个主要模块：1) 基于预训练模型的分支网络，用于生成图像；2) CNOCS Map编码器，将9自由度姿态信息转换为CNOCS Map；3) ObjectPose9D数据集，用于训练模型；4) 基于强化学习的两阶段训练策略，用于解决数据不平衡问题；5) 解耦对象采样，用于缓解对象生成不足和概念混淆。

**关键创新**：论文的关键创新在于：1) 提出了CNOCS Map，一种新的9自由度姿态表示方法，具有良好的几何解释性；2) 提出了基于强化学习的两阶段训练策略，有效解决了数据不平衡问题；3) 提出了解耦对象采样，缓解了复杂场景下的对象生成不足和概念混淆。

**关键设计**：CNOCS Map的具体计算方式未知，但强调了其几何解释性。两阶段训练策略中，第一阶段使用标准损失函数进行预训练，第二阶段使用基于奖励的强化学习目标，对低频姿态进行微调。解耦对象采样的具体实现方式未知，但旨在独立地控制每个对象的生成。

## 📊 实验亮点

SceneDesigner在多物体9自由度姿态控制的图像生成任务上，显著优于现有方法。通过定性和定量实验表明，SceneDesigner在可控性和生成质量方面均取得了显著提升。具体的性能数据和对比基线在论文中进行了详细展示，但摘要中未提供具体数值。

## 🎯 应用场景

SceneDesigner可应用于虚拟现实、游戏开发、电影制作等领域，实现对场景中多个物体的姿态进行精确控制，从而创造出更加逼真和可定制的虚拟环境。该技术还可用于数据增强，生成具有不同姿态的合成数据，提升计算机视觉模型的性能。未来，该技术有望应用于机器人操作和自动驾驶等领域，实现对环境的精确感知和控制。

## 📄 摘要（原文）

> Controllable image generation has attracted increasing attention in recent years, enabling users to manipulate visual content such as identity and style. However, achieving simultaneous control over the 9D poses (location, size, and orientation) of multiple objects remains an open challenge. Despite recent progress, existing methods often suffer from limited controllability and degraded quality, falling short of comprehensive multi-object 9D pose control. To address these limitations, we propose SceneDesigner, a method for accurate and flexible multi-object 9-DoF pose manipulation. SceneDesigner incorporates a branched network to the pre-trained base model and leverages a new representation, CNOCS map, which encodes 9D pose information from the camera view. This representation exhibits strong geometric interpretation properties, leading to more efficient and stable training. To support training, we construct a new dataset, ObjectPose9D, which aggregates images from diverse sources along with 9D pose annotations. To further address data imbalance issues, particularly performance degradation on low-frequency poses, we introduce a two-stage training strategy with reinforcement learning, where the second stage fine-tunes the model using a reward-based objective on rebalanced data. At inference time, we propose Disentangled Object Sampling, a technique that mitigates insufficient object generation and concept confusion in complex multi-object scenes. Moreover, by integrating user-specific personalization weights, SceneDesigner enables customized pose control for reference subjects. Extensive qualitative and quantitative experiments demonstrate that SceneDesigner significantly outperforms existing approaches in both controllability and quality. Code is publicly available at https://github.com/FudanCVL/SceneDesigner.

