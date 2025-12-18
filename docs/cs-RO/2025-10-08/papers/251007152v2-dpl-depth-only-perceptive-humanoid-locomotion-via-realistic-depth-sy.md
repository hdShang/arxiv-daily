---
layout: default
title: DPL: Depth-only Perceptive Humanoid Locomotion via Realistic Depth Synthesis and Cross-Attention Terrain Reconstruction
---

# DPL: Depth-only Perceptive Humanoid Locomotion via Realistic Depth Synthesis and Cross-Attention Terrain Reconstruction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.07152" class="toolbar-btn" target="_blank">📄 arXiv: 2510.07152v2</a>
  <a href="https://arxiv.org/pdf/2510.07152.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.07152v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.07152v2', 'DPL: Depth-only Perceptive Humanoid Locomotion via Realistic Depth Synthesis and Cross-Attention Terrain Reconstruction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jingkai Sun, Gang Han, Pihai Sun, Wen Zhao, Jiahang Cao, Jiaxu Wang, Yijie Guo, Qiang Zhang

**分类**: cs.RO

**发布日期**: 2025-10-08 (更新: 2025-10-10)

---

## 💡 一句话要点

**提出DPL框架，通过深度信息实现类人机器人在复杂地形上的稳健运动**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `类人机器人` `地形感知` `深度学习` `强化学习` `深度图像合成`

## 📋 核心要点

1. 现有基于深度图像的端到端学习方法，训练效率低，且存在较大的模拟到真实世界的差距。
2. 该论文提出一种新框架，利用预训练的高程图感知引导强化学习，并结合交叉注意力Transformer重建地形。
3. 通过逼真的深度图像合成方法，有效降低了地形重建误差，并在全尺寸类人机器人上验证了其性能。

## 📝 摘要（中文）

本文提出了一种新颖的框架，用于实现仅依赖深度信息的类人机器人感知运动。该框架紧密结合了三个关键组件：（1）具有盲骨干的地形感知运动策略，利用预训练的基于高程图的感知来指导强化学习，同时最大限度地减少视觉输入；（2）多模态交叉注意力Transformer，从嘈杂的深度图像中重建结构化的地形表示；（3）逼真的深度图像合成方法，采用自遮挡感知光线投射和噪声感知建模来合成逼真的深度观测，从而将地形重建误差降低30％以上。这种组合能够在有限的数据和硬件资源下实现高效的策略训练，同时保留泛化所需的关键地形特征。我们在全尺寸类人机器人上验证了该框架，展示了其在各种具有挑战性的地形上的敏捷和自适应运动能力。

## 🔬 方法详解

**问题定义**：现有类人机器人地形感知运动方法主要依赖于深度图像或高程图。基于深度图像的端到端学习方法训练效率低，且存在模拟到真实世界的差距。基于高程图的方法依赖于多个视觉传感器和定位系统，导致延迟和鲁棒性降低。因此，需要一种更高效、更鲁棒的仅依赖深度信息的类人机器人运动方法。

**核心思路**：该论文的核心思路是利用逼真的深度图像合成方法生成训练数据，并结合预训练的高程图感知和交叉注意力Transformer，实现仅依赖深度信息的类人机器人地形感知运动。通过这种方式，可以减少对真实数据的依赖，提高训练效率和鲁棒性。

**技术框架**：该框架包含三个主要模块：（1）地形感知运动策略，使用预训练的高程图感知作为先验知识，指导强化学习；（2）多模态交叉注意力Transformer，用于从深度图像中重建结构化的地形表示；（3）逼真的深度图像合成方法，用于生成训练数据。整体流程是：首先使用深度图像合成方法生成训练数据，然后使用这些数据训练地形感知运动策略和交叉注意力Transformer，最后将训练好的策略部署到真实的类人机器人上。

**关键创新**：该论文的关键创新在于：（1）提出了一种逼真的深度图像合成方法，可以有效减少模拟到真实世界的差距；（2）提出了一种多模态交叉注意力Transformer，可以从嘈杂的深度图像中重建结构化的地形表示；（3）将预训练的高程图感知与强化学习相结合，提高了训练效率和鲁棒性。与现有方法的本质区别在于，该方法仅依赖深度信息，并且能够有效减少模拟到真实世界的差距。

**关键设计**：深度图像合成方法采用自遮挡感知光线投射和噪声感知建模，以生成逼真的深度观测。交叉注意力Transformer使用深度图像和预训练的高程图特征作为输入，通过交叉注意力机制融合两种模态的信息。地形感知运动策略使用深度图像重建的地形表示作为输入，通过强化学习训练得到最优的运动控制策略。

## 📊 实验亮点

实验结果表明，该框架能够有效降低地形重建误差，降低幅度超过30%。在全尺寸类人机器人上的实验验证了该框架在各种具有挑战性的地形上的敏捷和自适应运动能力。相较于其他方法，该框架在训练效率和鲁棒性方面均有显著提升。

## 🎯 应用场景

该研究成果可应用于各种需要类人机器人在复杂地形上进行运动的场景，例如搜救、勘探、物流等。通过仅依赖深度信息，可以降低对硬件的要求，提高机器人的自主性和适应性。未来，该技术有望应用于更广泛的机器人领域，例如家庭服务机器人、医疗机器人等。

## 📄 摘要（原文）

> Recent advancements in legged robot perceptive locomotion have shown promising progress. However, terrain-aware humanoid locomotion remains largely constrained to two paradigms: depth image-based end-to-end learning and elevation map-based methods. The former suffers from limited training efficiency and a significant sim-to-real gap in depth perception, while the latter depends heavily on multiple vision sensors and localization systems, resulting in latency and reduced robustness. To overcome these challenges, we propose a novel framework that tightly integrates three key components: (1) Terrain-Aware Locomotion Policy with a Blind Backbone, which leverages pre-trained elevation map-based perception to guide reinforcement learning with minimal visual input; (2) Multi-Modality Cross-Attention Transformer, which reconstructs structured terrain representations from noisy depth images; (3) Realistic Depth Images Synthetic Method, which employs self-occlusion-aware ray casting and noise-aware modeling to synthesize realistic depth observations, achieving over 30\% reduction in terrain reconstruction error. This combination enables efficient policy training with limited data and hardware resources, while preserving critical terrain features essential for generalization. We validate our framework on a full-sized humanoid robot, demonstrating agile and adaptive locomotion across diverse and challenging terrains.

