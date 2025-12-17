---
layout: default
title: PhysMaster: Mastering Physical Representation for Video Generation via Reinforcement Learning
---

# PhysMaster: Mastering Physical Representation for Video Generation via Reinforcement Learning

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.13809" target="_blank" class="toolbar-btn">arXiv: 2510.13809v1</a>
    <a href="https://arxiv.org/pdf/2510.13809.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.13809v1" 
            onclick="toggleFavorite(this, '2510.13809v1', 'PhysMaster: Mastering Physical Representation for Video Generation via Reinforcement Learning')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Sihui Ji, Xi Chen, Xin Tao, Pengfei Wan, Hengshuang Zhao

**分类**: cs.CV

**发布日期**: 2025-10-15

**备注**: Project Page: https://sihuiji.github.io/PhysMaster-Page/

---

## 💡 一句话要点

**提出PhysMaster，通过强化学习物理表征，提升视频生成模型的物理合理性。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱四：生成式动作 (Generative Motion)**

**关键词**: `视频生成` `物理表征学习` `强化学习` `物理合理性` `直接偏好优化`

## 📋 核心要点

1. 现有视频生成模型视觉效果逼真，但缺乏对物理规律的遵守，限制了其在物理合理性方面的表现。
2. PhysMaster通过强化学习优化物理表征，利用PhysEncoder从输入图像中提取物理信息，并指导视频生成。
3. 实验证明PhysMaster能有效提升视频生成模型对物理规律的感知，并在多种物理场景中表现出良好的泛化性。

## 📝 摘要（中文）

本文提出PhysMaster，旨在提升视频生成模型对物理规律的感知能力，使其生成更符合物理规律的视频，从而更好地作为“世界模型”。PhysMaster基于图像到视频的生成任务，模型需要根据输入图像预测符合物理规律的动态过程。由于输入图像提供了物体相对位置和潜在交互等物理先验，因此设计了PhysEncoder来编码图像中的物理信息，并将其作为额外条件注入视频生成过程。为了更好地监督模型的物理性能，PhysEncoder采用强化学习和人类反馈进行物理表征学习，利用生成模型的反馈，通过直接偏好优化（DPO）以端到端的方式优化物理表征。实验表明，PhysMaster能够有效提高PhysEncoder的物理感知能力，从而提升视频生成的物理合理性，并在各种物理场景中展现出良好的泛化能力。PhysMaster通过强化学习范式中的表征学习统一解决各种物理过程，可以作为物理感知视频生成和更广泛应用的通用插件式解决方案。

## 🔬 方法详解

**问题定义**：现有视频生成模型虽然在视觉效果上表现出色，但往往忽略了物理规律，导致生成的视频在物理上不合理。这限制了它们在需要物理交互的场景中的应用，例如作为“世界模型”进行预测和规划。因此，如何提升视频生成模型对物理规律的感知能力是一个关键问题。

**核心思路**：PhysMaster的核心思路是通过学习一个有效的物理表征来指导视频生成过程。具体来说，它利用输入图像提供的物理先验信息（如物体位置、大小、相对关系等），通过PhysEncoder提取这些信息，并将其作为条件注入到视频生成模型中。为了更好地学习物理表征，采用了强化学习方法，利用生成模型的反馈来优化表征学习过程。

**技术框架**：PhysMaster的整体框架包括PhysEncoder和视频生成模型两部分。PhysEncoder负责从输入图像中提取物理表征，视频生成模型则根据该表征生成视频。PhysEncoder的训练采用强化学习方法，通过与视频生成模型交互，并根据生成视频的物理合理性进行奖励或惩罚，从而不断优化物理表征。具体来说，使用了直接偏好优化（DPO）算法，根据人类反馈来优化物理表征。

**关键创新**：PhysMaster的关键创新在于将强化学习引入物理表征学习，并利用人类反馈来指导表征的优化。与传统的监督学习方法相比，强化学习能够更好地捕捉物理规律的复杂性和多样性，并根据生成结果的物理合理性进行优化。此外，使用DPO算法可以直接优化策略，避免了传统强化学习中的一些问题。

**关键设计**：PhysEncoder的网络结构未知，但其目标是提取图像中的物理信息。视频生成模型可以使用现有的各种模型结构。强化学习的奖励函数设计至关重要，需要能够准确反映生成视频的物理合理性。DPO算法中的偏好数据来自人类反馈，需要设计合适的标注界面和流程，以获取高质量的偏好数据。具体参数设置和损失函数细节未知。

## 📊 实验亮点

论文通过实验证明了PhysMaster能够有效提高视频生成模型的物理合理性。具体性能数据未知，但实验结果表明，PhysMaster在各种物理场景中都表现出良好的泛化能力，能够生成更符合物理规律的视频。与没有物理表征的基线模型相比，PhysMaster能够显著提升生成视频的物理合理性。

## 🎯 应用场景

PhysMaster具有广泛的应用前景，例如可以用于生成更逼真的游戏场景、训练自动驾驶系统、进行机器人控制等。通过提升视频生成模型的物理合理性，可以使其更好地模拟真实世界，从而为各种应用提供更可靠的基础。此外，PhysMaster的强化学习框架也可以推广到其他需要物理感知的任务中，例如物体识别、场景理解等。

## 📄 摘要（原文）

> Video generation models nowadays are capable of generating visually realistic videos, but often fail to adhere to physical laws, limiting their ability to generate physically plausible videos and serve as ''world models''. To address this issue, we propose PhysMaster, which captures physical knowledge as a representation for guiding video generation models to enhance their physics-awareness. Specifically, PhysMaster is based on the image-to-video task where the model is expected to predict physically plausible dynamics from the input image. Since the input image provides physical priors like relative positions and potential interactions of objects in the scenario, we devise PhysEncoder to encode physical information from it as an extra condition to inject physical knowledge into the video generation process. The lack of proper supervision on the model's physical performance beyond mere appearance motivates PhysEncoder to apply reinforcement learning with human feedback to physical representation learning, which leverages feedback from generation models to optimize physical representations with Direct Preference Optimization (DPO) in an end-to-end manner. PhysMaster provides a feasible solution for improving physics-awareness of PhysEncoder and thus of video generation, proving its ability on a simple proxy task and generalizability to wide-ranging physical scenarios. This implies that our PhysMaster, which unifies solutions for various physical processes via representation learning in the reinforcement learning paradigm, can act as a generic and plug-in solution for physics-aware video generation and broader applications.

