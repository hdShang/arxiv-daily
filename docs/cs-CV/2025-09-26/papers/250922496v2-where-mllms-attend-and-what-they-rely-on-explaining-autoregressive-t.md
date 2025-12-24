---
layout: default
title: "Where MLLMs Attend and What They Rely On: Explaining Autoregressive Token Generation"
---

# Where MLLMs Attend and What They Rely On: Explaining Autoregressive Token Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22496" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22496v2</a>
  <a href="https://arxiv.org/pdf/2509.22496.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22496v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22496v2', 'Where MLLMs Attend and What They Rely On: Explaining Autoregressive Token Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ruoyu Chen, Xiaoqing Guo, Kangwei Liu, Siyuan Liang, Shiming Liu, Qunli Zhang, Hua Zhang, Xiaochun Cao

**分类**: cs.CV

**发布日期**: 2025-09-26 (更新: 2025-10-17)

**🔗 代码/项目**: [PROJECT_PAGE](https://ruoyuchen10.github.io/EAGLE/)

---

## 💡 一句话要点

**EAGLE：一种轻量级框架，用于解释多模态大语言模型自回归token生成过程。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `可解释性` `自回归生成` `视觉归因` `模态感知分析`

## 📋 核心要点

1. 现有的多模态大语言模型缺乏对生成token与视觉模态依赖程度的深入理解，限制了解释性和可靠性。
2. EAGLE框架通过量化语言先验和感知证据的影响，将token归因于紧凑的感知区域，从而解释自回归token生成。
3. 实验表明，EAGLE在忠实性、定位和幻觉诊断方面优于现有方法，且所需GPU内存更少，具有实用性。

## 📝 摘要（中文）

多模态大语言模型（MLLM）在视觉输入与自然语言输出的对齐方面表现出卓越的能力。然而，对于生成的token在多大程度上依赖于视觉模态的理解仍然不足，这限制了解释性和可靠性。本文提出EAGLE，一个轻量级的黑盒框架，用于解释MLLM中的自回归token生成。EAGLE将任何选定的token归因于紧凑的感知区域，同时量化语言先验和感知证据的相对影响。该框架引入了一个目标函数，统一了充分性（洞察力得分）和不可或缺性（必要性得分），通过对稀疏化图像区域的贪婪搜索进行优化，以实现忠实和高效的归因。除了空间归因之外，EAGLE还执行模态感知分析，解耦token所依赖的内容，从而提供对模型决策的细粒度解释。在开源MLLM上进行的大量实验表明，EAGLE在忠实性、定位和幻觉诊断方面始终优于现有方法，同时需要更少的GPU内存。这些结果突出了其在提高MLLM可解释性方面的有效性和实用性。代码将在https://ruoyuchen10.github.io/EAGLE/发布。

## 🔬 方法详解

**问题定义**：多模态大语言模型在生成文本时，我们难以理解每个token的生成究竟依赖于哪些视觉信息，以及语言先验知识在其中起到的作用。现有方法通常无法提供细粒度的解释，或者计算成本过高，难以应用。

**核心思路**：EAGLE的核心思路是通过量化每个token生成过程中视觉信息和语言先验知识的贡献，从而解释模型的决策过程。它通过寻找对token生成影响最大的图像区域来实现视觉归因，并结合模态感知分析来区分不同模态的影响。

**技术框架**：EAGLE框架主要包含以下几个阶段：1) **Token选择**：选择需要解释的目标token。2) **区域稀疏化**：对输入图像进行区域划分，并逐步稀疏化，即移除部分区域。3) **目标函数优化**：设计一个目标函数，同时考虑充分性（移除重要区域会导致token生成概率显著下降）和不可或缺性（保留重要区域能有效提升token生成概率）。通过贪婪搜索，找到对目标token影响最大的稀疏化图像区域。4) **模态感知分析**：分析token生成对不同模态的依赖程度，区分视觉信息和语言先验知识的贡献。

**关键创新**：EAGLE的关键创新在于其目标函数的设计，它同时考虑了充分性和不可或缺性，从而能够更准确地定位对token生成至关重要的图像区域。此外，EAGLE的模态感知分析能够提供更细粒度的解释，揭示模型决策过程中不同模态的作用。

**关键设计**：EAGLE使用贪婪搜索来优化目标函数，寻找最优的稀疏化图像区域。目标函数结合了insight score（衡量移除区域后token生成概率的下降程度）和necessity score（衡量保留区域后token生成概率的提升程度）。框架采用轻量级设计，降低了计算成本，使其能够应用于大规模MLLM。

## 📊 实验亮点

实验结果表明，EAGLE在忠实性、定位和幻觉诊断方面均优于现有方法。例如，在视觉归因任务中，EAGLE能够更准确地定位对token生成至关重要的图像区域。同时，EAGLE所需的GPU内存显著低于其他方法，使其更具实用性。

## 🎯 应用场景

EAGLE可用于提高多模态大语言模型的可解释性和可靠性，例如在医疗诊断、自动驾驶等安全攸关的领域，帮助用户理解模型的决策依据，从而增强信任。此外，EAGLE还可以用于诊断模型的幻觉问题，并指导模型训练，提升生成质量。

## 📄 摘要（原文）

> Multimodal large language models (MLLMs) have demonstrated remarkable capabilities in aligning visual inputs with natural language outputs. Yet, the extent to which generated tokens depend on visual modalities remains poorly understood, limiting interpretability and reliability. In this work, we present EAGLE, a lightweight black-box framework for explaining autoregressive token generation in MLLMs. EAGLE attributes any selected tokens to compact perceptual regions while quantifying the relative influence of language priors and perceptual evidence. The framework introduces an objective function that unifies sufficiency (insight score) and indispensability (necessity score), optimized via greedy search over sparsified image regions for faithful and efficient attribution. Beyond spatial attribution, EAGLE performs modality-aware analysis that disentangles what tokens rely on, providing fine-grained interpretability of model decisions. Extensive experiments across open-source MLLMs show that EAGLE consistently outperforms existing methods in faithfulness, localization, and hallucination diagnosis, while requiring substantially less GPU memory. These results highlight its effectiveness and practicality for advancing the interpretability of MLLMs. The code will be released at https://ruoyuchen10.github.io/EAGLE/.

