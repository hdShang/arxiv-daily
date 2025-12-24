---
layout: default
title: "DETONATE: A Benchmark for Text-to-Image Alignment and Kernelized Direct Preference Optimization"
---

# DETONATE: A Benchmark for Text-to-Image Alignment and Kernelized Direct Preference Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14903" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14903v1</a>
  <a href="https://arxiv.org/pdf/2506.14903.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14903v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14903v1', 'DETONATE: A Benchmark for Text-to-Image Alignment and Kernelized Direct Preference Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Renjith Prasad, Abhilekh Borah, Hasnat Md Abdullah, Chathurangi Shyalika, Gurpreet Singh, Ritvik Garimella, Rajarshi Roy, Harshul Surana, Nasrin Imanpour, Suranjana Trivedy, Amit Sheth, Amitava Das

**分类**: cs.CV

**发布日期**: 2025-06-17

**备注**: 59 pages, 10 figures

---

## 💡 一句话要点

**提出DETONATE基准以优化文本到图像模型的对齐问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本到图像` `对齐优化` `社会偏见` `深度学习` `生成模型`

## 📋 核心要点

1. 现有的文本到图像模型在对齐用户意图与生成图像之间存在挑战，尤其是在安全性和公平性方面。
2. 论文提出DPO-Kernels，通过混合损失、核化表示和发散选择三方面增强T2I模型的对齐能力。
3. 实验结果表明，DPO-Kernels在泛化能力上表现优异，且通过AQI揭示了潜在的安全隐患。

## 📝 摘要（中文）

对齐是文本到图像（T2I）模型的关键，确保生成的图像忠实捕捉用户意图，同时维护安全性和公平性。本文引入了DPO-Kernels，增强了T2I模型的对齐能力，主要通过三方面的创新：混合损失、核化表示和发散选择。DETONATE是首个大规模基准，包含约10万对经过策划的图像对，涵盖种族、性别和残疾等社会偏见。我们还提出了对齐质量指数（AQI），量化安全/不安全图像激活的潜在空间可分离性。实验证明，DPO-Kernels通过重尾自我正则化（HT-SR）保持强大的泛化界限。DETONATE及完整代码已公开发布。

## 🔬 方法详解

**问题定义**：本文旨在解决文本到图像模型在生成图像时对用户意图的对齐问题，现有方法在安全性和公平性方面存在不足。

**核心思路**：提出DPO-Kernels，通过引入混合损失、核化表示和多种发散选择，提升模型的对齐能力和稳定性。

**技术框架**：整体架构包括三个主要模块：混合损失模块、核化表示模块和发散选择模块，分别负责优化目标、特征转换和正则化选择。

**关键创新**：DPO-Kernels是对DPO的扩展，结合了多种损失函数和核函数，显著提升了模型在对齐任务中的表现。

**关键设计**：采用了混合损失函数，结合了基于嵌入的目标与传统概率损失；使用RBF、Polynomial和Wavelet核进行特征转换；引入Wasserstein和R'enyi发散以增强稳定性。

## 📊 实验亮点

实验结果显示，DPO-Kernels在对齐任务中显著优于传统方法，泛化能力强，且AQI指标揭示了潜在的安全隐患，提供了新的评估视角。具体性能数据和对比基线未详细披露，待进一步研究验证。

## 🎯 应用场景

该研究的潜在应用领域包括生成艺术、广告设计和社交媒体内容生成等。通过优化文本到图像模型的对齐能力，可以更好地满足用户需求，减少生成内容中的偏见和不安全因素，提升用户体验和社会责任感。

## 📄 摘要（原文）

> Alignment is crucial for text-to-image (T2I) models to ensure that generated images faithfully capture user intent while maintaining safety and fairness. Direct Preference Optimization (DPO), prominent in large language models (LLMs), is extending its influence to T2I systems. This paper introduces DPO-Kernels for T2I models, a novel extension enhancing alignment across three dimensions: (i) Hybrid Loss, integrating embedding-based objectives with traditional probability-based loss for improved optimization; (ii) Kernelized Representations, employing Radial Basis Function (RBF), Polynomial, and Wavelet kernels for richer feature transformations and better separation between safe and unsafe inputs; and (iii) Divergence Selection, expanding beyond DPO's default Kullback-Leibler (KL) regularizer by incorporating Wasserstein and R'enyi divergences for enhanced stability and robustness. We introduce DETONATE, the first large-scale benchmark of its kind, comprising approximately 100K curated image pairs categorized as chosen and rejected. DETONATE encapsulates three axes of social bias and discrimination: Race, Gender, and Disability. Prompts are sourced from hate speech datasets, with images generated by leading T2I models including Stable Diffusion 3.5 Large, Stable Diffusion XL, and Midjourney. Additionally, we propose the Alignment Quality Index (AQI), a novel geometric measure quantifying latent-space separability of safe/unsafe image activations, revealing hidden vulnerabilities. Empirically, we demonstrate that DPO-Kernels maintain strong generalization bounds via Heavy-Tailed Self-Regularization (HT-SR). DETONATE and complete code are publicly released.

