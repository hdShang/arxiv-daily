---
layout: default
title: DISCODE: Distribution-Aware Score Decoder for Robust Automatic Evaluation of Image Captioning
---

# DISCODE: Distribution-Aware Score Decoder for Robust Automatic Evaluation of Image Captioning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14420" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14420</a>
  <a href="https://arxiv.org/pdf/2512.14420.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14420" onclick="toggleFavorite(this, '2512.14420', 'DISCODE: Distribution-Aware Score Decoder for Robust Automatic Evaluation of Image Captioning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nakamasa Inoue, Kanoko Goto, Masanari Oi, Martyna Gruszka, Mahiro Ukai, Takumi Hirose, Yusuke Sekikawa

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出DISCODE，一种分布感知的无微调图像描述评估方法，提升领域泛化性。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图像描述评估` `领域泛化` `视觉-语言模型` `测试时自适应` `鲁棒性` `无参考评估` `多模态学习`

## 📋 核心要点

1. 现有LVLM的图像描述评估在领域迁移时鲁棒性不足，难以准确反映人类判断。
2. DISCODE利用测试时自适应评估，通过高斯先验和ATT损失提升评估分数鲁棒性。
3. MCEval基准测试和实验结果表明，DISCODE在多个数据集上实现了SOTA性能。

## 📝 摘要（中文）

大型视觉-语言模型(LVLMs)在多模态任务中表现出色。然而，使用LVLMs进行鲁棒的图像描述评估仍然具有挑战性，尤其是在领域迁移的情况下。为了解决这个问题，我们引入了分布感知分数解码器(DISCODE)，这是一种新颖的免微调方法，可以生成与不同领域的人工判断更一致的鲁棒评估分数。DISCODE的核心思想在于其测试时自适应评估方法，引入了自适应测试时(ATT)损失，利用高斯先验分布来提高评估分数估计的鲁棒性。我们推导出一个解析解，可以在测试时有效地最小化此损失。此外，我们还引入了多领域描述评估(MCEval)基准，这是一个新的图像描述评估基准，涵盖六个不同的领域，旨在评估评估指标的鲁棒性。实验表明，DISCODE在MCEval和四个具有代表性的现有基准测试中，作为一种无参考评估指标，实现了最先进的性能。

## 🔬 方法详解

**问题定义**：论文旨在解决图像描述自动评估在领域迁移场景下的鲁棒性问题。现有的基于大型视觉-语言模型（LVLM）的评估方法在面对不同领域的数据时，评估结果与人类判断的一致性较差，泛化能力不足。

**核心思路**：DISCODE的核心思路是在测试时进行自适应调整，利用领域内的信息来优化评估分数。通过引入高斯先验分布，并设计自适应测试时（ATT）损失函数，使得模型在评估过程中能够更好地适应当前领域的特征，从而提高评估结果的鲁棒性和准确性。

**技术框架**：DISCODE方法主要包含以下几个阶段：1) 使用LVLM生成图像描述的评估分数；2) 构建基于高斯先验的分布模型；3) 利用自适应测试时（ATT）损失函数，在测试时对评估分数进行优化；4) 输出最终的鲁棒性评估分数。整个框架无需额外的微调，可以在现有的LVLM评估模型上直接应用。

**关键创新**：DISCODE的关键创新在于其测试时自适应评估方法和ATT损失函数的设计。传统的评估方法通常在训练阶段确定模型参数，而在测试阶段直接使用。DISCODE则通过在测试时引入可优化的参数，并利用ATT损失函数进行调整，使得模型能够更好地适应当前领域的特征。此外，论文还提出了MCEval基准测试，为评估指标的鲁棒性提供了一个新的平台。

**关键设计**：ATT损失函数是DISCODE的关键设计之一，其目标是最小化评估分数与高斯先验分布之间的差异。具体而言，ATT损失函数可以表示为：L_ATT = ||s - μ||^2 / (2σ^2)，其中s是LVLM生成的评估分数，μ和σ分别是高斯分布的均值和标准差。论文推导出了该损失函数的解析解，可以在测试时高效地进行优化。此外，MCEval基准测试包含了六个不同的领域，为评估指标的鲁棒性提供了全面的评估。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14420/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14420/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14420/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

DISCODE在MCEval和四个现有基准测试中取得了SOTA性能，证明了其在领域迁移场景下的鲁棒性。例如，在MCEval基准测试中，DISCODE显著优于其他无参考评估指标。此外，DISCODE无需额外的微调，可以直接应用于现有的LVLM评估模型，具有很高的实用价值。

## 🎯 应用场景

DISCODE可应用于各种需要自动评估图像描述质量的场景，例如图像搜索引擎、视觉内容生成、多模态对话系统等。该方法能够提高评估的准确性和鲁棒性，从而提升用户体验和系统性能。未来，该方法可以扩展到其他多模态任务的评估中，例如视频描述、视觉问答等。

## 📄 摘要（原文）

> Large vision-language models (LVLMs) have shown impressive performance across a broad range of multimodal tasks. However, robust image caption evaluation using LVLMs remains challenging, particularly under domain-shift scenarios. To address this issue, we introduce the Distribution-Aware Score Decoder (DISCODE), a novel finetuning-free method that generates robust evaluation scores better aligned with human judgments across diverse domains. The core idea behind DISCODE lies in its test-time adaptive evaluation approach, which introduces the Adaptive Test-Time (ATT) loss, leveraging a Gaussian prior distribution to improve robustness in evaluation score estimation. This loss is efficiently minimized at test time using an analytical solution that we derive. Furthermore, we introduce the Multi-domain Caption Evaluation (MCEval) benchmark, a new image captioning evaluation benchmark covering six distinct domains, designed to assess the robustness of evaluation metrics. In our experiments, we demonstrate that DISCODE achieves state-of-the-art performance as a reference-free evaluation metric across MCEval and four representative existing benchmarks.

