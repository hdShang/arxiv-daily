---
layout: default
title: Adaptive Wiping: Adaptive contact-rich manipulation through few-shot imitation learning with Force-Torque feedback and pre-trained object representations
---

# Adaptive Wiping: Adaptive contact-rich manipulation through few-shot imitation learning with Force-Torque feedback and pre-trained object representations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.06451" class="toolbar-btn" target="_blank">📄 arXiv: 2505.06451v1</a>
  <a href="https://arxiv.org/pdf/2505.06451.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.06451v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.06451v1', 'Adaptive Wiping: Adaptive contact-rich manipulation through few-shot imitation learning with Force-Torque feedback and pre-trained object representations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chikaha Tsuji, Enrique Coronado, Pablo Osorio, Gentiane Venture

**分类**: cs.RO

**发布日期**: 2025-05-09

**期刊**: IEEE Robotics and Automation Letters, vol.10, no.1, pp.240-247, 2025

**DOI**: [10.1109/LRA.2024.3497713](https://doi.org/10.1109/LRA.2024.3497713)

---

## 💡 一句话要点

**提出自适应擦拭方法以解决机器人接触丰富任务的挑战**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `模仿学习` `自适应控制` `力-扭矩反馈` `机器人技术` `接触丰富任务` `深度学习` `物体表示`

## 📋 核心要点

1. 现有的模仿学习方法在执行接触丰富任务时需要大量的演示，且训练环境与实际环境之间存在显著差异，导致适应性不足。
2. 本文提出了一种结合实时力-扭矩反馈与预训练物体表示的自适应擦拭方法，能够动态调整以应对未见的环境变化。
3. 实验结果表明，所提方法在施加参考力的准确率上达到了96%，相比于传统方法的4%有了显著提升，展示了良好的适应性。

## 📝 摘要（中文）

模仿学习为机器人执行重复性任务提供了一条途径，使人类能够专注于更具吸引力和意义的活动。然而，广泛的演示需求和训练与现实环境之间的差异带来了挑战。本文聚焦于使用软性和可变形物体进行的接触丰富任务，如擦拭，这需要自适应的力控制来处理擦拭表面高度和海绵物理特性的变化。我们提出了一种新方法，将实时力-扭矩反馈与预训练的物体表示相结合，使机器人能够动态适应之前未见的表面高度和海绵物理特性的变化。在实际实验中，我们的方法在施加参考力方面达到了96%的准确率，显著优于缺乏FT反馈回路的先前方法，仅达到了4%的准确率。我们在不同条件下进行了适应性评估，涉及40种场景，使用10种具有不同物理特性的海绵和4种擦拭表面高度，分析力轨迹显示了机器人适应性的显著提升。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人在执行接触丰富任务（如擦拭）时，因环境变化导致的适应性不足问题。现有方法通常依赖大量的演示，且在真实环境中表现不佳。

**核心思路**：论文的核心思路是将实时的力-扭矩反馈与预训练的物体表示相结合，使机器人能够在面对未见的表面高度和物体特性时，进行自适应的力控制。这样的设计能够提高机器人在复杂环境下的操作能力。

**技术框架**：整体架构包括数据采集模块、力-扭矩反馈处理模块和自适应控制模块。数据采集模块负责获取实时的力和扭矩信息，反馈处理模块分析这些信息并调整控制策略，自适应控制模块则执行相应的操作。

**关键创新**：最重要的技术创新在于引入了实时的力-扭矩反馈机制，使得机器人能够在动态环境中进行自适应调整，这与传统方法的静态控制方式有本质区别。

**关键设计**：在参数设置上，采用了基于力反馈的损失函数，以优化机器人在不同环境下的表现；网络结构上，使用了深度学习模型来处理预训练的物体表示，增强了模型的泛化能力。

## 📊 实验亮点

实验结果显示，所提方法在施加参考力方面的准确率达到了96%，相比于传统方法的4%有了显著提升，展示了在不同条件下的强适应性，验证了方法的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括家庭清洁、工业自动化和服务机器人等。通过提高机器人在复杂环境中的适应能力，能够显著提升其在实际应用中的效率和可靠性，未来可能推动智能家居和自动化服务的发展。

## 📄 摘要（原文）

> Imitation learning offers a pathway for robots to perform repetitive tasks, allowing humans to focus on more engaging and meaningful activities. However, challenges arise from the need for extensive demonstrations and the disparity between training and real-world environments. This paper focuses on contact-rich tasks like wiping with soft and deformable objects, requiring adaptive force control to handle variations in wiping surface height and the sponge's physical properties. To address these challenges, we propose a novel method that integrates real-time force-torque (FT) feedback with pre-trained object representations. This approach allows robots to dynamically adjust to previously unseen changes in surface heights and sponges' physical properties. In real-world experiments, our method achieved 96% accuracy in applying reference forces, significantly outperforming the previous method that lacked an FT feedback loop, which only achieved 4% accuracy. To evaluate the adaptability of our approach, we conducted experiments under different conditions from the training setup, involving 40 scenarios using 10 sponges with varying physical properties and 4 types of wiping surface heights, demonstrating significant improvements in the robot's adaptability by analyzing force trajectories. The video of our work is available at: https://sites.google.com/view/adaptive-wiping

