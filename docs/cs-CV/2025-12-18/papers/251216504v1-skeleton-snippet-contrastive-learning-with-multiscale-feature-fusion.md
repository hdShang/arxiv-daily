---
layout: default
title: Skeleton-Snippet Contrastive Learning with Multiscale Feature Fusion for Action Localization
---

# Skeleton-Snippet Contrastive Learning with Multiscale Feature Fusion for Action Localization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16504" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16504v1</a>
  <a href="https://arxiv.org/pdf/2512.16504.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16504v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16504v1', 'Skeleton-Snippet Contrastive Learning with Multiscale Feature Fusion for Action Localization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qiushuo Cheng, Jingjing Liu, Catherine Morgan, Alan Whone, Majid Mirmehdi

**分类**: cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出基于骨骼片段对比学习和多尺度特征融合的动作定位方法**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `骨骼动作定位` `自监督学习` `对比学习` `时间片段判别` `多尺度特征融合`

## 📋 核心要点

1. 基于骨骼的动作定位需要捕捉帧间细微差异，现有方法难以有效学习时间敏感的特征。
2. 论文提出片段判别预训练任务，通过对比学习区分不同视频片段，增强模型对时间边界的感知能力。
3. 实验表明，该方法在BABEL和PKUMMD数据集上均取得了显著提升，验证了其有效性。

## 📝 摘要（中文）

本文针对基于骨骼的动作定位任务，提出了一种自监督预训练范式。不同于视频级别的动作识别，动作定位需要对时间敏感的特征，以捕捉相邻帧之间细微的标签变化。为此，我们设计了一个片段判别预训练任务，将骨骼序列密集地投影到非重叠的片段中，并通过对比学习来区分不同视频中的片段特征。此外，我们利用U型模块融合中间特征，增强特征分辨率，从而提升帧级别的定位性能。实验结果表明，我们的方法在BABEL数据集上持续改进了现有的基于骨骼的对比学习方法，并在PKUMMD数据集上实现了最先进的迁移学习性能，预训练数据来自NTU RGB+D和BABEL。

## 🔬 方法详解

**问题定义**：现有的基于骨骼的动作识别方法在视频级别表现良好，但直接应用于时间动作定位任务时，无法有效捕捉动作边界，尤其是在相邻帧标签发生变化时，对时间敏感的特征提取能力不足。

**核心思路**：论文的核心思路是通过自监督预训练，学习对时间片段具有区分性的特征表示。具体来说，将骨骼序列分割成多个非重叠的片段，然后利用对比学习，使得来自同一视频的片段特征尽可能相似，而来自不同视频的片段特征尽可能不同。这样可以迫使模型学习到能够区分不同时间片段的特征，从而提高动作定位的准确性。

**技术框架**：整体框架包括两个主要部分：片段判别预训练和多尺度特征融合。首先，使用片段判别预训练任务，在大量无标签的骨骼数据上训练模型，学习对时间片段具有区分性的特征表示。然后，将预训练好的模型作为骨干网络，并添加一个U型模块，用于融合不同尺度的特征。最后，在目标数据集上进行微调，以适应特定的动作定位任务。

**关键创新**：论文的关键创新在于提出了片段判别预训练任务，该任务能够有效地学习对时间片段具有区分性的特征表示。与传统的对比学习方法不同，该方法不是直接对比整个视频的特征，而是对比视频片段的特征，从而更加关注时间边界的信息。

**关键设计**：在片段判别预训练任务中，使用了InfoNCE损失函数，用于最大化正样本之间的相似度，最小化负样本之间的相似度。U型模块的具体结构未知，但其目的是融合不同层级的特征，以提高特征的分辨率。具体的参数设置和网络结构细节在论文中可能有所描述，但摘要中未提及。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16504v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16504v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16504v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

该方法在BABEL数据集上，相较于现有的基于骨骼的对比学习方法，取得了持续的改进。在PKUMMD数据集上，通过在NTU RGB+D和BABEL数据集上进行预训练，实现了最先进的迁移学习性能。具体的性能数据和提升幅度需要在论文中查找。

## 🎯 应用场景

该研究成果可应用于智能监控、人机交互、康复训练等领域。例如，在智能监控中，可以利用该方法自动检测异常行为；在人机交互中，可以利用该方法识别用户的动作意图；在康复训练中，可以利用该方法评估患者的康复进度。该研究有助于提升相关系统的智能化水平和用户体验。

## 📄 摘要（原文）

> The self-supervised pretraining paradigm has achieved great success in learning 3D action representations for skeleton-based action recognition using contrastive learning. However, learning effective representations for skeleton-based temporal action localization remains challenging and underexplored. Unlike video-level {action} recognition, detecting action boundaries requires temporally sensitive features that capture subtle differences between adjacent frames where labels change. To this end, we formulate a snippet discrimination pretext task for self-supervised pretraining, which densely projects skeleton sequences into non-overlapping segments and promotes features that distinguish them across videos via contrastive learning. Additionally, we build on strong backbones of skeleton-based action recognition models by fusing intermediate features with a U-shaped module to enhance feature resolution for frame-level localization. Our approach consistently improves existing skeleton-based contrastive learning methods for action localization on BABEL across diverse subsets and evaluation protocols. We also achieve state-of-the-art transfer learning performance on PKUMMD with pretraining on NTU RGB+D and BABEL.

