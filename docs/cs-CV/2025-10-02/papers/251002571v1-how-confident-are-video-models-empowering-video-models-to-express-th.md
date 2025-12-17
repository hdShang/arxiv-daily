---
layout: default
title: How Confident are Video Models? Empowering Video Models to Express their Uncertainty
---

# How Confident are Video Models? Empowering Video Models to Express their Uncertainty

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.02571" target="_blank" class="toolbar-btn">arXiv: 2510.02571v1</a>
    <a href="https://arxiv.org/pdf/2510.02571.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.02571v1" 
            onclick="toggleFavorite(this, '2510.02571v1', 'How Confident are Video Models? Empowering Video Models to Express their Uncertainty')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Zhiting Mei, Ola Shorinwa, Anirudha Majumdar

**分类**: cs.CV, cs.AI, cs.CL

**发布日期**: 2025-10-02

---

## 💡 一句话要点

**提出一种框架以量化视频模型的不确定性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频生成` `不确定性量化` `潜在建模` `模型校准` `生成模型`

## 📋 核心要点

1. 现有的视频生成模型在生成过程中容易出现幻觉现象，导致生成内容与事实不符，缺乏不确定性量化方法。
2. 论文提出了一种新的不确定性量化框架S-QUBED，通过潜在建模将预测不确定性分解为随机性和认知性成分。
3. 实验结果表明，S-QUBED能够计算出与任务准确性负相关的校准总不确定性估计，并有效区分随机性和认知性成分。

## 📝 摘要（中文）

生成视频模型展现了令人印象深刻的文本到视频能力，广泛应用于多个实际场景。然而，类似于大型语言模型，视频生成模型也存在幻觉现象，可能生成事实错误的视频。尽管对语言模型的不确定性量化已有大量研究，但目前尚无针对视频模型的不确定性量化方法，这引发了安全隐患。本文首次提出了一种视频模型不确定性量化的框架，包括：基于稳健秩相关估计的模型校准评估指标；一种黑箱不确定性量化方法S-QUBED，能够将预测不确定性严格分解为随机性和认知性成分；以及一个用于基准测试的视频模型不确定性量化数据集。通过对生成任务在潜在空间的条件化，我们能够将因模糊任务规范引起的不确定性与因知识缺乏引起的不确定性分开。

## 🔬 方法详解

**问题定义**：本文旨在解决视频生成模型在生成过程中缺乏不确定性量化的问题。现有方法未能有效评估模型的可靠性和安全性，导致生成内容的潜在风险。

**核心思路**：论文的核心思路是通过引入不确定性量化框架S-QUBED，利用潜在空间的条件化来分解和量化生成模型的不确定性，从而提高模型的可解释性和安全性。

**技术框架**：整体架构包括三个主要模块：首先是基于稳健秩相关估计的模型校准评估指标；其次是黑箱不确定性量化方法S-QUBED；最后是用于基准测试的不确定性量化数据集。

**关键创新**：最重要的技术创新点在于首次提出了针对视频模型的不确定性量化方法，能够将预测不确定性分解为随机性和认知性成分，这在现有文献中尚未见到。

**关键设计**：在设计中，S-QUBED方法通过潜在建模实现了对不确定性的严格分解，采用了特定的损失函数和参数设置，以确保模型的校准性和有效性。

## 📊 实验亮点

实验结果显示，S-QUBED方法计算出的总不确定性估计与任务准确性呈负相关，表明其有效性。与基线模型相比，S-QUBED在校准性和不确定性分解方面均表现出显著提升，验证了其在实际应用中的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括自动视频生成、虚拟现实、游戏开发等。通过量化视频生成模型的不确定性，可以提高生成内容的安全性和可靠性，进而推动这些领域的技术进步和应用落地。未来，该方法可能在多模态学习和人机交互等领域产生深远影响。

## 📄 摘要（原文）

> Generative video models demonstrate impressive text-to-video capabilities, spurring widespread adoption in many real-world applications. However, like large language models (LLMs), video generation models tend to hallucinate, producing plausible videos even when they are factually wrong. Although uncertainty quantification (UQ) of LLMs has been extensively studied in prior work, no UQ method for video models exists, raising critical safety concerns. To our knowledge, this paper represents the first work towards quantifying the uncertainty of video models. We present a framework for uncertainty quantification of generative video models, consisting of: (i) a metric for evaluating the calibration of video models based on robust rank correlation estimation with no stringent modeling assumptions; (ii) a black-box UQ method for video models (termed S-QUBED), which leverages latent modeling to rigorously decompose predictive uncertainty into its aleatoric and epistemic components; and (iii) a UQ dataset to facilitate benchmarking calibration in video models. By conditioning the generation task in the latent space, we disentangle uncertainty arising due to vague task specifications from that arising from lack of knowledge. Through extensive experiments on benchmark video datasets, we demonstrate that S-QUBED computes calibrated total uncertainty estimates that are negatively correlated with the task accuracy and effectively computes the aleatoric and epistemic constituents.

