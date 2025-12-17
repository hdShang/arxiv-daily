---
layout: default
title: BridgeEQA: Virtual Embodied Agents for Real Bridge Inspections
---

# BridgeEQA: Virtual Embodied Agents for Real Bridge Inspections

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.12676" class="toolbar-btn" target="_blank">📄 arXiv: 2511.12676v1</a>
  <a href="https://arxiv.org/pdf/2511.12676.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.12676v1" onclick="toggleFavorite(this, '2511.12676v1', 'BridgeEQA: Virtual Embodied Agents for Real Bridge Inspections')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Subin Varghese, Joshua Gao, Asad Ur Rahman, Vedhus Hoskere

**分类**: cs.CV, cs.AI

**发布日期**: 2025-11-16

---

## 💡 一句话要点

**提出BridgeEQA桥梁检测基准与EMVR模型，解决具身环境问答中的多尺度推理难题。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `具身环境问答` `桥梁检测` `视觉推理` `场景图` `多模态学习`

## 📋 核心要点

1. 现有具身环境问答基准难以捕捉真实场景的复杂性，尤其是在需要多尺度推理和长程空间理解的基础设施检测领域。
2. 提出BridgeEQA基准，利用专业桥梁检测报告和图像，构建更贴近实际应用的具身环境问答任务。
3. 提出EMVR模型，通过图像场景图上的序列导航，增强模型在复杂场景下的视觉推理能力，并在BridgeEQA上验证了有效性。

## 📝 摘要（中文）

本文提出BridgeEQA，一个用于真实桥梁检测的具身环境问答(EQA)基准。该基准包含2200个开放词汇问答对，基于200个真实桥梁场景的专业检测报告和图像数据，平均每个场景包含47.93张图像。问题需要综合多张图像中的视觉证据，并将答案与美国国家桥梁清单(NBI)的状况评级对齐。此外，本文还提出了一种新的EQA指标——图像引用相关性，用于评估模型引用相关图像的能力。对现有视觉语言模型的评估表明，在情景记忆EQA设置下存在显著的性能差距。为此，本文提出具身记忆视觉推理(EMVR)模型，将检测建模为基于图像场景图的顺序导航，并在该基准上取得了优于基线的性能。数据集和代码已公开。

## 🔬 方法详解

**问题定义**：现有具身环境问答（EQA）模型在真实世界场景，特别是基础设施检测领域，面临挑战。这些场景需要模型具备多尺度推理、长程空间理解和复杂的语义关系，而现有基准难以充分模拟这些复杂性，导致模型泛化能力不足。现有方法难以有效利用情景记忆进行推理，导致性能瓶颈。

**核心思路**：本文的核心思路是将桥梁检测任务建模为在图像场景图上的顺序导航问题。通过构建图像之间的连接关系，让智能体能够逐步探索环境，收集证据，并最终回答问题。这种方法模拟了人类检查员在实际场景中的工作方式，有助于提高模型的推理能力和泛化性。

**技术框架**：EMVR模型主要包含以下几个模块：1) 图像特征提取模块，用于提取图像的视觉特征；2) 场景图构建模块，基于图像之间的空间关系构建场景图；3) 导航模块，智能体在场景图上进行导航，选择下一个要访问的图像；4) 视觉推理模块，综合已访问图像的视觉特征和问题信息，进行推理并生成答案。整个过程可以看作是一个马尔可夫决策过程。

**关键创新**：EMVR的关键创新在于将具身环境问答任务转化为图像场景图上的导航问题。这种方法能够有效地利用图像之间的空间关系，帮助智能体更好地理解环境，并进行多步推理。此外，提出的图像引用相关性指标，能够更准确地评估模型在EQA任务中的表现。

**关键设计**：在场景图构建中，可以使用预训练的视觉定位模型来估计图像之间的相对位置关系。导航模块可以使用强化学习算法进行训练，奖励函数可以根据回答的准确性和图像引用相关性进行设计。视觉推理模块可以使用Transformer等模型，将视觉特征和问题信息进行融合，并生成答案。

## 📊 实验亮点

实验结果表明，提出的EMVR模型在BridgeEQA基准上取得了显著的性能提升，优于现有的视觉语言模型。EMVR在回答准确率和图像引用相关性方面均有提升，验证了其在复杂场景下进行视觉推理的有效性。该研究为具身环境问答领域提供了一个新的基准和一种有效的解决方案。

## 🎯 应用场景

该研究成果可应用于桥梁、道路、隧道等基础设施的自动化检测与维护。通过部署具身智能体，可以降低人工检测的成本和风险，提高检测效率和准确性。此外，该技术还可以扩展到其他需要复杂视觉推理的领域，如智能安防、机器人导航等。

## 📄 摘要（原文）

> Deploying embodied agents that can answer questions about their surroundings in realistic real-world settings remains difficult, partly due to the scarcity of benchmarks that faithfully capture practical operating conditions. We propose infrastructure inspection as a compelling domain for open-vocabulary Embodied Question Answering (EQA): it naturally demands multi-scale reasoning, long-range spatial understanding, and complex semantic relationships, while offering unique evaluation advantages via standardized National Bridge Inventory (NBI) condition ratings (0-9), professional inspection reports, and egocentric imagery.
>   We introduce BridgeEQA, a benchmark of 2,200 open-vocabulary question-answer pairs (in the style of OpenEQA) grounded in professional inspection reports across 200 real-world bridge scenes with 47.93 images on average per scene. Questions require synthesizing visual evidence across multiple images and aligning responses with NBI condition ratings. We further propose a new EQA metric Image Citation Relevance to evaluate the ability of a model to cite relevant images.
>   Evaluations of state-of-the-art vision-language models reveal substantial performance gaps under episodic memory EQA settings. To address this, we propose Embodied Memory Visual Reasoning (EMVR), which formulates inspection as sequential navigation over an image-based scene graph: images are nodes, and an agent takes actions to traverse views, compare evidence, and reason within a Markov decision process. EMVR shows strong performance over the baselines. We publicly release both the dataset and code.

