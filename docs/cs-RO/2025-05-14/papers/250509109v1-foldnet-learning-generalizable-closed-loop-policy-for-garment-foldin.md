---
layout: default
title: "FoldNet: Learning Generalizable Closed-Loop Policy for Garment Folding via Keypoint-Driven Asset and Demonstration Synthesis"
---

# FoldNet: Learning Generalizable Closed-Loop Policy for Garment Folding via Keypoint-Driven Asset and Demonstration Synthesis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.09109" class="toolbar-btn" target="_blank">📄 arXiv: 2505.09109v1</a>
  <a href="https://arxiv.org/pdf/2505.09109.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.09109v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.09109v1', 'FoldNet: Learning Generalizable Closed-Loop Policy for Garment Folding via Keypoint-Driven Asset and Demonstration Synthesis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuxing Chen, Bowen Xiao, He Wang

**分类**: cs.RO, cs.CV

**发布日期**: 2025-05-14

---

## 💡 一句话要点

**提出FoldNet以解决服装折叠任务中的数据生成挑战**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `服装折叠` `合成数据` `闭环模仿学习` `关键点驱动` `机器人技术` `数据生成` `鲁棒性提升`

## 📋 核心要点

1. 现有方法在服装折叠任务中面临数据生成困难，尤其是高质量数据的获取。
2. 本文提出了一种基于关键点的合成数据生成方法，并通过闭环模仿学习训练折叠策略，增强了模型的鲁棒性。
3. 实验结果表明，经过KG-DAgger训练后，模型在现实世界中的成功率达75%，相比基线提升了25%。

## 📝 摘要（中文）

由于服装的可变形性，为机器人服装操作任务生成大量高质量数据极具挑战性。本文提出了一种合成服装数据集，用于机器人折叠任务。通过构建基于关键点的几何服装模板，并应用生成模型生成逼真的纹理图案，利用这些关键点注释生成折叠演示，并通过闭环模仿学习训练折叠策略。为提高鲁棒性，提出KG-DAgger，利用基于关键点的策略生成演示数据以恢复失败。KG-DAgger显著提升模型性能，实际成功率提高25%。经过15K轨迹（约200万图像-动作对）的训练，模型在现实世界中实现了75%的成功率。仿真和现实场景的实验验证了所提框架的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人在服装折叠任务中面临的数据生成不足问题。现有方法难以获取高质量的训练数据，导致模型在实际应用中的表现不佳。

**核心思路**：论文提出了一种基于关键点的合成数据生成方法，通过构建几何服装模板和生成纹理图案，生成高质量的折叠演示数据，并利用闭环模仿学习训练折叠策略，以提高模型的鲁棒性和适应性。

**技术框架**：整体框架包括数据生成模块、折叠演示生成模块和闭环模仿学习模块。首先，通过关键点构建服装模板，然后生成逼真的纹理，最后利用生成的数据进行策略训练。

**关键创新**：最重要的创新点在于提出了KG-DAgger策略，通过关键点驱动的方式生成演示数据，能够有效应对模型在实际操作中可能遇到的失败情况。这一方法显著提升了模型的成功率。

**关键设计**：在技术细节上，采用了特定的损失函数来优化生成模型，并设计了适合服装折叠任务的网络结构，以确保生成数据的多样性和真实性。

## 📊 实验亮点

实验结果显示，经过KG-DAgger训练后，模型在现实世界中的成功率达75%，相比基线提升了25%。这一显著的性能提升验证了所提方法在实际应用中的有效性，表明其在机器人服装折叠任务中的潜力。

## 🎯 应用场景

该研究具有广泛的应用潜力，尤其是在智能家居、自动化洗衣和服装处理等领域。通过提高机器人在服装折叠任务中的表现，能够显著提升家庭和工业自动化的效率，减少人力成本。未来，该框架还可扩展到其他类型的物品处理任务中，推动机器人技术的进一步发展。

## 📄 摘要（原文）

> Due to the deformability of garments, generating a large amount of high-quality data for robotic garment manipulation tasks is highly challenging. In this paper, we present a synthetic garment dataset that can be used for robotic garment folding. We begin by constructing geometric garment templates based on keypoints and applying generative models to generate realistic texture patterns. Leveraging these keypoint annotations, we generate folding demonstrations in simulation and train folding policies via closed-loop imitation learning. To improve robustness, we propose KG-DAgger, which uses a keypoint-based strategy to generate demonstration data for recovering from failures. KG-DAgger significantly improves the model performance, boosting the real-world success rate by 25\%. After training with 15K trajectories (about 2M image-action pairs), the model achieves a 75\% success rate in the real world. Experiments in both simulation and real-world settings validate the effectiveness of our proposed framework.

