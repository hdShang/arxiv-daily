---
layout: default
title: Recurrent Attention-based Token Selection for Efficient Streaming Video-LLMs
---

# Recurrent Attention-based Token Selection for Efficient Streaming Video-LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.17364" class="toolbar-btn" target="_blank">📄 arXiv: 2510.17364v1</a>
  <a href="https://arxiv.org/pdf/2510.17364.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.17364v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.17364v1', 'Recurrent Attention-based Token Selection for Efficient Streaming Video-LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Vaggelis Dorovatas, Soroush Seifi, Gunshi Gupta, Rahaf Aljundi

**分类**: cs.CV, cs.LG

**发布日期**: 2025-10-20

**备注**: NeurIPS 2025

---

## 💡 一句话要点

**提出基于循环注意力的Token选择方法，用于高效的流式视频-LLM**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `流式视频理解` `视频大语言模型` `注意力机制` `Token选择` `循环神经网络`

## 📋 核心要点

1. 现有Video-LLM在处理长视频流时，计算成本高昂，难以满足实时性要求。
2. 该方法利用LLM的注意力机制选择关键视觉token，并循环处理，从而减少计算量并保持时间连贯性。
3. 实验表明，该方法在流式视频基准测试中取得了领先性能，同时显著提高了效率。

## 📝 摘要（中文）

视频大语言模型(Video-LLM)擅长理解视频上下文，但前提是它们在回答问题时可以完全访问视频。然而，这些模型在流式传输场景中面临挑战，因为需要在线处理长达数小时的视频，并及时响应问题。本文提出了一种与标准Video-LLM兼容的无训练方法，利用三个关键概念：1) LLM感知的视觉token选择，以识别LLM已关注并有助于其理解每个短片段的token。基于注意力的选择使我们能够丢弃高达约95%的不重要视觉token，而性能损失最小；2) 循环处理过去选择的token，以生成对每个已处理片段的时间连贯理解；3) 基于字幕的问答，以实现轻量级和准确的响应。我们的方法在流式视频基准测试中实现了最先进的性能，在效率和有效性之间取得了平衡。

## 🔬 方法详解

**问题定义**：现有Video-LLM在处理流式长视频时，需要处理大量的视觉token，计算复杂度高，难以满足实时性要求。尤其是在需要快速响应用户提问的场景下，效率问题更加突出。现有方法通常需要对整个视频进行编码，无法适应流式处理的需求。

**核心思路**：论文的核心思路是利用LLM自身的注意力机制，动态地选择对理解视频内容至关重要的视觉token，并丢弃冗余信息。通过循环处理选定的token，模型可以维护对视频内容的时间连贯性理解，从而在保证性能的同时显著降低计算成本。

**技术框架**：该方法主要包含三个阶段：1) **LLM-informed Token Selection**: 利用LLM的注意力权重，选择对当前视频片段理解贡献最大的视觉token。2) **Recurrent Processing**: 将选定的token输入循环神经网络，以捕捉视频片段之间的时间依赖关系，生成时间连贯的视频表示。3) **Caption-based Question Answering**: 基于生成的视频表示和问题，生成答案。

**关键创新**：该方法最重要的创新点在于利用LLM自身的注意力信息进行token选择，无需额外的训练。这种方法能够有效地识别并保留对LLM理解视频内容至关重要的token，同时丢弃冗余信息，从而显著降低计算成本。与现有方法相比，该方法更加高效，且易于集成到现有的Video-LLM框架中。

**关键设计**：Token选择模块使用LLM在处理当前视频片段时产生的注意力权重，选择权重最高的token。循环处理模块可以使用GRU或LSTM等循环神经网络。Caption-based Question Answering模块可以使用标准的文本生成模型，如Transformer。具体的参数设置和网络结构可以根据具体的Video-LLM和任务进行调整。

## 📊 实验亮点

该方法在流式视频基准测试中取得了state-of-the-art的性能，同时能够丢弃高达95%的视觉token，显著提高了计算效率。实验结果表明，该方法在保证性能的同时，能够有效地降低计算成本，使其更适用于实际应用场景。具体的性能提升数据和对比基线信息需要在论文中查找。

## 🎯 应用场景

该研究成果可广泛应用于需要实时视频理解的场景，例如智能监控、自动驾驶、在线教育、视频会议等。通过降低计算成本，该方法使得Video-LLM能够在资源受限的设备上运行，并能够更快地响应用户提问，提升用户体验。未来，该方法可以进一步扩展到其他多模态任务中，例如语音识别和自然语言处理。

## 📄 摘要（原文）

> Video Large Language Models (Video-LLMs) excel at understanding videos in-context, provided they have full access to the video when answering queries. However, these models face challenges in streaming scenarios where hour-long videos must be processed online, and questions need timely responses. In this work, we propose a training-free approach compatible with standard Video-LLMs, leveraging three key concepts: 1) LLM-informed selection of visual tokens to identify those that the LLM has attended to and contributed to its understanding of each short clip. Our attention-based selection allows us to discard up to ~95% of unimportant visual tokens with minimal performance loss; 2) Recurrent processing of past selected tokens to generate temporally coherent understanding of each processed clip; 3) Caption-based question answering for lightweight and accurate responses. Our method achieves state-of-the-art performance on streaming video benchmarks, striking a balance between efficiency and effectiveness.

