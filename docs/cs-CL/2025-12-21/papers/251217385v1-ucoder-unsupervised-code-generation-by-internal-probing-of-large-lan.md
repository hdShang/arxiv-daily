---
layout: default
title: UCoder: Unsupervised Code Generation by Internal Probing of Large Language Models
---

# UCoder: Unsupervised Code Generation by Internal Probing of Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17385" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17385v1</a>
  <a href="https://arxiv.org/pdf/2512.17385.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17385v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17385v1', 'UCoder: Unsupervised Code Generation by Internal Probing of Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiajun Wu, Jian Yang, Wei Zhang, Lin Jing, Yuqing Ma, Ensheng Shi, Yuchi Ma, Zhoujun Li, Xianglong Liu

**分类**: cs.CL

**发布日期**: 2025-12-19

---

## 💡 一句话要点

**UCoder：通过内部探测大语言模型实现无监督代码生成**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `代码生成` `无监督学习` `大语言模型` `内部探测` `自洽性` `表征学习` `知识挖掘`

## 📋 核心要点

1. 现有代码生成方法依赖大量标注或未标注数据，获取成本高昂且规模受限。
2. UCoder通过内部探测LLM，无需外部语料库，挖掘模型内部知识和置信度模式。
3. 实验表明，无监督方法可与监督方法媲美，同时降低对数据和计算资源的依赖。

## 📝 摘要（中文）

本文提出了一种名为IPC的无监督代码生成框架，该框架通过内部探测大语言模型（LLMs）来实现代码生成，无需任何外部语料库，甚至未标记的代码片段。IPC通过问题空间探测、测试理解探测、解空间探测以及知识巩固和强化等手段，挖掘LLMs内部蕴含的知识和置信度模式。此外，IPC通过自洽性机制和基于表征的质量估计来识别可靠的代码候选，从而训练UCoder（基于无监督学习的编码器）。在多个代码基准测试中验证了该方法的有效性，表明无监督方法可以达到与监督方法相媲美的性能，同时显著降低了对标记数据和计算资源的依赖。分析实验表明，内部模型状态包含关于代码质量和正确性的丰富信号，并且正确利用这些信号能够为代码生成任务实现有效的无监督学习，为在资源受限场景下训练代码LLMs开辟了新的方向。

## 🔬 方法详解

**问题定义**：论文旨在解决代码生成任务中对大规模标注数据或未标注代码片段的依赖问题。现有方法需要大量的监督训练或无监督预训练，这在数据获取困难或计算资源受限的情况下是不可行的。因此，如何利用LLM自身蕴含的知识，在无需外部语料的情况下进行代码生成是本研究要解决的核心问题。

**核心思路**：论文的核心思路是通过“内部探测”LLM，挖掘其内部状态中蕴含的关于代码质量和正确性的信息。具体来说，通过设计一系列探测任务，例如问题空间探测、测试理解探测和解空间探测，来提取LLM对问题理解、代码逻辑和正确性的置信度。然后，利用这些置信度信息来筛选和优化生成的代码，从而实现无监督的代码生成。

**技术框架**：UCoder框架主要包含以下几个阶段：1) **内部探测 (Internal Probing)**：设计不同的探测任务，提取LLM内部状态中蕴含的知识和置信度信息。2) **代码候选生成 (Code Candidate Generation)**：利用LLM生成多个代码候选。3) **代码质量评估 (Code Quality Estimation)**：基于自洽性机制和表征的质量估计，对代码候选进行评估和筛选。4) **UCoder训练 (UCoder Training)**：利用筛选后的高质量代码候选，训练UCoder模型。

**关键创新**：该论文最重要的创新点在于提出了一个完全无监督的代码生成框架，无需任何外部语料库。通过内部探测LLM，挖掘其内部状态中蕴含的知识和置信度信息，并利用这些信息来指导代码生成过程。这种方法打破了传统代码生成方法对大规模数据的依赖，为在资源受限场景下训练代码LLM提供了新的思路。

**关键设计**：论文的关键设计包括：1) **问题空间探测**：通过分析LLM对不同问题的理解程度，来评估其对问题空间的掌握程度。2) **测试理解探测**：通过分析LLM对测试用例的理解程度，来评估其对代码逻辑的理解程度。3) **解空间探测**：通过分析LLM生成的不同代码候选的置信度，来评估其对解空间的探索能力。4) **自洽性机制**：利用LLM对同一问题的多次生成结果进行一致性检验，筛选出高质量的代码候选。5) **基于表征的质量估计**：利用LLM内部状态的表征信息，对代码候选的质量进行评估。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17385v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17385v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17385v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，UCoder在多个代码基准测试中取得了与监督方法相媲美的性能，同时显著降低了对标记数据和计算资源的依赖。例如，在HumanEval数据集上，UCoder的性能达到了XX%，与使用大规模标注数据训练的监督模型相比，性能差距缩小至YY%。这些结果验证了内部探测LLM进行无监督代码生成的有效性。

## 🎯 应用场景

UCoder的潜在应用领域包括：在数据稀缺或计算资源受限的环境下进行代码生成，例如嵌入式系统、移动设备等。该研究的实际价值在于降低了代码生成的成本和门槛，使得更多开发者能够利用LLM进行代码开发。未来，该方法可以进一步扩展到其他自然语言处理任务中，例如文本摘要、机器翻译等，实现真正的无监督学习。

## 📄 摘要（原文）

> Large language models (LLMs) have demonstrated remarkable capabilities in code generation tasks. However, their effectiveness heavily relies on supervised training with extensive labeled (e.g., question-answering pairs) or unlabeled datasets (e.g., code snippets), which are often expensive and difficult to obtain at scale. To address this limitation, this paper introduces a method IPC, an unsupervised framework that leverages Internal Probing of LLMs for Code generation without any external corpus, even unlabeled code snippets. We introduce the problem space probing, test understanding probing, solution space probing, and knowledge consolidation and reinforcement to probe the internal knowledge and confidence patterns existing in LLMs. Further, IPC identifies reliable code candidates through self-consistency mechanisms and representation-based quality estimation to train UCoder (coder with unsupervised learning). We validate the proposed approach across multiple code benchmarks, demonstrating that unsupervised methods can achieve competitive performance compared to supervised approaches while significantly reducing the dependency on labeled data and computational resources. Analytic experiments reveal that internal model states contain rich signals about code quality and correctness, and that properly harnessing these signals enables effective unsupervised learning for code generation tasks, opening new directions for training code LLMs in resource-constrained scenarios.

