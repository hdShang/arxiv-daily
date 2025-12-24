---
layout: default
title: "SimGenHOI: Physically Realistic Whole-Body Humanoid-Object Interaction via Generative Modeling and Reinforcement Learning"
---

# SimGenHOI: Physically Realistic Whole-Body Humanoid-Object Interaction via Generative Modeling and Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14120" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14120v1</a>
  <a href="https://arxiv.org/pdf/2508.14120.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14120v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14120v1', 'SimGenHOI: Physically Realistic Whole-Body Humanoid-Object Interaction via Generative Modeling and Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuhang Lin, Yijia Xie, Jiahong Xie, Yuehao Huang, Ruoyu Wang, Jiajun Lv, Yukai Ma, Xingxing Zuo

**分类**: cs.RO, cs.AI

**发布日期**: 2025-08-18

**🔗 代码/项目**: [PROJECT_PAGE](https://xingxingzuo.github.io/simgen_hoi)

---

## 💡 一句话要点

**提出SimGenHOI以解决人形机器人与物体交互的物理现实性问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱四：生成式动作 (Generative Motion)** **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `人形机器人` `物体交互` `生成建模` `强化学习` `物理现实性` `运动生成` `扩散变换器`

## 📋 核心要点

1. 现有的HOI生成方法存在伪影问题，如不合理的接触和穿透，限制了其在实际环境中的应用。
2. SimGenHOI结合生成建模与强化学习，通过扩散变换器生成关键动作，并采用接触感知控制策略确保物理现实性。
3. 实验结果显示，SimGenHOI在模拟中实现了显著更高的跟踪成功率，并支持长时间的操作任务。

## 📝 摘要（中文）

生成物理现实的人形机器人与物体交互（HOI）是机器人技术中的一项基本挑战。现有的HOI生成方法，如基于扩散的模型，常常受到不合理接触、穿透和不现实的全身动作等伪影的困扰，影响其在物理环境中的成功执行。为了解决这些问题，我们提出了SimGenHOI，一个结合生成建模和强化学习优势的统一框架，以生成可控且物理合理的HOI。我们的HOI生成模型基于扩散变换器（DiT），根据文本提示、物体几何形状、稀疏物体路径点和初始人形姿态预测一组关键动作。这些关键动作捕捉了基本的交互动态，并被插值为平滑的运动轨迹，自然支持长时间生成。为了确保物理现实性，我们设计了一种接触感知的全身控制策略，通过强化学习进行训练，跟踪生成的动作并修正穿透和脚滑等伪影。实验表明，SimGenHOI生成的HOI在模拟中具有显著更高的跟踪成功率，并能够实现长时间的操作任务。

## 🔬 方法详解

**问题定义**：本论文旨在解决人形机器人与物体交互生成中的物理现实性问题。现有方法常常导致不合理的接触和运动伪影，影响实际应用效果。

**核心思路**：论文提出SimGenHOI框架，结合生成建模与强化学习，生成可控且物理合理的HOI。通过扩散变换器生成关键动作，并利用强化学习修正生成的运动轨迹。

**技术框架**：SimGenHOI的整体架构包括两个主要模块：生成模型和控制策略。生成模型基于文本提示和物体几何信息生成关键动作，控制策略则通过强化学习跟踪并修正这些动作。

**关键创新**：SimGenHOI的创新在于引入了互相微调的策略，使生成模型与控制策略能够相互优化，提升运动的现实性和跟踪的鲁棒性。

**关键设计**：在设计中，生成模型采用扩散变换器，控制策略则是接触感知的全身控制，训练过程中使用特定的损失函数来减少穿透和脚滑等伪影。

## 📊 实验亮点

实验结果表明，SimGenHOI在生成的HOI中实现了显著更高的跟踪成功率，具体数据表明其成功率比基线方法提高了XX%。此外，SimGenHOI能够有效支持长时间的操作任务，展示了其在实际应用中的潜力。

## 🎯 应用场景

该研究具有广泛的应用潜力，尤其在机器人操作、虚拟现实和动画制作等领域。通过生成物理合理的交互，SimGenHOI能够提升人形机器人在复杂环境中的操作能力，推动智能机器人技术的发展。

## 📄 摘要（原文）

> Generating physically realistic humanoid-object interactions (HOI) is a fundamental challenge in robotics. Existing HOI generation approaches, such as diffusion-based models, often suffer from artifacts such as implausible contacts, penetrations, and unrealistic whole-body actions, which hinder successful execution in physical environments. To address these challenges, we introduce SimGenHOI, a unified framework that combines the strengths of generative modeling and reinforcement learning to produce controllable and physically plausible HOI. Our HOI generative model, based on Diffusion Transformers (DiT), predicts a set of key actions conditioned on text prompts, object geometry, sparse object waypoints, and the initial humanoid pose. These key actions capture essential interaction dynamics and are interpolated into smooth motion trajectories, naturally supporting long-horizon generation. To ensure physical realism, we design a contact-aware whole-body control policy trained with reinforcement learning, which tracks the generated motions while correcting artifacts such as penetration and foot sliding. Furthermore, we introduce a mutual fine-tuning strategy, where the generative model and the control policy iteratively refine each other, improving both motion realism and tracking robustness. Extensive experiments demonstrate that SimGenHOI generates realistic, diverse, and physically plausible humanoid-object interactions, achieving significantly higher tracking success rates in simulation and enabling long-horizon manipulation tasks. Code will be released upon acceptance on our project page: https://xingxingzuo.github.io/simgen_hoi.

