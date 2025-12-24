---
layout: default
title: "ViRC: Enhancing Visual Interleaved Mathematical CoT with Reason Chunking"
---

# ViRC: Enhancing Visual Interleaved Mathematical CoT with Reason Chunking

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14654" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14654v1</a>
  <a href="https://arxiv.org/pdf/2512.14654.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14654v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14654v1', 'ViRC: Enhancing Visual Interleaved Mathematical CoT with Reason Chunking')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lihong Wang, Liangqi Li, Weiwei Feng, Jiamin Wu, Changtao Miao, Tieru Wu, Rui Ma, Bo Zhang, Zhe Li

**分类**: cs.CV

**发布日期**: 2025-12-16

**备注**: Code is available at https://github.com/Leon-LihongWang/ViRC

**🔗 代码/项目**: [GITHUB](https://github.com/Leon-LihongWang/ViRC)

---

## 💡 一句话要点

**提出ViRC框架，通过Reason Chunking增强视觉交错数学CoT推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `视觉推理` `数学推理` `链式思考` `Reason Chunking` `指令微调` `强化学习`

## 📋 核心要点

1. 现有多模态LLM在数学任务中，缺乏对推理过程中动态视觉信息的有效利用，限制了推理能力。
2. ViRC框架通过Reason Chunking机制，将推理过程分解为关键推理单元CRU，模拟人类专家逐步推理模式。
3. 实验结果表明，ViRC-7B模型在多个数学基准测试中，相比基线模型平均提升了18.8%的性能。

## 📝 摘要（中文）

本文提出ViRC框架，旨在提升多模态大型语言模型在数学任务中的推理能力。现有MLLM通常仅基于静态数学图像进行文本推理，忽略了推理过程中动态视觉信息的获取。ViRC框架受到人类专家解决问题模式的启发，引入Reason Chunking机制，将多模态数学CoT分解为连续的关键推理单元(CRU)，模拟人类逐步验证中间命题的过程。CRU确保单元内文本连贯性，用于中间命题验证，同时整合跨单元的视觉信息，生成后续命题并支持结构化推理。为此，本文构建了CRUX数据集，使用三种视觉工具和四种推理模式，为每个数学问题提供显式标注的CRU。此外，本文提出了一种受人类认知学习启发的渐进式训练策略，包括Instructional SFT、Practice SFT和Strategic RL，旨在进一步加强模型的Reason Chunking能力。ViRC-7B模型在多个数学基准测试中实现了平均18.8%的性能提升。

## 🔬 方法详解

**问题定义**：现有MLLM在解决视觉数学问题时，主要依赖于单一的静态图像，缺乏对动态视觉信息的利用，无法模拟人类在解决问题时反复观察图像并逐步推理的过程。这种静态推理方式限制了模型在复杂视觉数学问题上的表现。

**核心思路**：ViRC的核心思路是模仿人类专家解决问题的模式，将复杂的推理过程分解为一系列小的、连贯的推理步骤，即Reason Chunking。每个步骤对应一个关键推理单元(CRU)，CRU内部进行文本推理，CRU之间通过视觉信息进行连接，从而实现更有效的多模态推理。

**技术框架**：ViRC框架主要包含数据构建和模型训练两个部分。数据构建方面，作者构建了CRUX数据集，该数据集包含多个数学问题，并对每个问题标注了多个推理路径，每个推理路径由一系列CRU组成。模型训练方面，采用了一种渐进式训练策略，包括Instructional SFT、Practice SFT和Strategic RL三个阶段。Instructional SFT阶段使用CRUX数据集进行指令微调，使模型初步具备Reason Chunking能力。Practice SFT阶段使用更多的数据进行训练，提高模型的泛化能力。Strategic RL阶段使用强化学习进一步优化模型的推理策略。

**关键创新**：ViRC的关键创新在于Reason Chunking机制和CRUX数据集。Reason Chunking机制将复杂的推理过程分解为一系列小的、连贯的推理步骤，使得模型能够更好地利用视觉信息进行推理。CRUX数据集为模型的训练提供了高质量的标注数据，使得模型能够更好地学习Reason Chunking能力。

**关键设计**：CRU的设计是关键。每个CRU包含文本和视觉信息，文本信息用于描述当前的推理步骤，视觉信息用于支持当前的推理步骤。在模型训练过程中，作者使用了交叉熵损失函数来优化模型的文本生成能力，并使用了对比学习损失函数来优化模型的视觉表示能力。具体的网络结构和参数设置在论文中有详细描述。

## 📊 实验亮点

ViRC-7B模型在多个数学基准测试中取得了显著的性能提升，平均提升幅度达到18.8%。具体而言，在某些数据集上，ViRC-7B模型的性能甚至超过了更大的模型。这些实验结果表明，ViRC框架能够有效地提升多模态LLM在数学任务中的推理能力。

## 🎯 应用场景

ViRC框架可应用于各种需要视觉和数学推理的场景，例如自动解题机器人、智能教育系统、科学研究辅助工具等。该研究有助于提升机器在复杂多模态任务中的推理能力，推动人工智能在科学、教育等领域的应用。

## 📄 摘要（原文）

> CoT has significantly enhanced the reasoning ability of LLMs while it faces challenges when extended to multimodal domains, particularly in mathematical tasks. Existing MLLMs typically perform textual reasoning solely from a single static mathematical image, overlooking dynamic visual acquisition during reasoning. In contrast, humans repeatedly examine visual image and employ step-by-step reasoning to prove intermediate propositions. This strategy of decomposing the problem-solving process into key logical nodes adheres to Miller's Law in cognitive science. Inspired by this insight, we propose a ViRC framework for multimodal mathematical tasks, introducing a Reason Chunking mechanism that structures multimodal mathematical CoT into consecutive Critical Reasoning Units (CRUs) to simulate human expert problem-solving patterns. CRUs ensure intra-unit textual coherence for intermediate proposition verification while integrating visual information across units to generate subsequent propositions and support structured reasoning. To this end, we present CRUX dataset by using three visual tools and four reasoning patterns to provide explicitly annotated CRUs across multiple reasoning paths for each mathematical problem. Leveraging the CRUX dataset, we propose a progressive training strategy inspired by human cognitive learning, which includes Instructional SFT, Practice SFT, and Strategic RL, aimed at further strengthening the Reason Chunking ability of the model.The resulting ViRC-7B model achieves a 18.8\% average improvement over baselines across multiple mathematical benchmarks. Code is available at https://github.com/Leon-LihongWang/ViRC.

