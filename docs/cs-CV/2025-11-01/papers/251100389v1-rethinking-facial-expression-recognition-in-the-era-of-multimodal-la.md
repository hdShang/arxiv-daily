---
layout: default
title: Rethinking Facial Expression Recognition in the Era of Multimodal Large Language Models: Benchmark, Datasets, and Beyond
---

# Rethinking Facial Expression Recognition in the Era of Multimodal Large Language Models: Benchmark, Datasets, and Beyond

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.00389" class="toolbar-btn" target="_blank">📄 arXiv: 2511.00389v1</a>
  <a href="https://arxiv.org/pdf/2511.00389.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.00389v1" onclick="toggleFavorite(this, '2511.00389v1', 'Rethinking Facial Expression Recognition in the Era of Multimodal Large Language Models: Benchmark, Datasets, and Beyond')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fan Zhang, Haoxuan Li, Shengju Qian, Xin Wang, Zheng Lian, Hao Wu, Zhihong Zhu, Yuan Gao, Qiankun Li, Yefeng Zheng, Zhouchen Lin, Pheng-Ann Heng

**分类**: cs.CV

**发布日期**: 2025-11-01

---

## 💡 一句话要点

**提出UniFER-7B，提升多模态大语言模型在面部表情识别中的推理和可解释性。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `面部表情识别` `多模态大语言模型` `视觉问答` `强化学习` `情感计算` `可解释性` `后训练策略`

## 📋 核心要点

1. 现有面部表情识别方法依赖于特定领域模型，缺乏通用性和可解释性，且多模态大语言模型在FER任务上的性能有待探索。
2. 论文提出UniFER-7B，通过将FER任务转化为VQA形式，并利用后训练策略，提升MLLM在面部表情推理方面的能力。
3. 实验结果表明，UniFER-7B在多个FER数据集上优于许多开源和闭源的通用MLLM，证明了其有效性和优越性。

## 📝 摘要（中文）

多模态大语言模型（MLLMs）已经彻底改变了包括计算机视觉和情感计算在内的众多研究领域。作为该交叉领域中的一个关键挑战，面部表情识别（FER）已经从分离的、特定领域的模型发展到更统一的方法。一种统一FER任务的有希望的途径是将传统的FER数据集转换为视觉问答（VQA）格式，从而能够直接应用强大的通用MLLM进行推理。为了弥补MLLM在FER任务上的性能差距，我们提供了FERBench，这是一个系统的基准，包含了四个广泛使用的FER数据集上的20个最先进的MLLM。结果表明，虽然MLLM表现出良好的分类性能，但它们在推理和可解释性方面仍然面临重大限制。为此，我们引入了旨在增强MLLM的面部表情推理能力的后训练策略。具体来说，我们策划了两个高质量和大规模的数据集：用于冷启动初始化的UniFER-CoT-230K和用于具有可验证奖励的强化学习（RLVR）的UniFER-RLVR-360K。在此基础上，我们开发了一个统一且可解释的FER基础模型，称为UniFER-7B，它优于许多开源和闭源通用MLLM（例如，Gemini-2.5-Pro和Qwen2.5-VL-72B）。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态大语言模型（MLLMs）在面部表情识别（FER）任务中推理能力不足和可解释性差的问题。现有方法通常是领域特定的，无法充分利用MLLMs的通用能力。此外，缺乏专门为MLLMs设计的FER数据集和训练策略，导致其性能受限。

**核心思路**：论文的核心思路是将传统的FER任务转化为视觉问答（VQA）的形式，从而能够直接利用MLLMs进行推理。通过构建高质量的FER数据集，并采用后训练策略，增强MLLMs在面部表情推理方面的能力。具体而言，利用Chain-of-Thought (CoT) 数据集进行冷启动初始化，并使用Reinforcement Learning with Verifiable Rewards (RLVR) 进行强化学习，从而提升模型的推理能力和可解释性。

**技术框架**：UniFER-7B的整体框架包括以下几个主要阶段：1) 数据集构建：构建UniFER-CoT-230K和UniFER-RLVR-360K两个数据集，分别用于冷启动初始化和强化学习。2) 模型初始化：使用UniFER-CoT-230K数据集对MLLM进行冷启动初始化。3) 强化学习：使用UniFER-RLVR-360K数据集，通过强化学习提升模型的推理能力和可解释性。4) 模型评估：在FERBench基准上评估UniFER-7B的性能，并与其他MLLMs进行比较。

**关键创新**：论文最重要的技术创新点在于提出了UniFER-7B，这是一个统一且可解释的FER基础模型。与现有方法相比，UniFER-7B能够直接利用MLLMs的通用能力进行FER任务，并通过后训练策略显著提升了模型的推理能力和可解释性。此外，UniFER-CoT-230K和UniFER-RLVR-360K两个数据集的构建也为MLLMs在FER任务中的研究提供了重要资源。

**关键设计**：UniFER-CoT-230K数据集包含230K个样本，每个样本包含一张面部表情图像和一个CoT推理过程，用于引导模型进行推理。UniFER-RLVR-360K数据集包含360K个样本，每个样本包含一张面部表情图像和一个可验证的奖励信号，用于指导模型的强化学习过程。在强化学习过程中，论文设计了一个奖励函数，用于评估模型的推理过程是否正确和可解释。具体参数设置和网络结构细节未在摘要中详细说明，属于未知信息。

## 📊 实验亮点

UniFER-7B在FERBench基准测试中，优于许多开源和闭源的通用MLLM，例如Gemini-2.5-Pro和Qwen2.5-VL-72B。这表明通过专门的数据集和训练策略，可以显著提升MLLM在FER任务中的性能。具体的性能提升幅度未在摘要中给出，属于未知信息。

## 🎯 应用场景

该研究成果可应用于情感计算、人机交互、智能监控、医疗诊断等领域。例如，在人机交互中，UniFER-7B可以帮助机器理解人类的情绪，从而提供更自然和个性化的交互体验。在智能监控中，可以用于识别异常情绪，从而预防潜在的安全事件。在医疗诊断中，可以辅助医生诊断精神疾病。

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs) have revolutionized numerous research fields, including computer vision and affective computing. As a pivotal challenge in this interdisciplinary domain, facial expression recognition (FER) has evolved from separate, domain-specific models to more unified approaches. One promising avenue to unify FER tasks is converting conventional FER datasets into visual question-answering (VQA) formats, enabling the direct application of powerful generalist MLLMs for inference. However, despite the success of cutting-edge MLLMs in various tasks, their performance on FER tasks remains largely unexplored. To address this gap, we provide FERBench, a systematic benchmark that incorporates 20 state-of-the-art MLLMs across four widely used FER datasets. Our results reveal that, while MLLMs exhibit good classification performance, they still face significant limitations in reasoning and interpretability. To this end, we introduce post-training strategies aimed at enhancing the facial expression reasoning capabilities of MLLMs. Specifically, we curate two high-quality and large-scale datasets: UniFER-CoT-230K for cold-start initialization and UniFER-RLVR-360K for reinforcement learning with verifiable rewards (RLVR), respectively. Building upon them, we develop a unified and interpretable FER foundation model termed UniFER-7B, which outperforms many open-sourced and closed-source generalist MLLMs (e.g., Gemini-2.5-Pro and Qwen2.5-VL-72B).

