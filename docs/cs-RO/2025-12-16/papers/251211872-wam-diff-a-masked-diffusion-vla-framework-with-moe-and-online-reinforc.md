---
layout: default
title: WAM-Diff: A Masked Diffusion VLA Framework with MoE and Online Reinforcement Learning for Autonomous Driving
---

# WAM-Diff: A Masked Diffusion VLA Framework with MoE and Online Reinforcement Learning for Autonomous Driving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.11872" class="toolbar-btn" target="_blank">📄 arXiv: 2512.11872</a>
  <a href="https://arxiv.org/pdf/2512.11872.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.11872" onclick="toggleFavorite(this, '2512.11872', 'WAM-Diff: A Masked Diffusion VLA Framework with MoE and Online Reinforcement Learning for Autonomous Driving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mingwang Xu, Jiahao Cui, Feipeng Cai, Hanlin Shang, Zhihao Zhu, Shan Luan, Yifang Xu, Neng Zhang, Yaoyi Li, Jia Cai, Siyu Zhu

**分类**: cs.RO, cs.AI, cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出WAM-Diff，一种基于Masked Diffusion和MoE的VLA自动驾驶框架。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动驾驶` `Masked Diffusion` `视觉语言动作模型` `轨迹生成` `在线强化学习` `MoE` `端到端学习`

## 📋 核心要点

1. 现有基于自回归LLM和连续扩散策略的端到端自动驾驶系统，缺乏对离散Masked Diffusion在轨迹生成方面的探索。
2. WAM-Diff框架采用Masked Diffusion迭代优化离散轨迹序列，并结合MoE扩展模型容量，使用在线强化学习优化驾驶奖励。
3. 实验结果表明，WAM-Diff在NAVSIM-v1和NAVSIM-v2上取得了显著的性能，验证了Masked Diffusion在自动驾驶中的有效性。

## 📝 摘要（中文）

本文提出WAM-Diff，一个基于视觉-语言-动作(VLA)模型的端到端自动驾驶框架，该框架利用Masked Diffusion迭代地优化离散序列，该序列代表未来的车辆轨迹。该方法包含三个关键创新：系统性地调整Masked Diffusion以适应自动驾驶，支持灵活的非因果解码顺序；通过稀疏MoE架构扩展模型容量，并在运动预测和面向驾驶的视觉问答(VQA)上联合训练；使用群体序列策略优化(GSPO)进行在线强化学习，以优化序列级别的驾驶奖励。该模型在NAVSIM-v1上达到91.0 PDMS，在NAVSIM-v2上达到89.7 EPDMS，证明了Masked Diffusion在自动驾驶中的有效性。该方法为自动驾驶轨迹生成提供了一种有前景的替代方案，支持场景感知的解码策略。

## 🔬 方法详解

**问题定义**：现有端到端自动驾驶系统主要依赖自回归大型语言模型或连续扩散策略生成轨迹，但对离散Masked Diffusion在轨迹生成方面的潜力挖掘不足。如何有效地利用Masked Diffusion生成高质量的自动驾驶轨迹，并克服其在序列生成任务中的挑战，是本文要解决的关键问题。

**核心思路**：本文的核心思路是将自动驾驶轨迹生成问题建模为离散序列的Masked Diffusion过程。通过迭代地掩码和预测轨迹序列中的元素，模型能够学习到轨迹之间的依赖关系，并生成符合驾驶规则和场景约束的轨迹。同时，利用MoE架构扩展模型容量，并结合在线强化学习优化策略，进一步提升轨迹生成的质量和安全性。

**技术框架**：WAM-Diff框架主要包含三个核心模块：1) Masked Diffusion模块，负责迭代地掩码和预测离散轨迹序列；2) MoE模块，用于扩展模型容量，提升模型对复杂场景的理解能力；3) 在线强化学习模块，使用GSPO算法优化策略，提升驾驶奖励。整体流程为：首先，模型接收视觉和语言输入，然后通过Masked Diffusion模块生成初始轨迹序列，接着利用MoE模块进行特征提取和融合，最后通过在线强化学习模块优化策略，生成最终的驾驶轨迹。

**关键创新**：本文最重要的技术创新在于将Masked Diffusion成功应用于自动驾驶轨迹生成任务。与传统的自回归模型相比，Masked Diffusion支持非因果的解码顺序，能够更灵活地处理轨迹序列中的依赖关系。此外，结合MoE和在线强化学习，进一步提升了模型的性能和安全性。

**关键设计**：在Masked Diffusion模块中，采用了离散的轨迹表示，并将轨迹生成问题建模为离散序列的预测问题。MoE模块采用了稀疏激活机制，以降低计算复杂度。在线强化学习模块使用了GSPO算法，以优化序列级别的驾驶奖励。具体的损失函数包括运动预测损失、视觉问答损失和强化学习奖励。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.11872/figures/teaser.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.11872/figures/main_arch.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.11872/figures/scheduler.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

WAM-Diff在NAVSIM-v1上取得了91.0 PDMS的性能，在NAVSIM-v2上取得了89.7 EPDMS的性能。这些结果表明，Masked Diffusion在自动驾驶轨迹生成方面具有显著的优势。与现有的自回归模型和连续扩散模型相比，WAM-Diff能够生成更安全、更高效的驾驶轨迹。

## 🎯 应用场景

该研究成果可应用于各种自动驾驶场景，例如城市道路、高速公路和停车场等。通过结合视觉、语言和动作信息，WAM-Diff能够生成安全、高效的驾驶轨迹，提升自动驾驶系统的智能化水平。未来，该技术有望应用于无人配送、自动泊车等领域，并促进智能交通的发展。

## 📄 摘要（原文）

> End-to-end autonomous driving systems based on vision-language-action (VLA) models integrate multimodal sensor inputs and language instructions to generate planning and control signals. While autoregressive large language models and continuous diffusion policies are prevalent, the potential of discrete masked diffusion for trajectory generation remains largely unexplored. This paper presents WAM-Diff, a VLA framework that employs masked diffusion to iteratively refine a discrete sequence representing future ego-trajectories. Our approach features three key innovations: a systematic adaptation of masked diffusion for autonomous driving that supports flexible, non-causal decoding orders; scalable model capacity via a sparse MoE architecture trained jointly on motion prediction and driving-oriented visual question answering (VQA); and online reinforcement learning using Group Sequence Policy Optimization (GSPO) to optimize sequence-level driving rewards. Remarkably, our model achieves 91.0 PDMS on NAVSIM-v1 and 89.7 EPDMS on NAVSIM-v2, demonstrating the effectiveness of masked diffusion for autonomous driving. The approach provides a promising alternative to autoregressive and diffusion-based policies, supporting scenario-aware decoding strategies for trajectory generation. The code for this paper will be released publicly at:this https URL

