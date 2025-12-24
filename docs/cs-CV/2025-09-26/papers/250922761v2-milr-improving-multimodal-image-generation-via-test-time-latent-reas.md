---
layout: default
title: "MILR: Improving Multimodal Image Generation via Test-Time Latent Reasoning"
---

# MILR: Improving Multimodal Image Generation via Test-Time Latent Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22761" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22761v2</a>
  <a href="https://arxiv.org/pdf/2509.22761.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22761v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22761v2', 'MILR: Improving Multimodal Image Generation via Test-Time Latent Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yapeng Mi, Hengli Li, Yanpeng Zhao, Chenxi Li, Huimin Wu, Xiaojian Ma, Song-Chun Zhu, Ying Nian Wu, Qing Li

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-26 (更新: 2025-12-04)

**备注**: 21 pages,13 figures,9 tables

---

## 💡 一句话要点

**提出MILR，通过测试时潜在推理提升多模态图像生成质量。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态图像生成` `测试时推理` `潜在空间推理` `策略梯度` `跨模态理解`

## 📋 核心要点

1. 现有基于推理的图像生成方法通常局限于单模态推理，或依赖高质量的推理数据进行微调，存在局限性。
2. MILR的核心思想是在测试时，通过在统一的潜在空间中联合推理图像和文本信息，提升图像生成质量。
3. 实验结果表明，MILR在多个基准测试中取得了最先进的性能，尤其在知识密集型任务上提升显著。

## 📝 摘要（中文）

本文提出了一种名为MILR的测试时方法，旨在提升多模态图像生成效果。MILR在统一的潜在向量空间中联合推理图像和文本信息。推理过程通过搜索离散图像和文本token的向量表示来实现，具体采用策略梯度方法，并由图像质量评价器指导。MILR在统一的多模态理解和生成（MUG）框架内实现，该框架原生支持图像合成前的语言推理，从而促进跨模态推理。待优化的中间模型输出作为统一的潜在空间，使MILR能够在完全测试时运行。在GenEval、T2I-CompBench和WISE上的评估结果表明，MILR在所有基准测试中均取得了最先进的性能。尤其是在知识密集型WISE上，MILR的总分达到0.63，比基线提高了80%。进一步分析表明，统一潜在空间中的联合推理是其强大性能的关键。此外，定性研究揭示了MILR在时间和文化推理方面的能力，突出了该推理方法的有效性。

## 🔬 方法详解

**问题定义**：现有基于推理的图像生成方法要么仅限于对图像或文本进行单模态推理，要么需要高质量的推理数据进行微调。这限制了它们在复杂场景下的应用，尤其是在需要跨模态知识推理的场景中。

**核心思路**：MILR的核心思路是在测试阶段，通过在统一的潜在向量空间中联合推理图像和文本信息来提升图像生成质量。这种联合推理允许模型同时考虑图像和文本的上下文信息，从而生成更符合要求的图像。

**技术框架**：MILR构建于统一的多模态理解和生成（MUG）框架之上。MUG框架首先进行语言推理，然后进行图像合成，为跨模态推理提供了天然的优势。MILR利用MUG框架的中间输出作为统一的潜在空间，在这个空间中，图像和文本的离散token被表示为向量。然后，通过策略梯度方法在这个潜在空间中搜索最优的图像和文本表示，以提升图像质量。图像质量由一个图像质量评价器进行评估，并作为策略梯度的奖励信号。

**关键创新**：MILR的关键创新在于其测试时联合推理机制，它不需要额外的训练数据或微调。通过在统一的潜在空间中进行推理，MILR能够同时考虑图像和文本的上下文信息，从而生成更符合要求的图像。此外，MILR利用策略梯度方法来优化潜在空间中的表示，这使得模型能够自适应地学习如何进行推理。

**关键设计**：MILR使用策略梯度方法来优化潜在空间中的图像和文本表示。具体来说，模型通过采样一系列的图像和文本token，并根据图像质量评价器的输出计算奖励信号。然后，使用策略梯度算法更新模型参数，以最大化期望奖励。图像质量评价器可以使用预训练的图像质量评估模型，例如CLIP。此外，MILR还使用了温度参数来控制采样过程的探索程度。

## 📊 实验亮点

MILR在GenEval、T2I-CompBench和WISE等多个基准测试中取得了最先进的性能。尤其是在知识密集型WISE基准测试中，MILR的总分达到了0.63，比基线提高了80%。这表明MILR在处理需要跨模态知识推理的任务时具有显著的优势。

## 🎯 应用场景

MILR具有广泛的应用前景，例如图像编辑、图像描述生成、视觉问答等。它可以用于生成更符合用户需求的图像，提高图像生成系统的智能化水平。此外，MILR还可以应用于教育、娱乐等领域，例如生成个性化的学习材料、创建虚拟现实场景等。

## 📄 摘要（原文）

> Reasoning-augmented machine learning systems have shown improved performance in various domains, including image generation. However, existing reasoning-based methods for image generation either restrict reasoning to a single modality (image or text) or rely on high-quality reasoning data for fine-tuning. To tackle these limitations, we propose MILR, a test-time method that jointly reasons over image and text in a unified latent vector space. Reasoning in MILR is performed by searching through vector representations of discrete image and text tokens. Practically, this is implemented via the policy gradient method, guided by an image quality critic. We instantiate MILR within the unified multimodal understanding and generation (MUG) framework that natively supports language reasoning before image synthesis and thus facilitates cross-modal reasoning. The intermediate model outputs, which are to be optimized, serve as the unified latent space, enabling MILR to operate entirely at test time. We evaluate MILR on GenEval, T2I-CompBench, and WISE, achieving state-of-the-art results on all benchmarks. Notably, on knowledge-intensive WISE, MILR attains an overall score of 0.63, improving over the baseline by 80%. Our further analysis indicates that joint reasoning in the unified latent space is the key to its strong performance. Moreover, our qualitative studies reveal MILR's non-trivial ability in temporal and cultural reasoning, highlighting the efficacy of our reasoning method.

