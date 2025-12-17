---
layout: default
title: RAP: 3D Rasterization Augmented End-to-End Planning
---

# RAP: 3D Rasterization Augmented End-to-End Planning

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.04333" target="_blank" class="toolbar-btn">arXiv: 2510.04333v1</a>
    <a href="https://arxiv.org/pdf/2510.04333.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.04333v1" 
            onclick="toggleFavorite(this, '2510.04333v1', 'RAP: 3D Rasterization Augmented End-to-End Planning')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Lan Feng, Yang Gao, Eloi Zablocki, Quanyi Li, Wuyang Li, Sichao Liu, Matthieu Cord, Alexandre Alahi

**分类**: cs.CV, cs.RO

**发布日期**: 2025-10-05

**🔗 代码/项目**: [PROJECT_PAGE](https://alan-lanfeng.github.io/RAP/)

---

## 💡 一句话要点

**提出RAP：基于光栅化的端到端规划，提升驾驶策略的闭环鲁棒性和长尾泛化能力。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `端到端规划` `数据增强` `3D光栅化` `特征对齐` `自动驾驶`

## 📋 核心要点

1. 现有端到端驾驶模仿学习策略在闭环部署时缺乏恢复数据，导致小错误累积并最终失败。
2. RAP通过3D光栅化技术，以轻量级方式生成语义保真度高的数据，用于反事实恢复和跨视角合成等数据增强。
3. RAP引入光栅到真实特征空间对齐，弥合了合成数据与真实数据之间的差距，显著提升了闭环鲁棒性和长尾泛化能力。

## 📝 摘要（中文）

端到端驾驶的模仿学习策略仅在专家演示数据上训练。在闭环部署后，此类策略缺乏恢复数据：小错误无法纠正，并迅速累积成失败。一个有希望的方向是生成超出已记录路径的替代视角和轨迹。先前的工作探索了通过神经渲染或游戏引擎构建逼真的数字孪生，但这些方法速度慢且成本高，因此主要用于评估。本文认为，逼真度对于训练端到端规划器是不必要的。重要的是语义保真度和可扩展性：驾驶取决于几何和动力学，而不是纹理或光照。受此启发，我们提出了3D光栅化，它用轻量级的光栅化带注释的图元代替了昂贵的渲染，从而实现了诸如反事实恢复操作和跨代理视图合成之类的数据增强。为了有效地将这些合成视图转移到真实世界的部署中，我们引入了光栅到真实特征空间的对齐，从而弥合了sim-to-real的差距。这些组件共同构成了光栅化增强规划（RAP），这是一种用于规划的可扩展数据增强管道。RAP在四个主要基准测试中名列前茅：NAVSIM v1 / v2，Waymo开放数据集基于视觉的E2E驾驶和Bench2Drive，实现了最先进的闭环鲁棒性和长尾泛化。我们的结果表明，具有特征对齐的轻量级光栅化足以扩展E2E训练，从而为逼真的渲染提供了一种实用的替代方案。

## 🔬 方法详解

**问题定义**：端到端驾驶模仿学习策略在实际部署中，由于训练数据仅包含专家演示，缺乏从错误中恢复的数据，导致策略在遇到未见过的情况时容易失败。现有方法依赖于耗时的逼真渲染来生成更多数据，但效率低下，难以扩展。

**核心思路**：RAP的核心思想是用轻量级的3D光栅化代替耗时的逼真渲染，生成具有语义保真度的数据，并结合特征空间对齐，弥合合成数据和真实数据之间的差距。这种方法专注于几何和动力学等关键信息，忽略了不必要的纹理和光照细节，从而提高了效率和可扩展性。

**技术框架**：RAP包含以下主要模块：1) 3D光栅化模块，用于生成合成视图；2) 数据增强模块，利用光栅化数据进行反事实恢复和跨视角合成；3) Raster-to-Real特征空间对齐模块，用于将合成特征与真实特征对齐；4) 端到端规划网络，使用增强后的数据进行训练。

**关键创新**：RAP的关键创新在于使用3D光栅化进行数据增强，以及Raster-to-Real特征空间对齐。3D光栅化显著降低了数据生成成本，使得大规模数据增强成为可能。特征空间对齐则保证了合成数据能够有效地迁移到真实世界。

**关键设计**：3D光栅化模块使用预定义的图元（如车辆、道路、交通标志）进行光栅化，并赋予不同的语义标签。数据增强模块通过随机改变车辆位置、速度等参数，生成不同的驾驶场景。Raster-to-Real特征空间对齐模块使用对抗训练或域适应技术，学习一个共享的特征空间，使得合成特征和真实特征在该空间中尽可能接近。

## 📊 实验亮点

RAP在NAVSIM v1/v2、Waymo Open Dataset Vision-based E2E Driving和Bench2Drive四个主要基准测试中均排名第一，表明其在闭环鲁棒性和长尾泛化方面达到了最先进水平。实验结果证明，轻量级光栅化结合特征对齐足以扩展端到端训练，为逼真渲染提供了一种可行的替代方案。

## 🎯 应用场景

RAP可应用于自动驾驶、机器人导航等领域，通过低成本的数据增强，提高智能体在复杂环境中的鲁棒性和泛化能力。该方法尤其适用于训练数据匮乏或难以获取的场景，例如极端天气、罕见交通状况等。

## 📄 摘要（原文）

> Imitation learning for end-to-end driving trains policies only on expert demonstrations. Once deployed in a closed loop, such policies lack recovery data: small mistakes cannot be corrected and quickly compound into failures. A promising direction is to generate alternative viewpoints and trajectories beyond the logged path. Prior work explores photorealistic digital twins via neural rendering or game engines, but these methods are prohibitively slow and costly, and thus mainly used for evaluation. In this work, we argue that photorealism is unnecessary for training end-to-end planners. What matters is semantic fidelity and scalability: driving depends on geometry and dynamics, not textures or lighting. Motivated by this, we propose 3D Rasterization, which replaces costly rendering with lightweight rasterization of annotated primitives, enabling augmentations such as counterfactual recovery maneuvers and cross-agent view synthesis. To transfer these synthetic views effectively to real-world deployment, we introduce a Raster-to-Real feature-space alignment that bridges the sim-to-real gap. Together, these components form Rasterization Augmented Planning (RAP), a scalable data augmentation pipeline for planning. RAP achieves state-of-the-art closed-loop robustness and long-tail generalization, ranking first on four major benchmarks: NAVSIM v1/v2, Waymo Open Dataset Vision-based E2E Driving, and Bench2Drive. Our results show that lightweight rasterization with feature alignment suffices to scale E2E training, offering a practical alternative to photorealistic rendering. Project page: https://alan-lanfeng.github.io/RAP/.

