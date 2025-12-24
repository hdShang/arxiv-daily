---
layout: default
title: "StableMotion: Training Motion Cleanup Models with Unpaired Corrupted Data"
---

# StableMotion: Training Motion Cleanup Models with Unpaired Corrupted Data

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03154" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03154v2</a>
  <a href="https://arxiv.org/pdf/2505.03154.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03154v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03154v2', 'StableMotion: Training Motion Cleanup Models with Unpaired Corrupted Data')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuxuan Mu, Hung Yu Ling, Yi Shi, Ismael Baira Ojeda, Pengcheng Xi, Chang Shu, Fabio Zinno, Xue Bin Peng

**分类**: cs.CV, cs.AI, cs.GR

**发布日期**: 2025-05-06 (更新: 2025-09-15)

**备注**: Accepted for SIGGRAPH Asia 2025

---

## 💡 一句话要点

**提出StableMotion以解决运动捕捉数据清理问题**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `运动捕捉` `数据清理` `机器学习` `质量指标` `自动化处理`

## 📋 核心要点

1. 现有运动清理方法通常需要成对的受损与清洁数据，构建这样的数据集既繁琐又耗时。
2. StableMotion通过引入运动质量指标，允许从未配对的受损数据集中训练运动清理模型，简化了数据准备过程。
3. 在SoccerMocap数据集上，StableMotion有效减少了68%的运动跳动和81%的冻结帧，显示出显著的性能提升。

## 📝 摘要（中文）

运动捕捉（mocap）数据常因传感器不准确和后处理不当而出现视觉上令人不适的伪影。清理这些受损数据通常需要专家进行大量手动工作，既费时又费力。以往的数据驱动运动清理方法虽然有望自动化这一过程，但通常需要成对的受损与清洁训练数据。构建这样的配对数据集需要高质量、相对无伪影的运动片段，这往往需要繁琐的手动清理。本文提出StableMotion，一种直接从未配对的受损数据集中训练运动清理模型的简单有效方法。我们的方法引入了运动质量指标，能够通过手动标注或启发式算法轻松注释，从而使得在混合质量的原始运动数据上训练质量感知的运动生成模型成为可能。测试时，模型可以根据质量指标生成高质量的运动。我们在245小时的足球运动捕捉数据集SoccerMocap上验证了该方法的有效性，显著减少了运动伪影。

## 🔬 方法详解

**问题定义**：本文旨在解决运动捕捉数据中的伪影清理问题。现有方法依赖于成对的受损与清洁数据，导致数据准备过程复杂且耗时。

**核心思路**：StableMotion的核心思路是通过引入运动质量指标，使得可以在未配对的受损数据上训练质量感知的运动生成模型。这种设计使得数据准备变得更加高效。

**技术框架**：该方法采用简单的扩散基础框架，构建了一个统一的运动生成-判别模型。主要模块包括运动质量指标的生成、运动数据的处理和伪影的识别与修复。

**关键创新**：StableMotion的最大创新在于能够从未配对的受损数据中训练模型，而不需要高质量的配对数据。这一方法显著降低了数据准备的复杂性。

**关键设计**：模型设计中，运动质量指标通过手动标注或启发式算法生成，损失函数则结合了生成与判别的目标，以确保生成的运动质量符合预期。

## 📊 实验亮点

实验结果表明，StableMotion在SoccerMocap数据集上有效减少了68%的运动跳动和81%的冻结帧，展示了其在运动伪影修复方面的显著性能提升。这些结果表明该方法在实际应用中的有效性和可靠性。

## 🎯 应用场景

该研究在动画制作、游戏开发和虚拟现实等领域具有广泛的应用潜力。通过自动化运动数据的清理过程，能够显著降低人力成本，提高生产效率。此外，未来可能推动更高质量的运动捕捉技术的发展。

## 📄 摘要（原文）

> Motion capture (mocap) data often exhibits visually jarring artifacts due to inaccurate sensors and post-processing. Cleaning this corrupted data can require substantial manual effort from human experts, which can be a costly and time-consuming process. Previous data-driven motion cleanup methods offer the promise of automating this cleanup process, but often require in-domain paired corrupted-to-clean training data. Constructing such paired datasets requires access to high-quality, relatively artifact-free motion clips, which often necessitates laborious manual cleanup. In this work, we present StableMotion, a simple yet effective method for training motion cleanup models directly from unpaired corrupted datasets that need cleanup. The core component of our method is the introduction of motion quality indicators, which can be easily annotated - through manual labeling or heuristic algorithms - and enable training of quality-aware motion generation models on raw motion data with mixed quality. At test time, the model can be prompted to generate high-quality motions using the quality indicators. Our method can be implemented through a simple diffusion-based framework, leading to a unified motion generate-discriminate model, which can be used to both identify and fix corrupted frames. We demonstrate that our proposed method is effective for training motion cleanup models on raw mocap data in production scenarios by applying StableMotion to SoccerMocap, a 245-hour soccer mocap dataset containing real-world motion artifacts. The trained model effectively corrects a wide range of motion artifacts, reducing motion pops and frozen frames by 68% and 81%, respectively. Results and code are available at https://yxmu.foo/stablemotion-page

