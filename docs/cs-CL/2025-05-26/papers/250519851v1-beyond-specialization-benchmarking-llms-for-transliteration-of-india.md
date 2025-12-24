---
layout: default
title: "Beyond Specialization: Benchmarking LLMs for Transliteration of Indian Languages"
---

# Beyond Specialization: Benchmarking LLMs for Transliteration of Indian Languages

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.19851" class="toolbar-btn" target="_blank">📄 arXiv: 2505.19851v1</a>
  <a href="https://arxiv.org/pdf/2505.19851.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.19851v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.19851v1', 'Beyond Specialization: Benchmarking LLMs for Transliteration of Indian Languages')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gulfarogh Azam, Mohd Sadique, Saif Ali, Mohammad Nadeem, Erik Cambria, Shahab Saquib Sohail, Mohammad Sultan Alam

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-26

---

## 💡 一句话要点

**评估大型语言模型在印度语言音译中的表现**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `音译` `大型语言模型` `多语言处理` `自然语言处理` `模型评估`

## 📋 核心要点

1. 现有的音译模型在处理多样化语言时存在局限性，尤其是在印度这样的语言环境中。
2. 论文提出通过评估大型语言模型在音译任务中的表现，探索其在没有专门训练的情况下的潜力。
3. 实验结果显示，GPT系列模型在大多数情况下优于IndicXlit，且微调后在特定语言上的表现显著提升。

## 📝 摘要（中文）

音译是将文本从一种书写系统映射到另一种书写系统的过程，在多语言自然语言处理中特别重要，尤其是在语言多样性丰富的印度。尽管专门模型如IndicXlit取得了显著进展，但大型语言模型（LLMs）在此任务上也展现出潜力。本文系统评估了包括GPT-4o、GPT-4.5、GPT-4.1等在内的多种LLMs在十种主要印度语言上的表现，结果表明GPT系列模型在大多数情况下优于其他模型和IndicXlit，且对特定语言的微调显著提升了性能。通过错误分析和在噪声条件下的鲁棒性测试，进一步揭示了LLMs相较于专门模型的优势，强调了基础模型在多种专门应用中的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决在多语言环境中音译的准确性问题，现有的专门模型在处理多样化语言时存在局限性，尤其是在印度的复杂语言背景下。

**核心思路**：通过系统评估大型语言模型（LLMs）在音译任务中的表现，探索其在没有显式任务特定训练的情况下的有效性，验证其作为通用模型的潜力。

**技术框架**：研究使用了标准基准数据集（如Dakshina和Aksharantar），对比了多种LLMs的表现，评估指标包括Top-1准确率和字符错误率。

**关键创新**：最重要的创新在于将大型语言模型与专门音译模型进行系统对比，发现GPT系列模型在大多数情况下表现优越，且微调能够显著提升特定语言的性能。

**关键设计**：实验中采用了标准的评估指标，设置了不同的模型参数，并进行了广泛的错误分析和鲁棒性测试，以验证模型在噪声条件下的表现。

## 📊 实验亮点

实验结果显示，GPT系列模型在大多数情况下的表现优于IndicXlit，具体而言，GPT-4o在特定语言上的微调后性能提升显著。此外，错误分析表明LLMs在噪声条件下的鲁棒性优于专门模型，进一步验证了其广泛应用的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括多语言翻译、语音识别和跨文化交流等。通过提升音译的准确性，能够促进不同语言用户之间的沟通，增强多语言处理系统的实用性，未来可能对教育、信息传播等领域产生深远影响。

## 📄 摘要（原文）

> Transliteration, the process of mapping text from one script to another, plays a crucial role in multilingual natural language processing, especially within linguistically diverse contexts such as India. Despite significant advancements through specialized models like IndicXlit, recent developments in large language models suggest a potential for general-purpose models to excel at this task without explicit task-specific training. The current work systematically evaluates the performance of prominent LLMs, including GPT-4o, GPT-4.5, GPT-4.1, Gemma-3-27B-it, and Mistral-Large against IndicXlit, a state-of-the-art transliteration model, across ten major Indian languages. Experiments utilized standard benchmarks, including Dakshina and Aksharantar datasets, with performance assessed via Top-1 Accuracy and Character Error Rate. Our findings reveal that while GPT family models generally outperform other LLMs and IndicXlit for most instances. Additionally, fine-tuning GPT-4o improves performance on specific languages notably. An extensive error analysis and robustness testing under noisy conditions further elucidate strengths of LLMs compared to specialized models, highlighting the efficacy of foundational models for a wide spectrum of specialized applications with minimal overhead.

