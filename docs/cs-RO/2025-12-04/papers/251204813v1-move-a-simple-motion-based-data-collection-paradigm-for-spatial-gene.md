---
layout: default
title: "MOVE: A Simple Motion-Based Data Collection Paradigm for Spatial Generalization in Robotic Manipulation"
---

# MOVE: A Simple Motion-Based Data Collection Paradigm for Spatial Generalization in Robotic Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.04813" class="toolbar-btn" target="_blank">📄 arXiv: 2512.04813v1</a>
  <a href="https://arxiv.org/pdf/2512.04813.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.04813v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.04813v1', 'MOVE: A Simple Motion-Based Data Collection Paradigm for Spatial Generalization in Robotic Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Huanqian Wang, Chi Bene Chen, Yang Yue, Danhua Tao, Tong Guo, Shaoxuan Xie, Denghang Huang, Shiji Song, Guocai Yao, Gao Huang

**分类**: cs.RO

**发布日期**: 2025-12-04

**备注**: 9 pages, 9 figures

**🔗 代码/项目**: [GITHUB](https://github.com/lucywang720/MOVE)

---

## 💡 一句话要点

**提出MOVE以解决机器人操作中的数据稀缺问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `机器人操作` `模仿学习` `数据收集` `空间泛化` `动态演示` `数据效率` `运动增强`

## 📋 核心要点

1. 现有模仿学习方法在数据收集上存在局限，通常只从静态环境中获取轨迹，导致空间信息不足。
2. MOVE方法通过在演示中引入动态运动，增强了数据的空间多样性，从而提高了学习效率。
3. 实验结果显示，MOVE在空间泛化任务中成功率达到39.1%，相较于传统方法有显著提升。

## 📝 摘要（中文）

模仿学习方法在机器人操作中展现出巨大潜力，但其实际应用受到数据稀缺的限制。尽管已有研究致力于收集大规模数据集，但在空间泛化能力上仍存在显著差距。我们发现，现有方法通常只从单一静态空间配置中收集轨迹，限制了可用于学习的空间信息多样性。为了解决这一数据效率瓶颈，我们提出了MOtion-Based Variability Enhancement（MOVE），一种简单而有效的数据收集范式，通过在每次演示中为可移动物体注入运动，隐式生成丰富的空间配置。实验结果表明，MOVE在模拟任务中实现了39.1%的成功率，相较于静态数据收集方法提升了76.1%。

## 🔬 方法详解

**问题定义**：本论文旨在解决机器人操作中数据稀缺的问题。现有方法通常从单一静态空间配置中收集轨迹，导致空间信息的多样性不足，限制了模型的泛化能力。

**核心思路**：我们提出了MOVE方法，通过在每次演示中为可移动物体注入运动，生成丰富的空间配置。这种设计旨在提升数据的多样性和丰富性，从而提高模型的学习效果。

**技术框架**：MOVE的整体架构包括数据收集、动态演示和空间配置生成三个主要模块。在数据收集阶段，通过引入运动，生成多样化的轨迹；在动态演示阶段，利用可移动物体的运动增强空间信息；最后，通过生成的空间配置进行模型训练。

**关键创新**：MOVE的核心创新在于其动态数据收集策略，通过在演示中引入运动，显著提高了空间配置的多样性。这与传统的静态数据收集方法形成鲜明对比，后者无法提供足够的空间信息。

**关键设计**：在MOVE中，我们设置了多个可移动物体的运动参数，并设计了相应的损失函数，以确保生成的轨迹在空间上的多样性。此外，网络结构采用了适应性学习策略，以提高模型对动态环境的适应能力。

## 📊 实验亮点

MOVE在模拟任务中表现出色，成功率达到39.1%，相比于静态数据收集方法的22.2%提升了76.1%。在某些任务中，数据效率提升达到2至5倍，显示出其在空间泛化能力上的显著优势。

## 🎯 应用场景

该研究的潜在应用领域包括机器人抓取、自动化生产线和智能家居等场景。通过提升机器人在复杂环境中的操作能力，MOVE能够显著提高机器人在实际应用中的灵活性和效率，推动智能机器人技术的发展。

## 📄 摘要（原文）

> Imitation learning method has shown immense promise for robotic manipulation, yet its practical deployment is fundamentally constrained by the data scarcity. Despite prior work on collecting large-scale datasets, there still remains a significant gap to robust spatial generalization. We identify a key limitation: individual trajectories, regardless of their length, are typically collected from a \emph{single, static spatial configuration} of the environment. This includes fixed object and target spatial positions as well as unchanging camera viewpoints, which significantly restricts the diversity of spatial information available for learning. To address this critical bottleneck in data efficiency, we propose \textbf{MOtion-Based Variability Enhancement} (\emph{MOVE}), a simple yet effective data collection paradigm that enables the acquisition of richer spatial information from dynamic demonstrations. Our core contribution is an augmentation strategy that injects motion into any movable objects within the environment for each demonstration. This process implicitly generates a dense and diverse set of spatial configurations within a single trajectory. We conduct extensive experiments in both simulation and real-world environments to validate our approach. For example, in simulation tasks requiring strong spatial generalization, \emph{MOVE} achieves an average success rate of 39.1\%, a 76.1\% relative improvement over the static data collection paradigm (22.2\%), and yields up to 2--5$\times$ gains in data efficiency on certain tasks. Our code is available at https://github.com/lucywang720/MOVE.

