---
layout: default
title: "DiffusionRL: Efficient Training of Diffusion Policies for Robotic Grasping Using RL-Adapted Large-Scale Datasets"
---

# DiffusionRL: Efficient Training of Diffusion Policies for Robotic Grasping Using RL-Adapted Large-Scale Datasets

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.18876" class="toolbar-btn" target="_blank">📄 arXiv: 2505.18876v1</a>
  <a href="https://arxiv.org/pdf/2505.18876.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.18876v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.18876v1', 'DiffusionRL: Efficient Training of Diffusion Policies for Robotic Grasping Using RL-Adapted Large-Scale Datasets')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Maria Makarova, Qian Liu, Dzmitry Tsetserukou

**分类**: cs.RO

**发布日期**: 2025-05-24

**备注**: Submitted to CoRL 2025

---

## 💡 一句话要点

**提出DiffusionRL以解决机器人抓取中的数据限制问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `扩散模型` `强化学习` `机器人抓取` `数据增强` `灵巧操作` `模型泛化` `自动化技术`

## 📋 核心要点

1. 现有方法在机器人抓取任务中面临数据限制和场景特定适应的挑战，影响了模型的泛化能力。
2. 本文提出了一种基于强化学习的扩散策略训练方法，利用大型数据集进行优化，提升了训练效率。
3. 实验结果表明，该方法在三个DexGraspNet对象上实现了80%的成功率，显著提高了抓取任务的表现。

## 📝 摘要（中文）

扩散模型已成功应用于图像、视频和音频生成等领域。近期研究表明其在序列决策和灵巧操作中的潜力，尤其是在建模复杂动作分布方面。然而，由于数据限制和场景特定适应需求，仍面临挑战。本文提出了一种优化的扩散策略训练方法，利用大型预构建数据集，并通过强化学习（RL）进行增强。我们的端到端流程结合了基于RL的DexGraspNet数据集增强、轻量级扩散策略训练以及姿态采样算法验证。该流程在三个DexGraspNet对象上实现了80%的高成功率。通过消除手动数据收集，我们的方法降低了扩散模型在机器人领域的应用门槛，增强了实际应用的泛化能力和鲁棒性。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人抓取任务中由于数据限制和场景特定适应需求导致的性能瓶颈。现有方法通常依赖于手动数据收集，导致训练效率低下和泛化能力不足。

**核心思路**：论文提出通过强化学习增强大型预构建数据集，结合轻量级扩散策略训练，以提高机器人在灵巧操作中的表现。这样的设计旨在降低数据收集的复杂性，同时提升模型的适应性和鲁棒性。

**技术框架**：整体架构包括三个主要模块：首先是基于强化学习的DexGraspNet数据集增强，其次是轻量级的扩散策略训练，最后是用于验证的姿态采样算法。这一流程确保了从数据准备到模型训练的高效性。

**关键创新**：最重要的创新在于将强化学习与扩散模型结合，利用已有数据集进行优化，而非依赖于传统的手动数据收集。这一方法显著提高了训练效率和模型的泛化能力。

**关键设计**：在技术细节上，采用了特定的损失函数以优化抓取成功率，并设计了适合五指机器人手的轻量级网络结构，以确保在灵巧操作中的高效性和准确性。

## 📊 实验亮点

实验结果显示，本文提出的DiffusionRL方法在三个DexGraspNet对象上实现了80%的成功率，相较于传统方法有显著提升。这一成果表明，基于强化学习的扩散策略训练能够有效提高机器人抓取任务的性能。

## 🎯 应用场景

该研究的潜在应用领域包括智能机器人、自动化生产线和人机协作等场景。通过提高机器人抓取任务的成功率和适应性，该方法有助于推动机器人技术在实际应用中的广泛采用，提升生产效率和灵活性。

## 📄 摘要（原文）

> Diffusion models have been successfully applied in areas such as image, video, and audio generation. Recent works show their promise for sequential decision-making and dexterous manipulation, leveraging their ability to model complex action distributions. However, challenges persist due to the data limitations and scenario-specific adaptation needs. In this paper, we address these challenges by proposing an optimized approach to training diffusion policies using large, pre-built datasets that are enhanced using Reinforcement Learning (RL). Our end-to-end pipeline leverages RL-based enhancement of the DexGraspNet dataset, lightweight diffusion policy training on a dexterous manipulation task for a five-fingered robotic hand, and a pose sampling algorithm for validation. The pipeline achieved a high success rate of 80% for three DexGraspNet objects. By eliminating manual data collection, our approach lowers barriers to adopting diffusion models in robotics, enhancing generalization and robustness for real-world applications.

