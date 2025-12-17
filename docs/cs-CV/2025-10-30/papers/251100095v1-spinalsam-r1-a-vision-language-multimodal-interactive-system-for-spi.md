---
layout: default
title: SpinalSAM-R1: A Vision-Language Multimodal Interactive System for Spine CT Segmentation
---

# SpinalSAM-R1: A Vision-Language Multimodal Interactive System for Spine CT Segmentation

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.00095" target="_blank" class="toolbar-btn">arXiv: 2511.00095v1</a>
    <a href="https://arxiv.org/pdf/2511.00095.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.00095v1" 
            onclick="toggleFavorite(this, '2511.00095v1', 'SpinalSAM-R1: A Vision-Language Multimodal Interactive System for Spine CT Segmentation')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Jiaming Liu, Dingwei Fan, Junyong Zhao, Chunlin Li, Haipeng Si, Liang Sun

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-30

**备注**: 2 Tables,5 Figures,16 Equations

**🔗 代码/项目**: [GITHUB](https://github.com/6jm233333/spinalsam-r1)

---

## 💡 一句话要点

**SpinalSAM-R1：用于脊柱CT分割的视觉-语言多模态交互系统**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `脊柱CT分割` `视觉-语言模型` `多模态交互` `Segment Anything Model` `DeepSeek-R1`

## 📋 核心要点

1. 脊柱CT图像分割面临低对比度和复杂边界的挑战，现有方法需要大量标注且领域适应性差。
2. SpinalSAM-R1通过集成微调的SAM和DeepSeek-R1，利用解剖引导注意力机制和语义驱动交互协议，提升分割性能。
3. 实验表明SpinalSAM-R1实现了卓越的分割性能，并开发了支持多种交互方式的PyQt5软件，解析准确率达94.3%。

## 📝 摘要（中文）

脊柱及其邻近结构的CT图像解剖结构分割是脊柱疾病诊断和治疗的关键步骤。然而，CT图像的分割受到低对比度和复杂椎骨边界的阻碍。尽管诸如Segment Anything Model (SAM)等先进模型在各种分割任务中显示出前景，但它们在脊柱CT成像中的性能受到高标注要求和较差领域适应性的限制。为了解决这些限制，我们提出SpinalSAM-R1，一个多模态视觉-语言交互系统，它集成了微调的SAM与DeepSeek-R1，用于脊柱CT图像分割。具体来说，我们的SpinalSAM-R1引入了一种解剖引导的注意力机制来提高脊柱分割性能，以及一种由DeepSeek-R1驱动的语义驱动的交互协议，从而实现自然语言引导的细化。SpinalSAM-R1使用低秩适应(LoRA)进行微调，以实现高效适应。我们在脊柱CT图像的解剖结构上验证了我们的SpinalSAM-R1。实验结果表明，我们的方法实现了卓越的分割性能。同时，我们开发了一个基于PyQt5的交互式软件，它支持基于点、框和文本的提示。该系统支持11个临床操作，解析准确率为94.3%，响应时间低于800毫秒。该软件已在https://github.com/6jm233333/spinalsam-r1上发布。

## 🔬 方法详解

**问题定义**：论文旨在解决脊柱CT图像分割中，由于低对比度和复杂椎骨边界导致的分割精度不高的问题。现有方法，如直接应用SAM，需要大量的标注数据，且在脊柱CT图像这种特定领域表现不佳，泛化能力不足。

**核心思路**：论文的核心思路是将预训练的SAM模型与大型语言模型DeepSeek-R1相结合，构建一个多模态交互系统。通过微调SAM，并引入解剖引导的注意力机制，提升模型对脊柱结构的感知能力。同时，利用DeepSeek-R1的语义理解能力，实现自然语言引导的分割细化，降低对精确标注的依赖。

**技术框架**：SpinalSAM-R1系统主要包含三个模块：1) 微调的SAM模型，用于初步的脊柱分割；2) 解剖引导的注意力机制，用于增强模型对脊柱结构的关注；3) DeepSeek-R1驱动的语义交互模块，用于根据用户的自然语言指令，对分割结果进行精细调整。整个流程是：用户提供CT图像和自然语言描述，SAM模型进行初步分割，注意力机制优化分割结果，DeepSeek-R1解析用户指令并指导分割结果的进一步细化。

**关键创新**：论文的关键创新在于将视觉分割模型SAM与大型语言模型DeepSeek-R1进行有效融合，构建了一个多模态交互系统。这种融合方式不仅提升了分割精度，还降低了对大量精确标注数据的需求。此外，解剖引导的注意力机制也针对脊柱CT图像的特点进行了优化，提高了模型对关键区域的关注度。

**关键设计**：SpinalSAM-R1使用LoRA（Low-Rank Adaptation）进行高效微调，降低了计算成本。解剖引导的注意力机制的具体实现方式未知（论文未详细描述）。PyQt5交互软件支持点、框和文本三种提示方式，方便用户进行交互。DeepSeek-R1的prompt设计和指令解析策略未知。

## 📊 实验亮点

SpinalSAM-R1在脊柱CT图像分割任务上取得了优异的性能，但具体指标和对比基线未知。该系统支持11种临床操作，解析准确率达到94.3%，响应时间低于800毫秒，表明其具有较高的实用价值和交互效率。该软件已开源，方便其他研究者进行复现和改进。

## 🎯 应用场景

SpinalSAM-R1可应用于脊柱疾病的辅助诊断、手术规划和术后评估。通过自然语言交互，医生可以更高效、准确地分割脊柱CT图像，从而提高诊断效率和治疗效果。该系统有望减少人工标注的工作量，并为远程医疗和智能化医疗提供技术支持。

## 📄 摘要（原文）

> The anatomical structure segmentation of the spine and adjacent structures from computed tomography (CT) images is a key step for spinal disease diagnosis and treatment. However, the segmentation of CT images is impeded by low contrast and complex vertebral boundaries. Although advanced models such as the Segment Anything Model (SAM) have shown promise in various segmentation tasks, their performance in spinal CT imaging is limited by high annotation requirements and poor domain adaptability. To address these limitations, we propose SpinalSAM-R1, a multimodal vision-language interactive system that integrates a fine-tuned SAM with DeepSeek-R1, for spine CT image segmentation. Specifically, our SpinalSAM-R1 introduces an anatomy-guided attention mechanism to improve spine segmentation performance, and a semantics-driven interaction protocol powered by DeepSeek-R1, enabling natural language-guided refinement. The SpinalSAM-R1 is fine-tuned using Low-Rank Adaptation (LoRA) for efficient adaptation. We validate our SpinalSAM-R1 on the spine anatomical structure with CT images. Experimental results suggest that our method achieves superior segmentation performance. Meanwhile, we develop a PyQt5-based interactive software, which supports point, box, and text-based prompts. The system supports 11 clinical operations with 94.3\% parsing accuracy and sub-800 ms response times. The software is released on https://github.com/6jm233333/spinalsam-r1.

