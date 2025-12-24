---
layout: default
title: "AI-Generated Fall Data: Assessing LLMs and Diffusion Model for Wearable Fall Detection"
---

# AI-Generated Fall Data: Assessing LLMs and Diffusion Model for Wearable Fall Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.04660" class="toolbar-btn" target="_blank">📄 arXiv: 2505.04660v1</a>
  <a href="https://arxiv.org/pdf/2505.04660.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.04660v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.04660v1', 'AI-Generated Fall Data: Assessing LLMs and Diffusion Model for Wearable Fall Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sana Alamgeer, Yasine Souissi, Anne H. H. Ngu

**分类**: cs.CL, cs.CV

**发布日期**: 2025-05-07

---

## 💡 一句话要点

**利用大型语言模型生成合成跌倒数据以提升检测系统性能**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `跌倒检测` `合成数据` `大型语言模型` `长短期记忆` `文本到运动` `扩散模型` `生物力学数据`

## 📋 核心要点

1. 现有跌倒检测系统面临真实跌倒数据稀缺的挑战，尤其是老年人群体的数据不足。
2. 本文提出利用大型语言模型生成合成跌倒数据，并评估其对跌倒检测性能的影响。
3. 实验结果显示，LLM生成的数据在低频设置下表现最佳，而扩散模型生成的数据与真实数据对齐度最高。

## 📝 摘要（中文）

训练跌倒检测系统面临真实跌倒数据稀缺的挑战，尤其是老年人群体的数据。为此，本文探讨了大型语言模型（LLMs）在生成合成跌倒数据方面的潜力。研究评估了文本到运动（T2M）和文本到文本模型在模拟真实跌倒场景中的表现，并生成合成数据集与四个真实基线数据集结合，评估其对长短期记忆（LSTM）模型的跌倒检测性能的影响。结果表明，数据集特征显著影响合成数据的有效性，LLM生成的数据在低频设置下表现最佳，而在高频数据集中则表现不稳定。尽管文本到运动模型生成的生物力学数据更为真实，但其对跌倒检测的影响各异。扩散模型生成的合成数据与真实数据的对齐度最高，但并未始终提升模型性能。

## 🔬 方法详解

**问题定义**：本文旨在解决跌倒检测系统训练中真实跌倒数据稀缺的问题，现有方法在获取老年人跌倒数据方面存在显著不足。

**核心思路**：通过利用大型语言模型生成合成跌倒数据，结合真实数据集来提升跌倒检测模型的性能，探索不同模型生成数据的有效性。

**技术框架**：研究采用文本到运动（T2M）和文本到文本模型生成合成数据，生成的数据与四个真实基线数据集结合，使用长短期记忆（LSTM）模型进行性能评估。

**关键创新**：本文的创新在于首次系统性地评估了不同类型的LLM和扩散模型在合成跌倒数据生成中的有效性，揭示了合成数据对跌倒检测性能的影响。

**关键设计**：在实验中，设置了不同的传感器放置位置和跌倒表现形式，采用了多种数据频率（如20Hz和200Hz）进行对比，分析合成数据的有效性。

## 📊 实验亮点

实验结果表明，LLM生成的合成数据在低频设置（20Hz）下表现最佳，而在高频设置（200Hz）中则表现不稳定。扩散模型生成的数据与真实数据的对齐度最高，但未能始终提升模型性能。整体上，合成数据的有效性受数据集特征和传感器放置的显著影响。

## 🎯 应用场景

该研究的潜在应用领域包括老年人跌倒检测系统的开发与优化，能够为医疗监护、智能家居和健康管理提供支持。通过生成合成数据，研究为提升跌倒检测的准确性和可靠性提供了新的思路，未来可能在智能穿戴设备中得到广泛应用。

## 📄 摘要（原文）

> Training fall detection systems is challenging due to the scarcity of real-world fall data, particularly from elderly individuals. To address this, we explore the potential of Large Language Models (LLMs) for generating synthetic fall data. This study evaluates text-to-motion (T2M, SATO, ParCo) and text-to-text models (GPT4o, GPT4, Gemini) in simulating realistic fall scenarios. We generate synthetic datasets and integrate them with four real-world baseline datasets to assess their impact on fall detection performance using a Long Short-Term Memory (LSTM) model. Additionally, we compare LLM-generated synthetic data with a diffusion-based method to evaluate their alignment with real accelerometer distributions. Results indicate that dataset characteristics significantly influence the effectiveness of synthetic data, with LLM-generated data performing best in low-frequency settings (e.g., 20Hz) while showing instability in high-frequency datasets (e.g., 200Hz). While text-to-motion models produce more realistic biomechanical data than text-to-text models, their impact on fall detection varies. Diffusion-based synthetic data demonstrates the closest alignment to real data but does not consistently enhance model performance. An ablation study further confirms that the effectiveness of synthetic data depends on sensor placement and fall representation. These findings provide insights into optimizing synthetic data generation for fall detection models.

