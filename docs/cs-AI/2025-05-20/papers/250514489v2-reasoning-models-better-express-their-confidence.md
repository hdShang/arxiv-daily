---
layout: default
title: Reasoning Models Better Express Their Confidence
---

# Reasoning Models Better Express Their Confidence

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14489" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14489v2</a>
  <a href="https://arxiv.org/pdf/2505.14489.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14489v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14489v2', 'Reasoning Models Better Express Their Confidence')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dongkeun Yoon, Seungone Kim, Sohee Yang, Sunkyoung Kim, Soyeon Kim, Yongil Kim, Eunbi Choi, Yireun Kim, Minjoon Seo

**分类**: cs.AI, cs.CL

**发布日期**: 2025-05-20 (更新: 2025-10-22)

**备注**: Accepted to NeurIPS 2025

---

## 💡 一句话要点

**提出推理模型以提高信心表达的准确性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `信心表达` `推理模型` `链式思维` `慢思维行为` `信心校准` `机器学习`

## 📋 核心要点

1. 现有大型语言模型在表达信心方面存在不足，难以评估其错误可能性，影响可靠性。
2. 本研究提出通过扩展链式思维推理来提升模型的信心表达能力，强调慢思维行为的重要性。
3. 实验结果表明，推理模型在33个设置中表现出更好的信心校准，且慢思维行为是提升的关键因素。

## 📝 摘要（中文）

尽管大型语言模型（LLMs）具有优势，但它们在准确表达信心方面常常存在不足，导致难以评估其错误的可能性，从而限制了其可靠性。本研究表明，采用扩展链式思维（CoT）推理的模型在解决问题和准确表达信心方面表现优越。我们对六种推理模型在六个数据集上的表现进行了基准测试，发现它们在36种设置中有33种情况下的信心校准优于非推理模型。详细分析显示，这种校准的提升源于推理模型的慢思维行为，使其能够在CoT过程中动态调整信心，逐步提高准确性。尤其是，推理模型在CoT展开过程中校准效果逐渐提升，而非推理模型则未观察到此趋势。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型在信心表达上的不足，现有方法难以准确评估模型的错误概率，限制了其应用场景。

**核心思路**：论文提出通过引入扩展链式思维（CoT）推理，利用慢思维行为来动态调整模型的信心，从而提高信心表达的准确性。

**技术框架**：整体架构包括数据集选择、推理模型的设计与训练、信心校准的评估等多个阶段，重点在于慢思维行为的引入与分析。

**关键创新**：最重要的创新在于证明了推理模型在信心校准方面的显著提升，尤其是在CoT展开过程中，逐步提高信心的准确性，这是非推理模型所不具备的特性。

**关键设计**：在模型设计中，采用了特定的参数设置和损失函数，以支持慢思维行为的实现，并通过对比实验验证了其有效性。具体细节包括模型的训练策略和评估指标的选择。

## 📊 实验亮点

实验结果显示，推理模型在36种设置中有33种情况下的信心校准优于非推理模型，提升幅度显著。具体而言，去除慢思维行为后，校准效果显著下降，表明慢思维是提升信心表达的关键因素。

## 🎯 应用场景

该研究的潜在应用领域包括智能问答系统、自动化决策支持和人机交互等。通过提高模型的信心表达能力，可以增强用户对模型输出的信任度，进而提升实际应用的可靠性和有效性。未来，该方法可能在更广泛的AI系统中得到应用，推动智能系统的可信赖性发展。

## 📄 摘要（原文）

> Despite their strengths, large language models (LLMs) often fail to communicate their confidence accurately, making it difficult to assess when they might be wrong and limiting their reliability. In this work, we demonstrate that reasoning models that engage in extended chain-of-thought (CoT) reasoning exhibit superior performance not only in problem-solving but also in accurately expressing their confidence. Specifically, we benchmark six reasoning models across six datasets and find that they achieve strictly better confidence calibration than their non-reasoning counterparts in 33 out of the 36 settings. Our detailed analysis reveals that these gains in calibration stem from the slow thinking behaviors of reasoning models (e.g., exploring alternative approaches and backtracking) which enable them to adjust their confidence dynamically throughout their CoT, making it progressively more accurate. In particular, we find that reasoning models become increasingly better calibrated as their CoT unfolds, a trend not observed in non-reasoning models. Moreover, removing slow thinking behaviors from the CoT leads to a significant drop in calibration. Lastly, we show that non-reasoning models also demonstrate enhanced calibration when simply guided to slow think via in-context learning, fully isolating slow thinking as the source of the calibration gains.

