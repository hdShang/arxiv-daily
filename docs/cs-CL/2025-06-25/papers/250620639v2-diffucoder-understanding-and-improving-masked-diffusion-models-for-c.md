---
layout: default
title: "DiffuCoder: Understanding and Improving Masked Diffusion Models for Code Generation"
---

# DiffuCoder: Understanding and Improving Masked Diffusion Models for Code Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20639" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20639v2</a>
  <a href="https://arxiv.org/pdf/2506.20639.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20639v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20639v2', 'DiffuCoder: Understanding and Improving Masked Diffusion Models for Code Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shansan Gong, Ruixiang Zhang, Huangjie Zheng, Jiatao Gu, Navdeep Jaitly, Lingpeng Kong, Yizhe Zhang

**分类**: cs.CL

**发布日期**: 2025-06-25 (更新: 2025-06-26)

**备注**: minor update

**🔗 代码/项目**: [GITHUB](https://github.com/apple/ml-diffucoder)

---

## 💡 一句话要点

**提出DiffuCoder以提升代码生成的去噪效率**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `扩散模型` `代码生成` `强化学习` `去噪过程` `模型训练` `自回归偏差` `采样方案`

## 📋 核心要点

1. 现有的自回归模型在代码生成中存在局限，未能充分利用全局规划和迭代优化的优势。
2. 本文提出DiffuCoder，通过系统研究dLLMs的去噪过程和强化学习方法，探索其在代码生成中的潜力。
3. 实验结果表明，DiffuCoder在EvalPlus基准上提升了4.4%的性能，并有效降低了自回归偏差的影响。

## 📝 摘要（中文）

扩散大型语言模型（dLLMs）作为自回归模型的有力替代品，其去噪模型在整个序列上操作，特别适合代码生成。然而，目前dLLMs在编码方面的训练和推理机制仍未得到充分探索。为了解释dLLMs的解码行为并释放其在编码中的潜力，本文系统研究了其去噪过程和强化学习（RL）方法。我们训练了一个7B参数的dLLM模型DiffuCoder，并在130B代码标记上进行实验，分析其解码行为，发现与自回归模型的不同之处。通过提出新颖的coupled-GRPO采样方案，显著提高了DiffuCoder在代码生成基准上的表现，并减少了对自回归偏差的依赖。

## 🔬 方法详解

**问题定义**：本文旨在解决当前自回归模型在代码生成中的局限性，尤其是在全局规划和迭代优化方面的不足。现有方法未能充分利用扩散模型的去噪特性。

**核心思路**：论文的核心思路是通过训练DiffuCoder，系统研究其去噪过程，并结合强化学习方法，提升代码生成的效率和质量。通过这种方式，dLLMs能够在生成过程中更灵活地选择因果关系。

**技术框架**：整体架构包括数据预处理、模型训练和推理三个主要阶段。首先，使用130B代码标记进行训练，然后分析模型的解码行为，最后通过coupled-GRPO进行强化学习训练。

**关键创新**：最重要的技术创新是提出了coupled-GRPO采样方案，该方案通过构建互补的掩码噪声来减少标记对数似然估计的方差，从而提高训练效率。与现有方法相比，DiffuCoder在解码时不再依赖自回归偏差。

**关键设计**：在模型设计中，DiffuCoder采用了7B参数的架构，并通过调整采样温度来增加生成的多样性。此外，coupled-GRPO的引入有效提升了模型在代码生成任务中的表现。具体的损失函数和网络结构细节在实验中进行了优化。

## 📊 实验亮点

在实验中，DiffuCoder在EvalPlus基准上取得了4.4%的性能提升，显著优于传统自回归模型。同时，coupled-GRPO采样方案有效降低了对自回归偏差的依赖，展示了扩散模型在代码生成中的优势。

## 🎯 应用场景

DiffuCoder的研究成果在多个领域具有潜在应用价值，尤其是在自动化代码生成、智能编程助手和软件开发工具中。通过提升代码生成的效率和质量，该模型能够帮助开发者更快速地完成编程任务，降低错误率，并提高生产力。未来，DiffuCoder可能会在更广泛的编程语言和复杂项目中得到应用，推动软件开发的智能化进程。

## 📄 摘要（原文）

> Diffusion large language models (dLLMs) are compelling alternatives to autoregressive (AR) models because their denoising models operate over the entire sequence. The global planning and iterative refinement features of dLLMs are particularly useful for code generation. However, current training and inference mechanisms for dLLMs in coding are still under-explored. To demystify the decoding behavior of dLLMs and unlock their potential for coding, we systematically investigate their denoising processes and reinforcement learning (RL) methods. We train a 7B dLLM, \textbf{DiffuCoder}, on 130B tokens of code. Using this model as a testbed, we analyze its decoding behavior, revealing how it differs from that of AR models: (1) dLLMs can decide how causal their generation should be without relying on semi-AR decoding, and (2) increasing the sampling temperature diversifies not only token choices but also their generation order. This diversity creates a rich search space for RL rollouts. For RL training, to reduce the variance of token log-likelihood estimates and maintain training efficiency, we propose \textbf{coupled-GRPO}, a novel sampling scheme that constructs complementary mask noise for completions used in training. In our experiments, coupled-GRPO significantly improves DiffuCoder's performance on code generation benchmarks (+4.4\% on EvalPlus) and reduces reliance on AR bias during decoding. Our work provides deeper insight into the machinery of dLLM generation and offers an effective, diffusion-native RL training framework. https://github.com/apple/ml-diffucoder.

