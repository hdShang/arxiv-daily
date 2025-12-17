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

**提出ViRC框架，通过Reason Chunking增强视觉交互数学CoT推理能力**

🎯 **匹配领域**: **强化学习与模仿学习 (RL & IL)**

**关键词**: `多模态学习` `视觉交互` `数学推理` `链式思考` `Reason Chunking` `关键推理单元` `渐进式训练`

## 📋 核心要点

1. 现有多模态LLM在解决数学问题时，缺乏动态视觉交互，仅依赖静态图像进行推理。
2. ViRC框架引入Reason Chunking机制，将推理过程分解为关键推理单元CRU，模拟人类专家解题模式。
3. CRUX数据集包含显式标注的CRU，结合渐进式训练策略，ViRC-7B模型在数学基准测试中提升显著。

## 📝 摘要（中文）

CoT显著提升了LLM的推理能力，但当扩展到多模态领域，尤其是在数学任务中时，面临着挑战。现有的MLLM通常仅从单个静态数学图像执行文本推理，忽略了推理过程中的动态视觉获取。与此相反，人类会反复检查视觉图像并采用逐步推理来证明中间命题。这种将问题解决过程分解为关键逻辑节点的方法符合认知科学中的米勒定律。受此启发，我们提出了一个用于多模态数学任务的ViRC框架，引入了Reason Chunking机制，将多模态数学CoT构建为连续的关键推理单元(CRU)，以模拟人类专家的问题解决模式。CRU确保单元内文本连贯性，用于中间命题验证，同时跨单元集成视觉信息以生成后续命题并支持结构化推理。为此，我们使用三种视觉工具和四种推理模式提出了CRUX数据集，为每个数学问题提供跨多个推理路径的显式标注CRU。利用CRUX数据集，我们提出了一种受人类认知学习启发的渐进式训练策略，包括Instructional SFT、Practice SFT和Strategic RL，旨在进一步加强模型的Reason Chunking能力。最终的ViRC-7B模型在多个数学基准测试中实现了比基线平均18.8%的改进。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态大型语言模型（MLLM）在处理视觉交互数学问题时，缺乏动态视觉信息利用和有效推理结构的问题。现有方法通常仅依赖于静态的数学图像进行推理，忽略了人类在解决此类问题时反复观察图像并逐步推理的过程，导致推理能力受限。

**核心思路**：论文的核心思路是模拟人类专家解决数学问题的模式，将复杂的推理过程分解为一系列连续的关键推理单元（CRU），即Reason Chunking。每个CRU内部保持文本连贯性，用于验证中间命题，同时跨CRU集成视觉信息，以生成后续命题，从而实现结构化的推理过程。

**技术框架**：ViRC框架包含以下几个主要组成部分：1) CRUX数据集：一个包含显式标注CRU的多模态数学问题数据集，使用视觉工具和推理模式构建。2) Reason Chunking机制：将多模态数学CoT分解为连续CRU，每个CRU包含视觉信息和文本推理。3) 渐进式训练策略：包括Instructional SFT、Practice SFT和Strategic RL三个阶段，逐步提升模型的Reason Chunking能力。

**关键创新**：论文的关键创新在于Reason Chunking机制，它将复杂的推理过程分解为更小、更易于管理的CRU，并显式地建模了视觉信息在推理过程中的作用。这种方法更符合人类的认知过程，并能够有效提升模型的推理能力。与现有方法相比，ViRC框架能够更好地利用动态视觉信息，并生成更结构化的推理过程。

**关键设计**：CRUX数据集的构建使用了三种视觉工具（例如，绘图工具、计算器）和四种推理模式（例如，代数推理、几何推理）。渐进式训练策略中的Instructional SFT阶段使用CRUX数据集进行指令微调，Practice SFT阶段使用更复杂的数学问题进行训练，Strategic RL阶段使用强化学习进一步优化模型的推理策略。具体的损失函数和网络结构细节在论文中应该有更详细的描述，但摘要中未提及。

## 📊 实验亮点

ViRC-7B模型在多个数学基准测试中取得了显著的性能提升，平均提升幅度达到18.8%。这一结果表明，Reason Chunking机制和渐进式训练策略能够有效提升模型的推理能力。CRUX数据集的构建也为多模态数学推理研究提供了有价值的资源。

## 🎯 应用场景

ViRC框架具有广泛的应用前景，可应用于数学教育、科学研究、工程设计等领域。通过模拟人类专家的解题模式，ViRC可以帮助学生更好地理解数学概念，提高解题能力。在科学研究和工程设计中，ViRC可以辅助研究人员和工程师解决复杂的数学问题，提高工作效率。未来，ViRC有望成为一个强大的多模态推理工具，推动人工智能在各个领域的应用。

## 📄 摘要（原文）

> CoT has significantly enhanced the reasoning ability of LLMs while it faces challenges when extended to multimodal domains, particularly in mathematical tasks. Existing MLLMs typically perform textual reasoning solely from a single static mathematical image, overlooking dynamic visual acquisition during reasoning. In contrast, humans repeatedly examine visual image and employ step-by-step reasoning to prove intermediate propositions. This strategy of decomposing the problem-solving process into key logical nodes adheres to Miller's Law in cognitive science. Inspired by this insight, we propose a ViRC framework for multimodal mathematical tasks, introducing a Reason Chunking mechanism that structures multimodal mathematical CoT into consecutive Critical Reasoning Units (CRUs) to simulate human expert problem-solving patterns. CRUs ensure intra-unit textual coherence for intermediate proposition verification while integrating visual information across units to generate subsequent propositions and support structured reasoning. To this end, we present CRUX dataset by using three visual tools and four reasoning patterns to provide explicitly annotated CRUs across multiple reasoning paths for each mathematical problem. Leveraging the CRUX dataset, we propose a progressive training strategy inspired by human cognitive learning, which includes Instructional SFT, Practice SFT, and Strategic RL, aimed at further strengthening the Reason Chunking ability of the model.The resulting ViRC-7B model achieves a 18.8\% average improvement over baselines across multiple mathematical benchmarks. Code is available at https://github.com/Leon-LihongWang/ViRC.

