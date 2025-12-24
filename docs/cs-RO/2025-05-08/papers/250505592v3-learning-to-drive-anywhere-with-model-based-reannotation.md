---
layout: default
title: Learning to Drive Anywhere with Model-Based Reannotation
---

# Learning to Drive Anywhere with Model-Based Reannotation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.05592" class="toolbar-btn" target="_blank">📄 arXiv: 2505.05592v3</a>
  <a href="https://arxiv.org/pdf/2505.05592.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.05592v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.05592v3', 'Learning to Drive Anywhere with Model-Based Reannotation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Noriaki Hirose, Lydia Ignatova, Kyle Stachowicz, Catherine Glossop, Sergey Levine, Dhruv Shah

**分类**: cs.RO, cs.CV, cs.LG, eess.SY

**发布日期**: 2025-05-08 (更新: 2025-11-21)

**备注**: 9 pages, 8 figures, 6 tables

**期刊**: IEEE Robotics and Automation Letters 2025

---

## 💡 一句话要点

**提出基于模型的重标注方法以解决机器人导航数据不足问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `机器人导航` `模型重标注` `视觉目标` `数据蒸馏` `长视野策略` `多样化训练数据` `无人驾驶` `复杂环境`

## 📋 核心要点

1. 现有的机器人导航策略受限于高质量训练数据的稀缺，导致其在复杂环境中的泛化能力不足。
2. 本文提出的MBRA框架通过利用被动收集的数据源，生成高质量的动作标签，从而增强训练数据的多样性和质量。
3. 实验结果显示，LogoNav在多种环境中表现优异，能够在复杂场景中有效导航，验证了其强大的泛化能力。

## 📝 摘要（中文）

开发广泛可推广的视觉导航策略是机器人领域的一大挑战，主要受限于大规模多样化训练数据的可用性。虽然研究者收集的精心策划的数据集质量高，但其规模有限，限制了策略的泛化能力。为此，本文探索利用丰富的被动收集数据源，包括大量众包的遥控数据和未标记的YouTube视频，尽管这些数据可能存在质量较低或缺失动作标签的问题。我们提出了基于模型的重标注框架（MBRA），利用学习的短视野模型生成高质量的动作标签。经过MBRA处理的数据被蒸馏为LogoNav，一个基于视觉目标或GPS航点的长视野导航策略。实验表明，使用MBRA处理数据训练的LogoNav在超过300米的距离内，在未见过的室内和室外环境中实现了最先进的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人导航策略在多样化和大规模训练数据不足的问题。现有方法通常依赖于小规模的高质量数据集，限制了策略的泛化能力。

**核心思路**：论文提出的MBRA框架通过利用被动收集的数据源，生成高质量的动作标签，进而增强训练数据的多样性和质量。这种方法允许机器人在未见过的环境中进行有效导航。

**技术框架**：MBRA框架包括数据收集、模型训练和数据重标注三个主要模块。首先，收集大量的众包遥控数据和未标记视频；然后，训练一个短视野的模型以生成动作标签；最后，将这些标签应用于训练LogoNav策略。

**关键创新**：MBRA的核心创新在于利用模型生成高质量的动作标签，克服了传统方法对高质量标注数据的依赖。这种方法显著提高了训练数据的有效性和多样性。

**关键设计**：在模型训练中，采用了特定的损失函数以优化动作生成的准确性，并设计了适应性强的网络结构，以便在不同环境中进行有效的导航。

## 📊 实验亮点

实验结果表明，经过MBRA处理的数据训练的LogoNav在超过300米的导航任务中表现优异，成功在复杂的室内外环境中导航，超越了现有的基线方法，展示了显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、服务机器人和无人机等。通过提高机器人在复杂环境中的导航能力，能够显著提升其在实际场景中的应用价值，推动智能机器人技术的进一步发展。

## 📄 摘要（原文）

> Developing broadly generalizable visual navigation policies for robots is a significant challenge, primarily constrained by the availability of large-scale, diverse training data. While curated datasets collected by researchers offer high quality, their limited size restricts policy generalization. To overcome this, we explore leveraging abundant, passively collected data sources, including large volumes of crowd-sourced teleoperation data and unlabeled YouTube videos, despite their potential for lower quality or missing action labels. We propose Model-Based ReAnnotation (MBRA), a framework that utilizes a learned short-horizon, model-based expert model to relabel or generate high-quality actions for these passive datasets. This relabeled data is then distilled into LogoNav, a long-horizon navigation policy conditioned on visual goals or GPS waypoints. We demonstrate that LogoNav, trained using MBRA-processed data, achieves state-of-the-art performance, enabling robust navigation over distances exceeding 300 meters in previously unseen indoor and outdoor environments. Our extensive real-world evaluations, conducted across a fleet of robots (including quadrupeds) in six cities on three continents, validate the policy's ability to generalize and navigate effectively even amidst pedestrians in crowded settings.

