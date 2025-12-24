---
layout: default
title: "FloodVision: Urban Flood Depth Estimation Using Foundation Vision-Language Models and Domain Knowledge Graph"
---

# FloodVision: Urban Flood Depth Estimation Using Foundation Vision-Language Models and Domain Knowledge Graph

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04772" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04772v1</a>
  <a href="https://arxiv.org/pdf/2509.04772.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04772v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04772v1', 'FloodVision: Urban Flood Depth Estimation Using Foundation Vision-Language Models and Domain Knowledge Graph')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhangding Liu, Neda Mohammadi, John E. Taylor

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-05

---

## 💡 一句话要点

**FloodVision：结合视觉语言模型与领域知识图谱的城市洪水深度估计**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `洪水深度估计` `视觉语言模型` `领域知识图谱` `零样本学习` `城市防洪`

## 📋 核心要点

1. 现有洪水检测方法依赖固定目标检测器和特定任务训练，导致精度受限且泛化能力差，难以适应多样化的洪水场景。
2. FloodVision利用GPT-4o的语义推理能力，结合领域知识图谱中城市对象的尺寸信息，实现零样本的洪水深度估计。
3. 实验表明，FloodVision在洪水深度估计上优于GPT-4o基线和传统CNN方法，且具有良好的泛化性和实时性。

## 📝 摘要（中文）

本文提出FloodVision，一个零样本框架，用于准确估计城市洪水深度，这对道路通行和应急响应至关重要。该框架结合了基础视觉语言模型GPT-4o的语义推理能力和结构化的领域知识图谱。知识图谱编码了车辆、人员和基础设施等常见城市物体的标准尺寸，使模型推理与物理现实相结合。FloodVision动态识别RGB图像中的可见参考对象，从知识图谱检索验证的高度以减少幻觉，估计淹没比例，并应用统计异常值过滤来计算最终深度值。在MyCoast New York的110张众包图像上评估，FloodVision实现了8.17厘米的平均绝对误差，比GPT-4o基线降低了10.28厘米，降低幅度为20.5%，超过了先前的基于CNN的方法。该系统在不同场景中具有良好的泛化能力，并能近实时运行，适合未来集成到数字孪生平台和公民报告应用程序中，以提高智慧城市的洪水韧性。

## 🔬 方法详解

**问题定义**：论文旨在解决城市环境中准确估计洪水深度的问题。现有基于计算机视觉的洪水检测方法依赖于固定目标检测器和特定任务的训练数据，导致模型在面对不同场景时泛化能力不足，并且精度有限。因此，需要一种能够跨场景泛化且精度更高的洪水深度估计方法。

**核心思路**：论文的核心思路是结合大型视觉语言模型（如GPT-4o）的语义理解能力和领域知识图谱提供的结构化知识。通过让模型理解图像中的场景，并结合知识图谱中常见物体的尺寸信息，可以更准确地推断出洪水深度，而无需针对特定场景进行训练。

**技术框架**：FloodVision框架主要包含以下几个阶段：1) **图像输入与对象识别**：输入RGB图像，利用GPT-4o识别图像中可见的参考对象（如车辆、行人、建筑物等）。2) **知识图谱检索**：从预先构建的领域知识图谱中检索识别出的参考对象的标准尺寸信息。知识图谱用于提供物理世界的先验知识，减少模型幻觉。3) **淹没比例估计**：根据参考对象在图像中的可见部分，估计其被淹没的比例。4) **深度计算与异常值过滤**：结合参考对象的尺寸信息和淹没比例，计算洪水深度。应用统计异常值过滤方法，去除不合理的深度估计值，得到最终的洪水深度估计结果。

**关键创新**：该论文的关键创新在于将大型视觉语言模型与领域知识图谱相结合，实现零样本的洪水深度估计。与传统的依赖于特定数据集训练的方法不同，FloodVision能够利用GPT-4o的通用语义理解能力和知识图谱提供的结构化知识，从而在不同场景下实现更好的泛化能力。

**关键设计**：知识图谱的设计是关键。知识图谱需要包含常见城市对象的标准尺寸信息，并且需要保证信息的准确性。此外，异常值过滤算法的选择也会影响最终的深度估计精度。论文中使用了统计异常值过滤方法，但也可以尝试其他更复杂的异常值检测算法。

## 📊 实验亮点

FloodVision在MyCoast New York的110张众包图像上进行了评估，实现了8.17厘米的平均绝对误差。相比于GPT-4o基线，FloodVision的误差降低了10.28厘米，降幅达20.5%。此外，FloodVision的性能也优于先前的基于CNN的洪水深度估计方法，证明了该方法在泛化性和精度方面的优势。

## 🎯 应用场景

FloodVision可应用于智慧城市建设中的洪水监测和预警系统。它可以集成到数字孪生平台和公民报告应用程序中，为应急响应提供及时的洪水深度信息，帮助制定合理的疏散计划，减少洪水造成的损失。该技术还可用于评估城市基础设施的抗洪能力，为城市规划提供决策支持。

## 📄 摘要（原文）

> Timely and accurate floodwater depth estimation is critical for road accessibility and emergency response. While recent computer vision methods have enabled flood detection, they suffer from both accuracy limitations and poor generalization due to dependence on fixed object detectors and task-specific training. To enable accurate depth estimation that can generalize across diverse flood scenarios, this paper presents FloodVision, a zero-shot framework that combines the semantic reasoning abilities of the foundation vision-language model GPT-4o with a structured domain knowledge graph. The knowledge graph encodes canonical real-world dimensions for common urban objects including vehicles, people, and infrastructure elements to ground the model's reasoning in physical reality. FloodVision dynamically identifies visible reference objects in RGB images, retrieves verified heights from the knowledge graph to mitigate hallucination, estimates submergence ratios, and applies statistical outlier filtering to compute final depth values. Evaluated on 110 crowdsourced images from MyCoast New York, FloodVision achieves a mean absolute error of 8.17 cm, reducing the GPT-4o baseline 10.28 cm by 20.5% and surpassing prior CNN-based methods. The system generalizes well across varying scenes and operates in near real-time, making it suitable for future integration into digital twin platforms and citizen-reporting apps for smart city flood resilience.

