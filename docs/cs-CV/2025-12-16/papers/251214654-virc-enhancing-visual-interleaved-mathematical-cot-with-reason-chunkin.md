---
layout: default
title: ViRC: Enhancing Visual Interleaved Mathematical CoT with Reason Chunking
---

# ViRC: Enhancing Visual Interleaved Mathematical CoT with Reason Chunking

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14654" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14654</a>
  <a href="https://arxiv.org/pdf/2512.14654.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14654" onclick="toggleFavorite(this, '2512.14654', 'ViRC: Enhancing Visual Interleaved Mathematical CoT with Reason Chunking')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lihong Wang, Liangqi Li, Weiwei Feng, Jiamin Wu, Changtao Miao, Tieru Wu, Rui Ma, Bo Zhang, Zhe Li

**分类**: cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出ViRC框架，通过Reason Chunking增强视觉交错数学CoT推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `数学推理` `视觉交错` `Reason Chunking` `认知科学` `大语言模型` `CRUX数据集`

## 📋 核心要点

1. 现有MLLM在处理多模态数学问题时，缺乏对动态视觉信息的有效利用，限制了推理能力。
2. ViRC框架通过Reason Chunking机制，将推理过程分解为关键推理单元CRU，模拟人类专家逐步验证中间命题的模式。
3. 实验结果表明，ViRC-7B模型在多个数学基准测试中取得了显著的性能提升，平均提升幅度达到18.8%。

## 📝 摘要（中文）

本文提出ViRC框架，旨在提升多模态大语言模型在数学任务中的推理能力。现有MLLM通常仅依赖静态数学图像进行文本推理，忽略了推理过程中动态视觉信息的获取。ViRC框架受到人类专家解决问题模式的启发，引入Reason Chunking机制，将多模态数学CoT分解为连续的关键推理单元(CRU)，模拟人类逐步验证中间命题的过程。CRU确保单元内文本连贯性，并在单元间整合视觉信息以生成后续命题，支持结构化推理。为此，本文构建了CRUX数据集，使用三种视觉工具和四种推理模式，为每个数学问题提供显式标注的CRU。基于CRUX数据集，提出了一种受人类认知学习启发的渐进式训练策略，包括Instructional SFT、Practice SFT和Strategic RL，旨在进一步加强Reason Chunking能力。ViRC-7B模型在多个数学基准测试中实现了平均18.8%的性能提升。

## 🔬 方法详解

**问题定义**：现有的大型语言模型在处理视觉交错的数学问题时，通常只依赖于单一的静态图像，而忽略了人类在解决此类问题时会反复观察图像并逐步推理的动态过程。这导致模型无法充分利用视觉信息，影响了推理的准确性和效率。现有方法的痛点在于缺乏对视觉信息的动态建模和利用，以及缺乏对推理过程的结构化组织。

**核心思路**：ViRC的核心思路是模仿人类专家解决数学问题的模式，将复杂的推理过程分解为一系列关键的推理单元（CRU）。每个CRU专注于验证一个中间命题，并在单元内部保持文本连贯性。同时，CRU之间通过整合视觉信息来生成后续命题，从而实现结构化的推理过程。这种Reason Chunking机制借鉴了认知科学中的米勒定律，旨在提高模型的推理效率和准确性。

**技术框架**：ViRC框架主要包含三个部分：CRUX数据集的构建、Reason Chunking机制的引入以及渐进式训练策略。CRUX数据集提供了显式标注的CRU，用于训练模型学习Reason Chunking能力。Reason Chunking机制将推理过程分解为连续的CRU，每个CRU包含视觉信息和文本推理。渐进式训练策略包括Instructional SFT、Practice SFT和Strategic RL三个阶段，逐步提升模型的Reason Chunking能力。

**关键创新**：ViRC最重要的技术创新点在于Reason Chunking机制。与现有方法相比，ViRC不再依赖于单一的静态图像进行推理，而是通过动态地整合视觉信息和结构化地组织推理过程来提高模型的推理能力。Reason Chunking机制使得模型能够更好地模拟人类专家解决问题的模式，从而提高推理的准确性和效率。

**关键设计**：CRUX数据集使用了三种视觉工具（未知）和四种推理模式（未知）来标注CRU。渐进式训练策略中的Instructional SFT阶段使用CRUX数据集进行监督学习，Practice SFT阶段使用更复杂的数学问题进行训练，Strategic RL阶段使用强化学习来优化模型的推理策略。具体的参数设置、损失函数和网络结构等技术细节在论文中未详细说明，属于未知信息。

## 📊 实验亮点

ViRC-7B模型在多个数学基准测试中取得了显著的性能提升，平均提升幅度达到18.8%。这一结果表明，Reason Chunking机制能够有效地提高模型的推理能力。此外，CRUX数据集的构建也为多模态数学推理领域的研究提供了有价值的资源。

## 🎯 应用场景

ViRC框架具有广泛的应用前景，可应用于智能教育、数学辅助工具、科学研究等领域。例如，可以开发智能辅导系统，帮助学生理解和解决复杂的数学问题；可以应用于科学研究，辅助科学家进行数据分析和模型推理；还可以应用于机器人视觉领域，提高机器人对复杂环境的理解和推理能力。该研究的实际价值在于提升多模态大语言模型在数学推理方面的能力，为相关领域的发展提供新的思路。

## 📄 摘要（原文）

> CoT has significantly enhanced the reasoning ability of LLMs while it faces challenges when extended to multimodal domains, particularly in mathematical tasks. Existing MLLMs typically perform textual reasoning solely from a single static mathematical image, overlooking dynamic visual acquisition during reasoning. In contrast, humans repeatedly examine visual image and employ step-by-step reasoning to prove intermediate propositions. This strategy of decomposing the problem-solving process into key logical nodes adheres to Miller's Law in cognitive science. Inspired by this insight, we propose a ViRC framework for multimodal mathematical tasks, introducing a Reason Chunking mechanism that structures multimodal mathematical CoT into consecutive Critical Reasoning Units (CRUs) to simulate human expert problem-solving patterns. CRUs ensure intra-unit textual coherence for intermediate proposition verification while integrating visual information across units to generate subsequent propositions and support structured reasoning. To this end, we present CRUX dataset by using three visual tools and four reasoning patterns to provide explicitly annotated CRUs across multiple reasoning paths for each mathematical problem. Leveraging the CRUX dataset, we propose a progressive training strategy inspired by human cognitive learning, which includes Instructional SFT, Practice SFT, and Strategic RL, aimed at further strengthening the Reason Chunking ability of thethis http URLresulting ViRC-7B model achieves a 18.8\% average improvement over baselines across multiple mathematical benchmarks. Code is available atthis https URL.

