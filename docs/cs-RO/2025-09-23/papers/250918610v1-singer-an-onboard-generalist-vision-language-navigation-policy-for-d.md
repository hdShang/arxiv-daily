---
layout: default
title: "SINGER: An Onboard Generalist Vision-Language Navigation Policy for Drones"
---

# SINGER: An Onboard Generalist Vision-Language Navigation Policy for Drones

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.18610" class="toolbar-btn" target="_blank">📄 arXiv: 2509.18610v1</a>
  <a href="https://arxiv.org/pdf/2509.18610.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.18610v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.18610v1', 'SINGER: An Onboard Generalist Vision-Language Navigation Policy for Drones')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Maximilian Adang, JunEn Low, Ola Shorinwa, Mac Schwager

**分类**: cs.RO

**发布日期**: 2025-09-23

---

## 💡 一句话要点

**SINGER：一种用于无人机的通用视觉-语言导航策略，仅使用机载传感器。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `无人机导航` `视觉语言导航` `端到端学习` `模拟到真实迁移` `高斯溅射` `自主导航` `机器人控制`

## 📋 核心要点

1. 开放词汇无人机导航面临缺乏大规模数据、实时控制需求和外部姿态估计不可靠等挑战。
2. SINGER利用逼真模拟器生成数据，结合RRT专家演示，训练轻量级端到端视觉运动策略。
3. 硬件实验表明，SINGER在零样本迁移到新环境和目标方面优于基线方法，到达率更高。

## 📝 摘要（中文）

大型视觉-语言模型在开放词汇机器人策略方面取得了显著进展，例如，通用机器人操作策略，使机器人能够完成以自然语言指定的复杂任务。尽管取得了这些成功，但由于缺乏大规模演示、无人机稳定性的实时控制需求以及缺乏可靠的外部姿态估计模块，开放词汇自主无人机导航仍然是一个尚未解决的挑战。在这项工作中，我们提出了SINGER，用于在开放世界中使用仅机载传感和计算的语言引导自主无人机导航。为了训练鲁棒的开放词汇导航策略，SINGER利用了三个核心组件：（i）一个逼真的语言嵌入飞行模拟器，使用高斯溅射实现最小的sim-to-real差距，以实现高效的数据生成，（ii）一个受RRT启发的用于无碰撞导航演示的多轨迹生成专家，这些被用于训练（iii）一个用于实时闭环控制的轻量级端到端视觉运动策略。通过广泛的硬件飞行实验，我们证明了我们的策略对未见环境和未见语言条件目标对象的卓越零样本sim-to-real迁移。当在约700k-1M个语言条件视觉运动数据的观察-动作对上进行训练并部署在硬件上时，SINGER的平均查询到达率比速度控制的语义引导基线高23.33%，并且平均保持查询在视野中的时间高16.67%，碰撞次数减少10%。

## 🔬 方法详解

**问题定义**：论文旨在解决开放世界中，仅使用无人机载传感器和计算资源，实现基于自然语言指令的自主导航问题。现有方法通常依赖于大规模数据集、外部定位系统或复杂的环境建模，难以满足无人机实时性和鲁棒性的需求。

**核心思路**：论文的核心思路是利用逼真的模拟环境生成大量训练数据，并通过专家系统提供高质量的导航演示，从而训练一个轻量级的端到端视觉运动策略。这种方法旨在缩小模拟环境与真实环境之间的差距，并提高策略的泛化能力。

**技术框架**：SINGER的整体框架包含三个主要模块：1) 基于高斯溅射的语言嵌入飞行模拟器，用于生成逼真的训练数据；2) 受RRT启发的轨迹生成专家，用于提供无碰撞导航演示；3) 端到端视觉运动策略，用于实时闭环控制。训练数据由模拟器生成，专家系统用于生成高质量的导航轨迹，然后使用这些数据训练视觉运动策略。

**关键创新**：SINGER的关键创新在于其数据生成和策略训练方法。通过使用高斯溅射技术，SINGER能够生成逼真的模拟环境，从而减少了sim-to-real的差距。此外，SINGER还利用专家系统生成高质量的导航轨迹，从而提高了策略的训练效率和性能。

**关键设计**：SINGER使用轻量级的神经网络结构来实现视觉运动策略，以满足无人机实时控制的需求。损失函数的设计旨在鼓励策略学习到安全、高效的导航行为。具体参数设置和网络结构细节在论文中进行了详细描述（未知）。

## 📊 实验亮点

SINGER在硬件飞行实验中表现出色，零样本迁移到未见环境和未见语言条件目标对象。与速度控制的语义引导基线相比，SINGER的平均查询到达率提高了23.33%，平均保持查询在视野中的时间提高了16.67%，碰撞次数减少了10%。这些结果表明SINGER具有很强的泛化能力和鲁棒性。

## 🎯 应用场景

SINGER技术可应用于物流配送、环境监测、灾害救援、安防巡逻等领域。该研究成果有助于提升无人机在复杂环境中的自主导航能力，降低对外部基础设施的依赖，并扩展无人机的应用范围。未来，该技术有望与更高级别的任务规划和决策系统集成，实现更智能化的无人机应用。

## 📄 摘要（原文）

> Large vision-language models have driven remarkable progress in open-vocabulary robot policies, e.g., generalist robot manipulation policies, that enable robots to complete complex tasks specified in natural language. Despite these successes, open-vocabulary autonomous drone navigation remains an unsolved challenge due to the scarcity of large-scale demonstrations, real-time control demands of drones for stabilization, and lack of reliable external pose estimation modules. In this work, we present SINGER for language-guided autonomous drone navigation in the open world using only onboard sensing and compute. To train robust, open-vocabulary navigation policies, SINGER leverages three central components: (i) a photorealistic language-embedded flight simulator with minimal sim-to-real gap using Gaussian Splatting for efficient data generation, (ii) an RRT-inspired multi-trajectory generation expert for collision-free navigation demonstrations, and these are used to train (iii) a lightweight end-to-end visuomotor policy for real-time closed-loop control. Through extensive hardware flight experiments, we demonstrate superior zero-shot sim-to-real transfer of our policy to unseen environments and unseen language-conditioned goal objects. When trained on ~700k-1M observation action pairs of language conditioned visuomotor data and deployed on hardware, SINGER outperforms a velocity-controlled semantic guidance baseline by reaching the query 23.33% more on average, and maintains the query in the field of view 16.67% more on average, with 10% fewer collisions.

