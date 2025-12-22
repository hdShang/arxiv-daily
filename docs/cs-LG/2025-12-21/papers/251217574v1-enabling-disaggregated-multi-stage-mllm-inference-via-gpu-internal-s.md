---
layout: default
title: Enabling Disaggregated Multi-Stage MLLM Inference via GPU-Internal Scheduling and Resource Sharing
---

# Enabling Disaggregated Multi-Stage MLLM Inference via GPU-Internal Scheduling and Resource Sharing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17574" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17574v1</a>
  <a href="https://arxiv.org/pdf/2512.17574.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17574v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17574v1', 'Enabling Disaggregated Multi-Stage MLLM Inference via GPU-Internal Scheduling and Resource Sharing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lingxiao Zhao, Haoran Zhou, Yuezhi Che, Dazhao Cheng

**分类**: cs.DC, cs.LG

**发布日期**: 2025-12-19

---

## 💡 一句话要点

**提出FlashCodec和UnifiedServe，通过GPU内调度和资源共享加速多阶段MLLM推理。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `MLLM推理` `GPU加速` `视频解码` `资源调度` `系统优化` `低延迟` `高吞吐量`

## 📋 核心要点

1. 现有MLLM系统在多模态预处理（特别是视频解码）和视觉编码阶段存在瓶颈，导致TTFT过高和资源利用率不足。
2. 论文提出FlashCodec和UnifiedServe，分别加速视频解码和优化视觉编码与LLM推理的协同执行，从而提升整体性能。
3. 实验结果表明，该框架能够显著提升MLLM系统的请求服务能力、满足更严格的SLO，并提高吞吐量，最高可达4.4倍。

## 📝 摘要（中文）

多模态大型语言模型（MLLM）通过三个阶段的流程扩展了LLM的视觉理解能力：多模态预处理、视觉编码和LLM推理。这些阶段的增强能力也带来了显著的系统瓶颈。首先，多模态预处理，特别是视频解码，通常主导了首个token生成时间（TTFT）。大多数系统依赖于基于CPU的解码，这严重限制了吞吐量，而现有的基于GPU的方法优先考虑面向吞吐量的并行性，无法满足MLLM推理的延迟敏感性要求。其次，视觉编码器是一个独立的、计算密集型的阶段，它生成视觉嵌入，无法与LLM的预填充或解码进行联合批处理。这种异构性迫使阶段间阻塞，并增加了token生成延迟。即使部署在单独的GPU上，这些阶段也未能充分利用可用的计算和内存资源，从而降低了总体利用率并限制了系统吞吐量。为了解决这些挑战，我们提出了FlashCodec和UnifiedServe，这两个互补的设计共同优化端到端的MLLM流程。FlashCodec通过协作式多GPU视频解码加速多模态预处理阶段，从而在保持高吞吐量的同时降低解码延迟。UnifiedServe通过逻辑上解耦视觉到文本和推理阶段的执行来优化这两个阶段，从而消除阶段间阻塞，同时物理上共享GPU资源以最大化GPU系统利用率。通过精心编排跨阶段的执行并最小化干扰，UnifiedServe与FlashCodec共同构成了一个端到端优化的堆栈，与最先进的系统相比，可以提供高达3.0倍的请求服务能力或强制执行1.5倍更严格的SLO，同时实现高达4.4倍的吞吐量。

## 🔬 方法详解

**问题定义**：现有MLLM推理系统面临的主要问题是多模态预处理（尤其是视频解码）的延迟瓶颈以及视觉编码阶段与LLM推理阶段的异构性导致的资源利用率低下。CPU解码速度慢，GPU解码又难以兼顾低延迟。视觉编码器无法与LLM联合批处理，导致阶段间阻塞，降低了整体吞吐量和响应速度。

**核心思路**：论文的核心思路是通过软硬件协同优化，解决MLLM推理流程中的瓶颈。FlashCodec通过多GPU协作加速视频解码，降低预处理延迟。UnifiedServe通过解耦执行逻辑，同时共享GPU资源，消除阶段间阻塞，提高资源利用率。

**技术框架**：整体框架包含两个主要组件：FlashCodec和UnifiedServe。FlashCodec负责加速多模态预处理阶段的视频解码，采用多GPU并行解码策略。UnifiedServe负责优化视觉编码和LLM推理阶段，通过逻辑解耦和物理共享GPU资源，实现高效的阶段间协同。整个流程旨在最小化端到端延迟，最大化系统吞吐量。

**关键创新**：论文的关键创新在于：1) FlashCodec提出的协作式多GPU视频解码方法，能够在保证高吞吐量的同时降低解码延迟。2) UnifiedServe提出的逻辑解耦和物理共享的执行策略，消除了视觉编码和LLM推理阶段之间的阻塞，提高了GPU资源利用率。

**关键设计**：FlashCodec的关键设计在于如何有效地将视频帧分配给多个GPU进行并行解码，并保证解码后的帧顺序正确。UnifiedServe的关键设计在于如何实现视觉编码和LLM推理的逻辑解耦，使得两个阶段可以独立执行，同时又能够共享GPU资源，避免资源竞争和干扰。具体的参数设置和网络结构细节未在摘要中体现，属于未知信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17574v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17574v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17574v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，FlashCodec和UnifiedServe能够显著提升MLLM系统的性能。与最先进的系统相比，该框架可以提供高达3.0倍的请求服务能力，强制执行1.5倍更严格的SLO，并实现高达4.4倍的吞吐量。这些数据表明，该方法在实际应用中具有显著的优势。

## 🎯 应用场景

该研究成果可应用于各种需要实时多模态理解的场景，例如智能客服、视频分析、自动驾驶等。通过提高MLLM推理的效率和降低延迟，可以提升用户体验，并为更复杂的应用提供支持。未来，该技术有望推动多模态人工智能在实际场景中的广泛应用。

## 📄 摘要（原文）

> Multimodal large language models (MLLMs) extend LLMs with visual understanding through a three-stage pipeline: multimodal preprocessing, vision encoding, and LLM inference. While these stages enhance capability, they introduce significant system bottlenecks. First, multimodal preprocessing-especially video decoding-often dominates Time-to-First-Token (TTFT). Most systems rely on CPU-based decoding, which severely limits throughput, while existing GPU-based approaches prioritize throughput-oriented parallelism and fail to meet the latency-sensitive requirements of MLLM inference. Second, the vision encoder is a standalone, compute-intensive stage that produces visual embeddings and cannot be co-batched with LLM prefill or decoding. This heterogeneity forces inter-stage blocking and increases token-generation latency. Even when deployed on separate GPUs, these stages underutilize available compute and memory resources, reducing overall utilization and constraining system throughput.
>   To address these challenges, we present FlashCodec and UnifiedServe, two complementary designs that jointly optimize the end-to-end MLLM pipeline. FlashCodec accelerates the multimodal preprocessing stage through collaborative multi-GPU video decoding, reducing decoding latency while preserving high throughput. UnifiedServe optimizes the vision-to-text and inference stages using a logically decoupled their execution to eliminate inter-stage blocking, yet physically sharing GPU resources to maximize GPU system utilization. By carefully orchestrating execution across stages and minimizing interference, UnifiedServe Together, our proposed framework forms an end-to-end optimized stack that can serve up to 3.0$\times$ more requests or enforce 1.5$\times$ tighter SLOs, while achieving up to 4.4$\times$ higher throughput compared to state-of-the-art systems.

