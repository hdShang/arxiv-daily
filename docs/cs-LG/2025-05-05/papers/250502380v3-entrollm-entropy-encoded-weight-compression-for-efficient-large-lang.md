---
layout: default
title: EntroLLM: Entropy Encoded Weight Compression for Efficient Large Language Model Inference on Edge Devices
---

# EntroLLM: Entropy Encoded Weight Compression for Efficient Large Language Model Inference on Edge Devices

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02380" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02380v3</a>
  <a href="https://arxiv.org/pdf/2505.02380.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02380v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02380v3', 'EntroLLM: Entropy Encoded Weight Compression for Efficient Large Language Model Inference on Edge Devices')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Arnab Sanyal, Gourav Datta, Prithwish Mukherjee, Sandeep P. Chinchali, Michael Orshansky

**分类**: cs.LG

**发布日期**: 2025-05-05 (更新: 2025-07-14)

**备注**: 6 pages, 1 reference page

---

## 💡 一句话要点

**提出EntroLLM以解决边缘设备上大语言模型推理效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `边缘计算` `模型压缩` `混合量化` `熵编码` `霍夫曼编码` `推理效率` `实时处理`

## 📋 核心要点

1. 现有的大语言模型在边缘设备上的应用受到存储和计算资源的限制，难以高效推理。
2. EntroLLM通过混合量化和熵编码的结合，优化了模型的存储和推理效率，保持了准确性。
3. 实验表明，EntroLLM在存储上相比uint8模型减少了30%，并在推理吞吐量上提升了31.9%至146.6%。

## 📝 摘要（中文）

大语言模型（LLMs）在多种任务中表现出色，但其庞大的存储和计算需求限制了在边缘设备上的部署。为此，我们提出了EntroLLM，这是一种新颖的压缩框架，结合了混合量化和熵编码，以减少存储开销，同时保持模型准确性。我们采用逐层混合量化方案，根据各层权重分布选择对称或非对称量化，以优化可压缩性。接着，我们使用霍夫曼编码对量化权重进行无损压缩，显著降低内存带宽需求。此外，我们引入并行霍夫曼解码，确保在推理过程中高效检索编码权重，最小化延迟影响。实验结果表明，EntroLLM在边缘兼容的LLMs上实现了高达30%的存储减少，并在内存带宽受限的设备上提高了31.9%至146.6%的推理吞吐量。

## 🔬 方法详解

**问题定义**：当前大语言模型在边缘设备上的应用面临存储和计算资源的挑战，导致推理效率低下，无法满足实时需求。现有的压缩方法往往无法兼顾模型的准确性和推理速度。

**核心思路**：EntroLLM提出了一种结合混合量化和熵编码的压缩框架，通过逐层选择合适的量化方式，优化模型的存储需求，并采用霍夫曼编码实现无损压缩，确保在推理时的高效性。

**技术框架**：该方法的整体架构包括两个主要模块：首先是逐层混合量化，根据权重分布选择对称或非对称量化；其次是霍夫曼编码和并行解码模块，用于高效存储和快速检索量化后的权重。

**关键创新**：EntroLLM的创新之处在于其混合量化策略和并行霍夫曼解码的结合，显著提升了边缘设备的推理效率和存储利用率，与传统的单一量化方法相比，具有更好的性能表现。

**关键设计**：在量化过程中，模型根据每层的权重分布动态选择量化方式，霍夫曼编码则确保了量化权重的无损压缩。此外，设计中未增加额外的再训练步骤，使得该方法与现有的后训练量化方法完全兼容。

## 📊 实验亮点

EntroLLM在边缘兼容的LLMs上实现了高达30%的存储减少，相比于uint4模型更是达到了65%的存储减少。同时，在内存带宽受限的设备上，推理吞吐量提升了31.9%至146.6%，显示出显著的性能优势。

## 🎯 应用场景

EntroLLM的研究成果在边缘计算、移动设备和物联网等领域具有广泛的应用潜力。通过提高大语言模型的推理效率和降低存储需求，该方法能够支持更多智能应用的实时处理，推动边缘智能的发展。未来，该技术可能在智能助手、自动驾驶和智能家居等场景中发挥重要作用。

## 📄 摘要（原文）

> Large Language Models (LLMs) demonstrate exceptional performance across various tasks, but their large storage and computational requirements constrain their deployment on edge devices. To address this, we propose EntroLLM, a novel compression framework that integrates mixed quantization with entropy coding to reduce storage overhead while maintaining model accuracy. Our method applies a layer-wise mixed quantization scheme - choosing between symmetric and asymmetric quantization based on individual layer weight distributions - to optimize compressibility. We then employ Huffman encoding for lossless compression of the quantized weights, significantly reducing memory bandwidth requirements. Furthermore, we introduce parallel Huffman decoding, which enables efficient retrieval of encoded weights during inference, ensuring minimal latency impact. Our experiments on edge-compatible LLMs, including smolLM-1.7B-Instruct, phi3-mini-4k-Instruct, and mistral-7B-Instruct, demonstrate that EntroLLM achieves up to $30\%$ storage reduction compared to uint8 models and up to $65%$ storage reduction compared to uint4 models, while preserving perplexity and accuracy, on language benchmark tasks. We further show that our method enables $31.9\%$ - $146.6\%$ faster inference throughput on memory-bandwidth-limited edge devices, such as NVIDIA Jetson P3450, by reducing the required data movement. The proposed approach requires no additional re-training and is fully compatible with existing post-training quantization methods, making it a practical solution for edge LLMs.

