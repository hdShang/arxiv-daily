---
layout: default
title: "SMMILE: An Expert-Driven Benchmark for Multimodal Medical In-Context Learning"
---

# SMMILE: An Expert-Driven Benchmark for Multimodal Medical In-Context Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21355" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21355v2</a>
  <a href="https://arxiv.org/pdf/2506.21355.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21355v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21355v2', 'SMMILE: An Expert-Driven Benchmark for Multimodal Medical In-Context Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Melanie Rieff, Maya Varma, Ossian Rabow, Subathra Adithan, Julie Kim, Ken Chang, Hannah Lee, Nidhi Rohatgi, Christian Bluethgen, Mohamed S. Muneer, Jean-Benoit Delbrouck, Michael Moor

**分类**: cs.LG

**发布日期**: 2025-06-26 (更新: 2025-10-29)

**备注**: NeurIPS 2025 (Datasets & Benchmarks Track)

---

## 💡 一句话要点

**提出SMMILE基准以解决多模态医学任务学习问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `医学影像` `上下文学习` `大语言模型` `医学任务` `基准评估` `专家驱动`

## 📋 核心要点

1. 现有多模态大语言模型在医学任务的上下文学习能力尚不明确，且存在性能不足的问题。
2. SMMILE基准通过专家策划的多模态查询和示例，提供了一个系统化的评估框架，旨在提升医学任务的学习效果。
3. 实验结果显示，当前大多数模型在多模态ICL能力上表现中等偏下，且存在对无关示例的敏感性和近期偏见。

## 📝 摘要（中文）

尽管多模态上下文学习（ICL）在医学领域具有重要潜力，但仍未得到充分探索。临床医生常常需要从有限的示例中适应多样化的专业任务。本文介绍了SMMILE，这是首个专家驱动的多模态ICL基准，涵盖111个问题和517个问答图像三元组，涉及6个医学专业和13种成像模式。通过对15个多模态大语言模型（MLLMs）的评估，发现大多数模型在医学任务中的多模态ICL能力较弱，ICL仅在SMMILE上平均提升8%。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态大语言模型在医学任务中的上下文学习能力不足的问题。现有方法在处理多样化医学任务时，往往缺乏有效的示例和评估标准，导致模型性能不佳。

**核心思路**：论文提出SMMILE基准，通过医学专家策划的多模态查询和示例，系统化地评估和提升多模态ICL能力。这种设计旨在提供更具针对性的任务示例，以帮助模型更好地适应复杂的医学场景。

**技术框架**：SMMILE基准包含111个问题，涵盖6个医学专业和13种成像模式。每个问题都配有多模态查询和示例，形成517个问答图像三元组。SMMILE++是其增强版，包含1038个排列组合问题。

**关键创新**：SMMILE是首个专家驱动的多模态ICL基准，填补了当前医学任务评估的空白。与现有方法相比，SMMILE提供了更丰富的上下文示例，能够更好地反映临床实际需求。

**关键设计**：在实验中，模型的评估不仅关注准确性，还考虑了示例的相关性和排列顺序。研究发现，即使是单个无关示例也可能导致性能下降，而相关示例的顺序对模型表现有显著影响。具体的参数设置和损失函数设计在论文中详细描述。

## 📊 实验亮点

实验结果显示，15个多模态大语言模型在SMMILE基准上的平均提升仅为8%，而在SMMILE++上为9.4%。此外，模型对无关示例的敏感性导致性能下降高达9.5%，而相关示例的排列顺序对性能提升可达71%。

## 🎯 应用场景

SMMILE基准的提出为医学领域的多模态学习提供了新的评估工具，能够帮助研究人员和临床医生更好地理解和应用多模态大语言模型。其潜在应用包括医学影像分析、临床决策支持和个性化医疗等，未来可能推动医学人工智能的发展与应用。

## 📄 摘要（原文）

> Multimodal in-context learning (ICL) remains underexplored despite significant potential for domains such as medicine. Clinicians routinely encounter diverse, specialized tasks requiring adaptation from limited examples, such as drawing insights from a few relevant prior cases or considering a constrained set of differential diagnoses. While multimodal large language models (MLLMs) have shown advances in medical visual question answering (VQA), their ability to learn multimodal tasks from context is largely unknown. We introduce SMMILE, the first expert-driven multimodal ICL benchmark for medical tasks. Eleven medical experts curated problems, each including a multimodal query and multimodal in-context examples as task demonstrations. SMMILE encompasses 111 problems (517 question-image-answer triplets) covering 6 medical specialties and 13 imaging modalities. We further introduce SMMILE++, an augmented variant with 1038 permuted problems. A comprehensive evaluation of 15 MLLMs demonstrates that most models exhibit moderate to poor multimodal ICL ability in medical tasks. In open-ended evaluations, ICL contributes only an 8% average improvement over zero-shot on SMMILE and 9.4% on SMMILE++. We observe a susceptibility for irrelevant in-context examples: even a single noisy or irrelevant example can degrade performance by up to 9.5%. Moreover, we observe that MLLMs are affected by a recency bias, where placing the most relevant example last can lead to substantial performance improvements of up to 71%. Our findings highlight critical limitations and biases in current MLLMs when learning multimodal medical tasks from context. SMMILE is available at https://smmile-benchmark.github.io.

