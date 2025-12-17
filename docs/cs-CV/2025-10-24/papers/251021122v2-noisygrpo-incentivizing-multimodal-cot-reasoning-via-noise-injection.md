---
layout: default
title: NoisyGRPO: Incentivizing Multimodal CoT Reasoning via Noise Injection and Bayesian Estimation
---

# NoisyGRPO: Incentivizing Multimodal CoT Reasoning via Noise Injection and Bayesian Estimation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.21122" class="toolbar-btn" target="_blank">📄 arXiv: 2510.21122v2</a>
  <a href="https://arxiv.org/pdf/2510.21122.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.21122v2" onclick="toggleFavorite(this, '2510.21122v2', 'NoisyGRPO: Incentivizing Multimodal CoT Reasoning via Noise Injection and Bayesian Estimation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Longtian Qiu, Shan Ning, Jiaxuan Sun, Xuming He

**分类**: cs.CV

**发布日期**: 2025-10-24 (更新: 2025-10-29)

**备注**: Accepted by Neurips2025, Project page at at https://artanic30.github.io/project_pages/NoisyGRPO/

**🔗 代码/项目**: [PROJECT_PAGE](https://artanic30.github.io/project_pages/)

---

## 💡 一句话要点

**NoisyGRPO：通过噪声注入和贝叶斯估计激励多模态CoT推理**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `强化学习` `链式思考` `噪声注入` `贝叶斯估计` `视觉推理` `大语言模型`

## 📋 核心要点

1. 现有强化学习框架在提升多模态大语言模型的通用CoT推理能力时，泛化能力不足，难以超越训练分布。
2. NoisyGRPO通过向视觉输入注入噪声来鼓励更广泛的探索，并使用贝叶斯框架建模优势估计，提升泛化能力。
3. 实验表明，NoisyGRPO显著提高了泛化性和鲁棒性，尤其是在小规模MLLM上表现突出。

## 📝 摘要（中文）

本文提出了一种名为NoisyGRPO的多模态强化学习框架，旨在提升多模态大语言模型（MLLM）的通用Chain-of-Thought (CoT)推理能力。现有强化学习框架在提升通用CoT推理能力时，泛化能力往往受限于训练分布。NoisyGRPO通过向视觉输入中引入可控噪声来增强探索，并采用贝叶斯框架显式地建模优势估计过程。具体而言，NoisyGRPO通过噪声注入探索策略（使用高斯噪声扰动视觉输入，鼓励更广泛的视觉场景探索）和贝叶斯优势估计（将优势估计建模为贝叶斯推理问题，噪声水平作为先验，观测到的轨迹奖励作为似然）来改进强化学习训练。实验表明，NoisyGRPO显著提高了泛化性和鲁棒性，尤其是在Qwen2.5-VL 3B等小规模MLLM的强化学习设置中。

## 🔬 方法详解

**问题定义**：现有基于强化学习的多模态大语言模型（MLLM）的Chain-of-Thought (CoT)推理方法，在提升通用推理能力时，存在泛化性不足的问题。模型容易过拟合训练数据，难以适应新的、未知的视觉场景。现有方法对探索的鼓励不足，优势估计不够准确，导致模型难以学习到真正有效的推理策略。

**核心思路**：NoisyGRPO的核心思路是通过引入噪声来增强模型的探索能力，并使用贝叶斯方法来更准确地估计优势函数。通过向视觉输入添加噪声，模型可以接触到更多样化的视觉场景，从而提高泛化能力。贝叶斯优势估计则利用噪声水平作为先验信息，结合观测到的奖励，得到更鲁棒的优势函数估计。

**技术框架**：NoisyGRPO框架主要包含两个关键模块：噪声注入探索策略和贝叶斯优势估计。首先，噪声注入探索策略通过向视觉输入添加高斯噪声来扰动输入，鼓励模型探索更广泛的视觉场景。然后，贝叶斯优势估计模块将优势估计建模为一个贝叶斯推理问题，其中噪声水平作为先验，观测到的轨迹奖励作为似然。通过贝叶斯推理，可以得到一个更准确的优势函数估计，用于指导模型的策略学习。

**关键创新**：NoisyGRPO的关键创新在于将噪声注入和贝叶斯估计相结合，用于提升多模态CoT推理的泛化能力。与传统的强化学习方法相比，NoisyGRPO显式地建模了噪声对优势函数的影响，并利用贝叶斯方法进行推理，从而得到更鲁棒的优势函数估计。这种方法可以有效地提高模型在未知视觉场景下的推理能力。

**关键设计**：在噪声注入探索策略中，高斯噪声的方差是一个重要的超参数，需要根据具体任务进行调整。在贝叶斯优势估计中，先验分布的选择也会影响最终的估计结果。论文中可能使用了特定的损失函数来优化模型的策略，例如，可以使用策略梯度算法来更新模型的参数。具体的网络结构细节（例如，MLLM的具体架构）可能因不同的实验设置而异。

## 📊 实验亮点

NoisyGRPO在标准CoT质量、通用能力和幻觉基准测试中表现出色，证明了其在泛化性和鲁棒性方面的显著提升。尤其是在小规模MLLM（如Qwen2.5-VL 3B）上，NoisyGRPO的优势更为明显。具体的性能数据和提升幅度需要在论文中查找，但总体而言，NoisyGRPO为多模态CoT推理提供了一种有效的解决方案。

## 🎯 应用场景

NoisyGRPO具有广泛的应用前景，可用于提升各种多模态大语言模型的推理能力，例如视觉问答、图像描述、机器人导航等。该方法可以提高模型在复杂、未知的环境中的适应性和鲁棒性，使其能够更好地理解和处理真实世界的视觉信息。此外，NoisyGRPO的思路也可以推广到其他强化学习任务中，用于提高模型的探索能力和泛化能力。

## 📄 摘要（原文）

> Reinforcement learning (RL) has shown promise in enhancing the general Chain-of-Thought (CoT) reasoning capabilities of multimodal large language models (MLLMs). However, when applied to improve general CoT reasoning, existing RL frameworks often struggle to generalize beyond the training distribution. To address this, we propose NoisyGRPO, a systematic multimodal RL framework that introduces controllable noise into visual inputs for enhanced exploration and explicitly models the advantage estimation process via a Bayesian framework. Specifically, NoisyGRPO improves RL training by: (1) Noise-Injected Exploration Policy: Perturbing visual inputs with Gaussian noise to encourage exploration across a wider range of visual scenarios; and (2) Bayesian Advantage Estimation: Formulating advantage estimation as a principled Bayesian inference problem, where the injected noise level serves as a prior and the observed trajectory reward as the likelihood. This Bayesian modeling fuses both sources of information to compute a robust posterior estimate of trajectory advantage, effectively guiding MLLMs to prefer visually grounded trajectories over noisy ones. Experiments on standard CoT quality, general capability, and hallucination benchmarks demonstrate that NoisyGRPO substantially improves generalization and robustness, especially in RL settings with small-scale MLLMs such as Qwen2.5-VL 3B. The project page is available at https://artanic30.github.io/project_pages/NoisyGRPO/.

