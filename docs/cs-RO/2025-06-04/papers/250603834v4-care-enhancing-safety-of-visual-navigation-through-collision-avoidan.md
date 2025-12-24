---
layout: default
title: "CARE: Enhancing Safety of Visual Navigation through Collision Avoidance via Repulsive Estimation"
---

# CARE: Enhancing Safety of Visual Navigation through Collision Avoidance via Repulsive Estimation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.03834" class="toolbar-btn" target="_blank">📄 arXiv: 2506.03834v4</a>
  <a href="https://arxiv.org/pdf/2506.03834.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.03834v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.03834v4', 'CARE: Enhancing Safety of Visual Navigation through Collision Avoidance via Repulsive Estimation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Joonkyung Kim, Joonyeol Sim, Woojun Kim, Katia Sycara, Changjoo Nam

**分类**: cs.RO, cs.CV

**发布日期**: 2025-06-04 (更新: 2025-08-08)

**备注**: 16 pages, 6 figures

**🔗 代码/项目**: [PROJECT_PAGE](https://airlab-sogang.github.io/CARE/)

---

## 💡 一句话要点

**提出CARE以解决视觉导航中的碰撞避免问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉导航` `碰撞避免` `深度估计` `机器人技术` `安全性增强`

## 📋 核心要点

1. 现有视觉导航方法在面对未见场景时，容易产生碰撞，泛化能力不足。
2. CARE模块通过动态调整预训练模型生成的轨迹，利用从RGB输入直接估计的深度图像计算排斥力向量。
3. 实验证明，CARE在多种机器人平台上显著减少碰撞，并提高了探索任务的行驶距离。

## 📝 摘要（中文）

我们提出了CARE（通过排斥估计实现碰撞避免），旨在提高基于学习的视觉导航方法的鲁棒性。近年来，视觉导航模型，尤其是基础模型，通过仅使用RGB图像生成可行轨迹，表现出良好的性能。然而，这些策略在面对包含未见物体或不同相机设置（如视场变化、相机姿态或焦距变化）的环境时，泛化能力较差，可能导致碰撞。为了解决这一限制，我们引入了CARE，一个可附加模块，增强视觉导航的安全性，无需额外的范围传感器或对预训练模型的微调。通过与多种机器人平台的最先进视觉导航模型集成，实验证明CARE显著减少碰撞（高达100%），同时在目标导向导航中不影响导航性能，并在探索任务中进一步提高无碰撞行驶距离（高达10.7倍）。

## 🔬 方法详解

**问题定义**：本论文旨在解决视觉导航模型在未见场景中容易导致碰撞的问题。现有方法在不同相机设置下的泛化能力不足，导致生成的轨迹存在安全隐患。

**核心思路**：CARE模块通过计算排斥力向量，动态调整预训练模型生成的轨迹，从而增强导航的安全性。该设计不需要额外的传感器或对模型进行微调，简化了应用过程。

**技术框架**：CARE的整体架构包括一个可附加模块，能够与任何基于RGB的导航模型无缝集成。该模块通过深度图像估计生成排斥力向量，并调整机器人轨迹。

**关键创新**：CARE的主要创新在于其无需额外传感器的设计，利用RGB图像直接估计深度信息，从而实现碰撞避免。这一方法与传统依赖于额外传感器的方案有本质区别。

**关键设计**：CARE模块的设计包括深度图像的估计方法、排斥力向量的计算方式，以及如何将这些信息有效整合到轨迹生成过程中。

## 📊 实验亮点

实验结果显示，CARE在多种机器人平台上显著减少了碰撞，最高可达100%的碰撞率降低。同时，在目标导向导航中，导航性能未受影响，并在探索任务中提高了无碰撞行驶距离，最高提升幅度达到10.7倍。这些结果表明CARE的有效性和实用性。

## 🎯 应用场景

CARE模块具有广泛的应用潜力，特别是在自主机器人、无人驾驶汽车和无人机等领域。通过提高视觉导航的安全性，CARE能够在复杂和动态环境中实现更可靠的导航，减少事故风险，提升用户信任度。未来，随着技术的进一步发展，CARE有望在更多实际场景中得到应用。

## 📄 摘要（原文）

> We propose CARE (Collision Avoidance via Repulsive Estimation) to improve the robustness of learning-based visual navigation methods. Recently, visual navigation models, particularly foundation models, have demonstrated promising performance by generating viable trajectories using only RGB images. However, these policies can generalize poorly to environments containing out-of-distribution (OOD) scenes characterized by unseen objects or different camera setups (e.g., variations in field of view, camera pose, or focal length). Without fine-tuning, such models could produce trajectories that lead to collisions, necessitating substantial efforts in data collection and additional training. To address this limitation, we introduce CARE, an attachable module that enhances the safety of visual navigation without requiring additional range sensors or fine-tuning of pretrained models. CARE can be integrated seamlessly into any RGB-based navigation model that generates local robot trajectories. It dynamically adjusts trajectories produced by a pretrained model using repulsive force vectors computed from depth images estimated directly from RGB inputs. We evaluate CARE by integrating it with state-of-the-art visual navigation models across diverse robot platforms. Real-world experiments show that CARE significantly reduces collisions (up to 100%) without compromising navigation performance in goal-conditioned navigation, and further improves collision-free travel distance (up to 10.7x) in exploration tasks. Project page: https://airlab-sogang.github.io/CARE/

