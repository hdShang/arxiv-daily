---
layout: default
title: KineST: A Kinematics-guided Spatiotemporal State Space Model for Human Motion Tracking from Sparse Signals
---

# KineST: A Kinematics-guided Spatiotemporal State Space Model for Human Motion Tracking from Sparse Signals

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16791" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16791v1</a>
  <a href="https://arxiv.org/pdf/2512.16791.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16791v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16791v1', 'KineST: A Kinematics-guided Spatiotemporal State Space Model for Human Motion Tracking from Sparse Signals')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shuting Zhao, Zeyu Xiao, Xinrong Chen

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-18

**备注**: Accepted by AAAI 2026

**🔗 代码/项目**: [PROJECT_PAGE](https://kaka-1314.github.io/KineST/)

---

## 💡 一句话要点

**KineST：一种基于运动学引导的时空状态空间模型，用于从稀疏信号中进行人体运动跟踪**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `人体运动跟踪` `状态空间模型` `运动学引导` `时空建模` `AR/VR` `稀疏信号` `姿态重建`

## 📋 核心要点

1. 现有方法难以兼顾AR/VR中基于稀疏信号的全身姿态重建的准确性、时间连贯性和计算效率。
2. KineST通过运动学引导的双向扫描和混合时空表示学习，有效提取时空依赖性并整合局部和全局姿态感知。
3. 实验表明，KineST在轻量级框架内，在准确性和时间一致性方面都优于现有方法，提升了运动跟踪的性能。

## 📝 摘要（中文）

全身运动跟踪在AR/VR应用中至关重要，它连接了物理交互和虚拟交互。然而，基于头戴式显示器获取的稀疏信号重建逼真且多样化的全身姿态具有挑战性，而头戴式显示器是AR/VR场景中的主要设备。现有的姿态重建方法通常计算成本高昂，或者依赖于分别建模空间和时间依赖性，难以平衡准确性、时间连贯性和效率。为了解决这个问题，我们提出KineST，一种新颖的运动学引导的状态空间模型，它有效地提取时空依赖性，同时整合局部和全局姿态感知。创新来自两个核心思想。首先，为了更好地捕捉复杂的关节关系，状态空间对偶框架内的扫描策略被重新制定为运动学引导的双向扫描，从而嵌入运动学先验。其次，采用混合时空表示学习方法来紧密耦合空间和时间上下文，从而平衡准确性和平滑性。此外，引入了几何角速度损失，对旋转变化施加物理上有意义的约束，以进一步提高运动稳定性。大量实验表明，KineST在轻量级框架内，在准确性和时间一致性方面都具有优越的性能。

## 🔬 方法详解

**问题定义**：论文旨在解决基于AR/VR场景中头戴式显示器等设备提供的稀疏信号，进行准确、连贯且高效的全身运动跟踪问题。现有方法通常面临计算成本高、难以同时建模空间和时间依赖性，以及难以平衡准确性、时间连贯性和效率的挑战。

**核心思路**：论文的核心思路是利用运动学先验知识引导时空状态空间模型的构建，从而更有效地提取时空依赖关系。通过运动学引导的双向扫描，更好地捕捉关节之间的复杂关系；通过混合时空表示学习，紧密耦合空间和时间上下文，从而在准确性和平滑性之间取得平衡。

**技术框架**：KineST的核心是一个状态空间模型，其整体流程包括：1) 输入稀疏的运动信号；2) 利用运动学引导的双向扫描策略，在状态空间对偶框架内提取空间特征；3) 采用混合时空表示学习方法，融合空间和时间上下文信息；4) 通过几何角速度损失进行优化，保证运动的物理合理性；5) 输出重建的全身运动姿态。

**关键创新**：论文的关键创新在于：1) 提出了运动学引导的双向扫描策略，将运动学先验知识融入状态空间模型的构建中，从而更好地捕捉关节之间的复杂关系；2) 采用了混合时空表示学习方法，紧密耦合空间和时间上下文，从而在准确性和平滑性之间取得平衡；3) 引入了几何角速度损失，对旋转变化施加物理上有意义的约束，进一步提高了运动的稳定性。

**关键设计**：运动学引导的双向扫描策略具体实现方式未知，需要参考论文细节。混合时空表示学习的具体网络结构未知，需要参考论文细节。几何角速度损失的具体形式未知，需要参考论文细节。这些细节的设计是保证模型性能的关键。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16791v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16791v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16791v1/scan2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文通过实验验证了KineST在准确性和时间一致性方面的优越性能。具体性能数据和对比基线需要在论文中查找。论文强调KineST在轻量级框架下实现了高性能，这意味着它在计算资源受限的场景中具有更大的应用潜力。具体的提升幅度需要在论文中查找。

## 🎯 应用场景

该研究成果可广泛应用于AR/VR、游戏、动画制作、康复训练等领域。通过更准确、连贯和高效的全身运动跟踪，可以提升AR/VR应用的沉浸感和交互体验，为游戏和动画制作提供更逼真的角色动作，并为康复训练提供更精确的运动分析和指导。未来，该技术有望进一步应用于人机交互、远程协作等领域。

## 📄 摘要（原文）

> Full-body motion tracking plays an essential role in AR/VR applications, bridging physical and virtual interactions. However, it is challenging to reconstruct realistic and diverse full-body poses based on sparse signals obtained by head-mounted displays, which are the main devices in AR/VR scenarios. Existing methods for pose reconstruction often incur high computational costs or rely on separately modeling spatial and temporal dependencies, making it difficult to balance accuracy, temporal coherence, and efficiency. To address this problem, we propose KineST, a novel kinematics-guided state space model, which effectively extracts spatiotemporal dependencies while integrating local and global pose perception. The innovation comes from two core ideas. Firstly, in order to better capture intricate joint relationships, the scanning strategy within the State Space Duality framework is reformulated into kinematics-guided bidirectional scanning, which embeds kinematic priors. Secondly, a mixed spatiotemporal representation learning approach is employed to tightly couple spatial and temporal contexts, balancing accuracy and smoothness. Additionally, a geometric angular velocity loss is introduced to impose physically meaningful constraints on rotational variations for further improving motion stability. Extensive experiments demonstrate that KineST has superior performance in both accuracy and temporal consistency within a lightweight framework. Project page: https://kaka-1314.github.io/KineST/

