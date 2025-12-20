---
layout: default
title: Code-in-the-Loop Forensics: Agentic Tool Use for Image Forgery Detection
---

# Code-in-the-Loop Forensics: Agentic Tool Use for Image Forgery Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16300" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16300v1</a>
  <a href="https://arxiv.org/pdf/2512.16300.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16300v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16300v1', 'Code-in-the-Loop Forensics: Agentic Tool Use for Image Forgery Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fanrui Zhang, Qiang Zhang, Sizhuo Zhou, Jianwen Sun, Chuanhao Li, Jiaxin Ai, Yukang Feng, Yujie Zhang, Wenjie Li, Zizhen Li, Yifan Chang, Jiawei Liu, Kaipeng Zhang

**分类**: cs.AI

**发布日期**: 2025-12-18

**备注**: 11 pages, 6 figures

---

## 💡 一句话要点

**提出ForenAgent，利用Agentic工具进行图像伪造检测，实现更灵活和可解释的分析。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图像伪造检测` `多模态大语言模型` `Agentic工具` `强化学习` `可解释性` `图像取证` `工具学习`

## 📋 核心要点

1. 现有图像伪造检测方法难以有效融合低级伪影和高级语义知识，限制了检测性能和可解释性。
2. ForenAgent利用MLLM自主生成和执行低级工具，通过多轮交互迭代优化检测结果，实现更灵活的伪造分析。
3. 构建了包含10万张图像的FABench数据集，实验证明ForenAgent在图像伪造检测任务中展现出强大的工具使用能力。

## 📝 摘要（中文）

现有的图像伪造检测（IFD）方法要么利用低级、语义无关的伪影，要么依赖于具有高级语义知识的多模态大型语言模型（MLLM）。这两种信息流在范式和推理上高度异构，难以统一或有效建模其跨层交互。为了解决这个问题，我们提出了ForenAgent，一个多轮交互式IFD框架，使MLLM能够自主生成、执行和迭代改进基于Python的低级工具，从而实现更灵活和可解释的伪造分析。ForenAgent采用结合冷启动和强化微调的两阶段训练流程，逐步提高其工具交互能力和推理适应性。受人类推理的启发，我们设计了一个动态推理循环，包括全局感知、局部聚焦、迭代探测和整体判断，并将其实例化为数据采样策略和任务对齐的过程奖励。为了系统地训练和评估，我们构建了FABench，一个异构、高质量的agent-forensics数据集，包含10万张图像和大约20万个agent交互问答对。实验表明，在低级工具的辅助下，ForenAgent在具有挑战性的IFD任务中表现出涌现的工具使用能力和反思性推理，为通用IFD开辟了一条有希望的途径。

## 🔬 方法详解

**问题定义**：现有图像伪造检测方法主要存在两个痛点：一是依赖低级特征，缺乏语义理解；二是依赖多模态大语言模型，但难以有效利用低级信息。这两种信息流的异构性使得现有方法难以统一建模，导致检测精度和可解释性受限。

**核心思路**：ForenAgent的核心思路是利用多模态大语言模型（MLLM）作为智能体，使其能够自主生成、执行和迭代改进基于Python的低级工具，从而实现对图像伪造的更深入分析。通过工具的使用，MLLM可以更有效地利用低级信息，并结合其自身的高级语义知识，从而提高检测精度和可解释性。

**技术框架**：ForenAgent的整体框架是一个多轮交互式循环，包含以下几个主要模块：1) 全局感知：MLLM首先对图像进行全局感知，获取图像的整体信息。2) 局部聚焦：根据全局感知的结果，MLLM确定需要重点关注的区域。3) 迭代探测：MLLM生成并执行低级工具，对重点区域进行详细分析，例如边缘检测、噪声分析等。4) 整体判断：MLLM综合分析工具的执行结果和自身的高级语义知识，做出最终的伪造判断。

**关键创新**：ForenAgent的关键创新在于将MLLM与低级工具相结合，构建了一个可自主学习和迭代优化的图像伪造检测系统。通过工具的使用，MLLM可以更有效地利用低级信息，并结合其自身的高级语义知识，从而提高检测精度和可解释性。此外，该方法还设计了一个动态推理循环，模拟人类的推理过程，进一步提高了检测性能。

**关键设计**：ForenAgent采用了两阶段训练流程：冷启动和强化微调。冷启动阶段旨在使MLLM初步具备工具使用能力。强化微调阶段则通过奖励机制，鼓励MLLM生成更有效的工具和执行策略。此外，论文还设计了一个动态推理循环，包括全局感知、局部聚焦、迭代探测和整体判断，并将其实例化为数据采样策略和任务对齐的过程奖励。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16300v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16300v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16300v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，ForenAgent在图像伪造检测任务中表现出色，展现出涌现的工具使用能力和反思性推理。通过与现有方法的对比，ForenAgent在多个数据集上取得了显著的性能提升，证明了其有效性和优越性。具体性能数据和提升幅度在论文中详细展示。

## 🎯 应用场景

ForenAgent在图像取证、新闻真实性验证、版权保护等领域具有广泛的应用前景。该研究能够帮助人们更准确地识别伪造图像，维护网络空间的健康和安全，并为相关领域的法律诉讼提供技术支持。未来，该技术有望应用于视频伪造检测等更复杂的场景。

## 📄 摘要（原文）

> Existing image forgery detection (IFD) methods either exploit low-level, semantics-agnostic artifacts or rely on multimodal large language models (MLLMs) with high-level semantic knowledge. Although naturally complementary, these two information streams are highly heterogeneous in both paradigm and reasoning, making it difficult for existing methods to unify them or effectively model their cross-level interactions. To address this gap, we propose ForenAgent, a multi-round interactive IFD framework that enables MLLMs to autonomously generate, execute, and iteratively refine Python-based low-level tools around the detection objective, thereby achieving more flexible and interpretable forgery analysis. ForenAgent follows a two-stage training pipeline combining Cold Start and Reinforcement Fine-Tuning to enhance its tool interaction capability and reasoning adaptability progressively. Inspired by human reasoning, we design a dynamic reasoning loop comprising global perception, local focusing, iterative probing, and holistic adjudication, and instantiate it as both a data-sampling strategy and a task-aligned process reward. For systematic training and evaluation, we construct FABench, a heterogeneous, high-quality agent-forensics dataset comprising 100k images and approximately 200k agent-interaction question-answer pairs. Experiments show that ForenAgent exhibits emergent tool-use competence and reflective reasoning on challenging IFD tasks when assisted by low-level tools, charting a promising route toward general-purpose IFD. The code will be released after the review process is completed.

