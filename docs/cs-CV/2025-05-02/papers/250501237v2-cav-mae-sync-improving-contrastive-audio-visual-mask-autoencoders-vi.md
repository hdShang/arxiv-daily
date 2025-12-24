---
layout: default
title: CAV-MAE Sync: Improving Contrastive Audio-Visual Mask Autoencoders via Fine-Grained Alignment
---

# CAV-MAE Sync: Improving Contrastive Audio-Visual Mask Autoencoders via Fine-Grained Alignment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.01237" class="toolbar-btn" target="_blank">📄 arXiv: 2505.01237v2</a>
  <a href="https://arxiv.org/pdf/2505.01237.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.01237v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.01237v2', 'CAV-MAE Sync: Improving Contrastive Audio-Visual Mask Autoencoders via Fine-Grained Alignment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Edson Araujo, Andrew Rouditchenko, Yuan Gong, Saurabhchand Bhati, Samuel Thomas, Brian Kingsbury, Leonid Karlinsky, Rogerio Feris, James R. Glass, Hilde Kuehne

**分类**: cs.MM, cs.CV, cs.SD, eess.AS

**发布日期**: 2025-05-02 (更新: 2025-05-21)

**备注**: To be published at CVPR 2025, code available at https://github.com/edsonroteia/cav-mae-sync

---

## 💡 一句话要点

**提出CAV-MAE Sync以解决音视频模态对齐问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `音视频学习` `模态对齐` `自监督学习` `对比学习` `深度学习`

## 📋 核心要点

1. 现有音视频学习方法依赖全局音频表示，未能有效捕捉细粒度的时间对应关系，导致性能不足。
2. CAV-MAE Sync通过将音频视为与视频帧对齐的时间序列，分离对比与重建目标，提升了模态间的对齐效果。
3. 在多个数据集上进行的实验表明，该方法在零样本检索、分类和定位任务中表现优异，超越了复杂模型的效果。

## 📝 摘要（中文）

近年来，音视频学习的进展在跨模态表示学习中展现出良好效果。然而，大多数方法依赖于全局音频表示，未能捕捉与视觉帧的细粒度时间对应关系。此外，现有方法在联合学习重建与跨模态对齐时常面临优化目标冲突。本文提出CAV-MAE Sync，作为原始CAV-MAE框架的有效扩展，旨在解决这三大挑战。我们通过将音频视为与视频帧对齐的时间序列，分离对比与重建目标，并引入可学习的注册标记来改善空间定位。我们在AudioSet、VGG Sound和ADE20K Sound数据集上进行评估，展示了该方法在零样本检索、分类和定位任务上的最先进性能，超越了更复杂的架构。

## 🔬 方法详解

**问题定义**：本文旨在解决音视频模态对齐中的细粒度时间对应问题。现有方法通常依赖全局音频表示，无法有效捕捉与视觉帧的细节关系，同时在联合学习重建与对齐时面临优化目标冲突。

**核心思路**：CAV-MAE Sync通过将音频视为与视频帧对齐的时间序列，解决了模态间的粒度不匹配问题。通过分离对比和重建目标，避免了优化目标的冲突，从而提升了模型的学习效果。

**技术框架**：该方法的整体架构包括三个主要模块：音频时间序列处理模块、对比学习模块和重建模块。音频模块负责将音频信号转化为与视频帧对齐的表示，对比学习模块用于优化模态间的对齐，而重建模块则专注于重建输入信号。

**关键创新**：最重要的创新在于引入可学习的注册标记，减少了语义负担，使得补丁标记的表示更加有效。这一设计使得模型在空间定位上表现更佳，显著提升了对齐效果。

**关键设计**：在参数设置上，模型使用了专门的全局标记来分离对比和重建目标，损失函数则结合了对比损失与重建损失，以确保两者的优化不冲突。网络结构上，采用了深度学习框架以支持复杂的音视频特征提取。

## 📊 实验亮点

在多个数据集上的实验结果显示，CAV-MAE Sync在零样本检索、分类和定位任务中均达到了最先进的性能，超越了更复杂的模型架构。例如，在AudioSet数据集上，该方法的性能提升幅度达到了XX%，显示出其在音视频学习领域的显著优势。

## 🎯 应用场景

该研究的潜在应用领域包括多模态内容检索、视频理解、自动字幕生成等。通过提升音视频模态的对齐效果，CAV-MAE Sync可以在多种实际场景中提高信息提取的准确性和效率，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Recent advances in audio-visual learning have shown promising results in learning representations across modalities. However, most approaches rely on global audio representations that fail to capture fine-grained temporal correspondences with visual frames. Additionally, existing methods often struggle with conflicting optimization objectives when trying to jointly learn reconstruction and cross-modal alignment. In this work, we propose CAV-MAE Sync as a simple yet effective extension of the original CAV-MAE framework for self-supervised audio-visual learning. We address three key challenges: First, we tackle the granularity mismatch between modalities by treating audio as a temporal sequence aligned with video frames, rather than using global representations. Second, we resolve conflicting optimization goals by separating contrastive and reconstruction objectives through dedicated global tokens. Third, we improve spatial localization by introducing learnable register tokens that reduce semantic load on patch tokens. We evaluate the proposed approach on AudioSet, VGG Sound, and the ADE20K Sound dataset on zero-shot retrieval, classification and localization tasks demonstrating state-of-the-art performance and outperforming more complex architectures.

