---
layout: default
title: "OwlCap: Harmonizing Motion-Detail for Video Captioning via HMD-270K and Caption Set Equivalence Reward"
---

# OwlCap: Harmonizing Motion-Detail for Video Captioning via HMD-270K and Caption Set Equivalence Reward

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18634" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18634v2</a>
  <a href="https://arxiv.org/pdf/2508.18634.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18634v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18634v2', 'OwlCap: Harmonizing Motion-Detail for Video Captioning via HMD-270K and Caption Set Equivalence Reward')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chunlin Zhong, Qiuxia Hou, Zhangjun Zhou, Shuang Hao, Haonan Lu, Yanhao Zhang, He Tang, Xiang Bai

**分类**: cs.CV

**发布日期**: 2025-08-26 (更新: 2025-08-27)

**备注**: 9 pages, 6figures

---

## 💡 一句话要点

**提出OwlCap以解决视频字幕生成中的运动细节不平衡问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频字幕生成` `运动细节平衡` `多模态大语言模型` `数据集构建` `优化方法`

## 📋 核心要点

1. 现有视频字幕生成方法常常存在运动与细节不平衡的问题，导致生成的字幕不完整，影响视频理解。
2. 本文提出HMD-270K数据集和CSER优化方法，旨在通过平衡运动与细节来提升字幕生成的完整性与准确性。
3. OwlCap模型在VDC和DREAM-1K基准上分别提升了4.2和4.6的性能，显示出显著的改进效果。

## 📝 摘要（中文）

视频字幕生成旨在为视频内容生成全面且连贯的描述，推动视频理解与生成的进步。然而，现有方法常常面临运动细节不平衡的问题，导致模型过度强调某一方面而忽视另一面，从而生成不完整的字幕。为了解决这一问题，本文从数据和优化两个方面提出了解决方案：构建了Harmonizing Motion-Detail 270K（HMD-270K）数据集，并引入了基于Group Relative Policy Optimization（GRPO）的Caption Set Equivalence Reward（CSER）。通过HMD-270K的监督微调和GRPO后训练，开发了OwlCap模型，实验结果表明OwlCap在两个基准上显著提升了性能。

## 🔬 方法详解

**问题定义**：本文旨在解决视频字幕生成中运动与细节不平衡的问题。现有方法往往过于强调某一方面，导致生成的字幕缺乏完整性和一致性。

**核心思路**：通过构建HMD-270K数据集和引入CSER优化方法，旨在实现运动与细节的平衡，从而提升视频字幕的质量。

**技术框架**：整体架构包括两个主要阶段：数据构建阶段（MDF和FGE）和优化阶段（GRPO与CSER）。MDF负责融合运动与细节，FGE进行细致审查，CSER则通过单元到集合的匹配进行优化。

**关键创新**：HMD-270K数据集的构建和CSER的引入是本文的核心创新，前者提供了丰富的训练数据，后者通过双向验证提升了生成字幕的完整性与准确性。

**关键设计**：在模型训练中，采用了特定的损失函数来平衡运动与细节的权重，同时在网络结构上进行了优化，以适应多模态输入的处理。

## 📊 实验亮点

OwlCap模型在视频字幕生成任务中表现出色，在VDC基准上提升了4.2的准确率，在DREAM-1K基准上提升了4.6的F1分数，显著优于现有基线模型，验证了其在运动与细节平衡方面的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括视频监控、自动化视频编辑、在线教育等，能够为视频内容的自动理解和生成提供更高质量的支持。未来，OwlCap模型和HMD-270K数据集的发布将推动视频字幕生成技术的进一步发展，促进相关领域的研究进展。

## 📄 摘要（原文）

> Video captioning aims to generate comprehensive and coherent descriptions of the video content, contributing to the advancement of both video understanding and generation. However, existing methods often suffer from motion-detail imbalance, as models tend to overemphasize one aspect while neglecting the other. This imbalance results in incomplete captions, which in turn leads to a lack of consistency in video understanding and generation. To address this issue, we propose solutions from two aspects: 1) Data aspect: We constructed the Harmonizing Motion-Detail 270K (HMD-270K) dataset through a two-stage pipeline: Motion-Detail Fusion (MDF) and Fine-Grained Examination (FGE). 2) Optimization aspect: We introduce the Caption Set Equivalence Reward (CSER) based on Group Relative Policy Optimization (GRPO). CSER enhances completeness and accuracy in capturing both motion and details through unit-to-set matching and bidirectional validation. Based on the HMD-270K supervised fine-tuning and GRPO post-training with CSER, we developed OwlCap, a powerful video captioning multi-modal large language model (MLLM) with motion-detail balance. Experimental results demonstrate that OwlCap achieves significant improvements compared to baseline models on two benchmarks: the detail-focused VDC (+4.2 Acc) and the motion-focused DREAM-1K (+4.6 F1). The HMD-270K dataset and OwlCap model will be publicly released to facilitate video captioning research community advancements.

