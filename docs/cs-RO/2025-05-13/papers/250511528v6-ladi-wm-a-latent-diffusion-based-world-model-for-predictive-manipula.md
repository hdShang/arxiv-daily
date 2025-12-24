---
layout: default
title: "LaDi-WM: A Latent Diffusion-based World Model for Predictive Manipulation"
---

# LaDi-WM: A Latent Diffusion-based World Model for Predictive Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.11528" class="toolbar-btn" target="_blank">📄 arXiv: 2505.11528v6</a>
  <a href="https://arxiv.org/pdf/2505.11528.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.11528v6" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.11528v6', 'LaDi-WM: A Latent Diffusion-based World Model for Predictive Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuhang Huang, Jiazhao Zhang, Shilong Zou, Xinwang Liu, Ruizhen Hu, Kai Xu

**分类**: cs.RO, cs.AI, cs.LG

**发布日期**: 2025-05-13 (更新: 2025-09-12)

**备注**: CoRL 2025

---

## 💡 一句话要点

**提出LaDi-WM以解决机器人预测操控中的视觉状态生成问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `预测操控` `扩散建模` `潜在空间` `视觉基础模型` `机器人策略`

## 📋 核心要点

1. 现有方法在生成机器人与物体交互的未来视觉状态时面临挑战，尤其是高质量像素级表示的生成。
2. 本文提出LaDi-WM，通过扩散建模预测未来状态的潜在空间，结合几何和语义特征，提升学习效率和泛化能力。
3. 实验结果显示，LaDi-WM在LIBERO-LONG基准上提升了27.9%的策略性能，并在真实场景中提升了20%，展现了良好的泛化能力。

## 📝 摘要（中文）

预测操控在具身人工智能领域受到广泛关注，因其能够通过预测状态提升机器人策略性能。然而，从世界模型生成准确的机器人与物体交互的未来视觉状态仍然是一个挑战，尤其是在实现高质量像素级表示方面。为此，本文提出了LaDi-WM，一个基于扩散建模的世界模型，预测未来状态的潜在空间。LaDi-WM利用与预训练视觉基础模型（VFM）对齐的潜在空间，结合几何特征（基于DINO）和语义特征（基于CLIP）。我们发现，预测潜在空间的演变比直接预测像素级图像更易于学习且更具泛化能力。基于LaDi-WM，我们设计了一种扩散策略，通过整合预测状态迭代优化输出动作，从而生成更一致和准确的结果。大量实验表明，LaDi-WM在LIBERO-LONG基准上提升了27.9%的策略性能，并在真实场景中提升了20%。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人在操控任务中生成未来视觉状态的困难，现有方法在像素级表示生成上存在显著不足，导致策略性能受限。

**核心思路**：LaDi-WM通过扩散建模来预测潜在空间的演变，而非直接生成像素图像，这种方法更易于学习且具有更好的泛化能力。

**技术框架**：LaDi-WM的整体架构包括潜在空间的预测模块和扩散策略模块。潜在空间模块利用预训练的视觉基础模型提取几何和语义特征，而扩散策略模块则通过迭代优化输出动作。

**关键创新**：LaDi-WM的核心创新在于利用扩散建模来预测潜在空间的演变，这与传统的直接像素预测方法有本质区别，提升了学习效率和结果一致性。

**关键设计**：在设计中，采用了与DINO和CLIP对齐的潜在空间特征，损失函数设计上注重潜在空间的准确性和一致性，以确保生成结果的高质量。

## 📊 实验亮点

实验结果显示，LaDi-WM在LIBERO-LONG基准上提升了27.9%的策略性能，并在真实场景中提升了20%。这些结果表明，LaDi-WM在生成未来状态的准确性和一致性方面具有显著优势，展现了良好的泛化能力。

## 🎯 应用场景

该研究的潜在应用领域包括机器人操控、自动化制造和智能家居等。通过提升机器人在复杂环境中的预测能力，LaDi-WM能够显著改善机器人在实际任务中的表现，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Predictive manipulation has recently gained considerable attention in the Embodied AI community due to its potential to improve robot policy performance by leveraging predicted states. However, generating accurate future visual states of robot-object interactions from world models remains a well-known challenge, particularly in achieving high-quality pixel-level representations. To this end, we propose LaDi-WM, a world model that predicts the latent space of future states using diffusion modeling. Specifically, LaDi-WM leverages the well-established latent space aligned with pre-trained Visual Foundation Models (VFMs), which comprises both geometric features (DINO-based) and semantic features (CLIP-based). We find that predicting the evolution of the latent space is easier to learn and more generalizable than directly predicting pixel-level images. Building on LaDi-WM, we design a diffusion policy that iteratively refines output actions by incorporating forecasted states, thereby generating more consistent and accurate results. Extensive experiments on both synthetic and real-world benchmarks demonstrate that LaDi-WM significantly enhances policy performance by 27.9\% on the LIBERO-LONG benchmark and 20\% on the real-world scenario. Furthermore, our world model and policies achieve impressive generalizability in real-world experiments.

