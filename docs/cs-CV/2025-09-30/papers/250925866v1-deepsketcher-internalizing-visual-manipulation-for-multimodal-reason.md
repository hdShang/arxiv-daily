---
layout: default
title: "DeepSketcher: Internalizing Visual Manipulation for Multimodal Reasoning"
---

# DeepSketcher: Internalizing Visual Manipulation for Multimodal Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25866" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25866v1</a>
  <a href="https://arxiv.org/pdf/2509.25866.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25866v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25866v1', 'DeepSketcher: Internalizing Visual Manipulation for Multimodal Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chi Zhang, Haibo Qiu, Qiming Zhang, Zhixiong Zeng, Lin Ma, Jing Zhang

**分类**: cs.CV

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**DeepSketcher：通过内部视觉操作实现多模态推理**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态推理` `视觉语言模型` `思维链` `视觉嵌入` `图像操作`

## 📋 核心要点

1. 现有视觉语言模型在多模态推理中依赖文本主导的思维链，缺乏对图像细粒度区域的有效交互。
2. DeepSketcher通过构建图像-文本交错数据集，并设计在视觉嵌入空间中直接操作的模型，实现免工具的视觉思考。
3. 实验表明，DeepSketcher在多模态推理基准上表现出色，验证了数据集的有效性和模型设计的优越性。

## 📝 摘要（中文）

“用图像思考”范式代表了视觉语言模型（VLM）推理的一个关键转变，它从以文本为主的思维链转向图像交互式推理。通过调用视觉工具或生成中间视觉表示，VLM可以迭代地关注细粒度区域，从而实现更深入的图像理解和更忠实的多模态推理。然而，作为一个新兴的范式，它在数据构建的准确性、结构设计和更广泛的应用场景方面仍有很大的探索空间，这为推进多模态推理提供了丰富的机会。为了进一步推进这项工作，我们提出了DeepSketcher，这是一个综合套件，包括一个图像-文本交错数据集和一个独立的模型。该数据集包含31k个思维链（CoT）推理轨迹，具有不同的工具调用和生成的编辑图像，涵盖了各种数据类型和具有高标注准确性的操作指令。在此基础上，我们设计了一个模型，该模型执行交错的图像-文本推理，并通过直接在视觉嵌入空间中操作来原生生成“视觉思想”，而不是调用外部工具并重复重新编码生成的图像。这种设计实现了免工具和更灵活的“用图像思考”。在多模态推理基准上的大量实验证明了强大的性能，验证了数据集的效用和模型设计的有效性。

## 🔬 方法详解

**问题定义**：现有视觉语言模型（VLM）在进行多模态推理时，通常依赖于文本主导的思维链，或者需要调用外部视觉工具并重复编码图像。这种方式计算成本高昂，且对图像的理解不够深入，难以进行细粒度的视觉操作。因此，如何让VLM更有效地“用图像思考”，直接在视觉空间进行推理，是一个亟待解决的问题。

**核心思路**：DeepSketcher的核心思路是让VLM能够像人类一样，在脑海中“绘制”或“修改”图像，从而进行推理。具体来说，它通过在视觉嵌入空间中进行操作，生成“视觉思想”，避免了对外部工具的依赖和重复的图像编码。这种方式更加高效，也更灵活。

**技术框架**：DeepSketcher包含两个主要组成部分：一个图像-文本交错数据集和一个自包含模型。数据集包含31k个思维链推理轨迹，涵盖了各种数据类型和操作指令。模型则基于Transformer架构，能够执行交错的图像-文本推理，并在视觉嵌入空间中生成“视觉思想”。整个流程包括：输入图像和文本描述，模型进行多轮推理，每一轮推理都可能生成新的视觉表示，最终输出答案。

**关键创新**：DeepSketcher最重要的创新点在于它能够在视觉嵌入空间中直接进行操作，生成“视觉思想”。这与现有方法需要调用外部工具或重复编码图像有着本质的区别。通过这种方式，模型可以更高效、更灵活地进行多模态推理。

**关键设计**：DeepSketcher的关键设计包括：1) 图像-文本交错数据集，提供了丰富的训练数据；2) 基于Transformer的架构，能够有效处理图像和文本信息；3) 在视觉嵌入空间中进行操作的机制，允许模型直接生成“视觉思想”。具体的参数设置、损失函数和网络结构等细节在论文中进行了详细描述（未知）。

## 📊 实验亮点

DeepSketcher在多模态推理基准上取得了显著的性能提升。具体的数据和对比基线在论文中进行了详细描述（未知），但总体而言，实验结果验证了数据集的有效性和模型设计的优越性。该模型能够更有效地进行多模态推理，并生成更准确的答案。

## 🎯 应用场景

DeepSketcher的研究成果可应用于智能问答、图像编辑、机器人导航等领域。例如，在智能问答中，模型可以根据图像内容和用户提问，生成中间视觉表示，从而更准确地回答问题。在图像编辑中，模型可以根据用户指令，直接在视觉嵌入空间中修改图像，实现更灵活的编辑效果。在机器人导航中，模型可以根据视觉输入和导航指令，生成中间视觉表示，引导机器人完成导航任务。

## 📄 摘要（原文）

> The "thinking with images" paradigm represents a pivotal shift in the reasoning of Vision Language Models (VLMs), moving from text-dominant chain-of-thought to image-interactive reasoning. By invoking visual tools or generating intermediate visual representations, VLMs can iteratively attend to fine-grained regions, enabling deeper image understanding and more faithful multimodal reasoning. As an emerging paradigm, however, it still leaves substantial room for exploration in data construction accuracy, structural design, and broader application scenarios, which offer rich opportunities for advancing multimodal reasoning. To further advance this line of work, we present DeepSketcher, a comprehensive suite comprising both an image-text interleaved dataset and a self-contained model. The dataset contains 31k chain-of-thought (CoT) reasoning trajectories with diverse tool calls and resulting edited images, covering a wide range of data types and manipulation instructions with high annotation accuracy. Building on this resource, we design a model that performs interleaved image-text reasoning and natively generates "visual thoughts" by operating directly in the visual embedding space, rather than invoking external tools and repeatedly re-encoding generated images. This design enables tool-free and more flexible "thinking with images". Extensive experiments on multimodal reasoning benchmarks demonstrate strong performance, validating both the utility of the dataset and the effectiveness of the model design.

