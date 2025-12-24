---
layout: default
title: "Dissecting Bias in LLMs: A Mechanistic Interpretability Perspective"
---

# Dissecting Bias in LLMs: A Mechanistic Interpretability Perspective

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05166" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05166v2</a>
  <a href="https://arxiv.org/pdf/2506.05166.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05166v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05166v2', 'Dissecting Bias in LLMs: A Mechanistic Interpretability Perspective')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bhavik Chandna, Zubair Bashir, Procheta Sen

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-05 (更新: 2025-06-06)

---

## 💡 一句话要点

**通过机械解释方法分析大型语言模型中的偏见**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `偏见分析` `机械解释` `自然语言处理` `模型公平性`

## 📋 核心要点

1. 现有大型语言模型在处理社会和性别偏见时存在显著不足，导致输出结果的不公正性。
2. 本文通过机械解释的方法，系统分析模型内部结构，识别出导致偏见的具体组件。
3. 实验结果表明，移除偏见相关组件可有效减少偏见输出，同时影响其他自然语言处理任务的性能。

## 📝 摘要（中文）

大型语言模型（LLMs）通常表现出社会、人口和性别偏见，这往往是由于训练数据的影响。本文采用机械解释的方法，分析这些偏见在GPT-2和Llama2等模型中的结构性表现。我们重点关注人口和性别偏见，探索不同指标以识别导致偏见行为的内部边缘。通过系统的消融实验，我们证明偏见相关的计算高度局部化，通常集中在少数层中。此外，识别的组件在不同的微调设置中会发生变化，甚至与偏见无关的设置也会影响。最后，我们展示了移除这些组件不仅减少了偏见输出，还影响了其他自然语言处理任务，如命名实体识别和语言可接受性判断，因为这些任务与重要组件共享。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型中存在的社会、人口和性别偏见问题。现有方法未能有效识别和消除这些偏见，导致模型输出不公正。

**核心思路**：通过机械解释的方法，分析模型内部结构，识别出与偏见相关的计算组件，并评估其在不同数据集和语言变体中的稳定性和局部化特征。

**技术框架**：研究首先定义偏见的度量标准，然后通过系统的消融实验，分析不同层次的偏见表现，最后评估移除偏见组件对其他任务的影响。

**关键创新**：本研究的创新点在于揭示了偏见计算的高度局部化特征，且这些特征在不同的微调设置中会发生变化，提供了对偏见的深刻理解。

**关键设计**：采用了多种指标来评估偏见表现，设计了系统的消融实验以验证偏见组件的影响，确保了实验的全面性和可靠性。

## 📊 实验亮点

实验结果显示，移除偏见相关组件后，模型的偏见输出显著减少，且在命名实体识别和语言可接受性判断等任务中，性能变化明显。这表明偏见组件与其他任务存在重要的共享关系，影响了模型的整体表现。

## 🎯 应用场景

该研究为大型语言模型的公平性提供了新的视角，潜在应用于自然语言处理的各个领域，如社交媒体内容审核、招聘系统和教育技术等。通过识别和消除偏见，可以提高模型的公正性和可信度，促进更广泛的社会接受度。

## 📄 摘要（原文）

> Large Language Models (LLMs) are known to exhibit social, demographic, and gender biases, often as a consequence of the data on which they are trained. In this work, we adopt a mechanistic interpretability approach to analyze how such biases are structurally represented within models such as GPT-2 and Llama2. Focusing on demographic and gender biases, we explore different metrics to identify the internal edges responsible for biased behavior. We then assess the stability, localization, and generalizability of these components across dataset and linguistic variations. Through systematic ablations, we demonstrate that bias-related computations are highly localized, often concentrated in a small subset of layers. Moreover, the identified components change across fine-tuning settings, including those unrelated to bias. Finally, we show that removing these components not only reduces biased outputs but also affects other NLP tasks, such as named entity recognition and linguistic acceptability judgment because of the sharing of important components with these tasks.

