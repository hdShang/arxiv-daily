---
layout: default
title: MMSI-Bench: A Benchmark for Multi-Image Spatial Intelligence
---

# MMSI-Bench: A Benchmark for Multi-Image Spatial Intelligence

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23764" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23764v2</a>
  <a href="https://arxiv.org/pdf/2505.23764.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23764v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23764v2', 'MMSI-Bench: A Benchmark for Multi-Image Spatial Intelligence')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sihan Yang, Runsen Xu, Yiman Xie, Sizhe Yang, Mo Li, Jingli Lin, Chenming Zhu, Xiaochen Chen, Haodong Duan, Xiangyu Yue, Dahua Lin, Tai Wang, Jiangmiao Pang

**分类**: cs.CV, cs.CL

**发布日期**: 2025-05-29 (更新: 2025-09-25)

**备注**: 34 pages. A comprehensive, fully human-curated, multi-image-based spatial intelligence benchmark with reasoning annotation for MLLMs. Project page: https://runsenxu.com/projects/MMSI_Bench

---

## 💡 一句话要点

**提出MMSI-Bench以解决多图像空间智能评估问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多图像推理` `空间智能` `视觉问答` `基准测试` `人工智能`

## 📋 核心要点

1. 现有的基准测试仅关注单图像关系，无法有效评估多图像空间推理能力，限制了模型在复杂场景中的应用。
2. MMSI-Bench通过设计1000个多项选择题，结合120,000张图像，提供了一个全面评估多图像空间智能的基准。
3. 实验结果显示，当前最强的开源模型准确率仅为30%，而人类的准确率高达97%，表明该领域仍有显著提升空间。

## 📝 摘要（中文）

空间智能对于在复杂物理世界中运作的多模态大型语言模型（MLLMs）至关重要。然而，现有基准仅探讨单图像关系，无法评估实际应用所需的多图像空间推理。本文介绍了MMSI-Bench，这是一个专门针对多图像空间智能的视觉问答基准。六位3D视觉研究者花费超过300小时精心设计了1000个具有挑战性的多项选择题，基于超过120,000张图像，并配有精心设计的干扰项和逐步推理过程。实验评估了34个开源和专有的MLLMs，结果显示，最强的开源模型仅达到约30%的准确率，而OpenAI的o3推理模型达到40%，而人类得分为97%。这些结果凸显了MMSI-Bench的挑战性及未来研究的广阔空间。

## 🔬 方法详解

**问题定义**：本文旨在解决现有基准无法评估多图像空间推理能力的问题。现有方法主要集中于单图像关系，无法满足实际应用需求。

**核心思路**：MMSI-Bench通过设计多项选择题和逐步推理过程，评估模型在多图像场景中的空间智能能力，提供更具挑战性的测试环境。

**技术框架**：整体架构包括题目设计、图像选择、干扰项设计和推理过程的标注。研究者们从大量图像中提取信息，并构建多样化的测试题目。

**关键创新**：MMSI-Bench的创新在于其专注于多图像的空间推理，填补了现有基准的空白，提供了更具挑战性的评估标准。

**关键设计**：在设计过程中，研究者们注重题目的清晰性和干扰项的合理性，确保每个问题都能有效评估模型的推理能力。

## 📊 实验亮点

实验结果显示，最强的开源模型在MMSI-Bench上的准确率仅为30%，而OpenAI的o3推理模型达到40%。相比之下，人类的准确率高达97%，显示出当前模型在多图像空间推理方面的显著不足，且未来研究有广阔的提升空间。

## 🎯 应用场景

该研究的潜在应用领域包括机器人导航、自动驾驶、增强现实和虚拟现实等。通过提升多图像空间智能，能够使系统更好地理解和互动复杂的物理环境，进而推动智能系统的实际应用和发展。

## 📄 摘要（原文）

> Spatial intelligence is essential for multimodal large language models (MLLMs) operating in the complex physical world. Existing benchmarks, however, probe only single-image relations and thus fail to assess the multi-image spatial reasoning that real-world deployments demand. We introduce MMSI-Bench, a VQA benchmark dedicated to multi-image spatial intelligence. Six 3D-vision researchers spent more than 300 hours meticulously crafting 1,000 challenging, unambiguous multiple-choice questions from over 120,000 images, each paired with carefully designed distractors and a step-by-step reasoning process. We conduct extensive experiments and thoroughly evaluate 34 open-source and proprietary MLLMs, observing a wide gap: the strongest open-source model attains roughly 30% accuracy and OpenAI's o3 reasoning model reaches 40%, while humans score 97%. These results underscore the challenging nature of MMSI-Bench and the substantial headroom for future research. Leveraging the annotated reasoning processes, we also provide an automated error analysis pipeline that diagnoses four dominant failure modes, including (1) grounding errors, (2) overlap-matching and scene-reconstruction errors, (3) situation-transformation reasoning errors, and (4) spatial-logic errors, offering valuable insights for advancing multi-image spatial intelligence. Project page: https://runsenxu.com/projects/MMSI_Bench .

