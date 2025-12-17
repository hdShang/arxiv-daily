---
layout: default
title: Spatially anchored Tactile Awareness for Robust Dexterous Manipulation
---

# Spatially anchored Tactile Awareness for Robust Dexterous Manipulation

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.14647" target="_blank" class="toolbar-btn">arXiv: 2510.14647v1</a>
    <a href="https://arxiv.org/pdf/2510.14647.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.14647v1" 
            onclick="toggleFavorite(this, '2510.14647v1', 'Spatially anchored Tactile Awareness for Robust Dexterous Manipulation')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Jialei Huang, Yang Ye, Yuanqing Gong, Xuezhou Zhu, Yang Gao, Kaifeng Zhang

**分类**: cs.RO

**发布日期**: 2025-10-16

**备注**: 8 pages

---

## 💡 一句话要点

**提出SaTA框架，通过空间锚定的触觉感知实现鲁棒的灵巧操作**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `灵巧操作` `触觉感知` `空间锚定` `机器人学习` `几何推理`

## 📋 核心要点

1. 现有视觉-触觉学习方法在亚毫米级精度任务中表现不足，无法有效利用触觉信号的空间关系。
2. SaTA框架通过正向运动学将触觉特征锚定到手部运动学框架，实现精确几何推理，无需物体模型。
3. SaTA在USB-C插拔、灯泡安装和卡片滑动等任务中显著优于基线，成功率提升高达30%。

## 📝 摘要（中文）

灵巧操作需要精确的几何推理，但现有的视觉-触觉学习方法难以胜任传统基于模型方法能够轻松处理的亚毫米级精度任务。我们发现一个关键限制：虽然触觉传感器提供了丰富的接触信息，但当前的学习框架未能有效地利用触觉信号的感知丰富性及其与手部运动学的空间关系。我们认为理想的触觉表示应该在稳定的参考系中明确地锚定接触测量，同时保留详细的感官信息，使策略不仅能够检测接触的发生，而且能够精确地推断手部坐标系中的物体几何形状。我们引入了SaTA（用于灵巧操作的空间锚定触觉感知），这是一个端到端的策略框架，通过正向运动学将触觉特征明确地锚定到手部的运动学框架，从而实现精确的几何推理，而无需物体模型或显式姿态估计。我们的关键见解是，空间接地的触觉表示允许策略不仅检测接触的发生，而且精确地推断手部坐标系中的物体几何形状。我们在具有挑战性的灵巧操作任务上验证了SaTA，包括自由空间中的双手USB-C插拔（需要亚毫米级的对准精度）、需要精确螺纹啮合和旋转控制的灯泡安装以及需要精细力调节和角度精度的卡片滑动。由于其严格的精度要求，这些任务对基于学习的方法提出了重大挑战。在多个基准测试中，SaTA显著优于强大的视觉-触觉基线，成功率提高了高达30个百分点，同时减少了27个百分点的任务完成时间。

## 🔬 方法详解

**问题定义**：现有基于视觉-触觉的灵巧操作学习方法，难以达到亚毫米级别的操作精度，无法满足一些高精度操作任务的需求。这些方法通常无法充分利用触觉信息与手部运动学之间的空间关系，导致几何推理能力不足。

**核心思路**：论文的核心思路是将触觉信息与手部的运动学信息进行空间上的对齐和锚定。通过将触觉特征映射到手部的运动学框架中，使得策略能够更好地理解触觉信息所代表的物体几何信息，从而实现更精确的操作控制。

**技术框架**：SaTA是一个端到端的策略学习框架，主要包含以下几个模块：1) 触觉数据采集模块：使用触觉传感器获取手部与物体接触时的触觉信息。2) 空间锚定模块：通过正向运动学将触觉特征转换到手部的运动学框架中，实现触觉信息的空间锚定。3) 策略学习模块：使用深度神经网络学习操作策略，输入是空间锚定的触觉特征和手部的状态信息，输出是手部的控制指令。

**关键创新**：SaTA的关键创新在于提出了空间锚定的触觉感知方法。与以往方法不同，SaTA显式地将触觉特征与手部的运动学信息进行关联，从而使得策略能够更好地理解触觉信息所代表的物体几何信息。这种空间锚定的方法使得策略能够在没有物体模型或显式姿态估计的情况下，实现精确的几何推理。

**关键设计**：SaTA使用正向运动学将触觉特征转换到手部的运动学框架中。具体的转换方法是根据手部的关节角度和连杆长度，计算出触觉传感器在手部坐标系中的位置和姿态。然后，将触觉传感器的读数与该位置和姿态信息进行融合，得到空间锚定的触觉特征。策略学习模块使用深度神经网络，例如Transformer网络，来学习操作策略。损失函数可以使用强化学习中的策略梯度方法，例如PPO。

## 📊 实验亮点

实验结果表明，SaTA在USB-C插拔、灯泡安装和卡片滑动等高精度操作任务中显著优于现有的视觉-触觉学习方法。具体而言，SaTA在这些任务中的成功率提高了高达30个百分点，同时任务完成时间减少了27个百分点。这些结果验证了SaTA框架在提高机器人灵巧操作能力方面的有效性。

## 🎯 应用场景

SaTA框架在需要高精度操作的机器人应用中具有广泛的应用前景，例如精密装配、医疗手术、以及在狭小空间或复杂环境中进行操作。该方法无需预先建立物体模型，降低了部署成本，提升了机器人的适应性和鲁棒性，有望推动机器人技术在工业和服务领域的应用。

## 📄 摘要（原文）

> Dexterous manipulation requires precise geometric reasoning, yet existing visuo-tactile learning methods struggle with sub-millimeter precision tasks that are routine for traditional model-based approaches. We identify a key limitation: while tactile sensors provide rich contact information, current learning frameworks fail to effectively leverage both the perceptual richness of tactile signals and their spatial relationship with hand kinematics. We believe an ideal tactile representation should explicitly ground contact measurements in a stable reference frame while preserving detailed sensory information, enabling policies to not only detect contact occurrence but also precisely infer object geometry in the hand's coordinate system. We introduce SaTA (Spatially-anchored Tactile Awareness for dexterous manipulation), an end-to-end policy framework that explicitly anchors tactile features to the hand's kinematic frame through forward kinematics, enabling accurate geometric reasoning without requiring object models or explicit pose estimation. Our key insight is that spatially grounded tactile representations allow policies to not only detect contact occurrence but also precisely infer object geometry in the hand's coordinate system. We validate SaTA on challenging dexterous manipulation tasks, including bimanual USB-C mating in free space, a task demanding sub-millimeter alignment precision, as well as light bulb installation requiring precise thread engagement and rotational control, and card sliding that demands delicate force modulation and angular precision. These tasks represent significant challenges for learning-based methods due to their stringent precision requirements. Across multiple benchmarks, SaTA significantly outperforms strong visuo-tactile baselines, improving success rates by up to 30 percentage while reducing task completion times by 27 percentage.

