---
layout: default
title: "Parse-Augment-Distill: Learning Generalizable Bimanual Visuomotor Policies from Single Human Video"
---

# Parse-Augment-Distill: Learning Generalizable Bimanual Visuomotor Policies from Single Human Video

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.20286" class="toolbar-btn" target="_blank">📄 arXiv: 2509.20286v1</a>
  <a href="https://arxiv.org/pdf/2509.20286.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.20286v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.20286v1', 'Parse-Augment-Distill: Learning Generalizable Bimanual Visuomotor Policies from Single Human Video')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Georgios Tziafas, Jiayun Zhang, Hamidreza Kasaei

**分类**: cs.RO

**发布日期**: 2025-09-24

**🔗 代码/项目**: [PROJECT_PAGE](https://gtziafas.github.io/PAD_project/)

---

## 💡 一句话要点

**PAD：从单个人类视频学习可泛化的双臂视觉运动策略**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `双臂操作` `视觉运动策略` `模仿学习` `关键点表示` `任务和运动规划`

## 📋 核心要点

1. 现有方法依赖大量遥操作数据，泛化性差，且基于图像的策略存在sim-to-real差距。
2. PAD框架通过解析人类视频为关键点轨迹，利用任务和运动规划进行无模拟器的数据增强，并蒸馏成关键点条件策略。
3. 实验表明，PAD在成功率和样本效率上优于现有方法，并在真实世界的双臂任务中实现了良好的泛化能力。

## 📝 摘要（中文）

从专家演示中学习视觉运动策略是现代机器人研究的重要前沿，然而，大多数流行的方法需要大量的遥操作数据收集工作，并且难以泛化到分布外。扩展数据收集已经通过利用人类视频以及演示增强技术进行了探索。后一种方法通常需要昂贵的模拟rollout，并使用合成图像数据训练策略，因此引入了sim-to-real差距。同时，诸如关键点之类的替代状态表示已显示出在类别级别泛化的巨大前景。在这项工作中，我们将这些途径整合到一个统一的框架中：PAD（Parse-Augment-Distill），用于从单个人的视频中学习可泛化的双臂策略。我们的方法依赖于三个步骤：（a）将人的视频演示解析为机器人可执行的关键点-动作轨迹，（b）采用双臂任务和运动规划来大规模地增强演示，而无需模拟器，以及（c）将增强的轨迹提炼成关键点条件策略。在经验上，我们展示了PAD在成功率和样本/成本效率方面均优于依赖于具有模拟rollout的图像策略的最新双臂演示增强工作。我们在六个不同的现实世界双臂任务中部署了我们的框架，例如倒饮料，清理垃圾和打开容器，从而产生可以在看不见的空间排列，对象实例和背景干扰物中泛化的one-shot策略。

## 🔬 方法详解

**问题定义**：论文旨在解决从少量（甚至单个）人类视频中学习可泛化的双臂操作策略的问题。现有方法通常需要大量的机器人遥操作数据，成本高昂，且难以泛化到新的场景。基于图像的策略训练通常依赖于模拟环境，引入了sim-to-real的差距，影响了真实环境中的性能。

**核心思路**：论文的核心思路是利用关键点作为中间表示，将人类视频解析为机器人可执行的轨迹，并结合任务和运动规划进行数据增强，最后通过蒸馏学习得到一个关键点条件策略。这种方法避免了直接从图像学习策略，减少了sim-to-real差距，并利用任务和运动规划实现了高效的数据增强。

**技术框架**：PAD框架包含三个主要阶段：1) **解析(Parse)**：将人类视频演示解析为机器人可执行的关键点-动作轨迹。这通常涉及使用姿态估计模型提取关键点，并将其与相应的动作指令关联起来。2) **增强(Augment)**：利用双臂任务和运动规划器，在不同的场景和物体排列下生成更多的轨迹数据。这一步无需依赖模拟器，而是通过算法自动生成。3) **蒸馏(Distill)**：将增强后的轨迹数据提炼成一个关键点条件策略。该策略以关键点作为输入，输出相应的动作指令。

**关键创新**：PAD框架的关键创新在于将关键点表示、任务和运动规划以及蒸馏学习结合起来，实现了一种高效且可泛化的双臂操作策略学习方法。与传统的基于图像的策略学习方法相比，PAD避免了sim-to-real差距，并利用任务和运动规划实现了高效的数据增强。

**关键设计**：论文中关键的设计包括：1) 使用姿态估计模型提取关键点，并设计合适的关键点表示。2) 设计合适的任务和运动规划器，以生成多样化的轨迹数据。3) 选择合适的神经网络结构和损失函数，以训练关键点条件策略。具体的参数设置和网络结构在论文中可能有所描述，但摘要中未提及。

## 📊 实验亮点

PAD在六个不同的真实世界双臂任务中进行了评估，包括倒饮料、清理垃圾和打开容器等。实验结果表明，PAD在成功率和样本效率方面均优于依赖于具有模拟rollout的图像策略的最新双臂演示增强工作。PAD能够生成可以在看不见的空间排列，对象实例和背景干扰物中泛化的one-shot策略。

## 🎯 应用场景

该研究成果可应用于各种需要双臂操作的机器人任务，例如家庭服务机器人、工业自动化、医疗辅助机器人等。通过从少量人类演示中学习，机器人可以快速适应新的任务和环境，提高工作效率和灵活性。该方法有望降低机器人部署的成本和难度，加速机器人在现实世界中的应用。

## 📄 摘要（原文）

> Learning visuomotor policies from expert demonstrations is an important frontier in modern robotics research, however, most popular methods require copious efforts for collecting teleoperation data and struggle to generalize out-ofdistribution. Scaling data collection has been explored through leveraging human videos, as well as demonstration augmentation techniques. The latter approach typically requires expensive simulation rollouts and trains policies with synthetic image data, therefore introducing a sim-to-real gap. In parallel, alternative state representations such as keypoints have shown great promise for category-level generalization. In this work, we bring these avenues together in a unified framework: PAD (Parse-AugmentDistill), for learning generalizable bimanual policies from a single human video. Our method relies on three steps: (a) parsing a human video demo into a robot-executable keypoint-action trajectory, (b) employing bimanual task-and-motion-planning to augment the demonstration at scale without simulators, and (c) distilling the augmented trajectories into a keypoint-conditioned policy. Empirically, we showcase that PAD outperforms state-ofthe-art bimanual demonstration augmentation works relying on image policies with simulation rollouts, both in terms of success rate and sample/cost efficiency. We deploy our framework in six diverse real-world bimanual tasks such as pouring drinks, cleaning trash and opening containers, producing one-shot policies that generalize in unseen spatial arrangements, object instances and background distractors. Supplementary material can be found in the project webpage https://gtziafas.github.io/PAD_project/.

