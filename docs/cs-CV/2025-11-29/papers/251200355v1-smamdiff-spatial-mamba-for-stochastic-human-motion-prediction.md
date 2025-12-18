---
layout: default
title: SMamDiff: Spatial Mamba for Stochastic Human Motion Prediction
---

# SMamDiff: Spatial Mamba for Stochastic Human Motion Prediction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.00355" class="toolbar-btn" target="_blank">📄 arXiv: 2512.00355v1</a>
  <a href="https://arxiv.org/pdf/2512.00355.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.00355v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.00355v1', 'SMamDiff: Spatial Mamba for Stochastic Human Motion Prediction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junqiao Fan, Pengfei Liu, Haocong Rao

**分类**: cs.CV

**发布日期**: 2025-11-29

---

## 💡 一句话要点

**提出SMamDiff，一种基于空间Mamba的单阶段扩散模型，用于随机人体运动预测。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `人体运动预测` `扩散模型` `空间Mamba` `时空连贯性` `残差DCT` `单阶段模型` `边缘计算`

## 📋 核心要点

1. 现有HMP方法难以兼顾预测结果的准确性、多样性和运动学合理性，且多阶段扩散模型计算成本高昂，不利于边缘部署。
2. SMamDiff通过残差DCT编码提取高频运动信息，并利用空间Mamba模块建模关节间的长程依赖关系，从而提升时空连贯性。
3. 实验表明，SMamDiff在单阶段概率HMP方法中取得了SOTA结果，并在延迟和内存占用方面优于多阶段扩散模型。

## 📝 摘要（中文）

随着智能室内传感和服务机器人的广泛部署，人体运动预测（HMP）对于安全、主动的辅助至关重要。然而，许多现有的HMP方法要么产生单一的、确定性的预测，忽略了不确定性，要么依赖于牺牲运动学合理性的概率模型。扩散模型改善了准确性-多样性的权衡，但通常依赖于多阶段流程，这对于边缘部署来说成本高昂。这项工作侧重于如何在用于HMP的单阶段扩散模型中确保时空连贯性。我们引入了SMamDiff，一种基于空间Mamba的扩散模型，具有两个新颖的设计：（i）一种残差-DCT运动编码，在时间DCT之前减去最后观察到的姿势，减少了第一个DC分量（f=0）的主导地位，并突出了信息量更大的高频线索，因此模型学习关节如何移动而不是它们在哪里；（ii）一个火柴人绘制空间Mamba模块，以有序的、逐关节的方式处理关节，使后面的关节以前面的关节为条件，以诱导长程、跨关节的依赖关系。在Human3.6M和HumanEva上，这些连贯性机制在单阶段概率HMP方法中提供了最先进的结果，同时比多阶段扩散基线使用更少的延迟和内存。

## 🔬 方法详解

**问题定义**：人体运动预测（HMP）旨在根据过去一段时间的人体运动轨迹，预测未来一段时间的运动轨迹。现有方法的痛点在于，确定性模型忽略了运动的不确定性，概率模型又难以保证运动的合理性，而多阶段扩散模型计算开销大，难以部署在边缘设备上。

**核心思路**：论文的核心思路是在单阶段扩散模型中，通过精巧的设计来保证时空连贯性。具体来说，通过残差DCT编码，使模型关注关节的运动模式而非绝对位置；通过空间Mamba模块，建模关节间的长程依赖关系，保证运动的协调性。

**技术框架**：SMamDiff的整体框架是一个单阶段扩散模型。首先，使用残差DCT编码对输入的人体运动数据进行处理，提取运动特征。然后，将这些特征输入到基于空间Mamba的扩散模型中，该模型逐步去噪，最终生成预测的运动轨迹。

**关键创新**：论文的关键创新在于两个方面：一是残差DCT运动编码，它能够有效提取高频运动信息，减少低频分量的干扰；二是空间Mamba模块，它能够以有序的方式处理关节，并建模关节间的长程依赖关系。

**关键设计**：残差DCT编码的关键在于先减去最后一个观测到的姿势，再进行DCT变换，这样可以突出运动的变化信息。空间Mamba模块的关键在于按照火柴人骨架的顺序处理关节，使得后面的关节可以依赖于前面的关节的信息。损失函数采用标准的扩散模型损失函数，例如L2损失或Huber损失。

## 📊 实验亮点

SMamDiff在Human3.6M和HumanEva数据集上取得了SOTA结果，尤其是在单阶段概率HMP方法中。与多阶段扩散模型相比，SMamDiff在保证性能的同时，显著降低了延迟和内存占用，更适合边缘部署。具体性能数据（例如，预测误差的降低百分比）在论文中给出。

## 🎯 应用场景

该研究成果可应用于智能家居、服务机器人、自动驾驶等领域。例如，在智能家居中，机器人可以预测用户的运动轨迹，从而提前准备好所需物品或调整环境设置。在自动驾驶中，系统可以预测行人的运动轨迹，从而做出更安全的决策。该研究有助于提升人机交互的安全性、效率和舒适性。

## 📄 摘要（原文）

> With intelligent room-side sensing and service robots widely deployed, human motion prediction (HMP) is essential for safe, proactive assistance. However, many existing HMP methods either produce a single, deterministic forecast that ignores uncertainty or rely on probabilistic models that sacrifice kinematic plausibility. Diffusion models improve the accuracy-diversity trade-off but often depend on multi-stage pipelines that are costly for edge deployment. This work focuses on how to ensure spatial-temporal coherence within a single-stage diffusion model for HMP. We introduce SMamDiff, a Spatial Mamba-based Diffusion model with two novel designs: (i) a residual-DCT motion encoding that subtracts the last observed pose before a temporal DCT, reducing the first DC component ($f=0$) dominance and highlighting informative higher-frequency cues so the model learns how joints move rather than where they are; and (ii) a stickman-drawing spatial-mamba module that processes joints in an ordered, joint-by-joint manner, making later joints condition on earlier ones to induce long-range, cross-joint dependencies. On Human3.6M and HumanEva, these coherence mechanisms deliver state-of-the-art results among single-stage probabilistic HMP methods while using less latency and memory than multi-stage diffusion baselines.

