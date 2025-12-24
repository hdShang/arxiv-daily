---
layout: default
title: "CIR-CoT: Towards Interpretable Composed Image Retrieval via End-to-End Chain-of-Thought Reasoning"
---

# CIR-CoT: Towards Interpretable Composed Image Retrieval via End-to-End Chain-of-Thought Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.08003" class="toolbar-btn" target="_blank">📄 arXiv: 2510.08003v1</a>
  <a href="https://arxiv.org/pdf/2510.08003.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.08003v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.08003v1', 'CIR-CoT: Towards Interpretable Composed Image Retrieval via End-to-End Chain-of-Thought Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weihuang Lin, Yiwei Ma, Jiayi Ji, Xiaoshuai Sun, Rongrong Ji

**分类**: cs.CV

**发布日期**: 2025-10-09

---

## 💡 一句话要点

**提出CIR-CoT，通过端到端思维链推理实现可解释的组合图像检索**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `组合图像检索` `思维链推理` `多模态学习` `可解释性` `视觉语言模型`

## 📋 核心要点

1. 现有组合图像检索方法，如基于VLM和MLLM的模型，通常是黑盒，缺乏可解释性，难以理解检索逻辑。
2. CIR-CoT通过引入显式的思维链(CoT)推理，使模型能够生成可解释的推理过程，从而提高检索的准确性和透明度。
3. 论文创建了包含描述、推理和结论的结构化CoT标注数据集，并在FashionIQ、CIRR和CIRCO数据集上验证了CIR-CoT的有效性。

## 📝 摘要（中文）

组合图像检索(CIR)旨在根据参考图像和修改文本找到目标图像，其核心挑战在于执行跨视觉和语义模态的统一推理。当前基于视觉-语言模型(VLMs, 如CLIP)和多模态大型语言模型(MLLMs, 如Qwen-VL)的方法虽然取得了一些进展，但主要作为“黑盒”运行。这种固有的不透明性不仅阻止用户理解检索的基本原理，还限制了模型遵循复杂、细粒度指令的能力。为了克服这些限制，我们引入了CIR-CoT，这是第一个面向检索的端到端MLLM，旨在集成显式的思维链(CoT)推理。通过迫使模型首先生成可解释的推理链，CIR-CoT增强了其捕获关键跨模态交互的能力，从而实现更准确的检索，同时使其决策过程透明化。由于现有的数据集(如FashionIQ和CIRR)缺乏必要的推理数据，我们工作的一个关键贡献是使用包含描述、推理和结论的三阶段过程创建结构化的CoT标注。然后，对我们的模型进行微调，以生成这种结构化的输出，然后将其最终检索意图编码到专用嵌入中。综合实验表明，CIR-CoT在领域内数据集(FashionIQ, CIRR)上取得了极具竞争力的性能，并在领域外CIRCO数据集上展示了卓越的泛化能力，为更有效和值得信赖的检索系统开辟了一条新道路。

## 🔬 方法详解

**问题定义**：组合图像检索(CIR)任务旨在根据给定的参考图像和文本描述，从图像库中检索出符合描述的目标图像。现有方法，特别是基于VLM和MLLM的方法，通常缺乏可解释性，用户难以理解模型做出检索决策的原因。此外，这些模型在处理复杂、细粒度的指令时能力有限。

**核心思路**：CIR-CoT的核心思路是引入思维链(Chain-of-Thought, CoT)推理，使模型在检索之前先生成一个可解释的推理链。这个推理链明确地表达了模型如何理解参考图像和文本描述，以及如何将它们结合起来进行检索。通过这种方式，模型不仅提高了检索的准确性，还增强了其可解释性。

**技术框架**：CIR-CoT的整体框架包括以下几个主要模块：1) 输入模块：接收参考图像和文本描述作为输入。2) CoT生成模块：利用MLLM生成一个结构化的推理链，包括图像和文本的描述、推理过程和最终结论。3) 嵌入编码模块：将生成的推理链编码成一个嵌入向量，用于检索。4) 检索模块：根据嵌入向量从图像库中检索出最匹配的目标图像。

**关键创新**：CIR-CoT最重要的技术创新点在于将思维链推理引入到组合图像检索任务中，并设计了一个端到端的模型来实现这一目标。与现有方法相比，CIR-CoT不仅提高了检索的准确性，还增强了模型的可解释性，使得用户可以理解模型做出检索决策的原因。此外，论文还创建了一个结构化的CoT标注数据集，为训练CIR-CoT模型提供了必要的数据支持。

**关键设计**：CIR-CoT的关键设计包括：1) 使用MLLM（例如Qwen-VL）作为CoT生成模块的基础模型。2) 设计了一个三阶段的CoT标注过程，包括描述、推理和结论。3) 使用对比学习损失函数来训练嵌入编码模块，使得相似的图像和文本描述具有相似的嵌入向量。4) 对MLLM进行微调，使其能够生成结构化的CoT输出。

## 📊 实验亮点

CIR-CoT在FashionIQ和CIRR等数据集上取得了极具竞争力的性能，并在领域外CIRCO数据集上展示了卓越的泛化能力。具体性能数据未在摘要中给出，但强调了其在多个数据集上的优越表现，证明了其有效性和泛化能力。

## 🎯 应用场景

CIR-CoT在电商、时尚、室内设计等领域具有广泛的应用前景。例如，用户可以通过上传一张衣服的图片，并输入“换个颜色”等描述，快速找到满足要求的商品。该研究有助于提升检索系统的用户体验和信任度，并为开发更智能、更可信赖的AI系统提供借鉴。

## 📄 摘要（原文）

> Composed Image Retrieval (CIR), which aims to find a target image from a reference image and a modification text, presents the core challenge of performing unified reasoning across visual and semantic modalities. While current approaches based on Vision-Language Models (VLMs, e.g., CLIP) and more recent Multimodal Large Language Models (MLLMs, e.g., Qwen-VL) have shown progress, they predominantly function as ``black boxes." This inherent opacity not only prevents users from understanding the retrieval rationale but also restricts the models' ability to follow complex, fine-grained instructions. To overcome these limitations, we introduce CIR-CoT, the first end-to-end retrieval-oriented MLLM designed to integrate explicit Chain-of-Thought (CoT) reasoning. By compelling the model to first generate an interpretable reasoning chain, CIR-CoT enhances its ability to capture crucial cross-modal interactions, leading to more accurate retrieval while making its decision process transparent. Since existing datasets like FashionIQ and CIRR lack the necessary reasoning data, a key contribution of our work is the creation of structured CoT annotations using a three-stage process involving a caption, reasoning, and conclusion. Our model is then fine-tuned to produce this structured output before encoding its final retrieval intent into a dedicated embedding. Comprehensive experiments show that CIR-CoT achieves highly competitive performance on in-domain datasets (FashionIQ, CIRR) and demonstrates remarkable generalization on the out-of-domain CIRCO dataset, establishing a new path toward more effective and trustworthy retrieval systems.

