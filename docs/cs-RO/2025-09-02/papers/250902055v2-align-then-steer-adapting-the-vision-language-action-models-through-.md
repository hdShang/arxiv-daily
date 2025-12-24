---
layout: default
title: "Align-Then-stEer: Adapting the Vision-Language Action Models through Unified Latent Guidance"
---

# Align-Then-stEer: Adapting the Vision-Language Action Models through Unified Latent Guidance

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.02055" class="toolbar-btn" target="_blank">📄 arXiv: 2509.02055v2</a>
  <a href="https://arxiv.org/pdf/2509.02055.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.02055v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.02055v2', 'Align-Then-stEer: Adapting the Vision-Language Action Models through Unified Latent Guidance')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yang Zhang, Chenwei Wang, Ouyang Lu, Yuan Zhao, Yunfei Ge, Zhenglong Sun, Xiu Li, Chi Zhang, Chenjia Bai, Xuelong Li

**分类**: cs.RO, cs.AI

**发布日期**: 2025-09-02 (更新: 2025-09-05)

**备注**: The first three authors contributed equally

---

## 💡 一句话要点

**Align-Then-stEer框架通过统一潜在空间指导，实现VLA模型在机器人任务上的高效迁移。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言动作模型` `机器人操作` `迁移学习` `变分自编码器` `扩散模型` `动作空间对齐` `潜在空间` `模型引导`

## 📋 核心要点

1. 现有VLA模型在适应新机器人形态或任务时，面临动作分布不匹配的挑战，需要大量数据和计算资源进行微调。
2. ATE框架通过构建统一的潜在空间对齐动作空间，并利用引导机制在微调过程中将模型输出分布推向目标域。
3. 实验表明，ATE在模拟和真实环境中均显著提升了VLA模型在跨形态和跨任务操作中的成功率。

## 📝 摘要（中文）

本文提出了一种名为Align-Then-stEer（ATE）的全新、数据高效且即插即用的自适应框架，旨在解决视觉-语言-动作（VLA）模型在下游任务中的适应性问题，尤其是在机器人形态或任务与预训练数据存在差异时。ATE通过构建统一的潜在空间来对齐不同的动作空间，其中变分自编码器（VAE）受到反向KL散度的约束，将自适应动作嵌入到预训练动作潜在分布的模式中。随后，通过引导机制在微调期间控制基于扩散或流的VLA生成过程，将模型的输出分布推向目标域。在模拟和真实世界的跨形态和跨任务操作中进行了大量实验。与直接微调VLA模型相比，该方法在模拟中将平均多任务成功率提高了高达9.8％，并在真实世界的跨形态设置中实现了惊人的32％的成功率提升。该工作提出了一种通用且轻量级的解决方案，大大提高了将VLA模型部署到新的机器人平台和任务的实用性。

## 🔬 方法详解

**问题定义**：VLA模型在预训练数据与实际机器人任务存在差异时，动作空间不匹配，导致模型泛化能力下降，需要大量数据进行微调才能适应新的机器人形态或任务。现有方法通常采用直接微调，效率低下，且容易过拟合。

**核心思路**：论文的核心思路是解耦对齐（Align）和引导（Steer）两个过程。首先，通过统一的潜在空间对齐不同机器人形态或任务的动作空间，将它们映射到预训练动作的潜在分布中。然后，在微调过程中，利用引导机制，将模型的输出分布推向目标域，从而实现高效的迁移学习。

**技术框架**：ATE框架包含两个主要阶段：对齐阶段和引导阶段。在对齐阶段，使用变分自编码器（VAE）学习一个统一的潜在空间，将不同动作空间映射到该空间中。VAE的训练目标是最小化重构误差和反向KL散度，确保潜在空间能够捕捉到预训练动作的分布。在引导阶段，利用扩散模型或流模型生成动作，并使用引导机制将生成过程推向目标域。引导机制通过计算目标域的梯度，并将其添加到生成过程的噪声中，从而影响生成结果。

**关键创新**：ATE的关键创新在于将动作空间对齐和模型引导解耦，并使用统一的潜在空间作为桥梁。这种方法避免了直接微调带来的数据依赖性问题，提高了模型的泛化能力。此外，使用反向KL散度约束VAE的潜在空间，确保其能够捕捉到预训练动作的分布，从而提高了对齐的准确性。

**关键设计**：在对齐阶段，VAE的编码器和解码器采用多层感知机（MLP）结构。反向KL散度的权重是一个超参数，需要根据具体任务进行调整。在引导阶段，可以使用不同的扩散模型或流模型。引导强度也是一个超参数，需要根据具体任务进行调整。论文中使用了DDPM作为扩散模型，并使用Classifier-Free Guidance进行引导。

## 📊 实验亮点

实验结果表明，ATE框架在模拟和真实环境中均取得了显著的性能提升。在模拟环境中，ATE将平均多任务成功率提高了高达9.8％。在真实世界的跨形态设置中，ATE实现了惊人的32％的成功率提升。这些结果表明，ATE是一种有效且通用的VLA模型自适应方法。

## 🎯 应用场景

该研究成果可广泛应用于机器人操作领域，例如工业自动化、家庭服务机器人、医疗机器人等。通过ATE框架，可以快速将VLA模型部署到新的机器人平台和任务中，降低开发成本，提高机器人智能化水平。该方法还有潜力应用于其他视觉-语言任务，例如图像生成、文本编辑等。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models pre-trained on large, diverse datasets show remarkable potential for general-purpose robotic manipulation. However, a primary bottleneck remains in adapting these models to downstream tasks, especially when the robot's embodiment or the task itself differs from the pre-training data. This discrepancy leads to a significant mismatch in action distributions, demanding extensive data and compute for effective fine-tuning. To address this challenge, we introduce \textbf{Align-Then-stEer (\texttt{ATE})}, a novel, data-efficient, and plug-and-play adaptation framework. \texttt{ATE} first aligns disparate action spaces by constructing a unified latent space, where a variational autoencoder constrained by reverse KL divergence embeds adaptation actions into modes of the pre-training action latent distribution. Subsequently, it steers the diffusion- or flow-based VLA's generation process during fine-tuning via a guidance mechanism that pushes the model's output distribution towards the target domain. We conduct extensive experiments on cross-embodiment and cross-task manipulation in both simulation and real world. Compared to direct fine-tuning of representative VLAs, our method improves the average multi-task success rate by up to \textbf{9.8\%} in simulation and achieves a striking \textbf{32\% success rate gain} in a real-world cross-embodiment setting. Our work presents a general and lightweight solution that greatly enhances the practicality of deploying VLA models to new robotic platforms and tasks.

