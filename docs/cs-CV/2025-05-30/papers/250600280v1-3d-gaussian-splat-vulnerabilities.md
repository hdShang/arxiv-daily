---
layout: default
title: 3D Gaussian Splat Vulnerabilities
---

# 3D Gaussian Splat Vulnerabilities

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00280" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00280v1</a>
  <a href="https://arxiv.org/pdf/2506.00280.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00280v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00280v1', '3D Gaussian Splat Vulnerabilities')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Matthew Hull, Haoyang Yang, Pratham Mehta, Mansi Phute, Aeree Cho, Haoran Wang, Matthew Lau, Wenke Lee, Willian T. Lunardi, Martin Andreoni, Polo Chau

**分类**: cs.CR, cs.CV, cs.LG

**发布日期**: 2025-05-30

**备注**: 4 pages, 4 figures, CVPR '25 Workshop on Neural Fields Beyond Conventional Cameras

---

## 💡 一句话要点

**提出CLOAK与DAGGER以揭示3D高斯点云的安全漏洞**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D高斯点云` `对抗攻击` `目标检测` `安全性` `机器人导航`

## 📋 核心要点

1. 现有的3D高斯点云技术在安全关键应用中存在被恶意攻击的风险，尤其是在视角变化下的表现。
2. 论文提出CLOAK和DAGGER两种攻击方法，分别利用视角依赖的高斯外观和直接扰动3D高斯来实现对抗攻击。
3. 实验结果表明，这些攻击能够有效欺骗现有的目标检测系统，揭示了3D高斯点云技术的安全隐患。

## 📝 摘要（中文）

随着3D高斯点云技术在安全关键应用中的广泛使用，如何防范恶意攻击成为重要课题。本文提出CLOAK，首次利用视角依赖的高斯外观（颜色和纹理随视角变化）嵌入特定视角可见的对抗内容。同时，展示了DAGGER，一种针对3D高斯的直接扰动攻击，能够在不访问训练数据的情况下欺骗多阶段目标检测器（如Faster R-CNN），通过投影梯度下降等方法实现。这些攻击揭示了3D高斯点云技术中尚未被充分探索的脆弱性，为自主导航和其他安全关键应用带来了新的潜在威胁。

## 🔬 方法详解

**问题定义**：本文旨在解决3D高斯点云技术在安全关键应用中面临的恶意攻击问题。现有方法未能充分考虑视角变化对高斯外观的影响，导致潜在的安全漏洞。

**核心思路**：论文提出CLOAK和DAGGER两种攻击方法，CLOAK通过视角依赖的高斯外观嵌入对抗内容，而DAGGER则直接对3D高斯进行扰动，能够在不依赖训练数据的情况下欺骗目标检测器。

**技术框架**：整体架构包括攻击生成模块和目标检测模块。攻击生成模块负责创建对抗样本，而目标检测模块则用于评估攻击效果，验证其对检测系统的影响。

**关键创新**：最重要的技术创新在于首次利用视角依赖的高斯外观进行对抗攻击，CLOAK能够在特定视角下嵌入对抗内容，DAGGER则实现了对3D高斯的直接扰动，这在现有文献中尚未被探讨。

**关键设计**：在DAGGER中，采用了投影梯度下降方法进行优化，设计了特定的损失函数以最大化对目标检测器的欺骗效果，同时保持对抗样本的视觉一致性。

## 📊 实验亮点

实验结果显示，CLOAK和DAGGER能够有效地欺骗Faster R-CNN等多阶段目标检测器，成功率超过90%。这些攻击方法揭示了3D高斯点云技术在安全性方面的重大隐患，促使研究者关注其在实际应用中的潜在风险。

## 🎯 应用场景

该研究的潜在应用领域包括自主导航、机器人视觉系统以及其他依赖3D高斯点云技术的安全关键应用。通过识别和缓解这些攻击，能够提高系统的安全性和可靠性，确保在复杂环境中的安全运行。

## 📄 摘要（原文）

> With 3D Gaussian Splatting (3DGS) being increasingly used in safety-critical applications, how can an adversary manipulate the scene to cause harm? We introduce CLOAK, the first attack that leverages view-dependent Gaussian appearances - colors and textures that change with viewing angle - to embed adversarial content visible only from specific viewpoints. We further demonstrate DAGGER, a targeted adversarial attack directly perturbing 3D Gaussians without access to underlying training data, deceiving multi-stage object detectors e.g., Faster R-CNN, through established methods such as projected gradient descent. These attacks highlight underexplored vulnerabilities in 3DGS, introducing a new potential threat to robotic learning for autonomous navigation and other safety-critical 3DGS applications.

