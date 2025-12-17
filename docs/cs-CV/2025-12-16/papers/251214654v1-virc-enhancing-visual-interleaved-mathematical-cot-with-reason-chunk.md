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

**提出ViRC框架，通过Reason Chunking机制增强多模态数学推理中的视觉交错思维链，模拟人类专家解题模式。**

🎯 **匹配领域**: **强化学习**

**关键词**: `多模态数学推理` `视觉交错思维链` `Reason Chunking机制` `Critical Reasoning Units` `CRUX数据集` `渐进式训练策略` `多模态大语言模型` `认知科学启发`

## 📋 核心要点

1. 现有MLLMs在数学任务中仅从静态图像进行文本推理，缺乏动态视觉获取，导致推理能力受限。
2. 提出ViRC框架，通过Reason Chunking机制将推理分解为CRUs，模拟人类逐步验证和视觉整合的解题模式。
3. ViRC-7B模型在多个数学基准上平均提升18.8%，验证了框架在增强多模态数学推理方面的有效性。

## 📝 摘要（中文）

思维链（CoT）显著提升了大型语言模型的推理能力，但在扩展到多模态领域时面临挑战，特别是在数学任务中。现有的多模态大语言模型（MLLMs）通常仅从单个静态数学图像进行文本推理，忽视了推理过程中的动态视觉获取。相比之下，人类会反复检查视觉图像，并采用逐步推理来证明中间命题。这种将问题解决过程分解为关键逻辑节点的策略符合认知科学中的米勒定律。受此启发，我们提出了一个用于多模态数学任务的ViRC框架，引入了Reason Chunking机制，将多模态数学CoT结构化为连续的Critical Reasoning Units（CRUs），以模拟人类专家的问题解决模式。CRUs确保单元内的文本连贯性以验证中间命题，同时跨单元整合视觉信息以生成后续命题并支持结构化推理。为此，我们使用三种视觉工具和四种推理模式构建了CRUX数据集，为每个数学问题提供跨多个推理路径的显式标注CRUs。利用CRUX数据集，我们提出了一种受人类认知学习启发的渐进式训练策略，包括Instructional SFT、Practice SFT和Strategic RL，旨在进一步增强模型的Reason Chunking能力。由此产生的ViRC-7B模型在多个数学基准测试中比基线平均提升了18.8%。代码可在https://github.com/Leon-LihongWang/ViRC获取。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态数学推理中，现有MLLMs仅依赖静态图像进行文本推理，忽略动态视觉获取和结构化推理过程的问题，导致推理准确性和鲁棒性不足。

**核心思路**：受人类专家反复检查图像并逐步推理的启发，提出Reason Chunking机制，将多模态数学CoT分解为连续的Critical Reasoning Units（CRUs），模拟人类将问题分解为关键逻辑节点的认知策略，以增强视觉与文本的交错推理。

**技术框架**：整体架构包括数据构建、模型训练和推理三阶段。首先，使用三种视觉工具（如OCR、图表解析）和四种推理模式（如归纳、演绎）构建CRUX数据集，为每个数学问题提供显式标注的CRUs。然后，采用渐进式训练策略：Instructional SFT学习基本推理模式，Practice SFT强化CRU生成能力，Strategic RL优化整体推理策略。最后，在推理时，模型基于输入图像和问题，动态生成CRUs序列进行逐步验证。

**关键创新**：最重要的技术创新是Reason Chunking机制和CRUs的设计，将多模态推理结构化为可验证的中间命题单元，实现视觉信息的跨单元整合，与现有方法仅依赖单次图像处理有本质区别，更贴近人类认知过程。

**关键设计**：CRUs定义为包含视觉信息提取、文本推理步骤和中间命题验证的单元；训练策略中，Instructional SFT使用指令数据，Practice SFT基于CRUX数据集进行微调，Strategic RL采用强化学习优化奖励函数（如准确性、连贯性）；模型基于7B参数架构，具体网络结构未详细说明，但强调多模态编码器和解码器的集成。

## 📊 实验亮点

ViRC-7B模型在多个数学基准测试中表现出色，相比基线模型平均提升18.8%，具体提升幅度因任务而异，最高可达未知百分比。实验对比了现有MLLMs基线，验证了Reason Chunking机制在增强视觉交错推理方面的有效性，代码开源促进可复现性。

## 🎯 应用场景

该研究在数学教育、智能辅导系统和自动化解题工具中具有潜在应用价值，可提升多模态数学问题的理解和推理能力，未来可能扩展到科学、工程等领域的复杂视觉推理任务，推动多模态AI向更人类化的认知模式发展。

## 📄 摘要（原文）

> CoT has significantly enhanced the reasoning ability of LLMs while it faces challenges when extended to multimodal domains, particularly in mathematical tasks. Existing MLLMs typically perform textual reasoning solely from a single static mathematical image, overlooking dynamic visual acquisition during reasoning. In contrast, humans repeatedly examine visual image and employ step-by-step reasoning to prove intermediate propositions. This strategy of decomposing the problem-solving process into key logical nodes adheres to Miller's Law in cognitive science. Inspired by this insight, we propose a ViRC framework for multimodal mathematical tasks, introducing a Reason Chunking mechanism that structures multimodal mathematical CoT into consecutive Critical Reasoning Units (CRUs) to simulate human expert problem-solving patterns. CRUs ensure intra-unit textual coherence for intermediate proposition verification while integrating visual information across units to generate subsequent propositions and support structured reasoning. To this end, we present CRUX dataset by using three visual tools and four reasoning patterns to provide explicitly annotated CRUs across multiple reasoning paths for each mathematical problem. Leveraging the CRUX dataset, we propose a progressive training strategy inspired by human cognitive learning, which includes Instructional SFT, Practice SFT, and Strategic RL, aimed at further strengthening the Reason Chunking ability of the model.The resulting ViRC-7B model achieves a 18.8\% average improvement over baselines across multiple mathematical benchmarks. Code is available at https://github.com/Leon-LihongWang/ViRC.

