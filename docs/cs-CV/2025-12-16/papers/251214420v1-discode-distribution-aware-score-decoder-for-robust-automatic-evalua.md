---
layout: default
title: DISCODE: Distribution-Aware Score Decoder for Robust Automatic Evaluation of Image Captioning
---

# DISCODE: Distribution-Aware Score Decoder for Robust Automatic Evaluation of Image Captioning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14420" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14420v1</a>
  <a href="https://arxiv.org/pdf/2512.14420.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14420v1" onclick="toggleFavorite(this, '2512.14420v1', 'DISCODE: Distribution-Aware Score Decoder for Robust Automatic Evaluation of Image Captioning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nakamasa Inoue, Kanoko Goto, Masanari Oi, Martyna Gruszka, Mahiro Ukai, Takumi Hirose, Yusuke Sekikawa

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-16

**备注**: Paper accepted to AAAI 2026

---

## 💡 一句话要点

**提出DISCODE，一种分布感知的无微调方法，提升图像描述自动评估在跨域场景下的鲁棒性。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图像描述评估` `领域自适应` `无参考指标` `视觉-语言模型` `测试时自适应`

## 📋 核心要点

1. 现有LVLM的图像描述评估在领域迁移时表现不佳，难以保证评估结果的鲁棒性。
2. DISCODE通过引入自适应测试时损失(ATT)，利用高斯先验分布，提升评估分数估计的鲁棒性。
3. 实验表明，DISCODE在MCEval和多个现有基准上，作为无参考指标，达到了SOTA性能。

## 📝 摘要（中文）

大型视觉-语言模型(LVLMs)在广泛的多模态任务中表现出令人印象深刻的性能。然而，使用LVLMs进行鲁棒的图像描述评估仍然具有挑战性，尤其是在领域转移的情况下。为了解决这个问题，我们引入了分布感知分数解码器(DISCODE)，这是一种新颖的免微调方法，可以生成更鲁棒的评估分数，从而更好地与不同领域的人工判断对齐。DISCODE背后的核心思想在于其测试时自适应评估方法，该方法引入了自适应测试时(ATT)损失，利用高斯先验分布来提高评估分数估计的鲁棒性。这种损失可以在测试时使用我们推导出的解析解有效地最小化。此外，我们还引入了多域描述评估(MCEval)基准，这是一个新的图像描述评估基准，涵盖六个不同的领域，旨在评估评估指标的鲁棒性。在我们的实验中，我们证明了DISCODE在MCEval和四个具有代表性的现有基准上，作为一种无参考评估指标，实现了最先进的性能。

## 🔬 方法详解

**问题定义**：论文旨在解决图像描述自动评估在领域迁移场景下的鲁棒性问题。现有的基于大型视觉-语言模型（LVLM）的评估方法在面对不同领域的数据时，评估结果与人类判断的一致性会显著下降，缺乏泛化能力。

**核心思路**：DISCODE的核心思路是在测试时进行自适应调整，利用高斯先验分布来约束评估分数的估计，从而提高评估的鲁棒性。通过最小化一个自适应测试时损失（ATT loss），使模型在特定测试样本上生成更可靠的评估分数。

**技术框架**：DISCODE方法主要包含以下几个阶段：1) 使用LVLM生成图像描述的评估分数；2) 构建基于高斯先验的自适应测试时损失（ATT loss）；3) 通过解析解最小化ATT loss，得到调整后的评估分数。整个过程无需额外的微调，仅在测试阶段进行自适应调整。

**关键创新**：DISCODE的关键创新在于提出了自适应测试时损失（ATT loss），并推导出了该损失函数的解析解。ATT loss利用高斯先验分布对评估分数进行约束，使得模型在面对领域迁移时能够生成更稳定的评估结果。与传统的微调方法不同，DISCODE无需额外的训练数据，可以在测试时快速适应新的领域。

**关键设计**：ATT loss的设计是关键。它由两部分组成：一部分是LVLM原始评估分数与调整后评估分数之间的差异，另一部分是调整后评估分数与高斯先验分布之间的距离。通过最小化ATT loss，可以使得调整后的评估分数既接近LVLM的原始评估分数，又符合高斯先验分布。论文推导出了ATT loss的解析解，使得可以在测试时高效地计算出最优的调整后评估分数。具体的高斯分布参数（均值和方差）是预先设定的超参数。

## 📊 实验亮点

DISCODE在MCEval基准测试中取得了显著的性能提升，该基准包含六个不同的领域，证明了DISCODE的跨域鲁棒性。此外，DISCODE在COCO、Flickr30k等常用基准上也取得了与现有SOTA方法相当甚至更好的结果。重要的是，DISCODE无需额外的训练数据或微调，即可实现性能提升。

## 🎯 应用场景

DISCODE可应用于各种需要自动评估图像描述质量的场景，例如图像搜索引擎、图像标注系统、视觉对话系统等。该方法能够提高评估的准确性和鲁棒性，减少人工干预，从而提升系统的整体性能和用户体验。未来，该方法可以扩展到其他多模态任务的评估中，例如视频描述、视觉问答等。

## 📄 摘要（原文）

> Large vision-language models (LVLMs) have shown impressive performance across a broad range of multimodal tasks. However, robust image caption evaluation using LVLMs remains challenging, particularly under domain-shift scenarios. To address this issue, we introduce the Distribution-Aware Score Decoder (DISCODE), a novel finetuning-free method that generates robust evaluation scores better aligned with human judgments across diverse domains. The core idea behind DISCODE lies in its test-time adaptive evaluation approach, which introduces the Adaptive Test-Time (ATT) loss, leveraging a Gaussian prior distribution to improve robustness in evaluation score estimation. This loss is efficiently minimized at test time using an analytical solution that we derive. Furthermore, we introduce the Multi-domain Caption Evaluation (MCEval) benchmark, a new image captioning evaluation benchmark covering six distinct domains, designed to assess the robustness of evaluation metrics. In our experiments, we demonstrate that DISCODE achieves state-of-the-art performance as a reference-free evaluation metric across MCEval and four representative existing benchmarks.

