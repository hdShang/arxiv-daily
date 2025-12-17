---
layout: default
title: CompAgent: An Agentic Framework for Visual Compliance Verification
---

# CompAgent: An Agentic Framework for Visual Compliance Verification

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.00171" target="_blank" class="toolbar-btn">arXiv: 2511.00171v2</a>
    <a href="https://arxiv.org/pdf/2511.00171.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.00171v2" 
            onclick="toggleFavorite(this, '2511.00171v2', 'CompAgent: An Agentic Framework for Visual Compliance Verification')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Rahul Ghosh, Baishali Chaudhury, Hari Prasanna Das, Meghana Ashok, Ryan Razkenari, Sungmin Hong, Chun-Hao Liu

**分类**: cs.CV

**发布日期**: 2025-10-31 (更新: 2025-11-19)

**备注**: Under review

---

## 💡 一句话要点

**提出CompAgent，用于视觉合规性验证的Agent框架，提升细粒度推理能力。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉合规性验证` `多模态大语言模型` `Agent框架` `工具增强推理` `动态规划` `计算机视觉` `内容审核`

## 📋 核心要点

1. 现有视觉合规性验证方法依赖人工标注数据集训练的特定任务模型，泛化性差且成本高昂。
2. CompAgent通过Agent框架，结合MLLM和视觉工具，动态规划工具使用，提升细粒度视觉推理能力。
3. 实验表明，CompAgent在UnsafeBench数据集上F1值达到76%，相比SOTA方法提升10%。

## 📝 摘要（中文）

视觉合规性验证在计算机视觉领域是一个关键但未被充分探索的问题，尤其是在媒体、娱乐和广告等领域，这些领域的内容必须遵守复杂且不断变化的政策规则。现有的方法通常依赖于在手动标注的数据集上训练的特定于任务的深度学习模型，这些模型构建成本高昂且泛化能力有限。虽然最近的多模态大型语言模型（MLLM）提供了广泛的现实世界知识和策略理解，但它们难以对细粒度的视觉细节进行推理，也难以有效地应用结构化的合规性规则。在本文中，我们提出了CompAgent，这是第一个用于视觉合规性验证的Agent框架。CompAgent利用一系列视觉工具（如目标检测器、人脸分析器、NSFW检测器和字幕模型）来增强MLLM，并引入了一个规划Agent，该Agent根据合规性策略动态地选择合适的工具。然后，合规性验证Agent整合图像、工具输出和策略上下文以执行多模态推理。在公共基准测试上的实验表明，CompAgent优于专门的分类器、直接MLLM提示和精心设计的路由基线，在UnsafeBench数据集上实现了高达76%的F1分数，并且比最先进的方法提高了10%。我们的结果证明了Agent规划和强大的工具增强推理对于可扩展、准确和适应性强的视觉合规性验证的有效性。

## 🔬 方法详解

**问题定义**：视觉合规性验证旨在判断图像或视频内容是否符合预定的政策或规则。现有方法主要依赖于特定任务的深度学习模型，需要大量人工标注数据，且难以适应新的合规性规则。多模态大语言模型（MLLM）虽然具备一定的知识和推理能力，但在处理细粒度的视觉信息和结构化的合规性规则时表现不佳。

**核心思路**：CompAgent的核心思路是将MLLM与一系列视觉工具结合，通过一个规划Agent动态地选择合适的工具来辅助MLLM进行推理。这种方法借鉴了人类解决复杂问题的思路，即利用专业工具来增强自身的能力。通过工具的辅助，MLLM可以更好地理解图像内容，并结合合规性规则进行判断。

**技术框架**：CompAgent框架主要包含三个模块：1) 视觉工具集：包括目标检测器、人脸分析器、NSFW检测器、图像描述模型等，用于提取图像中的各种信息。2) 规划Agent：根据合规性策略，动态地选择合适的视觉工具。3) 合规性验证Agent：整合图像、工具输出和策略上下文，利用MLLM进行多模态推理，判断图像是否符合合规性要求。整个流程是，首先由规划Agent分析合规性策略，然后选择合适的视觉工具提取图像特征，最后由合规性验证Agent结合提取的特征和策略进行推理。

**关键创新**：CompAgent的关键创新在于引入了Agent框架，将MLLM与视觉工具结合，并通过规划Agent动态地选择工具。这种方法避免了直接使用MLLM进行推理的局限性，充分利用了各种视觉工具的专业能力。与现有方法相比，CompAgent具有更好的泛化能力和适应性，可以更容易地适应新的合规性规则。

**关键设计**：规划Agent的设计是关键。论文中规划Agent的具体实现方式未知，但其核心功能是根据合规性策略选择合适的工具。合规性验证Agent使用MLLM进行推理，具体的MLLM选择和训练方式未知。视觉工具的选择也至关重要，需要根据具体的合规性验证任务进行选择。

## 📊 实验亮点

CompAgent在UnsafeBench数据集上取得了显著的性能提升，F1值达到76%，相比最先进的方法提高了10%。实验结果表明，CompAgent优于专门的分类器、直接MLLM提示和精心设计的路由基线，证明了Agent规划和工具增强推理对于视觉合规性验证的有效性。

## 🎯 应用场景

CompAgent可应用于媒体内容审核、广告合规性检查、电商平台商品审核等领域。该研究的实际价值在于降低人工审核成本，提高审核效率和准确性。未来，CompAgent可以扩展到更多领域，例如智能安防、自动驾驶等，实现更广泛的视觉合规性验证。

## 📄 摘要（原文）

> Visual compliance verification is a critical yet underexplored problem in computer vision, especially in domains such as media, entertainment, and advertising where content must adhere to complex and evolving policy rules. Existing methods often rely on task-specific deep learning models trained on manually labeled datasets, which are costly to build and limited in generalizability. While recent Multimodal Large Language Models (MLLMs) offer broad real-world knowledge and policy understanding, they struggle to reason over fine-grained visual details and apply structured compliance rules effectively on their own. In this paper, we propose CompAgent, the first agentic framework for visual compliance verification. CompAgent augments MLLMs with a suite of visual tools-such as object detectors, face analyzers, NSFW detectors, and captioning models-and introduces a planning agent that dynamically selects appropriate tools based on the compliance policy. A compliance verification agent then integrates image, tool outputs, and policy context to perform multimodal reasoning. Experiments on public benchmarks show that CompAgent outperforms specialized classifiers, direct MLLM prompting, and curated routing baselines, achieving up to 76% F1 score and a 10% improvement over the state-of-the-art on the UnsafeBench dataset. Our results demonstrate the effectiveness of agentic planning and robust tool-augmented reasoning for scalable, accurate, and adaptable visual compliance verification.

