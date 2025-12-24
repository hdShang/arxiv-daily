---
layout: default
title: "OmniGaze: Reward-inspired Generalizable Gaze Estimation In The Wild"
---

# OmniGaze: Reward-inspired Generalizable Gaze Estimation In The Wild

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.13660" class="toolbar-btn" target="_blank">📄 arXiv: 2510.13660v2</a>
  <a href="https://arxiv.org/pdf/2510.13660.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.13660v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.13660v2', 'OmniGaze: Reward-inspired Generalizable Gaze Estimation In The Wild')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hongyu Qu, Jianan Wei, Xiangbo Shu, Yazhou Yao, Wenguan Wang, Jinhui Tang

**分类**: cs.CV

**发布日期**: 2025-10-15 (更新: 2025-10-16)

**备注**: Accepted to NeurIPS 2025; Project page: https://github.com/quhongyu/OmniGaze

---

## 💡 一句话要点

**OmniGaze：提出奖励驱动的通用凝视估计框架，解决野外场景泛化性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `凝视估计` `半监督学习` `伪标签` `领域泛化` `奖励模型`

## 📋 核心要点

1. 现有3D凝视估计方法在跨领域泛化性方面存在不足，主要受限于标注数据稀缺和多样性不足。
2. OmniGaze利用大规模无标注数据，通过伪标签和奖励模型来提升模型在野外场景的泛化能力。
3. 实验表明，OmniGaze在多个数据集上取得了SOTA性能，并展现出强大的零样本泛化能力。

## 📝 摘要（中文）

现有的3D凝视估计方法难以在不同的数据领域中泛化，这主要是由于带标注数据集的稀缺以及标注数据的多样性不足。本文提出了OmniGaze，一个半监督的3D凝视估计框架，它利用从多样且无约束的真实世界环境中收集的大规模无标注数据来缓解领域偏差，并推广野外场景下的凝视估计。首先，构建了一个多样化的无标注面部图像集合，这些图像在面部外观、背景环境、光照条件、头部姿势和眼睛遮挡方面各不相同。为了利用更广泛分布的无标注数据，OmniGaze采用标准的伪标签策略，并设计了一个奖励模型来评估伪标签的可靠性。除了将伪标签作为3D方向向量外，奖励模型还结合了由现成的视觉编码器提取的视觉嵌入以及通过提示多模态大型语言模型生成的凝视视角的语义线索，以计算置信度分数。然后，这些分数用于选择高质量的伪标签并对其进行加权以进行损失计算。大量实验表明，OmniGaze在五个数据集上实现了最先进的性能，包括同领域和跨领域设置。此外，我们还评估了OmniGaze作为凝视估计的可扩展数据引擎的有效性，它在四个未见数据集上表现出强大的零样本泛化能力。

## 🔬 方法详解

**问题定义**：现有3D凝视估计方法在真实场景中泛化能力差，主要原因是缺乏足够多样性和数量的标注数据，导致模型容易过拟合特定领域的数据，难以适应野外场景中复杂的光照、姿态和遮挡等情况。

**核心思路**：利用大规模无标注数据来提升模型的泛化能力。核心思想是使用伪标签方法，从未标注数据中生成带噪声的标签，并设计一个奖励模型来评估和筛选高质量的伪标签，从而训练一个更鲁棒的凝视估计模型。

**技术框架**：OmniGaze框架主要包含以下几个模块：1) 无标注数据收集模块：收集来自不同环境和场景的大量无标注面部图像。2) 伪标签生成模块：使用现有的凝视估计模型为无标注数据生成伪标签。3) 奖励模型：评估伪标签的质量，并为每个伪标签分配一个置信度分数。4) 模型训练模块：使用带权重的伪标签和少量标注数据来训练凝视估计模型。

**关键创新**：奖励模型的构建是关键创新点。它不仅仅依赖于伪标签本身，还结合了视觉嵌入和语义线索来评估伪标签的可靠性。视觉嵌入捕捉了面部图像的视觉特征，而语义线索则通过提示多模态大型语言模型来生成，从而提供更丰富的上下文信息。这种多模态融合的奖励模型能够更准确地评估伪标签的质量。

**关键设计**：奖励模型的设计细节包括：1) 使用预训练的视觉编码器提取视觉嵌入。2) 使用多模态大型语言模型（例如，通过提示工程）生成凝视视角的语义描述。3) 将视觉嵌入、语义描述和伪标签作为输入，训练一个回归模型来预测置信度分数。4) 使用置信度分数来加权损失函数，从而更重视高质量的伪标签。

## 📊 实验亮点

OmniGaze在五个数据集上取得了state-of-the-art的性能，包括在跨领域设置下的显著提升。此外，OmniGaze在四个未见数据集上展现出强大的零样本泛化能力，证明了其在野外场景下的鲁棒性和泛化性。具体性能数据未知，但论文强调了其在多个数据集上的优越性。

## 🎯 应用场景

OmniGaze具有广泛的应用前景，例如人机交互、虚拟现实/增强现实、驾驶员监控、安全监控等。通过提高凝视估计的准确性和鲁棒性，可以实现更自然和高效的人机交互，并为各种应用提供更可靠的视觉信息。

## 📄 摘要（原文）

> Current 3D gaze estimation methods struggle to generalize across diverse data domains, primarily due to i) the scarcity of annotated datasets, and ii) the insufficient diversity of labeled data. In this work, we present OmniGaze, a semi-supervised framework for 3D gaze estimation, which utilizes large-scale unlabeled data collected from diverse and unconstrained real-world environments to mitigate domain bias and generalize gaze estimation in the wild. First, we build a diverse collection of unlabeled facial images, varying in facial appearances, background environments, illumination conditions, head poses, and eye occlusions. In order to leverage unlabeled data spanning a broader distribution, OmniGaze adopts a standard pseudo-labeling strategy and devises a reward model to assess the reliability of pseudo labels. Beyond pseudo labels as 3D direction vectors, the reward model also incorporates visual embeddings extracted by an off-the-shelf visual encoder and semantic cues from gaze perspective generated by prompting a Multimodal Large Language Model to compute confidence scores. Then, these scores are utilized to select high-quality pseudo labels and weight them for loss computation. Extensive experiments demonstrate that OmniGaze achieves state-of-the-art performance on five datasets under both in-domain and cross-domain settings. Furthermore, we also evaluate the efficacy of OmniGaze as a scalable data engine for gaze estimation, which exhibits robust zero-shot generalization on four unseen datasets.

