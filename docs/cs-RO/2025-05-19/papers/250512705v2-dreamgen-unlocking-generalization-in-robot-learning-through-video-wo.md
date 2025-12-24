---
layout: default
title: DreamGen: Unlocking Generalization in Robot Learning through Video World Models
---

# DreamGen: Unlocking Generalization in Robot Learning through Video World Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.12705" class="toolbar-btn" target="_blank">📄 arXiv: 2505.12705v2</a>
  <a href="https://arxiv.org/pdf/2505.12705.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.12705v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.12705v2', 'DreamGen: Unlocking Generalization in Robot Learning through Video World Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Joel Jang, Seonghyeon Ye, Zongyu Lin, Jiannan Xiang, Johan Bjorck, Yu Fang, Fengyuan Hu, Spencer Huang, Kaushil Kundalia, Yen-Chen Lin, Loic Magne, Ajay Mandlekar, Avnish Narayan, You Liang Tan, Guanzhi Wang, Jing Wang, Qi Wang, Yinzhen Xu, Xiaohui Zeng, Kaiyuan Zheng, Ruijie Zheng, Ming-Yu Liu, Luke Zettlemoyer, Dieter Fox, Jan Kautz, Scott Reed, Yuke Zhu, Linxi Fan

**分类**: cs.RO, cs.AI, cs.LG

**发布日期**: 2025-05-19 (更新: 2025-06-17)

**备注**: See website for videos: https://research.nvidia.com/labs/gear/dreamgen

**🔗 代码/项目**: [GITHUB](https://github.com/NVIDIA/GR00T-Dreams)

---

## 💡 一句话要点

**提出DreamGen以解决机器人学习中的泛化问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `机器人学习` `视频生成` `环境泛化` `合成数据` `深度学习`

## 📋 核心要点

1. 现有的机器人学习方法在不同环境和行为之间的泛化能力不足，通常依赖大量的手动数据收集。
2. 论文提出的DreamGen通过视频世界模型生成合成机器人数据，利用图像到视频生成模型来提高泛化能力。
3. 实验结果表明，DreamGen使得人形机器人能够在多种环境中执行22种新行为，且仅需少量的遥操作数据。

## 📝 摘要（中文）

我们介绍了DreamGen，一个简单而高效的四阶段管道，用于训练能够在不同行为和环境中泛化的机器人策略。DreamGen利用最先进的图像到视频生成模型，适应目标机器人形态，生成在多样环境中熟悉或新任务的逼真合成视频。通过使用潜在动作模型或逆动力学模型恢复伪动作序列，尽管方法简单，DreamGen实现了强大的行为和环境泛化：一个人形机器人能够在已见和未见环境中执行22种新行为，仅需一个环境中的单一抓取和放置任务的遥操作数据。我们还引入了DreamGen Bench，一个视频生成基准，显示基准性能与下游策略成功之间的强相关性。我们的工作为机器人学习的扩展提供了一个新的方向，超越了手动数据收集的限制。

## 🔬 方法详解

**问题定义**：本论文旨在解决机器人学习中泛化能力不足的问题，现有方法通常需要大量的手动数据收集，限制了其在新环境和新任务中的应用。

**核心思路**：DreamGen通过生成合成视频数据来训练机器人策略，利用视频世界模型生成的合成数据来提高机器人在不同环境中的泛化能力。

**技术框架**：DreamGen包含四个主要阶段：首先，使用图像到视频生成模型生成合成视频；其次，通过潜在动作模型或逆动力学模型恢复伪动作序列；然后，利用这些数据训练机器人策略；最后，评估策略在新环境中的表现。

**关键创新**：DreamGen的核心创新在于将视频生成模型与机器人学习相结合，显著减少了对手动数据的依赖，并实现了在多种环境中强大的行为泛化能力。

**关键设计**：在设计中，采用了先进的图像到视频生成模型，并通过潜在动作模型和逆动力学模型来恢复动作序列，确保生成数据的有效性和多样性。

## 📊 实验亮点

实验结果显示，使用DreamGen训练的人形机器人能够在已见和未见的环境中成功执行22种新行为，且仅需一个环境中的单一抓取和放置任务的遥操作数据。这表明DreamGen在行为和环境泛化方面的显著提升，展示了其在机器人学习中的实际应用潜力。

## 🎯 应用场景

该研究的潜在应用领域包括服务机器人、工业自动化和自主驾驶等。通过提高机器人在不同环境中的泛化能力，DreamGen可以显著降低数据收集成本，加速机器人在实际应用中的部署和适应能力，推动智能机器人技术的进步。

## 📄 摘要（原文）

> We introduce DreamGen, a simple yet highly effective 4-stage pipeline for training robot policies that generalize across behaviors and environments through neural trajectories - synthetic robot data generated from video world models. DreamGen leverages state-of-the-art image-to-video generative models, adapting them to the target robot embodiment to produce photorealistic synthetic videos of familiar or novel tasks in diverse environments. Since these models generate only videos, we recover pseudo-action sequences using either a latent action model or an inverse-dynamics model (IDM). Despite its simplicity, DreamGen unlocks strong behavior and environment generalization: a humanoid robot can perform 22 new behaviors in both seen and unseen environments, while requiring teleoperation data from only a single pick-and-place task in one environment. To evaluate the pipeline systematically, we introduce DreamGen Bench, a video generation benchmark that shows a strong correlation between benchmark performance and downstream policy success. Our work establishes a promising new axis for scaling robot learning well beyond manual data collection. Code available at https://github.com/NVIDIA/GR00T-Dreams.

