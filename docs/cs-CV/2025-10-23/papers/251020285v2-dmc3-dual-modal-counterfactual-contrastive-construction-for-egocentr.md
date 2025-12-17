---
layout: default
title: DMC$^3$: Dual-Modal Counterfactual Contrastive Construction for Egocentric Video Question Answering
---

# DMC$^3$: Dual-Modal Counterfactual Contrastive Construction for Egocentric Video Question Answering

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.20285" target="_blank" class="toolbar-btn">arXiv: 2510.20285v2</a>
    <a href="https://arxiv.org/pdf/2510.20285.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.20285v2" 
            onclick="toggleFavorite(this, '2510.20285v2', 'DMC$^3$: Dual-Modal Counterfactual Contrastive Construction for Egocentric Video Question Answering')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Jiayi Zou, Chaofan Chen, Bing-Kun Bao, Changsheng Xu

**分类**: cs.CV, cs.MM

**发布日期**: 2025-10-23 (更新: 2025-12-01)

**DOI**: [10.1145/3746027.3755085](https://doi.org/10.1145/3746027.3755085)

---

## 💡 一句话要点

**提出DMC$^3$框架以解决第一人称视频问答中的挑战**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `第一人称视频问答` `反事实学习` `对比优化` `多模态学习` `视频理解`

## 📋 核心要点

1. 现有方法在处理第一人称视频问答时，未能有效应对多事件理解和手物交互识别等独特挑战。
2. 本文提出DMC$^3$框架，通过反事实样本构建和对比优化，增强了文本和视觉模态的样本生成与学习。
3. 实验结果显示，DMC$^3$在多个数据集上均取得了领先的性能，验证了其有效性和优越性。

## 📝 摘要（中文）

第一人称视频问答（Egocentric VideoQA）在理解第一人称视频中扮演着重要角色，旨在基于第一人称视频回答问题。现有方法在预训练和微调的范式下取得了一定进展，但忽视了第一人称视角带来的独特挑战，如理解多个事件和识别手物交互。为应对这些挑战，本文提出了一种双模态反事实对比构建（DMC$^3$）框架，包含一个基础的Egocentric VideoQA模型、一个反事实样本构建模块和一个反事实样本参与的对比优化模块。实验结果表明，该方法在EgoTaskQA的正常和间接分割上分别达到了52.51%和46.04%的性能，在QAEGO4D上达到了13.2%，均达到了最先进的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决第一人称视频问答中的多事件理解和手物交互识别等挑战。现有方法在处理这些问题时存在明显不足，无法充分利用第一人称视角的信息。

**核心思路**：提出双模态反事实对比构建（DMC$^3$）框架，通过生成正负样本来增强模型的学习能力，特别是在文本和视觉模态之间的对比学习。

**技术框架**：DMC$^3$框架包括三个主要模块：基础的Egocentric VideoQA模型、反事实样本构建模块和反事实样本参与的对比优化模块。首先生成样本，然后将其与原始样本一起输入基础模型，最后进行对比优化。

**关键创新**：最重要的创新在于反事实样本构建模块，通过事件描述的改写和核心交互挖掘生成样本，显著提升了模型对复杂场景的理解能力。

**关键设计**：在对比优化中，采用对比损失函数来最小化原始样本特征与正样本特征之间的距离，同时最大化与负样本的距离，确保模型能够有效区分不同类型的样本。该设计使得模型在多模态学习中表现出色。

## 📊 实验亮点

实验结果表明，DMC$^3$在EgoTaskQA的正常和间接分割上分别达到了52.51%和46.04%的性能，在QAEGO4D上达到了13.2%，均超越了现有的最先进方法，展示了显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括智能监控、虚拟现实和人机交互等场景，能够帮助系统更好地理解和分析第一人称视频内容，提升用户体验和交互质量。未来，随着技术的进步，该框架有望在更多实际应用中发挥重要作用。

## 📄 摘要（原文）

> Egocentric Video Question Answering (Egocentric VideoQA) plays an important role in egocentric video understanding, which refers to answering questions based on first-person videos. Although existing methods have made progress through the paradigm of pre-training and fine-tuning, they ignore the unique challenges posed by the first-person perspective, such as understanding multiple events and recognizing hand-object interactions. To deal with these challenges, we propose a Dual-Modal Counterfactual Contrastive Construction (DMC$^3$) framework, which contains an egocentric videoqa baseline, a counterfactual sample construction module and a counterfactual sample-involved contrastive optimization. Specifically, We first develop a counterfactual sample construction module to generate positive and negative samples for textual and visual modalities through event description paraphrasing and core interaction mining, respectively. Then, We feed these samples together with the original samples into the baseline. Finally, in the counterfactual sample-involved contrastive optimization module, we apply contrastive loss to minimize the distance between the original sample features and the positive sample features, while maximizing the distance from the negative samples. Experiments show that our method achieve 52.51\% and 46.04\% on the \textit{normal} and \textit{indirect} splits of EgoTaskQA, and 13.2\% on QAEGO4D, both reaching the state-of-the-art performance.

