---
layout: default
title: "KineST: A Kinematics-guided Spatiotemporal State Space Model for Human Motion Tracking from Sparse Signals"
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

**关键词**: `人体运动跟踪` `状态空间模型` `运动学引导` `时空表示学习` `AR/VR` `稀疏信号` `全身姿势重建`

## 📋 核心要点

1. 现有基于稀疏信号的全身运动跟踪方法计算成本高，或难以同时建模空间和时间依赖性，导致精度、连贯性和效率难以兼顾。
2. KineST通过运动学引导的双向扫描嵌入运动学先验，并采用混合时空表示学习方法紧密耦合空间和时间上下文，从而平衡精度和平滑性。
3. 实验结果表明，KineST在轻量级框架下，在准确性和时间一致性方面均表现出优越的性能，优于现有方法。

## 📝 摘要（中文）

全身运动跟踪在AR/VR应用中至关重要，它连接了物理交互和虚拟交互。然而，基于头戴式显示器获取的稀疏信号重建逼真且多样化的全身姿势仍然具有挑战性。现有的姿势重建方法通常计算成本高昂，或者依赖于分别建模空间和时间依赖性，难以平衡准确性、时间连贯性和效率。为了解决这个问题，我们提出了一种新颖的运动学引导的状态空间模型KineST，它有效地提取时空依赖性，同时整合局部和全局姿势感知。其创新来自两个核心思想：首先，为了更好地捕捉复杂的关节关系，我们将状态空间对偶框架内的扫描策略重新定义为运动学引导的双向扫描，从而嵌入运动学先验。其次，采用混合时空表示学习方法来紧密耦合空间和时间上下文，从而平衡准确性和平滑性。此外，引入了几何角速度损失，对旋转变化施加物理意义上的约束，以进一步提高运动稳定性。大量实验表明，KineST在轻量级框架内具有卓越的准确性和时间一致性。

## 🔬 方法详解

**问题定义**：论文旨在解决基于AR/VR场景中头戴式显示器等设备获取的稀疏信号，进行准确、高效且时间连贯的全身运动跟踪问题。现有方法的痛点在于，要么计算复杂度高，难以实时应用；要么空间和时间依赖性建模分离，导致重建的运动不自然、不流畅。

**核心思路**：论文的核心思路是利用人体运动学先验知识，指导时空状态空间模型的构建，从而更有效地提取时空依赖关系，并约束运动的合理性。通过运动学引导的双向扫描，将关节之间的运动学关系嵌入到模型中，并使用混合时空表示学习方法，紧密耦合空间和时间信息，从而在精度、效率和时间连贯性之间取得平衡。

**技术框架**：KineST采用状态空间模型作为基础框架，主要包含以下几个阶段：1) 稀疏信号输入：接收来自头戴式显示器等设备的稀疏运动信号。2) 运动学引导的双向扫描：利用人体运动学结构，对状态空间进行双向扫描，提取关节之间的依赖关系。3) 混合时空表示学习：学习紧密耦合空间和时间信息的运动表示。4) 运动状态预测：基于学习到的运动表示，预测下一时刻的全身姿势。5) 几何角速度损失约束：使用几何角速度损失，约束预测的运动符合物理规律。

**关键创新**：KineST最重要的技术创新点在于运动学引导的双向扫描和混合时空表示学习。运动学引导的双向扫描将人体运动学先验知识嵌入到状态空间模型中，使得模型能够更好地捕捉关节之间的依赖关系。混合时空表示学习方法能够紧密耦合空间和时间信息，从而提高运动跟踪的准确性和时间连贯性。与现有方法相比，KineST能够更有效地利用人体运动学信息，从而在精度、效率和时间连贯性之间取得更好的平衡。

**关键设计**：论文的关键设计包括：1) 运动学引导的双向扫描策略，具体实现方式未知。2) 混合时空表示学习的具体网络结构未知。3) 几何角速度损失的具体计算方式，可能是通过计算相邻帧之间关节旋转角度的变化率，并对其进行约束。4) 状态空间模型的具体参数设置未知。

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

论文通过实验验证了KineST在准确性和时间一致性方面的优越性。具体性能数据未知，但论文强调KineST在轻量级框架下实现了优于现有方法的性能，表明其具有较高的实用价值。与现有方法相比，KineST在保持较高精度的同时，显著提高了运动跟踪的效率和时间连贯性。

## 🎯 应用场景

KineST在AR/VR领域具有广泛的应用前景，例如虚拟化身控制、体感游戏、远程协作等。通过准确、高效地跟踪用户的全身运动，KineST可以增强AR/VR应用的沉浸感和交互性，提升用户体验。未来，KineST还可以应用于康复训练、运动分析等领域，为人们的生活带来更多便利。

## 📄 摘要（原文）

> Full-body motion tracking plays an essential role in AR/VR applications, bridging physical and virtual interactions. However, it is challenging to reconstruct realistic and diverse full-body poses based on sparse signals obtained by head-mounted displays, which are the main devices in AR/VR scenarios. Existing methods for pose reconstruction often incur high computational costs or rely on separately modeling spatial and temporal dependencies, making it difficult to balance accuracy, temporal coherence, and efficiency. To address this problem, we propose KineST, a novel kinematics-guided state space model, which effectively extracts spatiotemporal dependencies while integrating local and global pose perception. The innovation comes from two core ideas. Firstly, in order to better capture intricate joint relationships, the scanning strategy within the State Space Duality framework is reformulated into kinematics-guided bidirectional scanning, which embeds kinematic priors. Secondly, a mixed spatiotemporal representation learning approach is employed to tightly couple spatial and temporal contexts, balancing accuracy and smoothness. Additionally, a geometric angular velocity loss is introduced to impose physically meaningful constraints on rotational variations for further improving motion stability. Extensive experiments demonstrate that KineST has superior performance in both accuracy and temporal consistency within a lightweight framework. Project page: https://kaka-1314.github.io/KineST/

