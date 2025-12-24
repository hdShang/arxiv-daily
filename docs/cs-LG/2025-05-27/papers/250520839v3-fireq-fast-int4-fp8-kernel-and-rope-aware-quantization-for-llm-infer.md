---
layout: default
title: "FireQ: Fast INT4-FP8 Kernel and RoPE-aware Quantization for LLM Inference Acceleration"
---

# FireQ: Fast INT4-FP8 Kernel and RoPE-aware Quantization for LLM Inference Acceleration

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20839" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20839v3</a>
  <a href="https://arxiv.org/pdf/2505.20839.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20839v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20839v3', 'FireQ: Fast INT4-FP8 Kernel and RoPE-aware Quantization for LLM Inference Acceleration')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Daehyeon Baek, Jieun Choi, Jimyoung Son, Kyungmin Bin, Seungbeom Choi, Kihyo Moon, Minsung Jang, Hyojung Lee

**分类**: cs.LG

**发布日期**: 2025-05-27 (更新: 2025-07-18)

---

## 💡 一句话要点

**提出FireQ以解决大语言模型推理加速问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `推理加速` `后训练量化` `INT4` `FP8` `异常平滑` `FlashAttention` `RoPE`

## 📋 核心要点

1. 现有方法在大语言模型推理中面临内存带宽限制，导致吞吐量不足。
2. FireQ通过将线性层权重和关键值量化为INT4，激活值和查询量化为FP8，显著提升推理速度。
3. 在Llama2-7B上，FireQ实现了1.68倍的推理加速，在Llama3-8B的预填充阶段性能提升1.26倍，且精度损失极小。

## 📝 摘要（中文）

随着大语言模型的广泛应用，内存带宽限制显著影响推理吞吐量，促使后训练量化（PTQ）技术的发展。本文提出了FireQ，一个共同设计的PTQ框架和INT4-FP8矩阵乘法内核，旨在加速所有线性层的LLM推理。FireQ将线性层权重和关键值量化为INT4，将激活值和查询量化为FP8，从而显著提高吞吐量。此外，我们引入了三阶段的预填充管道，修改了FlashAttention-3内核，有效减少了预填充阶段的首次令牌时间。为最小化量化带来的精度损失，我们开发了针对线性和注意力层的独特异常平滑技术。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型推理中的内存带宽限制问题，现有方法在推理吞吐量上存在显著不足。

**核心思路**：FireQ通过将不同层的权重和激活值采用不同的量化格式（INT4和FP8），以此来提高推理效率并减少内存占用。

**技术框架**：FireQ的整体架构包括量化模块、三阶段预填充管道和异常平滑技术，分别针对线性层和注意力层进行优化。

**关键创新**：FireQ的主要创新在于结合了INT4和FP8的量化策略，并针对RoPE的挑战提出了预后平滑策略，显著提升了推理性能。

**关键设计**：在量化过程中，采用了每个张量的缩放因子以防止FP8量化引起的下溢，并在注意力层中结合了预RoPE和后RoPE的缩放策略。

## 📊 实验亮点

FireQ在Llama2-7B上实现了1.68倍的推理加速，在Llama3-8B的预填充阶段性能提升1.26倍，相较于QServe，且精度损失几乎可以忽略不计，展示了其在实际应用中的显著优势。

## 🎯 应用场景

FireQ的研究成果可广泛应用于大语言模型的推理加速，特别是在需要高吞吐量和低延迟的场景中，如实时对话系统、智能客服和在线翻译等领域。其技术创新将推动相关领域的进一步发展，提升用户体验。

## 📄 摘要（原文）

> As large language models become increasingly prevalent, memory bandwidth constraints significantly limit inference throughput, motivating post-training quantization (PTQ). In this paper, we propose FireQ, a co-designed PTQ framework and an INT4-FP8 matrix multiplication kernel that accelerates LLM inference across all linear layers. Specifically, FireQ quantizes linear layer weights and key-values to INT4, and activations and queries to FP8, significantly enhancing throughput. Additionally, we introduce a three-stage pipelining for the prefill phase, which modifies the FlashAttention-3 kernel, effectively reducing time-to-first-token in the prefill phase. To minimize accuracy loss from quantization, we develop novel outlier smoothing techniques tailored separately for linear and attention layers. In linear layers, we explicitly use per-tensor scaling to prevent underflow caused by the FP8 quantization scaling factor of INT4 quantization, and channel-wise scaling to compensate for coarse granularity of INT4. In attention layers, we address quantization challenges posed by rotary positional embeddings (RoPE) by combining pre-RoPE and post-RoPE scaling strategies. FireQ significantly outperforms state-of-the-art methods, achieving 1.68x faster inference in feed-forward network layers on Llama2-7B and 1.26x faster prefill phase performance on Llama3-8B compared to QServe, with negligible accuracy loss.

