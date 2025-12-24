---
layout: default
title: "Beyond Human Demonstrations: Diffusion-Based Reinforcement Learning to Generate Data for VLA Training"
---

# Beyond Human Demonstrations: Diffusion-Based Reinforcement Learning to Generate Data for VLA Training

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.19752" class="toolbar-btn" target="_blank">📄 arXiv: 2509.19752v2</a>
  <a href="https://arxiv.org/pdf/2509.19752.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.19752v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.19752v2', 'Beyond Human Demonstrations: Diffusion-Based Reinforcement Learning to Generate Data for VLA Training')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rushuai Yang, Hangxing Wei, Ran Zhang, Zhiyuan Feng, Xiaoyu Chen, Tong Li, Chuheng Zhang, Li Zhao, Jiang Bian, Xiu Su, Yi Chen

**分类**: cs.RO

**发布日期**: 2025-09-24 (更新: 2025-09-29)

---

## 💡 一句话要点

**提出基于扩散模型的强化学习方法，为VLA模型生成高质量训练数据。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `扩散模型` `强化学习` `视觉-语言-动作模型` `机器人操作` `长程任务`

## 📋 核心要点

1. VLA模型依赖大量人工标注数据，成本高昂且限制了模型扩展性，因此需要寻找自动生成高质量训练数据的方法。
2. 论文提出一种改进的扩散策略优化算法，利用扩散模型生成高质量、低方差的轨迹，用于VLA模型的训练。
3. 实验表明，该方法生成的轨迹比人工数据和传统RL方法更平滑，VLA模型在生成数据上训练后性能提升显著。

## 📝 摘要（中文）

视觉-语言-动作(VLA)模型在跨任务和跨具身智能方面表现出强大的泛化能力。然而，它们对大规模人工演示数据的依赖限制了其可扩展性，因为手动数据收集成本高昂。强化学习(RL)为自主生成演示数据提供了一种潜在的替代方案，但传统的RL算法通常难以应对具有稀疏奖励的长程操作任务。本文提出了一种改进的扩散策略优化算法，以生成高质量和低方差的轨迹，从而构建一个基于扩散RL的VLA训练流程。该算法不仅受益于扩散模型在探索复杂和多样化行为方面的高表达性，还受益于迭代去噪过程的隐式正则化，从而产生平滑和一致的演示。我们在包含130个长程操作任务的LIBERO基准上评估了我们的方法，结果表明，生成的轨迹比人工演示和标准高斯RL策略生成的轨迹更平滑和一致。此外，仅在扩散RL生成的数据上训练VLA模型，平均成功率达到81.9%，比在人工数据上训练的模型高+5.3%，比在高斯RL生成的数据上训练的模型高+12.6%。结果表明，我们的扩散RL是为VLA模型生成丰富、高质量和低方差演示数据的有效替代方案。

## 🔬 方法详解

**问题定义**：VLA模型依赖于大量人工标注的演示数据，这限制了其可扩展性。传统的强化学习方法在长程操作任务中，由于稀疏奖励和探索困难，难以生成高质量的训练数据。因此，需要一种能够自动生成高质量、低方差轨迹的方法，以替代人工标注数据。

**核心思路**：利用扩散模型的强大生成能力和隐式正则化特性，生成高质量的轨迹。通过改进扩散策略优化算法，使得生成的轨迹更加平滑和一致，从而提高VLA模型的训练效果。核心在于将强化学习与扩散模型相结合，克服传统RL在长程任务中的挑战。

**技术框架**：该方法构建了一个基于扩散RL的VLA训练流程。首先，使用改进的扩散策略优化算法生成轨迹数据。然后，使用这些生成的数据训练VLA模型。整个流程包括以下几个主要阶段：1) 扩散策略优化算法生成轨迹；2) VLA模型使用生成轨迹进行训练；3) 在LIBERO基准上评估VLA模型的性能。

**关键创新**：关键创新在于将扩散模型引入强化学习，用于生成VLA模型的训练数据。与传统的高斯RL策略相比，扩散模型具有更高的表达能力，能够探索更复杂和多样化的行为。此外，扩散模型的迭代去噪过程具有隐式正则化作用，可以生成更平滑和一致的轨迹。这使得生成的数据更适合VLA模型的训练。

**关键设计**：论文修改了扩散策略优化算法，使其更适合生成高质量的轨迹。具体的参数设置和损失函数细节未在摘要中详细说明，但强调了利用扩散模型的特性来生成平滑和一致的轨迹。LIBERO基准包含130个长程操作任务，用于评估生成轨迹的质量和VLA模型的性能。

## 📊 实验亮点

实验结果表明，该方法生成的轨迹比人工数据和高斯RL策略生成的轨迹更平滑和一致。仅使用扩散RL生成的数据训练VLA模型，平均成功率达到81.9%，比在人工数据上训练的模型高+5.3%，比在高斯RL生成的数据上训练的模型高+12.6%。这些结果验证了该方法在生成高质量VLA模型训练数据方面的有效性。

## 🎯 应用场景

该研究成果可应用于机器人操作、自动驾驶等领域，通过自动生成高质量的训练数据，降低对人工标注数据的依赖，加速VLA模型的开发和部署。尤其在复杂、长程任务中，该方法具有显著优势，有望推动机器人智能水平的提升。

## 📄 摘要（原文）

> Vision-language-action (VLA) models have shown strong generalization across tasks and embodiments; however, their reliance on large-scale human demonstrations limits their scalability owing to the cost and effort of manual data collection. Reinforcement learning (RL) offers a potential alternative to generate demonstrations autonomously, yet conventional RL algorithms often struggle on long-horizon manipulation tasks with sparse rewards. In this paper, we propose a modified diffusion policy optimization algorithm to generate high-quality and low-variance trajectories, which contributes to a diffusion RL-powered VLA training pipeline. Our algorithm benefits from not only the high expressiveness of diffusion models to explore complex and diverse behaviors but also the implicit regularization of the iterative denoising process to yield smooth and consistent demonstrations. We evaluate our approach on the LIBERO benchmark, which includes 130 long-horizon manipulation tasks, and show that the generated trajectories are smoother and more consistent than both human demonstrations and those from standard Gaussian RL policies. Further, training a VLA model exclusively on the diffusion RL-generated data achieves an average success rate of 81.9%, which outperforms the model trained on human data by +5.3% and that on Gaussian RL-generated data by +12.6%. The results highlight our diffusion RL as an effective alternative for generating abundant, high-quality, and low-variance demonstrations for VLA models.

