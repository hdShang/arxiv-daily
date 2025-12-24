---
layout: default
title: "Abstract, Align, Predict: Zero-Shot Stance Detection via Cognitive Inductive Reasoning"
---

# Abstract, Align, Predict: Zero-Shot Stance Detection via Cognitive Inductive Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.13470" class="toolbar-btn" target="_blank">📄 arXiv: 2506.13470v2</a>
  <a href="https://arxiv.org/pdf/2506.13470.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.13470v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.13470v2', 'Abstract, Align, Predict: Zero-Shot Stance Detection via Cognitive Inductive Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bowen Zhang, Jun Ma, Fuqiang Niu, Li Dong, Jinzhou Cao, Genan Dai

**分类**: cs.CL

**发布日期**: 2025-06-16 (更新: 2025-12-21)

---

## 💡 一句话要点

**提出Cognitive Inductive Reasoning框架以解决零样本立场检测问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `零样本学习` `立场检测` `认知推理` `模式图` `自然语言处理`

## 📋 核心要点

1. 现有的零样本立场检测方法在处理复杂推理时表现不足，且难以泛化到新目标。
2. 论文提出的CIRF框架通过认知推理模式将语言输入与抽象推理连接，提升了推理能力。
3. 实验结果显示，CIRF在多个基准上取得了新的最先进结果，并在低资源条件下表现优异。

## 📝 摘要（中文）

零样本立场检测（ZSSD）旨在判断文本对未见目标的立场，这在分析动态和极化的在线讨论中至关重要，尤其是在标注数据有限的情况下。尽管大型语言模型（LLMs）具备零样本能力，但基于提示的方法在处理复杂推理时往往表现不佳，且在新目标上的泛化能力不足。同时，LLM增强的方法仍需大量标注数据，且难以超越实例级模式，限制了其可解释性和适应性。受认知科学启发，我们提出了Cognitive Inductive Reasoning Framework（CIRF），一种通过自动归纳和应用认知推理模式，将语言输入与抽象推理连接起来的框架。CIRF以无监督方式将原始文本中的一阶逻辑模式抽象为多关系模式图，并利用增强模式图内核模型将输入结构与模式模板对齐，实现稳健且可解释的零样本推理。大量在SemEval-2016、VAST和COVID-19-Stance基准上的实验表明，CIRF不仅建立了新的最先进结果，还在仅使用30%的标注数据时实现了可比性能，展示了其在低资源环境中的强泛化能力和效率。

## 🔬 方法详解

**问题定义**：论文要解决的具体问题是如何在缺乏标注数据的情况下进行有效的零样本立场检测。现有方法在复杂推理和新目标泛化方面存在显著不足，限制了其应用。

**核心思路**：论文的核心解决思路是通过Cognitive Inductive Reasoning Framework（CIRF）将语言输入与认知推理模式结合，利用无监督学习抽象出逻辑模式，从而提升推理的准确性和可解释性。

**技术框架**：CIRF的整体架构包括三个主要模块：首先，从原始文本中自动归纳出多关系模式图；其次，使用模式图内核模型对输入结构与模式模板进行对齐；最后，进行零样本推理以获得立场判断。

**关键创新**：CIRF的最重要技术创新在于其无监督的模式抽象能力和模式图内核模型的结合，这使得其在处理复杂推理时具备更强的适应性和解释能力，与现有方法相比具有显著优势。

**关键设计**：在关键设计上，CIRF采用了无监督学习方法进行模式抽象，使用了特定的损失函数来优化模式对齐过程，并设计了适应性强的网络结构以支持多关系模式的处理。具体参数设置和网络结构细节在论文中进行了详细描述。

## 📊 实验亮点

实验结果表明，CIRF在SemEval-2016、VAST和COVID-19-Stance基准上取得了新的最先进结果，且在仅使用30%的标注数据时，性能与全量数据相当，展示了其在低资源环境下的强泛化能力和高效性。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体分析、舆情监测和在线评论情感分析等。通过提升零样本立场检测的能力，CIRF能够帮助研究人员和企业更好地理解公众对特定事件或话题的态度，从而在决策和策略制定中发挥重要作用。未来，该方法有望在更广泛的自然语言处理任务中得到应用，推动相关领域的发展。

## 📄 摘要（原文）

> Zero-shot stance detection (ZSSD) seeks to determine the stance of text toward previously unseen targets, a task critical for analyzing dynamic and polarized online discourse with limited labeled data. While large language models (LLMs) offer zero-shot capabilities, prompting-based approaches often fall short in handling complex reasoning and lack robust generalization to novel targets. Meanwhile, LLM-enhanced methods still require substantial labeled data and struggle to move beyond instance-level patterns, limiting their interpretability and adaptability. Inspired by cognitive science, we propose the Cognitive Inductive Reasoning Framework (CIRF), a schema-driven method that bridges linguistic inputs and abstract reasoning via automatic induction and application of cognitive reasoning schemas. CIRF abstracts first-order logic patterns from raw text into multi-relational schema graphs in an unsupervised manner, and leverages a schema-enhanced graph kernel model to align input structures with schema templates for robust, interpretable zero-shot inference. Extensive experiments on SemEval-2016, VAST, and COVID-19-Stance benchmarks demonstrate that CIRF not only establishes new state-of-the-art results, but also achieves comparable performance with just 30\% of the labeled data, demonstrating its strong generalization and efficiency in low-resource settings.

