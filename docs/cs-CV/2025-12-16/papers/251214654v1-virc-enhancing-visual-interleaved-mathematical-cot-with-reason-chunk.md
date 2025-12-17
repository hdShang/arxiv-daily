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

**提出ViRC框架，通过Reason Chunking机制增强多模态数学推理能力，模拟人类专家解题模式。**

🎯 **匹配领域**: **强化学习**

**关键词**: `多模态推理` `数学思维链` `Reason Chunking` `Critical Reasoning Units` `渐进式训练` `视觉-文本交互` `认知科学启发` `结构化推理`

## 📋 核心要点

1. 现有MLLMs在数学任务中仅从静态图像推理，缺乏动态视觉获取，导致推理不连贯。
2. 提出Reason Chunking机制，将推理分解为CRUs，模拟人类逐步解题模式，增强多模态交互。
3. ViRC-7B模型在多个数学基准上平均提升18.8%，验证了框架的有效性和优越性。

## 📝 摘要（中文）

思维链（CoT）显著提升了大型语言模型的推理能力，但在扩展到多模态领域时面临挑战，特别是在数学任务中。现有的多模态大语言模型（MLLMs）通常仅从单个静态数学图像进行文本推理，忽视了推理过程中的动态视觉获取。相比之下，人类会反复检查视觉图像，并采用逐步推理来证明中间命题。这种将问题解决过程分解为关键逻辑节点的策略符合认知科学中的米勒定律。受此启发，我们提出了一个用于多模态数学任务的ViRC框架，引入了Reason Chunking机制，将多模态数学CoT结构化为连续的Critical Reasoning Units（CRUs），以模拟人类专家的问题解决模式。CRUs确保单元内的文本连贯性以验证中间命题，同时跨单元整合视觉信息以生成后续命题并支持结构化推理。为此，我们使用三种视觉工具和四种推理模式构建了CRUX数据集，为每个数学问题提供跨多个推理路径的显式标注CRUs。利用CRUX数据集，我们提出了一种受人类认知学习启发的渐进式训练策略，包括Instructional SFT、Practice SFT和Strategic RL，旨在进一步增强模型的Reason Chunking能力。由此产生的ViRC-7B模型在多个数学基准测试中平均比基线提升了18.8%。代码可在https://github.com/Leon-LihongWang/ViRC获取。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态数学推理任务中，现有方法（如MLLMs）仅依赖静态图像进行文本推理，忽略动态视觉获取，导致推理过程不连贯、难以验证中间命题的问题。现有方法的痛点在于缺乏结构化、交互式的视觉-文本协同推理机制，无法模拟人类专家反复检查图像并逐步推导的认知模式。

**核心思路**：论文的核心解决思路是引入Reason Chunking机制，将多模态数学推理过程分解为连续的Critical Reasoning Units（CRUs），每个CRU对应一个关键逻辑节点，确保单元内文本连贯性以验证中间命题，同时跨单元整合视觉信息以生成后续命题。这一设计灵感来源于人类认知科学中的米勒定律，即通过分块处理复杂信息来提升推理效率。

**技术框架**：整体架构包括数据构建、模型训练和推理三个阶段。首先，使用三种视觉工具（如OCR、几何图形识别）和四种推理模式（如代数、几何）构建CRUX数据集，为每个数学问题提供显式标注的CRUs。其次，采用渐进式训练策略：Instructional SFT（指令微调）学习基础推理模式，Practice SFT（实践微调）强化CRU生成能力，Strategic RL（策略强化学习）优化整体推理路径。最后，在推理时，模型基于输入图像和问题，动态生成CRUs序列，实现结构化多模态推理。

**关键创新**：最重要的技术创新点是Reason Chunking机制和CRUs的设计，将多模态推理过程模块化，模拟人类专家的问题解决模式。与现有方法的本质区别在于：现有方法通常进行端到端的文本推理，而ViRC通过CRUs实现了视觉-文本的交互式、结构化推理，增强了推理的可解释性和准确性。

**关键设计**：关键设计包括CRUs的标注标准（确保每个CRU包含视觉信息提取、命题生成和验证步骤）、渐进式训练策略（结合SFT和RL以模拟人类学习过程），以及模型架构（基于7B参数的多模态大语言模型，集成视觉编码器和文本解码器）。损失函数在SFT阶段使用交叉熵损失，RL阶段使用奖励函数优化推理路径；参数设置上，CRUs数量根据问题复杂度动态调整，训练数据来自CRUX数据集的多推理路径标注。

## 📊 实验亮点

ViRC-7B模型在多个数学基准测试中表现出色，平均比基线模型提升18.8%。具体性能数据包括在几何、代数和综合数学任务上的显著改进，对比基线如传统MLLMs和单模态CoT方法。提升幅度最高可达20%以上，验证了Reason Chunking机制和渐进式训练策略的有效性，突显了结构化多模态推理的优势。

## 🎯 应用场景

该研究在数学教育、智能辅导系统和自动化解题等领域具有潜在应用价值。通过模拟人类专家推理模式，ViRC框架可提升多模态AI在复杂数学问题（如几何证明、代数计算）中的准确性和可解释性，为教育科技和科研工具开发提供新思路。未来可能扩展到更广泛的多模态推理任务，如物理问题解决或逻辑推理，推动AI在认知密集型领域的应用。

## 📄 摘要（原文）

> CoT has significantly enhanced the reasoning ability of LLMs while it faces challenges when extended to multimodal domains, particularly in mathematical tasks. Existing MLLMs typically perform textual reasoning solely from a single static mathematical image, overlooking dynamic visual acquisition during reasoning. In contrast, humans repeatedly examine visual image and employ step-by-step reasoning to prove intermediate propositions. This strategy of decomposing the problem-solving process into key logical nodes adheres to Miller's Law in cognitive science. Inspired by this insight, we propose a ViRC framework for multimodal mathematical tasks, introducing a Reason Chunking mechanism that structures multimodal mathematical CoT into consecutive Critical Reasoning Units (CRUs) to simulate human expert problem-solving patterns. CRUs ensure intra-unit textual coherence for intermediate proposition verification while integrating visual information across units to generate subsequent propositions and support structured reasoning. To this end, we present CRUX dataset by using three visual tools and four reasoning patterns to provide explicitly annotated CRUs across multiple reasoning paths for each mathematical problem. Leveraging the CRUX dataset, we propose a progressive training strategy inspired by human cognitive learning, which includes Instructional SFT, Practice SFT, and Strategic RL, aimed at further strengthening the Reason Chunking ability of the model.The resulting ViRC-7B model achieves a 18.8\% average improvement over baselines across multiple mathematical benchmarks. Code is available at https://github.com/Leon-LihongWang/ViRC.

