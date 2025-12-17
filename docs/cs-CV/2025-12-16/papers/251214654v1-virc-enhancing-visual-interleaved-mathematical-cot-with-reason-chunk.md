---
layout: default
title: ViRC: Enhancing Visual Interleaved Mathematical CoT with Reason Chunking
---

# ViRC: Enhancing Visual Interleaved Mathematical CoT with Reason Chunking

**arXiv**: [2512.14654v1](https://arxiv.org/abs/2512.14654) | [PDF](https://arxiv.org/pdf/2512.14654.pdf)

**作者**: Lihong Wang, Liangqi Li, Weiwei Feng, Jiamin Wu, Changtao Miao, Tieru Wu, Rui Ma, Bo Zhang, Zhe Li

**分类**: cs.CV

**发布日期**: 2025-12-16

**备注**: Code is available at https://github.com/Leon-LihongWang/ViRC

**🔗 代码/项目**: [GITHUB](https://github.com/Leon-LihongWang/ViRC)

---

## 💡 一句话要点

**提出ViRC框架，通过Reason Chunking机制增强多模态数学推理中的视觉交错思维链**

**关键词**: `多模态推理` `数学思维链` `视觉交错` `Reason Chunking` `Critical Reasoning Units` `渐进式训练` `认知科学启发` `结构化推理`

## 📋 核心要点

1. 现有MLLMs在数学任务中仅从静态图像推理，缺乏动态视觉获取，导致多模态推理能力受限。
2. 提出Reason Chunking机制，将推理过程分解为Critical Reasoning Units，模拟人类逐步验证的认知模式。
3. ViRC-7B模型在多个数学基准上平均提升18.8%，验证了框架在增强多模态数学推理中的有效性。

## 📝 摘要（中文）

思维链显著提升了大型语言模型的推理能力，但在扩展到多模态领域时面临挑战，特别是在数学任务中。现有的多模态大语言模型通常仅从单个静态数学图像进行文本推理，忽视了推理过程中的动态视觉获取。相比之下，人类会反复检查视觉图像，并采用逐步推理来证明中间命题。这种将问题解决过程分解为关键逻辑节点的策略符合认知科学中的米勒定律。受此启发，我们提出了一个用于多模态数学任务的ViRC框架，引入了Reason Chunking机制，将多模态数学思维链结构化为连续的Critical Reasoning Units，以模拟人类专家的问题解决模式。CRUs确保单元内的文本连贯性以验证中间命题，同时跨单元整合视觉信息以生成后续命题并支持结构化推理。为此，我们使用三种视觉工具和四种推理模式构建了CRUX数据集，为每个数学问题提供跨多个推理路径的显式标注CRUs。利用CRUX数据集，我们提出了一种受人类认知学习启发的渐进式训练策略，包括Instructional SFT、Practice SFT和Strategic RL，旨在进一步增强模型的Reason Chunking能力。由此产生的ViRC-7B模型在多个数学基准测试中平均比基线提升了18.8%。代码可在https://github.com/Leon-LihongWang/ViRC获取。

## 🔬 方法详解

ViRC框架的核心是Reason Chunking机制，它将多模态数学思维链分解为连续的Critical Reasoning Units。每个CRU作为一个关键逻辑节点，确保单元内文本连贯性以验证中间命题，同时跨单元整合视觉信息生成后续命题。关键创新包括：构建CRUX数据集，使用三种视觉工具和四种推理模式提供显式标注的CRUs；设计渐进式训练策略，结合Instructional SFT、Practice SFT和Strategic RL，模拟人类认知学习过程。与现有方法的主要区别在于，ViRC强调动态视觉获取和结构化推理，而非仅依赖静态图像的单次文本推理。

## 📊 实验亮点

ViRC-7B模型在多个数学基准测试中实现平均18.8%的性能提升，显著优于基线方法，证明了Reason Chunking机制在增强多模态数学推理中的有效性。

## 🎯 应用场景

该研究可应用于教育技术中的智能数学辅导系统，帮助学生通过视觉交互逐步解决复杂问题；也可用于自动化数学问题求解工具，提升多模态场景下的推理准确性。潜在价值在于推动多模态AI在科学、工程等领域的结构化推理能力发展。

## 📄 摘要（原文）

> CoT has significantly enhanced the reasoning ability of LLMs while it faces challenges when extended to multimodal domains, particularly in mathematical tasks. Existing MLLMs typically perform textual reasoning solely from a single static mathematical image, overlooking dynamic visual acquisition during reasoning. In contrast, humans repeatedly examine visual image and employ step-by-step reasoning to prove intermediate propositions. This strategy of decomposing the problem-solving process into key logical nodes adheres to Miller's Law in cognitive science. Inspired by this insight, we propose a ViRC framework for multimodal mathematical tasks, introducing a Reason Chunking mechanism that structures multimodal mathematical CoT into consecutive Critical Reasoning Units (CRUs) to simulate human expert problem-solving patterns. CRUs ensure intra-unit textual coherence for intermediate proposition verification while integrating visual information across units to generate subsequent propositions and support structured reasoning. To this end, we present CRUX dataset by using three visual tools and four reasoning patterns to provide explicitly annotated CRUs across multiple reasoning paths for each mathematical problem. Leveraging the CRUX dataset, we propose a progressive training strategy inspired by human cognitive learning, which includes Instructional SFT, Practice SFT, and Strategic RL, aimed at further strengthening the Reason Chunking ability of the model.The resulting ViRC-7B model achieves a 18.8\% average improvement over baselines across multiple mathematical benchmarks. Code is available at https://github.com/Leon-LihongWang/ViRC.

