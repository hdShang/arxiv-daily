---
layout: default
title: "DepthVanish: Optimizing Adversarial Interval Structures for Stereo-Depth-Invisible Patches"
---

# DepthVanish: Optimizing Adversarial Interval Structures for Stereo-Depth-Invisible Patches

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16690" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16690v2</a>
  <a href="https://arxiv.org/pdf/2506.16690.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16690v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16690v2', 'DepthVanish: Optimizing Adversarial Interval Structures for Stereo-Depth-Invisible Patches')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yun Xing, Yue Cao, Nhat Chung, Jie Zhang, Ivor Tsang, Ming-Ming Cheng, Yang Liu, Lei Ma, Qing Guo

**分类**: cs.CV

**发布日期**: 2025-06-20 (更新: 2025-11-03)

**🔗 代码/项目**: [GITHUB](https://github.com/WiWiN42/DepthVanish)

---

## 💡 一句话要点

**提出DepthVanish以优化立体深度估计中的对抗性补丁**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `立体深度估计` `对抗性攻击` `优化算法` `安全评估` `机器人技术` `自动驾驶` `深度学习`

## 📋 核心要点

1. 现有方法在物理实现中表现不佳，重复的优化纹理无法有效攻击立体深度估计系统。
2. 本研究提出通过引入规则间隔的网格结构来优化对抗性补丁，从而提升攻击效果。
3. 实验结果表明，生成的补丁在多种深度估计方法中表现优异，且能在真实环境中有效攻击商业相机。

## 📝 摘要（中文）

立体深度估计是自动驾驶和机器人技术中的关键任务，错误的深度识别可能导致危险情况。对立体深度估计的对抗性攻击可以揭示其在部署前的脆弱性。以往研究表明，重复优化的纹理在数字环境中能够有效误导深度估计，但在实际应用中效果不佳。本研究首次发现，通过在重复纹理之间引入规则间隔，形成网格结构，显著提升了补丁的攻击性能。我们开发了一种新型的立体深度攻击，联合优化间隔结构和纹理元素，生成的对抗补丁能够在各种场景中成功攻击不同范式的深度估计方法，包括商业RGB-D相机，展示了其在安全评估中的实际应用价值。

## 🔬 方法详解

**问题定义**：本论文旨在解决立体深度估计中的对抗性补丁在实际应用中的效果不足问题。现有方法依赖于简单重复的纹理，导致在物理环境中攻击效果不理想。

**核心思路**：论文提出通过在重复纹理之间引入规则间隔，形成网格结构，以增强补丁的攻击性能。这种设计旨在提高补丁在真实世界中的有效性。

**技术框架**：整体方法包括两个主要阶段：首先，优化纹理元素；其次，优化纹理之间的间隔结构。通过联合优化，提升了补丁的整体攻击效果。

**关键创新**：最重要的创新点在于首次引入了规则间隔的网格结构，这与以往单一重复纹理的设计有本质区别，显著提高了对抗性补丁的有效性。

**关键设计**：在参数设置上，采用了特定的损失函数来平衡纹理优化和间隔优化，确保生成的补丁在多种场景中均能有效攻击深度估计系统。

## 📊 实验亮点

实验结果显示，生成的对抗补丁在多种立体深度估计方法中均表现出色，能够成功攻击RAST-Stereo和STTR等先进模型。此外，补丁在真实环境中对Intel RealSense相机的攻击成功率显著提高，展示了提升幅度和实际应用的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、机器人导航以及安全监控等。通过优化对抗性补丁，能够有效评估和提升立体深度估计系统的安全性，减少潜在的安全隐患，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Stereo depth estimation is a critical task in autonomous driving and robotics, where inaccuracies (such as misidentifying nearby objects as distant) can lead to dangerous situations. Adversarial attacks against stereo depth estimation can help reveal vulnerabilities before deployment. Previous works have shown that repeating optimized textures can effectively mislead stereo depth estimation in digital settings. However, our research reveals that these naively repeated textures perform poorly in physical implementations, i.e., when deployed as patches, limiting their practical utility for stress-testing stereo depth estimation systems. In this work, for the first time, we discover that introducing regular intervals among the repeated textures, creating a grid structure, significantly enhances the patch's attack performance. Through extensive experimentation, we analyze how variations of this novel structure influence the adversarial effectiveness. Based on these insights, we develop a novel stereo depth attack that jointly optimizes both the interval structure and texture elements. Our generated adversarial patches can be inserted into any scenes and successfully attack advanced stereo depth estimation methods of different paradigms, i.e., RAFT-Stereo and STTR. Most critically, our patch can also attack commercial RGB-D cameras (Intel RealSense) in real-world conditions, demonstrating their practical relevance for security assessment of stereo systems. The code is officially released at: https://github.com/WiWiN42/DepthVanish

