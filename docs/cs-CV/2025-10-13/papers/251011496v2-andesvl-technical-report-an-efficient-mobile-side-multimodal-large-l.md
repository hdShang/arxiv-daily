---
layout: default
title: AndesVL Technical Report: An Efficient Mobile-side Multimodal Large Language Model
---

# AndesVL Technical Report: An Efficient Mobile-side Multimodal Large Language Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.11496" class="toolbar-btn" target="_blank">📄 arXiv: 2510.11496v2</a>
  <a href="https://arxiv.org/pdf/2510.11496.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.11496v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.11496v2', 'AndesVL Technical Report: An Efficient Mobile-side Multimodal Large Language Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhiwei Jin, Xiaohui Song, Nan Wang, Yafei Liu, Chao Li, Xin Li, Ruichen Wang, Zhihao Li, Qi Qi, Long Cheng, Dongze Hao, Quanlong Zheng, Yanhao Zhang, Haobo Ji, Jian Ma, Zhitong Zheng, Zhenyi Lin, Haolin Deng, Xin Zou, Xiaojie Yin, Ruilin Wang, Liankai Cai, Haijing Liu, Yuqing Qiu, Ke Chen, Zixian Li, Chi Xie, Huafei Li, Chenxing Li, Chuangchuang Wang, Kai Tang, Zhiguang Zhu, Kai Tang, Wenmei Gao, Rui Wang, Jun Wu, Chao Liu, Qin Xie, Chen Chen, Haonan Lu

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-13 (更新: 2025-10-14)

**备注**: Tech report of OPPO AndesVL Team

**🔗 代码/项目**: [HUGGINGFACE](https://huggingface.co/OPPOer)

---

## 💡 一句话要点

**AndesVL：面向移动端的高效多模态大语言模型，实现性能与效率的平衡**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `移动端部署` `模型压缩` `量化感知微调` `缓存淘汰算法` `推测解码` `边缘计算`

## 📋 核心要点

1. 现有云端MLLM参数量巨大，边缘设备在内存、功耗和算力上难以满足需求。
2. AndesVL基于Qwen3，通过优化模型架构和训练流程，构建了参数量为0.6B-4B的移动端MLLM。
3. 实验表明，AndesVL在多个基准测试中达到一流水平，并通过优化策略显著提升了移动端部署效率。

## 📝 摘要（中文）

本文介绍了AndesVL，一套基于Qwen3的LLM和多种视觉编码器的移动端多模态大语言模型，参数规模从0.6B到4B。论文全面概述了AndesVL的模型架构、训练流程和训练数据。与同等规模的SOTA模型相比，AndesVL在一系列开源基准测试中取得了领先的性能，涵盖了富文本图像理解、推理与数学、多图像理解、通用VQA、幻觉缓解、多语言理解和GUI相关任务等领域。此外，论文还提出了一种1+N LoRA架构以及量化感知LoRA微调（QALFT）框架，以促进AndesVL在移动端部署期间的有效任务适配和模型压缩。而且，通过使用缓存淘汰算法OKV以及定制的推测解码和压缩策略，在联发科天玑9500芯片上部署AndesVL-4B时，实现了6.7倍的峰值解码速度提升，高达30.9%的内存减少以及1.8 bits-per-weight的模型压缩。

## 🔬 方法详解

**问题定义**：现有的大型多模态语言模型（MLLM），如QwenVL、InternVL、GPT-4o等，虽然在云端表现出色，但由于模型规模庞大（数百亿参数），对移动端等边缘设备的内存、功耗和计算能力提出了巨大挑战。因此，如何在移动端部署高性能的MLLM是一个亟待解决的问题。

**核心思路**：AndesVL的核心思路是构建一个参数规模适中（0.6B-4B），但性能接近甚至超过同等规模SOTA模型的MLLM。通过模型架构优化、高效的训练流程和数据，以及针对移动端部署的优化策略，实现性能与效率的平衡。

**技术框架**：AndesVL的技术框架主要包括以下几个部分：1) 基于Qwen3的LLM作为语言模型的基础；2) 多种视觉编码器用于处理图像输入；3) 1+N LoRA架构和QALFT框架用于任务适配和模型压缩；4) OKV缓存淘汰算法、推测解码和压缩策略用于加速推理和减少内存占用。整体流程是从数据准备和模型训练开始，然后进行任务微调和模型压缩，最后部署到移动端设备上。

**关键创新**：AndesVL的几个关键创新点包括：1) 针对移动端设计的轻量级模型架构；2) 量化感知LoRA微调（QALFT）框架，能够在模型压缩的同时保持性能；3) OKV缓存淘汰算法，有效管理移动端有限的内存资源；4) 定制的推测解码策略，加速模型推理。

**关键设计**：在模型设计上，AndesVL选择了Qwen3作为LLM的基础，并探索了不同的视觉编码器。在训练过程中，采用了多种数据增强技术和混合精度训练。QALFT框架的关键在于在量化过程中引入LoRA模块，并在微调过程中同时优化量化参数和LoRA参数。OKV算法的关键在于根据token的使用频率和重要性进行缓存管理，优先保留重要的token。

## 📊 实验亮点

AndesVL在多个开源基准测试中取得了领先的性能，与同等规模的SOTA模型相比，在文本丰富的图像理解、推理和数学、多图像理解、通用VQA、幻觉缓解、多语言理解和GUI相关任务中表现出色。在联发科天玑9500芯片上部署AndesVL-4B时，实现了6.7倍的峰值解码速度提升，高达30.9%的内存减少以及1.8 bits-per-weight的模型压缩。

## 🎯 应用场景

AndesVL具有广泛的应用前景，包括移动端的智能助手、图像搜索、视觉问答、文档理解、GUI自动化等。它可以在资源受限的设备上实现高性能的多模态交互，为用户提供更智能、更便捷的服务。未来，AndesVL有望推动边缘计算和人工智能的普及。

## 📄 摘要（原文）

> In recent years, while cloud-based MLLMs such as QwenVL, InternVL, GPT-4o, Gemini, and Claude Sonnet have demonstrated outstanding performance with enormous model sizes reaching hundreds of billions of parameters, they significantly surpass the limitations in memory, power consumption, and computing capacity of edge devices such as mobile phones. This paper introduces AndesVL, a suite of mobile-side MLLMs with 0.6B to 4B parameters based on Qwen3's LLM and various visual encoders. We comprehensively outline the model architectures, training pipeline, and training data of AndesVL, which achieves first-tier performance across a wide range of open-source benchmarks, including fields such as text-rich image understanding, reasoning and math, multi-image comprehension, general VQA, hallucination mitigation, multilingual understanding, and GUI-related tasks when compared with state-of-the-art models of a similar scale. Furthermore, we introduce a 1+N LoRA architecture alongside a Quantization-Aware LoRA Fine-Tuning (QALFT) framework to facilitate efficient task adaptation and model compression during mobile-side deployment of AndesVL. Moreover, utilizing our cache eviction algorithm -- OKV -- along with customized speculative decoding and compression strategies, we achieve a 6.7x peak decoding speedup ratio, up to 30.9% memory reduction, and 1.8 bits-per-weight when deploying AndesVL-4B on MediaTek Dimensity 9500 chips. We release all models on https://huggingface.co/OPPOer.

