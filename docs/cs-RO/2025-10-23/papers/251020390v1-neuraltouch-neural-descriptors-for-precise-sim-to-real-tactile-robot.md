---
layout: default
title: NeuralTouch: Neural Descriptors for Precise Sim-to-Real Tactile Robot Control
---

# NeuralTouch: Neural Descriptors for Precise Sim-to-Real Tactile Robot Control

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.20390" target="_blank" class="toolbar-btn">arXiv: 2510.20390v1</a>
    <a href="https://arxiv.org/pdf/2510.20390.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.20390v1" 
            onclick="toggleFavorite(this, '2510.20390v1', 'NeuralTouch: Neural Descriptors for Precise Sim-to-Real Tactile Robot Control')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Yijiong Lin, Bowen Deng, Chenghua Lu, Max Yang, Efi Psomopoulou, Nathan F. Lepora

**分类**: cs.RO

**发布日期**: 2025-10-23

---

## 💡 一句话要点

**NeuralTouch：融合神经描述符和触觉反馈，实现精确的Sim2Real机器人控制**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `触觉感知` `机器人抓取` `深度强化学习` `神经描述符场` `Sim2Real` `多模态融合` `机器人控制`

## 📋 核心要点

1. 现有基于视觉的抓取方法（如NDF）易受相机标定误差和点云不完整的影响，导致抓取精度不足。
2. NeuralTouch融合NDF和触觉反馈，利用NDF隐式表示目标接触几何，并通过强化学习策略优化抓取。
3. 实验表明，NeuralTouch在仿真和真实环境中均能显著提高抓取精度和鲁棒性，无需额外微调。

## 📝 摘要（中文）

本文提出了一种名为NeuralTouch的多模态框架，它集成了神经描述符场（NDF）和触觉传感，通过轻柔的物理交互实现精确且可泛化的抓取。该方法利用NDF隐式地表示目标接触几何形状，并在此基础上训练一个深度强化学习（RL）策略，利用触觉反馈来优化抓取。该策略以神经描述符为条件，无需显式指定接触类型。通过仿真中的消融研究和零样本迁移到真实世界的操作任务（如插孔和开瓶盖）的验证，结果表明NeuralTouch显著提高了抓取的准确性和鲁棒性，为精确的、接触丰富的机器人操作提供了一个通用框架。

## 🔬 方法详解

**问题定义**：现有基于视觉的抓取方法，例如使用神经描述符场（NDF），虽然能够泛化到不同的物体类别，但由于相机标定误差、点云数据不完整以及物体本身的多样性，导致抓取姿态不够精确。另一方面，触觉传感虽然能实现更精确的接触，但现有方法通常学习到的策略仅限于简单的、预定义的接触几何形状，缺乏泛化能力。

**核心思路**：NeuralTouch的核心思路是将视觉信息（通过NDF编码）和触觉反馈相结合，利用视觉信息提供初始的抓取姿态估计，然后通过触觉反馈进行精细调整。这种结合方式既能利用视觉的泛化能力，又能利用触觉的精确性，从而实现更准确、更鲁棒的抓取。

**技术框架**：NeuralTouch的整体框架包含两个主要模块：1) 基于NDF的视觉感知模块，用于估计初始抓取姿态；2) 基于深度强化学习（RL）的触觉反馈控制模块，用于根据触觉传感器的数据调整抓取姿态。整个流程是：首先，利用相机获取物体的视觉信息，通过NDF生成抓取姿态的建议。然后，机器人执行初始抓取动作，并利用触觉传感器感知与物体的接触情况。最后，RL策略根据触觉反馈调整机器人的动作，直到达到期望的抓取效果。

**关键创新**：NeuralTouch的关键创新在于将NDF和触觉反馈无缝集成，并使用深度强化学习来学习触觉反馈控制策略。与传统方法相比，NeuralTouch不需要显式地指定接触类型，而是通过学习的方式自动提取有用的触觉信息。此外，该方法能够实现零样本迁移，即在仿真环境中训练的策略可以直接应用到真实机器人上，无需额外的微调。

**关键设计**：在RL策略的设计上，NeuralTouch使用了一个以神经描述符为条件的策略网络。这意味着策略网络的输入不仅包括触觉传感器的读数，还包括从NDF中提取的神经描述符。这种设计使得策略网络能够更好地理解物体的几何形状和抓取任务的要求。在训练过程中，使用了合适的奖励函数来鼓励机器人实现精确的抓取，并避免不必要的碰撞。具体的网络结构和超参数设置在论文中有详细描述。

## 📊 实验亮点

NeuralTouch在仿真和真实世界的实验中均表现出色。在仿真环境中，通过消融实验验证了触觉反馈和神经描述符的有效性。在真实世界的peg-out-in-hole和bottle lid opening任务中，NeuralTouch实现了零样本迁移，显著提高了抓取成功率和鲁棒性，优于传统的基于视觉的抓取方法。

## 🎯 应用场景

NeuralTouch在需要精确操作的机器人应用中具有广泛的应用前景，例如：精密装配、医疗手术、家庭服务等。该方法能够提高机器人在复杂环境下的操作能力，降低对环境和物体模型的依赖，从而实现更智能、更灵活的机器人系统。未来，该技术有望应用于自动化生产线、远程操作机器人以及人机协作等领域。

## 📄 摘要（原文）

> Grasping accuracy is a critical prerequisite for precise object manipulation, often requiring careful alignment between the robot hand and object. Neural Descriptor Fields (NDF) offer a promising vision-based method to generate grasping poses that generalize across object categories. However, NDF alone can produce inaccurate poses due to imperfect camera calibration, incomplete point clouds, and object variability. Meanwhile, tactile sensing enables more precise contact, but existing approaches typically learn policies limited to simple, predefined contact geometries. In this work, we introduce NeuralTouch, a multimodal framework that integrates NDF and tactile sensing to enable accurate, generalizable grasping through gentle physical interaction. Our approach leverages NDF to implicitly represent the target contact geometry, from which a deep reinforcement learning (RL) policy is trained to refine the grasp using tactile feedback. This policy is conditioned on the neural descriptors and does not require explicit specification of contact types. We validate NeuralTouch through ablation studies in simulation and zero-shot transfer to real-world manipulation tasks--such as peg-out-in-hole and bottle lid opening--without additional fine-tuning. Results show that NeuralTouch significantly improves grasping accuracy and robustness over baseline methods, offering a general framework for precise, contact-rich robotic manipulation.

