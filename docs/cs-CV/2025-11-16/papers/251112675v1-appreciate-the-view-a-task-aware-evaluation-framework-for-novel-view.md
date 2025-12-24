---
layout: default
title: "Appreciate the View: A Task-Aware Evaluation Framework for Novel View Synthesis"
---

# Appreciate the View: A Task-Aware Evaluation Framework for Novel View Synthesis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.12675" class="toolbar-btn" target="_blank">📄 arXiv: 2511.12675v1</a>
  <a href="https://arxiv.org/pdf/2511.12675.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.12675v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.12675v1', 'Appreciate the View: A Task-Aware Evaluation Framework for Novel View Synthesis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Saar Stern, Ido Sobol, Or Litany

**分类**: cs.CV

**发布日期**: 2025-11-16

**备注**: 3DV 2026. Project page: https://saarst.github.io/appreciate-the-view-website

---

## 💡 一句话要点

**提出任务感知的新视角合成评估框架，解决现有指标与人类感知不一致问题**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `新视角合成` `评估指标` `任务感知` `Zero123` `生成模型`

## 📋 核心要点

1. 现有新视角合成(NVS)评估指标，如像素相似度等，无法准确反映生成图像的真实性和视角变换的忠实性。
2. 利用强大的NVS基础模型Zero123的特征，通过轻量级微调，提出任务感知的评估框架，增强判别能力。
3. 引入基于参考的$D_{	ext{PRISM}}$和无参考的$	ext{MMD}_{	ext{PRISM}}$两个指标，与人类偏好更一致，能更可靠地识别错误生成。

## 📝 摘要（中文）

新视角合成(NVS)的目标是从未见过的视角生成给定内容逼真的图像。然而，如何保证生成的图像真正反映了预期的变换仍然是一个主要的挑战。尽管最近的生成模型，特别是基于扩散的方法，已经显著提高了NVS的质量，但现有的评估指标难以评估生成的图像是否既逼真又忠实于源视图和预期的视点变换。标准的指标，如像素级相似度和基于分布的度量，常常错误地将不正确的结果排在前面，因为它们未能捕捉到源图像、视点变化和生成输出之间细微的关系。我们提出了一个任务感知的评估框架，该框架利用了强大的NVS基础模型Zero123的特征，并结合轻量级的微调步骤来增强判别能力。使用这些特征，我们引入了两个互补的评估指标：一个基于参考的分数$D_{	ext{PRISM}}$和一个无参考的分数$	ext{MMD}_{	ext{PRISM}}$。两者都能可靠地识别不正确的生成结果，并根据人类偏好研究对模型进行排序，从而解决了NVS评估中的一个根本性差距。我们的框架提供了一种原则性和实用的方法来评估合成质量，为新视角合成中更可靠的进展铺平了道路。为了进一步支持这一目标，我们将我们的无参考指标应用于Toys4K、Google Scanned Objects (GSO)和OmniObject3D这三个基准测试中的六种NVS方法，其中$	ext{MMD}_{	ext{PRISM}}$产生了一个清晰而稳定的排名，较低的分数始终表明更强的模型。

## 🔬 方法详解

**问题定义**：新视角合成(NVS)旨在从不同视角生成图像，但现有评估指标无法准确衡量生成图像的质量，特别是真实性和视角变换的忠实性。传统的像素级相似度等指标无法捕捉源图像、视角变化和生成图像之间的复杂关系，导致评估结果与人类感知不一致。

**核心思路**：论文的核心思路是利用一个强大的预训练NVS模型（Zero123）提取的特征，并在此基础上进行轻量级的微调，以增强特征的判别能力。通过这种方式，可以获得更具语义信息的特征表示，从而更准确地评估生成图像的质量。

**技术框架**：该评估框架主要包含以下几个阶段：1) 使用预训练的NVS模型（Zero123）提取源图像和生成图像的特征。2) 对提取的特征进行轻量级的微调，以增强其判别能力。3) 基于微调后的特征，计算两个评估指标：基于参考的$D_{	ext{PRISM}}$和无参考的$	ext{MMD}_{	ext{PRISM}}$。$D_{	ext{PRISM}}$衡量生成图像与参考图像之间的相似度，而$	ext{MMD}_{	ext{PRISM}}$衡量生成图像分布与真实图像分布之间的差异。

**关键创新**：该论文的关键创新在于提出了一个任务感知的评估框架，该框架利用了预训练NVS模型的特征，并通过微调增强了特征的判别能力。与传统的评估指标相比，该框架能够更准确地评估生成图像的真实性和视角变换的忠实性，并且与人类感知更一致。此外，论文还提出了两个互补的评估指标，分别是基于参考的$D_{	ext{PRISM}}$和无参考的$	ext{MMD}_{	ext{PRISM}}$，可以根据不同的应用场景选择合适的指标。

**关键设计**：论文中关键的设计包括：1) 选择Zero123作为基础模型，因为它是一个强大的NVS模型，能够提取丰富的图像特征。2) 使用轻量级的微调方法，以避免过度拟合训练数据。3) 设计了两个互补的评估指标，分别是基于参考的$D_{	ext{PRISM}}$和无参考的$	ext{MMD}_{	ext{PRISM}}$，可以根据不同的应用场景选择合适的指标。具体的损失函数和网络结构等细节在论文中未详细说明，属于未知信息。

## 📊 实验亮点

实验结果表明，提出的$	ext{MMD}_{	ext{PRISM}}$指标在Toys4K、GSO和OmniObject3D三个数据集上，对六种NVS方法进行了稳定排序，且排序结果与人类偏好一致。较低的$	ext{MMD}_{	ext{PRISM}}$分数始终对应于更强的模型，验证了该指标的有效性。

## 🎯 应用场景

该研究成果可应用于新视角合成模型的评估与改进，推动相关技术发展。在自动驾驶、机器人导航、虚拟现实、增强现实等领域，高质量的新视角合成至关重要，该评估框架能帮助选择和优化更可靠的NVS模型，提升用户体验。

## 📄 摘要（原文）

> The goal of Novel View Synthesis (NVS) is to generate realistic images of a given content from unseen viewpoints. But how can we trust that a generated image truly reflects the intended transformation? Evaluating its reliability remains a major challenge. While recent generative models, particularly diffusion-based approaches, have significantly improved NVS quality, existing evaluation metrics struggle to assess whether a generated image is both realistic and faithful to the source view and intended viewpoint transformation. Standard metrics, such as pixel-wise similarity and distribution-based measures, often mis-rank incorrect results as they fail to capture the nuanced relationship between the source image, viewpoint change, and generated output. We propose a task-aware evaluation framework that leverages features from a strong NVS foundation model, Zero123, combined with a lightweight tuning step to enhance discrimination. Using these features, we introduce two complementary evaluation metrics: a reference-based score, $D_{\text{PRISM}}$, and a reference-free score, $\text{MMD}_{\text{PRISM}}$. Both reliably identify incorrect generations and rank models in agreement with human preference studies, addressing a fundamental gap in NVS evaluation. Our framework provides a principled and practical approach to assessing synthesis quality, paving the way for more reliable progress in novel view synthesis. To further support this goal, we apply our reference-free metric to six NVS methods across three benchmarks: Toys4K, Google Scanned Objects (GSO), and OmniObject3D, where $\text{MMD}_{\text{PRISM}}$ produces a clear and stable ranking, with lower scores consistently indicating stronger models.

