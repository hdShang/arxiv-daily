---
layout: default
title: Scaling Laws for Energy Efficiency of Local LLMs
---

# Scaling Laws for Energy Efficiency of Local LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16531" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16531v1</a>
  <a href="https://arxiv.org/pdf/2512.16531.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16531v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16531v1', 'Scaling Laws for Energy Efficiency of Local LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ander Alvarez, Alessandro Genuardi, Nilotpal Sinha, Antonio Tiene, Samuel Mugel, Román Orús

**分类**: cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**针对本地LLM，揭示CPU能效缩放规律，并提出量子启发压缩优化方案。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `本地LLM` `CPU能效` `缩放规律` `边缘计算` `模型压缩` `量子启发` `视觉语言模型`

## 📋 核心要点

1. 现有方法在边缘设备上部署LLM时，未能充分探索CPU的能效缩放规律，导致资源利用率不高。
2. 本文通过在主流CPU上进行基准测试，揭示了语言模型和视觉语言模型在CPU上的能耗缩放规律。
3. 实验表明，量子启发压缩能显著降低CPU和内存使用率，并降低能耗，同时保持甚至提高模型精度。

## 📝 摘要（中文）

在边缘设备上部署本地大型语言模型和视觉语言模型需要在精度、计算和能源预算之间取得平衡。尽管图形处理器在现代人工智能部署中占据主导地位，但大多数消费级硬件（包括笔记本电脑、台式机、工业控制器和嵌入式系统）依赖于中央处理器。本文系统地对两种广泛用于本地推理的中央处理器进行了基准测试：MacBook Pro M2（代表主流笔记本电脑）和 Raspberry Pi 5（代表低功耗嵌入式环境）。通过统一的方法，即连续采样处理器和内存使用情况以及曲线下面积积分，我们描述了语言模型的计算负载如何随输入文本长度缩放，以及视觉语言模型的计算负载如何随图像分辨率缩放。我们发现了两个经验缩放规律：（1）语言模型推理的计算成本与token长度近似线性缩放；（2）视觉语言模型表现出由预处理驱动的“分辨率膝点”，即计算量在内部分辨率钳位之上保持不变，而在其之下急剧下降。此外，我们表明，量子启发压缩可将处理器和内存使用率降低高达71.9%，并将能耗降低高达62%，同时保持或提高语义准确性。这些结果系统地量化了多模态中央处理器在本地语言和视觉语言工作负载中的缩放规律，并确定了模型压缩和输入分辨率预处理是可持续边缘推理的有效且低成本的手段。

## 🔬 方法详解

**问题定义**：论文旨在解决在CPU上部署本地大型语言模型和视觉语言模型时，如何优化能效的问题。现有方法缺乏对CPU上LLM能耗缩放规律的系统研究，导致在资源受限的边缘设备上部署时，难以做出合理的性能和能耗权衡。

**核心思路**：论文的核心思路是通过实验测量和分析，揭示LLM和VLM在CPU上的计算负载与输入长度/分辨率之间的关系，从而建立经验性的缩放规律。然后，利用模型压缩技术（量子启发压缩）来降低计算和内存需求，从而提高能效。

**技术框架**：论文采用的整体框架包括：1) 在两种代表性的CPU平台（MacBook Pro M2和Raspberry Pi 5）上进行基准测试；2) 使用统一的方法，连续采样CPU和内存使用情况，并计算曲线下面积；3) 分析计算负载与输入长度/分辨率之间的关系，建立缩放规律；4) 应用量子启发压缩，评估其对性能和能耗的影响。

**关键创新**：论文的关键创新在于：1) 首次系统地研究了LLM和VLM在CPU上的能耗缩放规律，并提出了两个经验性的缩放规律；2) 验证了量子启发压缩在降低CPU能耗方面的有效性，并表明其可以在保持甚至提高模型精度的前提下，显著降低资源消耗。

**关键设计**：论文的关键设计包括：1) 选择具有代表性的CPU平台，覆盖主流笔记本电脑和低功耗嵌入式设备；2) 采用连续采样和曲线下面积积分的方法，准确测量CPU和内存使用情况；3) 使用量子启发压缩，具体实现细节未知，但强调了其在压缩模型的同时保持或提高语义准确性的能力。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16531v1/figures/updated/llm_mac_cpu_auc.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16531v1/figures/updated/llm_rpi_cpu_auc.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16531v1/figures/updated/vlm_mac_cpu_auc.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，语言模型推理的计算成本与token长度近似线性缩放；视觉语言模型存在“分辨率膝点”现象。量子启发压缩可将处理器和内存使用率降低高达71.9%，并将能耗降低高达62%，同时保持或提高语义准确性。这些数据突出了模型压缩在边缘设备上部署LLM和VLM的潜力。

## 🎯 应用场景

该研究成果可应用于各种边缘计算场景，例如在智能家居设备、工业控制器、机器人等资源受限的设备上部署本地LLM和VLM，实现低功耗、高性能的AI应用。通过模型压缩和输入分辨率预处理，可以有效降低部署成本，并提高设备续航能力。

## 📄 摘要（原文）

> Deploying local large language models and vision-language models on edge devices requires balancing accuracy with constrained computational and energy budgets. Although graphics processors dominate modern artificial-intelligence deployment, most consumer hardware--including laptops, desktops, industrial controllers, and embedded systems--relies on central processing units. Despite this, the computational laws governing central-processing-unit-only inference for local language and vision-language workloads remain largely unexplored. We systematically benchmark large language and vision-language models on two representative central-processing-unit tiers widely used for local inference: a MacBook Pro M2, reflecting mainstream laptop-class deployment, and a Raspberry Pi 5, representing constrained, low-power embedded settings. Using a unified methodology based on continuous sampling of processor and memory usage together with area-under-curve integration, we characterize how computational load scales with input text length for language models and with image resolution for vision-language models. We uncover two empirical scaling laws: (1) computational cost for language-model inference scales approximately linearly with token length; and (2) vision-language models exhibit a preprocessing-driven "resolution knee", where compute remains constant above an internal resolution clamp and decreases sharply below it. Beyond these laws, we show that quantum-inspired compression reduces processor and memory usage by up to 71.9% and energy consumption by up to 62%, while preserving or improving semantic accuracy. These results provide a systematic quantification of multimodal central-processing-unit-only scaling for local language and vision-language workloads, and they identify model compression and input-resolution preprocessing as effective, low-cost levers for sustainable edge inference.

