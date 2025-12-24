---
layout: default
title: LoFT-LLM: Low-Frequency Time-Series Forecasting with Large Language Models
---

# LoFT-LLM: Low-Frequency Time-Series Forecasting with Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20002" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20002v1</a>
  <a href="https://arxiv.org/pdf/2512.20002.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20002v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20002v1', 'LoFT-LLM: Low-Frequency Time-Series Forecasting with Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiacheng You, Jingcheng Yang, Yuhang Xie, Zhongxuan Wu, Xiucheng Li, Feng Li, Pengjie Wang, Jian Xu, Bo Zheng, Xinyang Chen

**分类**: cs.LG

**发布日期**: 2025-12-23

**备注**: Accepted at KDD 2026. 9 pages

---

## 💡 一句话要点

**LoFT-LLM：结合低频学习与大语言模型的时间序列预测框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `时间序列预测` `低频学习` `大语言模型` `频率分析` `语义校准`

## 📋 核心要点

1. 现有深度预测模型使用全长时序窗口进行监督，包含大量高频噪声，掩盖长期趋势，且对辅助变量的利用不足。
2. LoFT-LLM通过频率感知的方式，提取低频趋势并结合大语言模型进行语义校准，从而提升预测性能。
3. 实验表明，LoFT-LLM在金融和能源数据集上，相比现有方法，在准确性、鲁棒性和可解释性方面均有显著提升。

## 📝 摘要（中文）

本文提出了一种名为LoFT-LLM的频率感知预测流程，它结合了低频学习和通过大语言模型（LLM）进行的语义校准，旨在解决实际应用中时间序列预测面临的挑战，如训练数据有限和复杂、嘈杂的时间动态。该方法首先使用Patch低频预测模块（PLFM）从局部频谱块中提取稳定的低频趋势，然后使用残差学习器对高频变化进行建模。最后，通过微调的LLM，利用结构化的自然语言提示，结合辅助上下文和领域知识来优化预测结果。在金融和能源数据集上的大量实验表明，LoFT-LLM在全数据和少样本情况下均显著优于强大的基线模型，提供了更高的准确性、鲁棒性和可解释性。

## 🔬 方法详解

**问题定义**：现实世界的时间序列预测，例如金融和能源领域，面临着训练数据有限以及复杂和嘈杂的时间动态的挑战。现有的深度预测模型通常使用全长的时间窗口来监督预测，这包含了大量的高频噪声，掩盖了长期的趋势。此外，包含丰富领域信息的辅助变量通常没有得到充分利用，尤其是在少样本的情况下。

**核心思路**：LoFT-LLM的核心思路是将时间序列分解为低频趋势和高频残差，分别进行建模。低频趋势反映了数据的长期模式，对噪声不敏感，更容易学习。同时，利用大语言模型（LLM）的语义理解能力，将辅助变量和领域知识融入预测过程，从而提高预测的准确性和鲁棒性。

**技术框架**：LoFT-LLM的整体框架包含三个主要模块：Patch低频预测模块（PLFM）、残差学习器和LLM语义校准模块。PLFM负责从局部频谱块中提取稳定的低频趋势。残差学习器用于建模高频变化。LLM语义校准模块则通过微调的LLM，利用结构化的自然语言提示，结合辅助上下文和领域知识来优化预测结果。

**关键创新**：LoFT-LLM的关键创新在于频率感知的预测方法和LLM的语义校准。频率感知方法通过提取低频趋势，降低了噪声的影响，提高了模型的鲁棒性。LLM的语义校准则将领域知识融入预测过程，提高了预测的准确性和可解释性。

**关键设计**：PLFM使用局部频谱分析提取低频成分，具体实现细节（如窗口大小、重叠率等）未知。残差学习器的具体网络结构未知。LLM使用微调方式，提示工程的具体形式未知，损失函数也未知。这些细节会影响最终的性能表现，但论文摘要中未详细说明。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20002v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20002v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20002v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

LoFT-LLM在金融和能源数据集上进行了广泛的实验，结果表明，在全数据和少样本情况下，LoFT-LLM均显著优于强大的基线模型。具体的性能提升数据未知，但论文强调了其在准确性、鲁棒性和可解释性方面的优势。这些结果表明，LoFT-LLM是一种有效的时间序列预测方法。

## 🎯 应用场景

LoFT-LLM具有广泛的应用前景，尤其是在金融、能源等对预测精度要求高的领域。它可以用于股票价格预测、电力负荷预测、风力发电预测等。通过结合领域知识和辅助变量，LoFT-LLM可以提高预测的准确性和鲁棒性，为决策提供更可靠的依据。此外，该方法还可以应用于其他类型的时间序列预测问题，例如交通流量预测、销售预测等。

## 📄 摘要（原文）

> Time-series forecasting in real-world applications such as finance and energy often faces challenges due to limited training data and complex, noisy temporal dynamics. Existing deep forecasting models typically supervise predictions using full-length temporal windows, which include substantial high-frequency noise and obscure long-term trends. Moreover, auxiliary variables containing rich domain-specific information are often underutilized, especially in few-shot settings. To address these challenges, we propose LoFT-LLM, a frequency-aware forecasting pipeline that integrates low-frequency learning with semantic calibration via a large language model (LLM). Firstly, a Patch Low-Frequency forecasting Module (PLFM) extracts stable low-frequency trends from localized spectral patches. Secondly, a residual learner then models high-frequency variations. Finally, a fine-tuned LLM refines the predictions by incorporating auxiliary context and domain knowledge through structured natural language prompts. Extensive experiments on financial and energy datasets demonstrate that LoFT-LLM significantly outperforms strong baselines under both full-data and few-shot regimes, delivering superior accuracy, robustness, and interpretability.

