---
layout: default
title: Efficient Probabilistic Planning with Maximum-Coverage Distributionally Robust Backward Reachable Trees
---

# Efficient Probabilistic Planning with Maximum-Coverage Distributionally Robust Backward Reachable Trees

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.04807" target="_blank" class="toolbar-btn">arXiv: 2510.04807v1</a>
    <a href="https://arxiv.org/pdf/2510.04807.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.04807v1" 
            onclick="toggleFavorite(this, '2510.04807v1', 'Efficient Probabilistic Planning with Maximum-Coverage Distributionally Robust Backward Reachable Trees')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Alex Rose, Naman Aggarwal, Christopher Jewison, Jonathan P. How

**分类**: eess.SY, cs.RO

**发布日期**: 2025-10-06

---

## 💡 一句话要点

**提出一种高效的多查询运动规划算法以解决高概率到达问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `运动规划` `高斯分布` `模糊集` `分布鲁棒` `信念路线图` `控制器合成` `仿真实验`

## 📋 核心要点

1. 现有的运动规划方法在处理高斯分布时，往往无法保证在模糊集中的安全性和覆盖率。
2. 本文提出了一种新的分布鲁棒信念路线图生成算法，能够合成安全控制器并处理最大尺寸的模糊集。
3. 实验结果表明，所提算法在覆盖率上优于现有的最大覆盖算法，并在特定情况下实现了最大覆盖。

## 📝 摘要（中文）

本文提出了一种新的多查询运动规划算法，适用于线性高斯系统，旨在以高概率到达一个欧几里得球体。我们开发了一种新的高斯分布的球形模糊集的表述，并利用该表述构建了一个分布鲁棒的信念路线图生成算法。该算法合成了经过认证的安全控制器，能够处理最大尺寸的球形模糊集。此外，我们还提出了第二种多查询运动规划算法，目标是以高概率到达由椭球体和欧几里得球体的闵可夫斯基和参数化的区域。通过广泛的仿真实验，我们验证了这两种方法在多种条件下的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决线性高斯系统中多查询运动规划的问题，现有方法在处理模糊集时存在覆盖率不足和安全性不确定的问题。

**核心思路**：我们提出了一种新的高斯分布模糊集的表述，利用该表述构建分布鲁棒的信念路线图生成算法，以确保在最大模糊集下的安全性和覆盖率。

**技术框架**：整体框架包括模糊集的构建、信念路线图的生成和控制器的合成三个主要模块。首先构建球形模糊集，然后生成信念路线图，最后合成安全控制器。

**关键创新**：最重要的创新在于提出了球形模糊集的新的表述方式，并在此基础上构建了分布鲁棒的信念路线图生成算法，显著提高了覆盖率。

**关键设计**：算法中关键的参数设置包括模糊集的大小和高斯分布的参数，损失函数设计为确保覆盖率最大化，同时考虑安全性约束。

## 📊 实验亮点

实验结果表明，所提算法在覆盖率上优于现有的最大覆盖算法，特别是在没有过程噪声或状态约束的情况下，能够实现最大覆盖。此外，在处理椭球体模糊集时，算法的覆盖率与最佳已知算法相当或更优。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、机器人路径规划和无人机导航等。通过提高运动规划的安全性和覆盖率，可以在复杂环境中实现更高效的自主决策，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> This paper presents a new multi-query motion planning algorithm for linear Gaussian systems with the goal of reaching a Euclidean ball with high probability. We develop a new formulation for ball-shaped ambiguity sets of Gaussian distributions and leverage it to develop a distributionally robust belief roadmap construction algorithm. This algorithm synthe- sizes robust controllers which are certified to be safe for maximal size ball-shaped ambiguity sets of Gaussian distributions. Our algorithm achieves better coverage than the maximal coverage algorithm for planning over Gaussian distributions [1], and we identify mild conditions under which our algorithm achieves strictly better coverage. For the special case of no process noise or state constraints, we formally prove that our algorithm achieves maximal coverage. In addition, we present a second multi-query motion planning algorithm for linear Gaussian systems with the goal of reaching a region parameterized by the Minkowski sum of an ellipsoid and a Euclidean ball with high probability. This algorithm plans over ellipsoidal sets of maximal size ball-shaped ambiguity sets of Gaussian distributions, and provably achieves equal or better coverage than the best-known algorithm for planning over ellipsoidal ambiguity sets of Gaussian distributions [2]. We demonstrate the efficacy of both methods in a wide range of conditions via extensive simulation experiments.

