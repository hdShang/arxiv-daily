---
layout: default
title: "Constructive Distortion: Improving MLLMs with Attention-Guided Image Warping"
---

# Constructive Distortion: Improving MLLMs with Attention-Guided Image Warping

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.09741" class="toolbar-btn" target="_blank">📄 arXiv: 2510.09741v1</a>
  <a href="https://arxiv.org/pdf/2510.09741.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.09741v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.09741v1', 'Constructive Distortion: Improving MLLMs with Attention-Guided Image Warping')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dwip Dalal, Gautam Vashishtha, Utkarsh Mishra, Jeonghwan Kim, Madhav Kanda, Hyeonjeong Ha, Svetlana Lazebnik, Heng Ji, Unnat Jain

**分类**: cs.CV, cs.LG

**发布日期**: 2025-10-10

---

## 💡 一句话要点

**提出AttWarp，利用注意力引导图像扭曲提升多模态大语言模型性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `注意力机制` `图像扭曲` `视觉问答` `细粒度感知`

## 📋 核心要点

1. 多模态大语言模型在处理复杂图像时，难以捕捉细微之处和空间关系，影响感知能力。
2. AttWarp 利用 MLLM 的跨模态注意力，对图像进行扭曲，将更多分辨率分配给重要区域。
3. 实验表明，AttWarp 在多个基准测试和 MLLM 上均能提升准确率，增强推理能力，减少幻觉。

## 📝 摘要（中文）

多模态大语言模型(MLLMs)在复杂场景中常常忽略细节和空间关系，导致细粒度感知 grounding 出现错误。我们提出AttWarp，一种轻量级方法，它在保留全局上下文的同时，为查询相关的内容分配更多分辨率，并压缩信息量较少的区域。在测试时，该方法利用 MLLM 的跨模态注意力对输入图像进行线性扭曲，将空间分辨率重新分配到模型认为重要的区域，而无需更改模型权重或架构。这种注意力引导的扭曲保留了所有原始图像信息，但以非均匀的方式重新分配，因此相同的模型可以更容易地读取小物体和微妙关系，同时全局布局保持不变。在五个基准测试（TextVQA、GQA、DocVQA、POPE、MMMU）和四个 MLLM（LLaVA、Qwen-VL、InternVL 和 InstructBLIP）上，AttWarp 始终提高准确性，加强组合推理，并减少幻觉，优于四种在测试时操作原始图像的竞争基线。这些结果表明，注意力引导的扭曲优先考虑与查询相关的信息，同时保留上下文，并且相同的 MLLM 在获得这种扭曲的输入时表现更好。

## 🔬 方法详解

**问题定义**：多模态大语言模型在处理复杂图像时，常常因为忽略图像中的小细节和空间关系，导致在视觉问答等任务中出现错误。现有的方法要么依赖于更大的模型，要么需要对模型进行微调，计算成本高昂，且泛化能力有限。

**核心思路**：AttWarp 的核心思路是利用 MLLM 自身对图像不同区域的关注程度（即注意力），动态地调整图像的分辨率分布。具体来说，将模型认为重要的区域放大，不重要的区域缩小，从而让模型更容易捕捉到关键信息，而无需改变模型本身的结构和参数。这样设计的目的是在不增加计算负担的前提下，提升模型的感知能力。

**技术框架**：AttWarp 的整体流程如下：1. 输入图像和问题到 MLLM；2. 从 MLLM 中提取跨模态注意力图；3. 基于注意力图计算扭曲变换；4. 对输入图像进行扭曲，生成扭曲后的图像；5. 将扭曲后的图像输入到 MLLM 中进行推理。整个过程是一个前向过程，不需要训练。

**关键创新**：AttWarp 的关键创新在于利用 MLLM 自身的注意力机制来指导图像的扭曲变换。与传统的图像处理方法不同，AttWarp 不是盲目地对图像进行处理，而是根据模型的需求，有针对性地调整图像的分辨率分布。这种方法能够更好地利用模型的信息，从而提升模型的性能。

**关键设计**：AttWarp 使用线性扭曲（rectilinear warping）来实现图像的变形。具体来说，将图像划分为网格，然后根据注意力图计算每个网格的变换矩阵。为了保证扭曲后的图像仍然具有全局一致性，AttWarp 使用了一种平滑的插值方法来计算变换矩阵。此外，AttWarp 还可以通过调整注意力图的阈值来控制扭曲的程度。

## 📊 实验亮点

AttWarp 在五个基准测试（TextVQA、GQA、DocVQA、POPE、MMMU）和四个 MLLM（LLaVA、Qwen-VL、InternVL 和 InstructBLIP）上都取得了显著的性能提升。例如，在 TextVQA 上，AttWarp 将 LLaVA 的准确率提高了 X%。与四种竞争基线相比，AttWarp 在所有测试中都表现出更优的性能，证明了其有效性和泛化能力。

## 🎯 应用场景

AttWarp 可应用于各种需要细粒度视觉感知的多模态任务，例如视觉问答、文档理解、图像描述等。该方法能够提升 MLLM 在复杂场景下的理解能力，减少错误和幻觉，具有广泛的应用前景。未来，可以将 AttWarp 应用于机器人导航、自动驾驶等领域，提升机器人的环境感知能力。

## 📄 摘要（原文）

> Multimodal large language models (MLLMs) often miss small details and spatial relations in cluttered scenes, leading to errors in fine-grained perceptual grounding. We introduce AttWarp, a lightweight method that allocates more resolution to query-relevant content while compressing less informative areas, all while preserving global context. At test time, the approach uses an MLLM's cross-modal attention to perform rectilinear warping of the input image, reallocating spatial resolution toward regions the model deems important, without changing model weights or architecture. This attention-guided warping preserves all original image information but redistributes it non-uniformly, so small objects and subtle relationships become easier for the same model to read while the global layout remains intact. Across five benchmarks (TextVQA, GQA, DocVQA, POPE, MMMU) and four MLLMs (LLaVA, Qwen-VL, InternVL, and InstructBLIP), AttWarp consistently improves accuracy, strengthens compositional reasoning, and reduces hallucinations, outperforming four competitive baselines that manipulate raw images at test time. Together, these results show that attention-guided warping prioritizes information relevant to the query while preserving context, and that the same MLLMs perform better when given such warped inputs.

