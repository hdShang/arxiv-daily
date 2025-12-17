---
layout: default
title: Small Drafts, Big Verdict: Information-Intensive Visual Reasoning via Speculation
---

# Small Drafts, Big Verdict: Information-Intensive Visual Reasoning via Speculation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.20812" class="toolbar-btn" target="_blank">📄 arXiv: 2510.20812v3</a>
  <a href="https://arxiv.org/pdf/2510.20812.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.20812v3" onclick="toggleFavorite(this, '2510.20812v3', 'Small Drafts, Big Verdict: Information-Intensive Visual Reasoning via Speculation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuhan Liu, Lianhui Qin, Shengjie Wang

**分类**: cs.CV, cs.AI, cs.CL

**发布日期**: 2025-10-23 (更新: 2025-12-09)

**🔗 代码/项目**: [GITHUB](https://github.com/Tinaliu0123/speculative-verdict)

---

## 💡 一句话要点

**提出Speculative Verdict框架，解决信息密集型图像的视觉推理难题。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉问答` `多模态推理` `信息密集型图像` `推测解码` `视觉-语言模型`

## 📋 核心要点

1. 现有VLM在处理信息密集型图像时，难以精确定位关键线索并进行多跳推理。
2. Speculative Verdict框架利用多个小型VLM生成推理路径，再由大型VLM综合判断，实现高效推理。
3. 实验表明，SV在多个信息密集型VQA基准上取得了显著提升，兼顾了准确性和效率。

## 📝 摘要（中文）

大型视觉-语言模型(VLMs)在多模态理解方面取得了显著进展，但当推理信息密集型图像时，它们表现不佳，这些图像将文本注释与精细的图形元素密集地交织在一起。主要的挑战在于精确地定位密集布局中的关键线索以及进行多跳推理以整合分散的证据。我们提出了一种受推测解码启发的免训练框架Speculative Verdict (SV)，它将多个轻量级草案专家与一个大型判决模型相结合。在草案阶段，小型VLM充当草案专家，生成提供多样化定位候选的推理路径；在判决阶段，强大的VLM综合这些路径以产生最终答案，从而在恢复正确答案的同时最大限度地降低计算成本。为了进一步提高效率和准确性，SV引入了一种共识专家选择机制，该机制仅将高度一致的推理路径转发给判决模型。在具有挑战性的信息密集型和高分辨率视觉问答基准测试（包括InfographicVQA、ChartMuseum、ChartQAPro和HR-Bench 4K）上，SV实现了持续的收益。通过综合来自多个部分准确的推理路径的正确见解，与大型专有模型或训练流程相比，SV实现了错误纠正和成本效率。

## 🔬 方法详解

**问题定义**：论文旨在解决视觉-语言模型（VLM）在处理信息密集型图像时面临的挑战。这类图像通常包含大量的文本注释和复杂的图形元素，使得VLM难以准确定位关键信息并进行多步推理。现有方法要么计算成本高昂，要么准确率不足，无法有效解决此类问题。

**核心思路**：论文的核心思路是借鉴推测解码的思想，利用多个小型、轻量级的VLM作为“草案专家”，并行生成多个可能的推理路径。然后，使用一个大型、强大的VLM作为“判决模型”，综合评估这些推理路径，并给出最终答案。这种方法旨在利用小型模型的效率和大型模型的准确性，实现计算成本和性能之间的平衡。

**技术框架**：Speculative Verdict (SV) 框架包含两个主要阶段：草案阶段和判决阶段。在草案阶段，多个小型VLM（草案专家）独立地对输入图像进行推理，生成多个候选的推理路径。每个推理路径都包含对图像中关键信息的定位和推理过程。在判决阶段，一个大型VLM（判决模型）接收所有草案专家生成的推理路径，并综合评估这些路径，最终生成答案。为了提高效率，SV还引入了一个共识专家选择机制，只将草案专家达成高度一致的推理路径传递给判决模型。

**关键创新**：SV框架的关键创新在于其推测式的推理方式，它将复杂的推理任务分解为多个并行的小任务，然后通过综合评估这些小任务的结果来得到最终答案。这种方法有效地利用了多个模型的优势，实现了错误纠正和成本效率。此外，共识专家选择机制进一步提高了效率，减少了判决模型的计算负担。

**关键设计**：论文中没有明确说明具体的参数设置、损失函数或网络结构等技术细节。草案专家可以是任何小型VLM，判决模型可以是任何大型VLM。共识专家选择机制的具体实现方式也未详细描述，但可以基于不同草案专家输出的相似度或置信度进行设计。这些细节可能根据具体的应用场景和模型选择而有所不同，属于实现层面的优化。

## 📊 实验亮点

Speculative Verdict框架在InfographicVQA、ChartMuseum、ChartQAPro和HR-Bench 4K等信息密集型视觉问答基准测试上取得了显著提升。具体性能数据和对比基线未在摘要中给出，但强调了SV能够综合多个部分准确的推理路径，实现错误纠正和成本效率，优于大型专有模型或训练流程。

## 🎯 应用场景

该研究成果可应用于信息图表分析、金融报告解读、科学文献理解等领域。通过提高VLM在信息密集型图像上的推理能力，可以帮助用户更高效地从复杂数据中提取关键信息，辅助决策，并提升自动化分析的准确性。

## 📄 摘要（原文）

> Large Vision-Language Models (VLMs) have achieved remarkable progress in multimodal understanding, yet they struggle when reasoning over information-intensive images that densely interleave textual annotations with fine-grained graphical elements. The main challenges lie in precisely localizing critical cues in dense layouts and multi-hop reasoning to integrate dispersed evidence. We propose Speculative Verdict (SV), a training-free framework inspired by speculative decoding that combines multiple lightweight draft experts with a large verdict model. In the draft stage, small VLMs act as draft experts to generate reasoning paths that provide diverse localization candidates; in the verdict stage, a strong VLM synthesizes these paths to produce the final answer, minimizing computational cost while recovering correct answers. To further improve efficiency and accuracy, SV introduces a consensus expert selection mechanism that forwards only high-agreement reasoning paths to the verdict. Empirically, SV achieves consistent gains on challenging information-intensive and high-resolution visual question answering benchmarks, including InfographicVQA, ChartMuseum, ChartQAPro, and HR-Bench 4K. By synthesizing correct insights from multiple partially accurate reasoning paths, SV achieves both error correction and cost-efficiency compared to large proprietary models or training pipelines. Code is available at https://github.com/Tinaliu0123/speculative-verdict.

