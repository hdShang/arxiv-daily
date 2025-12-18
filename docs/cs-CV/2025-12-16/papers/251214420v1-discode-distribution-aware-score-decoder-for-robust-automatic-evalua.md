---
layout: default
title: DISCODE: Distribution-Aware Score Decoder for Robust Automatic Evaluation of Image Captioning
---

# DISCODE: Distribution-Aware Score Decoder for Robust Automatic Evaluation of Image Captioning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14420" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14420v1</a>
  <a href="https://arxiv.org/pdf/2512.14420.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14420v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14420v1', 'DISCODE: Distribution-Aware Score Decoder for Robust Automatic Evaluation of Image Captioning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nakamasa Inoue, Kanoko Goto, Masanari Oi, Martyna Gruszka, Mahiro Ukai, Takumi Hirose, Yusuke Sekikawa

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-16

**备注**: Paper accepted to AAAI 2026

---

## 💡 一句话要点

**提出DISCODE，一种分布感知的分数解码器，用于提升图像描述自动评估的鲁棒性。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图像描述评估` `领域自适应` `视觉-语言模型` `鲁棒性` `测试时自适应` `高斯先验` `无参考评估`

## 📋 核心要点

1. 现有LVLMs在图像描述评估中，领域迁移场景下的鲁棒性不足，难以准确反映人工判断。
2. DISCODE通过引入自适应测试时损失(ATT)和高斯先验，实现测试时自适应评估，提升鲁棒性。
3. 实验表明，DISCODE在MCEval等多个基准测试中，作为无参考指标，达到了SOTA性能。

## 📝 摘要（中文）

大型视觉-语言模型(LVLMs)在广泛的多模态任务中表现出了令人印象深刻的性能。然而，使用LVLMs进行鲁棒的图像描述评估仍然具有挑战性，尤其是在领域迁移的情况下。为了解决这个问题，我们引入了分布感知分数解码器(DISCODE)，这是一种新颖的无需微调的方法，可以生成更鲁棒的评估分数，更好地与不同领域的人工判断对齐。DISCODE的核心思想在于其测试时自适应评估方法，该方法引入了自适应测试时(ATT)损失，利用高斯先验分布来提高评估分数估计的鲁棒性。我们在测试时使用我们推导出的解析解有效地最小化这个损失。此外，我们还引入了多领域描述评估(MCEval)基准，这是一个新的图像描述评估基准，涵盖六个不同的领域，旨在评估评估指标的鲁棒性。在我们的实验中，我们证明了DISCODE在MCEval和四个具有代表性的现有基准上，作为一种无参考评估指标，实现了最先进的性能。

## 🔬 方法详解

**问题定义**：论文旨在解决图像描述自动评估在领域迁移场景下的鲁棒性问题。现有方法，特别是基于大型视觉-语言模型(LVLMs)的方法，在面对不同领域的数据时，评估结果与人类判断的一致性较差，泛化能力不足。

**核心思路**：DISCODE的核心思路是在测试时进行自适应调整，利用领域内数据的分布信息来优化评估分数。通过引入一个高斯先验分布，并结合自适应测试时(ATT)损失，使得模型能够更好地适应当前领域的特点，从而提高评估的准确性和鲁棒性。

**技术框架**：DISCODE主要包含以下几个关键部分：1) 使用LVLM提取图像和描述的特征；2) 定义一个评估分数解码器，将特征映射到评估分数；3) 引入高斯先验分布，对评估分数进行约束；4) 定义自适应测试时(ATT)损失，用于在测试时优化评估分数。整个框架无需额外的微调，即可在不同领域的数据上进行评估。

**关键创新**：DISCODE的关键创新在于其测试时自适应评估方法。与传统的固定模型评估方法不同，DISCODE能够根据当前领域的数据分布，动态调整评估分数，从而提高鲁棒性。ATT损失和高斯先验的结合，使得模型能够在保证评估准确性的同时，避免过拟合领域内的数据。

**关键设计**：ATT损失的设计是关键。它基于高斯先验，鼓励评估分数靠近先验分布的均值，同时惩罚与领域内其他样本评估分数差异过大的情况。论文推导出了ATT损失的解析解，使得测试时的优化过程非常高效。此外，MCEval基准的构建也为评估指标的鲁棒性提供了更全面的测试平台。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14420v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14420v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14420v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

DISCODE在MCEval基准测试中取得了显著的性能提升，超越了现有的无参考评估指标。同时，在COCO、Flickr30k等常用基准测试中也表现出SOTA性能，证明了其在不同领域和数据集上的泛化能力。实验结果表明，DISCODE能够更准确地反映人类对图像描述质量的判断。

## 🎯 应用场景

DISCODE可应用于各种需要自动评估图像描述质量的场景，例如图像搜索引擎、视觉内容生成、多模态对话系统等。该方法能够提升评估的准确性和鲁棒性，从而改善用户体验，并促进相关技术的发展。未来，该方法可以扩展到其他多模态任务的评估中。

## 📄 摘要（原文）

> Large vision-language models (LVLMs) have shown impressive performance across a broad range of multimodal tasks. However, robust image caption evaluation using LVLMs remains challenging, particularly under domain-shift scenarios. To address this issue, we introduce the Distribution-Aware Score Decoder (DISCODE), a novel finetuning-free method that generates robust evaluation scores better aligned with human judgments across diverse domains. The core idea behind DISCODE lies in its test-time adaptive evaluation approach, which introduces the Adaptive Test-Time (ATT) loss, leveraging a Gaussian prior distribution to improve robustness in evaluation score estimation. This loss is efficiently minimized at test time using an analytical solution that we derive. Furthermore, we introduce the Multi-domain Caption Evaluation (MCEval) benchmark, a new image captioning evaluation benchmark covering six distinct domains, designed to assess the robustness of evaluation metrics. In our experiments, we demonstrate that DISCODE achieves state-of-the-art performance as a reference-free evaluation metric across MCEval and four representative existing benchmarks.

