---
layout: default
title: "OmniD: Generalizable Robot Manipulation Policy via Image-Based BEV Representation"
---

# OmniD: Generalizable Robot Manipulation Policy via Image-Based BEV Representation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.11898" class="toolbar-btn" target="_blank">📄 arXiv: 2508.11898v1</a>
  <a href="https://arxiv.org/pdf/2508.11898.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.11898v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.11898v1', 'OmniD: Generalizable Robot Manipulation Policy via Image-Based BEV Representation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jilei Mao, Jiarui Guan, Yingjuan Tang, Qirui Hu, Zhihang Li, Junjie Yu, Yongjie Mao, Yunzhe Sun, Shuang Liu, Xiaozhu Ju

**分类**: cs.RO

**发布日期**: 2025-08-16

**🔗 代码/项目**: [GITHUB](https://github.com/1mather/omnid.git)

---

## 💡 一句话要点

**提出Omni-Vision Diffusion Policy以解决机器人操作中的过拟合问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `机器人操作` `视觉运动策略` `多视角融合` `鸟瞰图表示` `可变形注意力` `特征提取` `泛化能力` `自动化`

## 📋 核心要点

1. 现有的视觉运动策略容易对训练数据集过拟合，导致在异分布场景中的表现不佳。
2. 本文提出的OmniD框架通过多视角融合生成统一的鸟瞰图表示，克服了现有方法的局限性。
3. 实验结果表明，OmniD在不同场景下的表现显著优于最佳基线模型，提升幅度可达84%。

## 📝 摘要（中文）

视觉运动策略容易对训练数据集过拟合，例如固定的摄像机位置和背景。这种过拟合使得策略在同分布场景中表现良好，但在异分布泛化中表现不佳。此外，现有方法在融合多视角信息以生成有效的3D表示时也面临困难。为了解决这些问题，本文提出了Omni-Vision Diffusion Policy（OmniD），一个将图像观测合成统一鸟瞰图（BEV）表示的多视角融合框架。我们引入了一种基于可变形注意力的Omni特征生成器（OFG），以选择性地抽象与任务相关的特征，同时抑制视角特定的噪声和背景干扰。OmniD在同分布、异分布和少样本实验中分别比最佳基线模型提高了11%、17%和84%的平均性能。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人操作中视觉运动策略的过拟合问题，现有方法在固定摄像机位置和背景下训练，导致在新环境中的泛化能力不足。

**核心思路**：提出Omni-Vision Diffusion Policy（OmniD），通过多视角图像融合生成统一的鸟瞰图（BEV）表示，以增强策略的泛化能力。设计中引入可变形注意力机制，以选择性地提取任务相关特征，减少视角特定噪声的影响。

**技术框架**：OmniD的整体架构包括图像输入模块、Omni特征生成器（OFG）和策略网络。OFG负责从多视角图像中提取和融合特征，而策略网络则基于生成的BEV表示进行决策。

**关键创新**：最重要的创新在于引入了可变形注意力机制的Omni特征生成器，能够有效地抑制背景干扰和视角噪声，与传统方法相比，显著提升了特征提取的准确性。

**关键设计**：在设计中，OFG的网络结构采用了多层卷积和注意力机制，损失函数则结合了重建损失和策略损失，以确保生成的BEV表示既准确又具备良好的泛化能力。训练过程中还采用了数据增强技术，以进一步提高模型的鲁棒性。

## 📊 实验亮点

实验结果显示，OmniD在同分布、异分布和少样本实验中分别比最佳基线模型提高了11%、17%和84%的平均性能，展现出显著的泛化能力和优越的操作效果。

## 🎯 应用场景

该研究的潜在应用领域包括自动化机器人操作、智能制造、无人驾驶等。通过提高机器人在不同环境中的操作能力，OmniD能够显著提升机器人在复杂任务中的适应性和效率，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> The visuomotor policy can easily overfit to its training datasets, such as fixed camera positions and backgrounds. This overfitting makes the policy perform well in the in-distribution scenarios but underperform in the out-of-distribution generalization. Additionally, the existing methods also have difficulty fusing multi-view information to generate an effective 3D representation. To tackle these issues, we propose Omni-Vision Diffusion Policy (OmniD), a multi-view fusion framework that synthesizes image observations into a unified bird's-eye view (BEV) representation. We introduce a deformable attention-based Omni-Feature Generator (OFG) to selectively abstract task-relevant features while suppressing view-specific noise and background distractions. OmniD achieves 11\%, 17\%, and 84\% average improvement over the best baseline model for in-distribution, out-of-distribution, and few-shot experiments, respectively. Training code and simulation benchmark are available: https://github.com/1mather/omnid.git

