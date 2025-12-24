---
layout: default
title: "Struct2D: A Perception-Guided Framework for Spatial Reasoning in MLLMs"
---

# Struct2D: A Perception-Guided Framework for Spatial Reasoning in MLLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04220" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04220v3</a>
  <a href="https://arxiv.org/pdf/2506.04220.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04220v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04220v3', 'Struct2D: A Perception-Guided Framework for Spatial Reasoning in MLLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fangrui Zhu, Hanhui Wang, Yiming Xie, Jing Gu, Tianye Ding, Jianwei Yang, Huaizu Jiang

**分类**: cs.CV

**发布日期**: 2025-06-04 (更新: 2025-11-05)

**备注**: NeurIPS 2025, code link: https://github.com/neu-vi/struct2d

---

## 💡 一句话要点

**提出Struct2D框架以解决MLLMs空间推理问题**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `空间推理` `多模态大型语言模型` `结构化2D表示` `鸟瞰图` `对象标记` `指令调优` `3D问答` `智能交互`

## 📋 核心要点

1. 现有方法多依赖显式的3D输入或特定模型架构，限制了MLLMs在空间推理任务中的应用。
2. 本研究提出Struct2D框架，通过结构化的2D表示来引导空间推理，探索MLLMs在仅使用2D输入时的推理能力。
3. 实验结果显示，微调后的开源MLLM在3D问答、密集标注和对象定位等任务上表现出色，验证了方法的有效性。

## 📝 摘要（中文）

在多模态大型语言模型（MLLMs）中，解锁空间推理能力对于智能与3D环境的交互至关重要。以往的研究通常依赖于显式的3D输入或专门的模型架构，而本研究提出Struct2D框架，利用结构化的2D表示（如鸟瞰图和对象标记）进行空间推理。通过对闭源MLLMs的零-shot分析，发现其在处理相对方向估计和路径规划等任务时表现出强大的空间推理能力。此外，构建了包含20万个细粒度问答对的大规模指令调优数据集Struct2D-Set，并在开源MLLM上进行微调，取得了在多个基准测试中的竞争性表现。该研究表明，结构化的2D输入可以有效地连接感知与语言推理，且无需显式的3D表示。

## 🔬 方法详解

**问题定义**：本研究旨在解决多模态大型语言模型（MLLMs）在空间推理任务中对显式3D输入的依赖，现有方法在处理3D环境时存在局限性。

**核心思路**：提出Struct2D框架，利用结构化的2D表示（如鸟瞰图和对象标记）来引导MLLMs进行空间推理，探索其在仅使用2D输入时的推理能力。

**技术框架**：整体架构包括鸟瞰图输入、对象标记和对象中心元数据，必要时可加入自我中心关键帧。框架通过感知引导的提示方式，结合这些2D信息进行空间推理。

**关键创新**：最重要的创新在于通过结构化的2D输入实现了感知与语言推理的有效连接，避免了对显式3D表示的需求，拓宽了MLLMs的应用范围。

**关键设计**：在数据集构建中，生成了包含20万个细粒度问答对的Struct2D-Set，涵盖八个空间推理类别，并在开源MLLM（Qwen2.5VL）上进行了微调，采用了适当的损失函数和网络结构以优化性能。

## 📊 实验亮点

实验结果表明，微调后的开源MLLM在多个基准测试中表现优异，尤其是在3D问答、密集标注和对象定位任务上，取得了与闭源模型相当的性能，展示了结构化2D输入的有效性和潜力。

## 🎯 应用场景

该研究的潜在应用领域包括智能机器人、虚拟现实和增强现实等3D环境中的人机交互。通过提升MLLMs的空间推理能力，可以实现更自然的交互体验，推动智能系统在复杂环境中的应用。未来，Struct2D框架有望在更多领域得到推广和应用。

## 📄 摘要（原文）

> Unlocking spatial reasoning in Multimodal Large Language Models (MLLMs) is crucial for enabling intelligent interaction with 3D environments. While prior efforts often rely on explicit 3D inputs or specialized model architectures, we ask: can MLLMs reason about 3D space using only structured 2D representations derived from perception? We introduce Struct2D, a perception-guided prompting framework that combines bird's-eye-view (BEV) images with object marks and object-centric metadata, optionally incorporating egocentric keyframes when needed. Using Struct2D, we conduct an in-depth zero-shot analysis of closed-source MLLMs (e.g., GPT-o3) and find that they exhibit surprisingly strong spatial reasoning abilities when provided with structured 2D inputs, effectively handling tasks such as relative direction estimation and route planning. Building on these insights, we construct Struct2D-Set, a large-scale instruction tuning dataset with 200K fine-grained QA pairs across eight spatial reasoning categories, generated automatically from 3D indoor scenes. We fine-tune an open-source MLLM (Qwen2.5VL) on Struct2D-Set, achieving competitive performance on multiple benchmarks, including 3D question answering, dense captioning, and object grounding. Our approach demonstrates that structured 2D inputs can effectively bridge perception and language reasoning in MLLMs-without requiring explicit 3D representations as input. We will release both our code and dataset to support future research.

