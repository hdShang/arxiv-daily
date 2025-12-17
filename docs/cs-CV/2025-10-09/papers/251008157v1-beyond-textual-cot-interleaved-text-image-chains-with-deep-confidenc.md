---
layout: default
title: Beyond Textual CoT: Interleaved Text-Image Chains with Deep Confidence Reasoning for Image Editing
---

# Beyond Textual CoT: Interleaved Text-Image Chains with Deep Confidence Reasoning for Image Editing

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.08157" target="_blank" class="toolbar-btn">arXiv: 2510.08157v1</a>
    <a href="https://arxiv.org/pdf/2510.08157.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.08157v1" 
            onclick="toggleFavorite(this, '2510.08157v1', 'Beyond Textual CoT: Interleaved Text-Image Chains with Deep Confidence Reasoning for Image Editing')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Zhentao Zou, Zhengrong Yue, Kunpeng Du, Binlei Bao, Hanting Li, Haizhen Xie, Guozheng Xu, Yue Zhou, Yali Wang, Jie Hu, Xue Jiang, Xinghao Chen

**分类**: cs.CV

**发布日期**: 2025-10-09

**备注**: 25pages,20figures

---

## 💡 一句话要点

**提出MURE框架，利用交错文本-图像链和深度置信推理进行图像编辑**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图像编辑` `多模态推理` `Chain-of-Thought` `深度置信学习` `文本-图像交错` `视觉推理` `大型语言模型` `图像生成`

## 📋 核心要点

1. 现有基于文本的图像编辑方法难以处理复杂的对象关系和精细的空间布局，缺乏显式的推理过程。
2. MURE框架采用交错的文本和图像推理链，结合视觉线索指导像素级别的细节生成，提升编辑精度。
3. 引入多模态深度置信推理，通过置信度评估修剪低质量推理路径，减轻大型语言模型的幻觉问题，提升编辑质量。

## 📝 摘要（中文）

本文提出了一种名为多模态推理编辑（MURE）的新框架，旨在解决现有方法在处理复杂对象交叉和精细空间关系时面临的挑战。MURE将图像编辑过程从纯文本推理转变为一系列交错的文本和视觉依据，采用原生多模态的交错文本-图像CoT，生成逐步推理链，其中文本描述后跟相应的视觉提示，如定义目标编辑区域的位置掩码或新内容的表示。此外，引入多模态深度置信（MMDC）推理范式，通过探索视觉推理路径树，并使用奖励模型的深度置信度分数修剪低质量分支，从而减轻大型语言模型的幻觉现象。该方法将复杂的编辑任务分解为相互依赖的子任务，从而在每个阶段实现更高的精度，并产生高保真度的编辑结果。我们定义了交错文本-图像链的公式，并发布了首个CoT-Edit-14K数据集，包含14K个高质量的编辑示例。大量实验表明，我们的方法在三个图像编辑基准测试中均取得了显著的改进。

## 🔬 方法详解

**问题定义**：现有基于自然语言的图像编辑方法，尤其是在处理复杂对象之间的交互和精细的空间关系时，面临着挑战。纯文本的Chain-of-Thought (CoT) 或坐标增强的CoT在表示复杂的视觉布局方面存在根本性限制，并且缺乏指导生成精细像素级细节所需的视觉线索。因此，需要一种能够有效利用视觉信息进行推理和编辑的方法。

**核心思路**：本文的核心思路是将图像编辑过程从纯文本推理转变为交错的文本和视觉推理。通过在文本描述后跟随相应的视觉提示（例如位置掩码或新内容的表示），模型可以更好地理解和执行编辑任务。此外，引入多模态深度置信推理，通过评估不同推理路径的质量，选择高质量的路径，从而减少大型语言模型的幻觉问题。

**技术框架**：MURE框架包含以下主要模块：1) 交错文本-图像CoT生成器：负责生成逐步的推理链，其中文本描述与相应的视觉提示交替出现。2) 多模态深度置信（MMDC）推理模块：在每个推理步骤中，探索多个视觉推理路径，并使用奖励模型评估每个路径的置信度。3) 路径修剪模块：根据MMDC的置信度分数，修剪低质量的推理路径，确保模型始终沿着高质量的轨迹前进。4) 图像编辑模块：根据最终的推理结果，对图像进行编辑。

**关键创新**：该论文的关键创新在于：1) 提出了交错文本-图像CoT的概念，将视觉信息融入到推理过程中。2) 引入了多模态深度置信推理，通过评估推理路径的质量来减少幻觉问题。3) 构建了CoT-Edit-14K数据集，为交错文本-图像CoT的图像编辑研究提供了数据支持。与现有方法相比，MURE能够更有效地利用视觉信息进行推理和编辑，从而提高编辑的精度和质量。

**关键设计**：在MMDC推理中，使用奖励模型来评估每个视觉推理路径的置信度。奖励模型可以是一个预训练的图像质量评估模型，也可以是一个专门训练的用于评估编辑结果质量的模型。在路径修剪过程中，可以设置一个置信度阈值，低于该阈值的路径将被丢弃。此外，在交错文本-图像CoT生成器中，可以使用不同的视觉提示类型，例如位置掩码、分割掩码或新内容的表示。具体选择哪种视觉提示类型取决于具体的编辑任务。

## 📊 实验亮点

实验结果表明，MURE在三个图像编辑基准测试中均取得了显著的改进。具体性能数据和对比基线在论文中有详细展示，总体而言，MURE在编辑质量和用户满意度方面均优于现有方法。CoT-Edit-14K数据集的发布也为后续研究提供了宝贵资源。

## 🎯 应用场景

该研究成果可应用于多种图像编辑场景，例如电商产品的图像优化、社交媒体内容的个性化定制、以及专业设计领域的图像处理等。通过更精确的理解用户意图和生成高质量的编辑结果，该方法能够显著提升图像编辑的效率和用户体验，并为未来的智能图像编辑工具奠定基础。

## 📄 摘要（原文）

> Image editing with natural language has gained significant popularity, yet existing methods struggle with intricate object intersections and fine-grained spatial relationships due to the lack of an explicit reasoning process. While Chain-of-Thought (CoT) has been explored to enhance reasoning, purely textual CoT or CoT augmented with coordinate information is fundamentally limited in its ability to represent intricate visual layouts and lacks the necessary visual cues to guide the generation of fine-grained, pixel-level details. To address these challenges, we propose Multimodal Reasoning Edit (MURE), a novel framework that shifts the visual editing process from purely text-based reasoning to a series of interleaved textual and visual rationales. Our framework performs image editing using a natively multimodal, interleaved text-image CoT. This approach generates a step-by-step chain of reasoning where a textual description is followed by a corresponding visual cue, such as a positional mask that defined intended edited regions or a representation of new content. Furthermore, to mitigate the hallucination phenomenon of large language models, we introduce Multimodal Deep Confidence (MMDC) reasoning paradigm. This paradigm explores a tree of visual reasoning paths at each step. By pruning low-quality branches using a deep confidence score from a reward model, it ensures the model consistently follows a high-quality trajectory towards the final edited result. The proposed method decomposes complex editing tasks into interdependent sub-tasks, achieving greater precision at each stage and yielding high-fidelity edited results. We define the formulation for interleaved text-image chains and release the first CoT-Edit-14K dataset, comprising 14K high-quality editing examples. Extensive experiments show that our method yields significant improvements across three image editing benchmarks.

