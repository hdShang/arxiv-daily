---
layout: default
title: Comet: Accelerating Private Inference for Large Language Model by Predicting Activation Sparsity
---

# Comet: Accelerating Private Inference for Large Language Model by Predicting Activation Sparsity

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07239" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07239v1</a>
  <a href="https://arxiv.org/pdf/2505.07239.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07239v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07239v1', 'Comet: Accelerating Private Inference for Large Language Model by Predicting Activation Sparsity')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guang Yan, Yuhui Zhang, Zimu Guo, Lutan Zhao, Xiaojun Chen, Chen Wang, Wenhao Wang, Dan Meng, Rui Hou

**分类**: cs.CR, cs.AI

**发布日期**: 2025-05-12

**备注**: Accepted to SP 2025

**DOI**: [10.1109/SP61157.2025.00182](https://doi.org/10.1109/SP61157.2025.00182)

---

## 💡 一句话要点

**提出Comet以加速大语言模型的私密推理**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱八：物理动画 (Physics-based Animation)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `私密推理` `安全多方计算` `激活稀疏性` `性能优化` `云计算` `隐私保护`

## 📋 核心要点

1. 现有的安全多方计算方法在LLM推理中存在频繁通信导致的性能开销问题。
2. Comet通过预测激活函数输出的稀疏分布，设计了一种新的私密推理协议，避免不必要的计算。
3. 实验结果表明，Comet在速度和通信效率上均显著优于现有的私密推理系统，提升幅度可达2.63倍和2.64倍。

## 📝 摘要（中文）

随着大型语言模型（LLMs）在云平台上提供推理服务的日益普及，关于敏感信息泄露的隐私担忧也在加剧。安全多方计算（MPC）是一种保护LLM推理隐私的有前景的解决方案，但其频繁的服务器间通信导致了高性能开销。针对LLMs中普遍存在的激活稀疏性，我们提出了一种高效的私密推理系统Comet。该系统使用准确快速的预测器来预测激活函数输出的稀疏分布，并引入了一种新的私密推理协议，通过利用预测的稀疏分布的空间局部性，安全高效地避免涉及零值的计算。我们在四个常见的LLMs上评估了Comet，并与六个最先进的私密推理系统进行了比较，结果显示Comet实现了1.87x-2.63x的速度提升和1.94x-2.64x的通信减少。

## 🔬 方法详解

**问题定义**：本论文旨在解决在大型语言模型推理中，安全多方计算因频繁的服务器间通信而导致的性能开销问题。现有方法在保护隐私的同时，未能有效降低计算和通信成本。

**核心思路**：论文提出的Comet系统通过预测激活函数输出的稀疏分布，利用这一特性来避免涉及零值的计算，从而提高推理效率。该设计旨在减少不必要的计算负担，同时确保隐私保护。

**技术框架**：Comet的整体架构包括一个快速准确的稀疏预测器和一个新的私密推理协议。系统首先通过预测器获取激活稀疏性分布，然后根据该分布优化计算流程，减少通信和计算开销。

**关键创新**：Comet的主要创新在于其稀疏预测机制和计算避免策略，利用空间局部性来高效处理稀疏激活，显著降低了计算复杂度，与传统MPC方法相比具有本质区别。

**关键设计**：在设计中，Comet采用了低通信开销的缓存补充策略，合并缺失请求并引入预取机制，以应对稀疏性对KV缓存条目的时空连续性影响。

## 📊 实验亮点

Comet在四个常见的LLMs上进行评估，结果显示其在速度上实现了1.87x至2.63x的提升，同时在通信效率上减少了1.94x至2.64x，相较于六个最先进的私密推理系统表现出显著的优势。

## 🎯 应用场景

Comet系统的潜在应用领域包括云计算环境中的私密推理服务，尤其是在处理敏感数据时，如医疗、金融等领域。通过提高推理速度和降低通信成本，Comet能够为企业提供更高效的隐私保护解决方案，推动大语言模型的广泛应用。

## 📄 摘要（原文）

> With the growing use of large language models (LLMs) hosted on cloud platforms to offer inference services, privacy concerns about the potential leakage of sensitive information are escalating. Secure multi-party computation (MPC) is a promising solution to protect the privacy in LLM inference. However, MPC requires frequent inter-server communication, causing high performance overhead.
>   Inspired by the prevalent activation sparsity of LLMs, where most neuron are not activated after non-linear activation functions, we propose an efficient private inference system, Comet. This system employs an accurate and fast predictor to predict the sparsity distribution of activation function output. Additionally, we introduce a new private inference protocol. It efficiently and securely avoids computations involving zero values by exploiting the spatial locality of the predicted sparse distribution. While this computation-avoidance approach impacts the spatiotemporal continuity of KV cache entries, we address this challenge with a low-communication overhead cache refilling strategy that merges miss requests and incorporates a prefetching mechanism. Finally, we evaluate Comet on four common LLMs and compare it with six state-of-the-art private inference systems. Comet achieves a 1.87x-2.63x speedup and a 1.94x-2.64x communication reduction.

